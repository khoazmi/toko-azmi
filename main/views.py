from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245812',
        'name': 'Khoirul Azmi',
        'class': 'PBP C'
    }

    return render(request, 'main.html', context)