JAWABAN TUGAS 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. Membuat proyek django baru dengan menggunakan django-admin startproject toko_azmi pada terminal
    b. Membuat aplikasi dengan nama 'main' mennggunakan python manage.py startapp main pada cmd
    c. Melakukan routing agar dapat mnejalankan aplikasi 'main' dengan menambahkan kode dibawah pada urls.py

        from django.urls import include, path

        urlpatterns = [
            path('', include('main.urls')),
        ]

    d. Mengubah isi models.py yang telah disediakan oleh django dengan ketentuan tugas yaitu harus berisi name sebagai nama item dengan tipe CharField, 
    price sebagai harga item dengan tipe IntegerField, dan description sebagai deskripsi item dengan tipe TextField.

    Tidak lupa untuk melakukan migrations dengan memasukan command berikut pada terminal:
    - python manage.py makemigrations
    - python manage.py migrate


    e. Merubah isi views.py sesuai dengan kebutuhan dari nama barang, harga barang, dan deskripsi barangg agar bisa ditampilkan dari template
    dengan isi data pad views sesuai kebutuhan seperti pada program saya berikut:

            from django.shortcuts import render
            def show_main(request):
                context = {
                    'name' : 'Sepatu Hedon',
                    'price': 'Rp 2.000.000,00',
                    'description': 'Sepatu mahal biar keliatan kaya'
                }
            return render(request, 'main.html', context)

    f. Membuat template dengan HTML dengan membuat direktori template yang berisi main.HTML sebagai template. Pada program saya contoh isi programnya 
    sebagai berikut:

        <h1>Mental Health Tracker</h1>
        <h5>Nama: </h5>
        <p>{{ name }}</p>
        <h5>Harga: </h5>
        <p>{{ price }}</p>
        <h5>Deskripsi: </h5>
        <p>{{ description }}</p> 

    g. Melakukan routing di urls.py untuk fungsi index

    h. Melakukan deployment ke pws dengan menambahkan "khoirul-azmi-tokoazmi.pbp.cs.ui.ac.id" pada settings.py melalui create project di PWS.
    kemudian melakukan command berikut pada terminal:
    - git remote add pws http://pbp.cs.ui.ac.id/khoirul.azmi/tokoazmi
    - git branch -M master
    - git push pws master

    i. Lalu yang terakhir membuat REAME.txt untuk menjawab beberapa pertanyaan yang diberikan


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Dijango server flow](https://github.com/user-attachments/assets/e7043796-f481-4e38-8898-40cc0d322658)

Ketika client mengirimkan request, URL menentukan jalur yang sesuai dan memilih fungsi di views untuk memproses permintaan tersebut. Jika diperlukan, views akan berinteraksi dengan model untuk mengambil data dari database. Setelah data diperoleh, views mengirimkan data tersebut ke template untuk dirender menjadi halaman HTML. Akhirnya, halaman yang telah dirender dikirim kembali ke client sebagai response berupa halaman web yang dapat ditampilkan di browser.



3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
    
    Git berfungsi sebagai sistem kontrol versi yang sangat penting dalam pengembangan perangkat lunak karena memungkinkan tim pengembang untuk:
        
        a. Melacak perubahan kode: Git mencatat setiap perubahan yang dilakukan pada kode, sehingga pengembang dapat melihat versi sebelumnya dan memahami sejarah pengembangan.
        
        b. Kolaborasi tim: Git memungkinkan beberapa pengembang bekerja pada kode yang sama secara bersamaan, menggabungkan perubahan mereka tanpa konflik, dan memfasilitasi 
        pengembangan yang lebih terkoordinasi.

        c. Branching: Git memungkinkan pembuatan cabang (branches) yang terisolasi dari kode utama, sehingga pengembang dapat bekerja pada fitur baru atau perbaikan bug tanpa 
        mengganggu kode yang sudah stabil.

        d. Penyatuan kode (merging): Setelah pengembangan pada cabang selesai, Git memungkinkan penggabungan (merging) cabang tersebut kembali ke kode utama secara aman.

        e. Backup dan pemulihan: Dengan Git, kode disimpan dalam repositori yang bisa digunakan sebagai cadangan, sehingga jika terjadi kesalahan atau kehilangan, versi sebelumnya 
        dapat dipulihkan dengan mudah.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menggunakan Django memungkinkan pengembang untuk menerapkan pola Model-View-Template (MVT), yang memberikan struktur yang jelas dan memudahkan dalam pengembangan aplikasi web. Django juga dilengkapi dengan berbagai fitur bawaan, seperti sistem autentikasi, pengelolaan URL, dan ORM untuk basis data, sehingga mengurangi kebutuhan integrasi library eksternal. Selain itu, Django terkenal dengan dokumentasinya yang lengkap dan keamanan yang terjamin, menjadikannya pilihan yang optimal bagi pengembang, baik pemula maupun profesional, untuk membangun aplikasi yang aman, efisien, dan terstruktur dengan baik. Keunggulan-keunggulan ini membuat Django tidak hanya memudahkan, tetapi juga meningkatkan produktivitas pengembang dalam menciptakan aplikasi berkualitas tinggi.

5. Mengapa model pada Django disebut sebagai ORM? Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena memungkinkan pengembang berinteraksi dengan basis data melalui objek dan kelas Python tanpa menulis SQL secara langsung. ORM menerjemahkan operasi pada objek model ke perintah SQL, mempermudah operasi CRUD, dan mendukung berbagai jenis basis data. Django ORM juga menyederhanakan pengelolaan relasi antar tabel seperti one-to-one, one-to-many, dan many-to-many, sehingga pengelolaan data lebih intuitif dan portabel.

JAWABAN TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery penting dalam platform untuk memastikan pertukaran data antara server dan klien berjalan lancar, aman, dan efisien, serta memungkinkan interaksi pengguna dengan data secara real-time.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Tergantung kebutuhan. Untuk JSON lebih populer dari XML karena lebih ringan, mudah diparsing oleh JavaScript, lebih ringkas, dan lebih mudah dibaca. JSON lebih efisien untuk aplikasi web modern, sementara XML lebih cocok untuk data kompleks.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? is_valid() di Django memvalidasi input form. Jika valid, data disimpan di cleaned_data. Ini penting untuk mencegah kesalahan dan masalah keamanan dari data input yang tidak valid.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? csrf_token melindungi dari serangan CSRF. Tanpa token ini, penyerang bisa mengirim permintaan palsu atas nama pengguna, misalnya melakukan perubahan data tanpa izin.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   a. Tambahkan model Product berisi nama, harga, dan deskripsi di models.py, lalu buat form Product dengan fieldsnya berissi nama, harga, dan deskripsi di forms.py untuk menangani input dari pengguna. Setelah itu, tambahkan view create_product di views.py untuk menyimpan data yang diinput melalui form, dan buat template create_product.html untuk menampilkan form tersebut di halaman web.
    b. pada views.py, buat view show_json untuk menampilkan semua objek dalam format JSON dan show_xml untuk menampilkan semua objek dalam format XML. Tambahkan juga path show_json_by_id dan show_xml_by_id untuk menampilkan objek berdasarkan ID dalam format JSON dan XML.
    c. Di urls.py pada direktori main, tambahkan routing URL untuk setiap view yang sudah dibuat, yaitu create_product, show_json, show_xml, show_json_by_id, dan show_xml_by_id, sehingga pengguna dapat mengakses form input dan melihat data dalam format JSON atau XML.

6. Screenshot Postman
   
![Screenshot (2009)](https://github.com/user-attachments/assets/73f35cb6-7814-40ba-9c79-12b2022233dd)
![Screenshot (2008)](https://github.com/user-attachments/assets/23656997-1a9f-4397-afaf-51bee5375529)
![Screenshot (2011)](https://github.com/user-attachments/assets/084a2b02-8871-4bf4-a36d-5fd1bbea0833)
![Screenshot (2010)](https://github.com/user-attachments/assets/ee0fdcac-7f2c-490e-9106-3719edd5700f)

   

JAWABAN TUGAS 4
1. Apa perbedaan antara HttpResponseRedirect dan redirect
    `HttpResponseRedirect()` adalah kelas yang hanya mengarahkan ke URL tertentu, sedangkan `redirect()` adalah shortcut yang lebih fleksibel karena dapat menerima URL, nama view, atau objek model dan mengonversinya secara otomatis menjadi URL. `redirect()` lebih praktis dan sering digunakan.

2. Jelaskan cara kerja penghubungan model Product dengan User!
    Penghubungan model `Product` dengan `User` biasanya dilakukan dengan menambahkan relasi ForeignKey di model `Product` yang mengacu pada model `User`. Ini memungkinkan setiap produk dikaitkan dengan pengguna tertentu yang membuat atau mengelolanya. Saat pengguna membuat produk, data pengguna disimpan di kolom `User` pada model `Product`.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
    Authentication adalah proses memverifikasi identitas pengguna, sedangkan authorization adalah proses menentukan apa yang diizinkan pengguna lakukan setelah identitasnya diverifikasi. Ketika pengguna login, authentication memastikan pengguna adalah siapa yang mereka klaim (misalnya, dengan memeriksa username dan password), sementara authorization memastikan apakah pengguna tersebut memiliki izin untuk mengakses fitur atau data tertentu. Contoh pada Django:
  - Autentikasi  dipakai untuk melakukan login
  - Autorisasi dipakai untuk menentukan hal-hal apa yang boleh dilakukan oleh akun pengguna seperti menambah barang

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

    Django mengingat pengguna yang telah login dengan menggunakan session framework yang menyimpan informasi pengguna di server dan mencatat ID sesi di cookie pada browser pengguna. Ketika pengguna login, Django mengirimkan cookie yang berisi session ID ke browser. Setiap kali pengguna mengirim permintaan ke server, session ID ini dikirim kembali, sehingga server dapat mengidentifikasi pengguna yang sedang aktif.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Berikut adalah langkah-langkah yang saya lakukan untuk mengimplementasikan checklist yang diberikan:


### 1. **Implementasi Registrasi**
   - **Membuat View untuk Registrasi**: Membuat view `register` yang menggunakan form `UserCreationForm` bawaan dari Django. Ini menyediakan form standar untuk registrasi pengguna.
     - Path: `main/views.py`
     ```python
     from django.contrib.auth.forms import UserCreationForm

     def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
    ```

   - **Routing untuk Registrasi**: Saya menambahkan path ke URL pattern di `main/urls.py` untuk mengarahkan URL registrasi ke view yang sudah dibuat.
     ```python
     from .views import register
     urlpatterns = [
         path('register/', register, name='register'),
     ]
     ```

   - **Menyiapkan Template Registrasi**: Membuat template `register.html` di folder `templates/main/`.
     - Path: `main/templates/main/register.html`
     ```html
     <div class="login">
        <h1>Register</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" name="submit" value="Daftar" /></td>
            </tr>
            </table>
        </form>
     ```

### 2. **Implementasi Login dan Logout**
   - **View untuk Login dan Logout**: Menggunakan `login` dan `logout` , yang sudah meng-handle sesi pengguna secara otomatis.
     - Path: `main/views.py`
     ```python
        from django.contrib.auth import authenticate, login
        from django.contrib.auth import logout
     ```

   - **Routing untuk Login dan Logout**: Saya menambahkan path untuk login dan logout di `urls.py`.
     ```python
     urlpatterns = [
            path('login/', login_user, name='login'),
            path('logout/', logout_user, name='logout'),
     ]
     ```

   - **Menyiapkan Template Login**: Membuat template `login.html`.
     - Path: `main/templates/main/login.html`
     ```html
     <div class="login">
        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login" /></td>
            </tr>
            </table>
        </form>
     ```

### 3. **Menampilkan Username dan Cookies pada Halaman Utama**
   - **Menampilkan Username**: Di halaman utama (`main.html`), menampilkan username dari pengguna yang sedang login dengan menggunakan context `{{ user.username }}` pada `views.py`.
     - Path: `main/templates/main.html`
     ```python
    @login_required(login_url='/login')
    def show_main(request):
        create_product = Product.objects.filter(user=request.user)
        context = {
            'nama_siswa' : request.user.username,
            'kelas_siswa' : 'PBP C',
            'npm_siswa' : '2306245812',
            'create_product' : create_product,
            'last_login': request.COOKIES['last_login'],
    }
     ```

   - **Menambahkan Cookie Last Login**: Saat login, saya memanfaatkan middleware bawaan Django yang menyimpan informasi `last_login`. Saya mengambil cookie ini dan menampilkannya di halaman utama dengan meenggunakan kode ini di `views.py` di class `show_main`.
     ```python
    'last_login': request.COOKIES['last_login'],
     ```

### 4. **Menghubungkan Model Product dengan User**
   - **Modifikasi Model Product**: Menambahkan ForeignKey pada model `Product` untuk menghubungkan produk dengan pengguna yang membuatnya.
     - Path: `main/models.py`
     ```python
        from django.contrib.auth.models import User
        class Product(models.Model):
            id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            name_product = models.CharField(max_length=50, default='Masukan Nama Produk')
            price = models.IntegerField(default='0')
            description = models.TextField(max_length=400, default='Tambahkan Deskripsi (max: 400 kata)')
     ```

   - **Menambahkan Data Dummy**: Setelah membuat dua akun pengguna, saya menggunakan `python manage.py runserver` untuk menambahkan data dummy untuk setiap pengguna di lokal.






