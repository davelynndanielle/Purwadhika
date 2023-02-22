# CAPSTONE MODUL 1 DAVELYNN DANIELLE

#DATA KARYAWAN
DataKaryawanPerusahaan = [{
    'ID' :1,
    'Nama' : 'Billkin Mediyan', 
    'Umur' : 27, 
    'Pendidikan' : 'S1',
    'Posisi' : 'Senior Staff unit Sekretaris Perusahaan'}, 
    {'ID' :2, 
    'Nama' : 'Tisha Andriana', 
    'Umur' : 27, 
    'Pendidikan' : 'S1', 
    'Posisi' : 'Ketua Unit Sekretaris Perusahaan'},
    {
    'ID' :3, 
    'Nama' : 'Muhammad Tegar', 
    'Umur' : 30, 
    'Pendidikan' : 'S2', 
    'Posisi' : 'Kepala Divisi Keuangan'},
    { 
    'ID' :4, 
    'Nama' : 'Rosalinda Putri', 
    'Umur' : 26, 
    'Pendidikan' : 'D3', 
    'Posisi' : 'Sekretaris Divisi Operasional '}
]

#DATA KARYAWAN PERUSAHAAN

def KaryawanDDX():
    while True:
        MainMenu = input('''
        \n Selamat Datang di Database Perusahaan DDX \n
        Berikut ini adalah daftar menu yang tersedia di program ini:
        1. Menampilkan Data Karyawan 
        2. Menambahkan Data Karyawan Baru
        3. Mengubah Data Karyawan 
        4. Menghapus Data Karyawan
        5. Keluar

        Silahkan pilih Menu Yang Diinginkan dengan memilih angka 1-5 :''')

        if (MainMenu == '1'): 
            readdata()

        elif (MainMenu == '2') :
            CreateData()
            
        elif (MainMenu == '3') :
            UpdateData() 

        elif (MainMenu == '4') :
            DeleteData()

        elif (MainMenu == '5'):
            print ('\n TERIMAKASIH SUDAH DATANG, SEE YOU AND GOODBYE!')
            break

        else :
            print ('\nPilihan tidak tersedia, silahkan masukan pilihan yang benar')
            KaryawanDDX()

def checkID(x):
    for i, d in enumerate(DataKaryawanPerusahaan):
        if d['ID'] == x:
             return i
    return None


