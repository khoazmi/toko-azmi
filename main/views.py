from django.shortcuts import render

def show_main(request):
    context = {
        'nama_siswa' : 'Khoirul Azmi',
        'kelas_siswa' : 'PBP C',
        'name_product' : 'Sepatu Hedon',
        'price': 'Rp 2.000.000,00',
        'description': 'Sepatu mahal biar keliatan kaya'
    }

    return render(request, 'main.html', context)