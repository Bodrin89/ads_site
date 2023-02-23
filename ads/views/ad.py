from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, CreateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Category

import json

from ads.permissions import CheckAuthorPermission
from ads.serializers import AdListSerializer, AdDetailSerializer, AdUpdateSerializer, AdDeleteSerializer
from users.models import User


def index(request):
    return JsonResponse({"status": "ok"})


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        """Получение всех объявлений, по id категории, по вхождению слова в строку,
        по локации, по диапазону цены"""

        if categories := request.GET.getlist('cat'):
            self.queryset = self.queryset.filter(category_id__in=categories)

        if search_text := request.GET.get('text'):
            self.queryset = self.queryset.filter(description__icontains=search_text)

        if location := request.GET.get('location'):
            self.queryset = self.queryset.filter(author__location__name__icontains=location)

        if price_from := request.GET.get('price_from'):
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to := request.GET.get('price_to'):
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    """Получение детальной информации об объявлении по id"""
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    """Обновление объявления с доступом для модераторов, админов и авторов"""
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [CheckAuthorPermission]


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'price', 'description', 'image', 'is_published', 'author_id', 'category_id']

    def post(self, request, *args, **kwargs):
        """Создание объявления"""
        ad_data = json.loads(request.body)

        new_ad = Ad.objects.create(
            name=ad_data['name'],
            price=ad_data['price'],
            description=ad_data['description'],
            is_published=ad_data['is_published']
        )
        new_ad.image = ad_data.get('image', None)
        new_ad.author = get_object_or_404(User, pk=ad_data['author'])
        new_ad.category = get_object_or_404(Category, pk=ad_data['category'])

        new_ad.save()
        response = {
            "name": new_ad.name,
            "price": new_ad.price,
            "description": new_ad.description,
            "image": None,
            "is_published": new_ad.is_published,
            "author": new_ad.author_id,
            "category": new_ad.category_id
        }
        if new_ad.image:
            response['image'] = new_ad.image.url
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageLoadView(UpdateView):
    model = Ad
    fields = ['name', 'price', 'description', 'image', 'is_published', 'author_id', 'category_id']

    def post(self, request, *args, **kwargs):
        """Добавление картинки"""
        self.object = self.get_object()

        self.object.image = request.FILES['image']
        self.object.save()
        return JsonResponse({
            "id": self.object.pk,
            "name": self.object.name,
            "image": self.object.image.url
        })


class AdDeleteView(DestroyAPIView):
    """Удаление объявления с доступом для модераторов, админов и авторов"""
    queryset = Ad.objects.all()
    serializer_class = AdDeleteSerializer
    permission_classes = [CheckAuthorPermission]