def readdata() :
    while True :
        MenuReadData = (input (''' \n -------------MENAMPILKAN DATA KARAYAWAN-------------
        1. Menampilkan Seluruh Data
        2. Menampilkan Data Tertentu
        3. Kembali ke Menu Utama

        Silahkan pilih menu Read Data yang diinginkan dengan memilih angka 1-3: '''))

        if (MenuReadData == '1') :
            if len (DataKaryawanPerusahaan) == 0:
                print ('Data Tidak Tersedia')

            else :
                print (' \n ---Data Karyawan Perusahaan DDX---\n ')
                print ('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
                for i in range(len(DataKaryawanPerusahaan)):
                        print("{} \t| {} \t| {} \t| {} \t\t| {}".format(DataKaryawanPerusahaan[i]["ID"],DataKaryawanPerusahaan[i]["Nama"],DataKaryawanPerusahaan[i]["Umur"],DataKaryawanPerusahaan[i]["Pendidikan"],DataKaryawanPerusahaan[i]["Posisi"]))

        elif (MenuReadData == '2'):   
            while True :
                Input_ID =input('\n Masukkan Nomor ID karyawan yang ingin ditampilkan:')
                if Input_ID.isdigit():
                    Input_ID = int(Input_ID) 
                    Search_ID = checkID(Input_ID)
                    if Search_ID != None:
                        print('\n Daftar Karyawan Perusahaan DDX\n')
                        print('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
                        print (f'{DataKaryawanPerusahaan[Search_ID]["ID"]}\t|{DataKaryawanPerusahaan[Search_ID]["Nama"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Umur"]}\t|{DataKaryawanPerusahaan[Search_ID]["Pendidikan"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Posisi"]}')
                        break
                    else:
                        print ('\n Data Tidak Tersedia')
                        break
                else : 
                    print('\n Masukan ID dalam angka')  

        elif (MenuReadData == '3'):
            break
        else : 
            print('\nPilihan tidak tersedia')
    

def CreateData() : #CREATE DATA
    while True :
        Menucreatedata = input (''' \n\n------------- MENAMBAHKAN DATA KARAYAWAN BARU-------------
        1. Menambahkan Data Baru
        2. Kembali ke Menu Utama

        Silahkan pilih menu Create Data yang diinginkan dengan memilih angka 1-2: ''')

        if (Menucreatedata == '1'):
            while True :
                print ( '\nSilahkan Masukan Data yang Diperlukan')
                print ('Masukan ID dalam bentuk angka')
                Input_ID = (input('ID:'))
                if Input_ID.isdigit():
                    Input_ID = int(Input_ID) 
                    Search_ID = checkID(Input_ID)
                    if Search_ID != None:
                        print('\n ID Sudah Ada, silahkan mengisi dengan ID lain')

    
                    else:
                        Dict1 = {
                            'ID' :'x', 
                            'Nama' : 'xxxx', 
                            'Umur' : 'xx', 
                            'Pendidikan' : 'xx', 
                            'Posisi' : 'xxx '}
                        print('ID baru, silahkan melanjutkan mengisi kelengkapan data:')
                        Dict1['ID'] = Input_ID
                        Dict1['Nama'] = input('Name :').capitalize()
                        Dict1['Umur'] = input('Umur : ')
                        Dict1['Pendidikan'] = input('Pendidikan  :').capitalize()
                        Dict1['Posisi'] = input('Posisi :').capitalize()

                        Save_Data = input('\n Apakah anda ingin menyimpan data yang sudah dibuat?(YA/TIDAK) : ').upper()
                        if Save_Data == 'YA' :
                            DataKaryawanPerusahaan.append (Dict1)
                            print('\nData Berhasil Disimpan'.upper())
                            CreateData()

                        else : 
                            Dict1.clear 
                            CreateData()
                else :
                    print('\n Masukan ID dalam angka')
                    CreateData() 
        

                

        elif (Menucreatedata == '2') :
            KaryawanDDX()


        else :
            print('\n PILIHAN MENU TIDAK TERSEDIA')
            CreateData()

def UpdateData() :
    while True :
        MenuUpdateData = input (''' \n\n ------------- MENGUBAH DATA KARAYAWAN-------------
        1. Mengubah Data Karyawan
        2. Kembali ke Menu Utama

        Silahkan pilih menu Update Data yang diinginkan dengan memilih angka 1-2: ''')

        if (MenuUpdateData == '1'):
            print (' \n ---Data Karyawan Perusahaan DDX---\n ')
            print ('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
            for i in range(len(DataKaryawanPerusahaan)):
                print("{} \t| {} \t| {} \t| {} \t\t| {}".format(DataKaryawanPerusahaan[i]["ID"],DataKaryawanPerusahaan[i]["Nama"],DataKaryawanPerusahaan[i]["Umur"],DataKaryawanPerusahaan[i]["Pendidikan"],DataKaryawanPerusahaan[i]["Posisi"]))
            print ( '\n Silahkan Masukan ID Data yang ingin di update')
            Input_ID = (input('ID:')) 
            if Input_ID.isdigit():
                Input_ID = int(Input_ID) 
                Search_ID = checkID(Input_ID)
                if Search_ID != None:
                    print('\n Data Karyawan Perusahaan DDX : \n')
                    print('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
                    print (f'{DataKaryawanPerusahaan[Search_ID]["ID"]}\t|{DataKaryawanPerusahaan[Search_ID]["Nama"]}\t|{DataKaryawanPerusahaan[Search_ID]["Umur"]}\t|{DataKaryawanPerusahaan[Search_ID]["Pendidikan"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Posisi"]}')
    
                    while True:
                        lanjut = input(f'Apakah anda ingin mengupdate data ini? {Input_ID}?(YA/TIDAK):')
                        lanjut = lanjut.upper()
                        if lanjut == 'YA':
                             while True:
                                PilihanKolom = input('''
                                Daftar Kolom : \n

                                1. Nama Karyawan
                                2. Umur
                                3. Pendidikan
                                4. Posisi 
                                5. Keluar 
                                \nMasukkan nomor sesuai dengan kolom yang ingin diupdate:''')
                    

                                if PilihanKolom == '1' :
                                        Nama_Update = (input('Masukan Nama Baru:')) 
                                        SaveUpdate = input('Simpan  Data Terupdate?(YA/TIDAK):').upper()
                                        if SaveUpdate == 'YA':
                                            DataKaryawanPerusahaan[Search_ID]['Nama'] = Nama_Update
                                            print('Data Terupdate'.upper())
                                            print('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
                                            print (f'{DataKaryawanPerusahaan[Search_ID]["ID"]}\t|{DataKaryawanPerusahaan[Search_ID]["Nama"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Umur"]}\t|{DataKaryawanPerusahaan[Search_ID]["Pendidikan"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Posisi"]}')
                            

                                if PilihanKolom == '2' :
                                        Umur_Update = (input('Masukan Umur Baru:')) 
                                        SaveUpdate = input('Simpan  Data Terupdate?(YA/TIDAK):').upper()
                                        if SaveUpdate == 'YA':
                                            DataKaryawanPerusahaan[Search_ID]['Umur'] = Umur_Update
                                            print('Data Terupdate'.upper())
                                            print('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
                                            print (f'{DataKaryawanPerusahaan[Search_ID]["ID"]}\t|{DataKaryawanPerusahaan[Search_ID]["Nama"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Umur"]}\t|{DataKaryawanPerusahaan[Search_ID]["Pendidikan"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Posisi"]}')
                               
                                elif PilihanKolom == '3' :
                                        Pendidikan_Update = (input('Masukan Pendidikan terupdate:')) 
                                        SaveUpdate = input('Simpan  Data Terupdate?(YA/TIDAK):').upper()
                                        if SaveUpdate == 'YA':
                                            DataKaryawanPerusahaan[Search_ID]['Pendidikan'] = Pendidikan_Update
                                            print('Data Terupdate'.upper())
                                            print('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
                                            print (f'{DataKaryawanPerusahaan[Search_ID]["ID"]}\t|{DataKaryawanPerusahaan[Search_ID]["Nama"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Umur"]}\t|{DataKaryawanPerusahaan[Search_ID]["Pendidikan"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Posisi"]}')
                               
                                elif PilihanKolom == '4' :
                                        Posisi_Update = (input('Masukan Posisi terupdate:')) 
                                        SaveUpdate = input('Simpan  Data Terupdate?(YA/TIDAK):').upper()
                                        if SaveUpdate == 'YA':
                                            DataKaryawanPerusahaan[Search_ID]['Posisi'] = Posisi_Update
                                            print('Data Terupdate'.upper())
                                            print('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
                                            print (f'{DataKaryawanPerusahaan[Search_ID]["ID"]}\t|{DataKaryawanPerusahaan[Search_ID]["Nama"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Umur"]}\t|{DataKaryawanPerusahaan[Search_ID]["Pendidikan"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Posisi"]}')
                                
                                elif PilihanKolom == '5' :
                                       UpdateData()
                                       break

                                else :
                                    print('Pilihan tidak tersedia silahkan pilih lagi')   
                        else :
                            UpdateData()
                            break

                else :
                    print('DATA TIDAK ADA')
                    UpdateData()


        elif (MenuUpdateData == '2'):   
            KaryawanDDX()
            break            

def DeleteData() :
    while True :
        MenuDeleteData = input (''' \n\n ------------- MENGHAPUS DATA KARAYAWAN-------------
        1. Menghapus Data Karyawan
        2. Kembali ke Menu Utama

        Silahkan pilih menu Delete Data yang diinginkan dengan memilih angka 1-2: ''')

        if (MenuDeleteData == '1'):
            print ( '\n Silahkan Masukan ID Data yang ingin di hapus')
            print ('*notes : ID dalam bentuk angka') 
            Input_ID = (input('ID:')) 
            if Input_ID.isdigit():
                Input_ID = int(Input_ID) 
                Search_ID = checkID(Input_ID)
                if Search_ID != None:
                    print('\n Data Karyawan Perusahaan DDX : \n')
                    print('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
                    print (f'{DataKaryawanPerusahaan[Search_ID]["ID"]}\t|{DataKaryawanPerusahaan[Search_ID]["Nama"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Umur"]}\t|{DataKaryawanPerusahaan[Search_ID]["Pendidikan"]}\t\t|{DataKaryawanPerusahaan[Search_ID]["Posisi"]}')
                    
                    lanjut = input(f'Ingin menghapus data dengan ID {Input_ID}?(ya/tidak):').upper()
                    if lanjut == 'YA':
                        while True:
                            lanjut2 = input('Apakah anda yakin?(ya/tidak):')
                            lanjut2 = lanjut2.upper()
                            if lanjut2 == 'YA':
                                del DataKaryawanPerusahaan[Search_ID]
                                print('Data Berhasil Terhapus')
                                print (' \n ---Data Karyawan Perusahaan DDX---\n ')
                                print ('ID\t|Nama Karyawan\t\t|Umur\t|Pendidikan\t|Posisi')
                                for i in range(len(DataKaryawanPerusahaan)):
                                    print("{} \t| {} \t| {} \t| {} \t\t| {}".format(DataKaryawanPerusahaan[i]["ID"],DataKaryawanPerusahaan[i]["Nama"],DataKaryawanPerusahaan[i]["Umur"],DataKaryawanPerusahaan[i]["Pendidikan"],DataKaryawanPerusahaan[i]["Posisi"]))
                                break
                            else :
                                DeleteData()


                else :
                    print('DATA TIDAK TERSEDIA')
                    DeleteData()
                    

        elif (MenuDeleteData == '2') :
            KaryawanDDX() 
            break

        else :
            print('Menu tidak tersedia, silahkan masukan pilihan lain')


KaryawanDDX()

