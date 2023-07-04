from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {
        'title': 'Productos',
        'message': 'Listado de productos.',
        'products' : [
            {
                'title': 'Playera',
                'price': 5,
                'stock': True,
            },
            {
                'title': 'Camisa',
                'price': 7,
                'stock': True,
            },
            {
                'title': 'Mochila',
                'price': 20,
                'stock': False,
            },
            {
                'title': 'Laptop',
                'price': 500,
                'stock': True,
            },
        ]
    });