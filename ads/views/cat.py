import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from ads.models import Category


class CategoryDetailView(DetailView):
    model = Category

    def get(self, *args, **kwargs):
        """Получение категории по id"""
        categories = self.get_object()
        return JsonResponse({
            "id": categories.pk,
            "name": categories.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CatListView(View):

    def get(self, request):
        """Получение всех категорий"""

        cat_list = Category.objects.all()
        cat_list = cat_list.order_by('name')
        return JsonResponse([
            {"id": i.pk, "name": i.name}
            for i in cat_list], safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        """Создание категории"""
        cat_data = json.loads(request.body)

        new_cat = Category.objects.create(name=cat_data['name'])
        return JsonResponse({"name": new_cat.name})


@method_decorator(csrf_exempt, name='dispatch')
class CatUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        """Обновление категории"""
        super().post(self, request, *args, **kwargs)

        cat_data = json.loads(request.body)

        self.object.name = cat_data.get('name', self.object.name)
        self.object.save()
        return JsonResponse({"name": self.object.name})


@method_decorator(csrf_exempt, name='dispatch')
class CatDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        """Удаление категории"""
        super().delete(self, request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)
