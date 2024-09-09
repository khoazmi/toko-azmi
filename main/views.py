from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Sepatu Hedon',
        'price': 'Rp 2.000.000,00',
        'description': 'Sepatu mahal biar keliatan kaya'
    }

    return render(request, 'main.html', context)