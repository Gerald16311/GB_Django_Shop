from django.shortcuts import render
import json
# Create your views here.

# Скрипт создания Json файла
# links_menu = [
#     {'href': 'products', 'name': 'все'},
#     {'href': 'products_home', 'name': 'дом'},
#     {'href': 'products_office', 'name': 'офис'},
#     {'href': 'products_modern', 'name': 'модерн'},
#     {'href': 'products_classic', 'name': 'классика'},
# ]
# with open('links_menu.json', 'w') as f:
#     json.dump(links_menu, f)
from mainapp.models import ProductCategory


def products(request):
    title = "Каталог"
    links_menu = ProductCategory.objects.all()

    # with open('mainapp/links_menu.json', 'r') as f:
    #     data = json.loads(f.read())
    #     for i in data:
    #         links_menu.append(i)

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context)

