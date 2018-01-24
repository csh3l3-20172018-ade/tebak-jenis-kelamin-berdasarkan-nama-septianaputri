def tebak_gender():
    pil= input("masukkan sebuah nama : ")                       #variabel penampung untuk meerima inputan user nama yang akan di cek gendernya
    pil=pil.split()                                             #fungsi untuk memisahkan suatu kalimat menjadi bentuk array perkata
    nickname =pil[0]                                            #terusan fungsi split untuk mengambil array pada indeks ke-0
    print(nickname)                                             #untuk menampilkan isi dari variable penampung nickname
    i=0                                                         #untuk menginisiasi variable i supaya terdefinisi oleh program
    lady=0                                                      #untuk menginisiasi variable lady supaya terdefinisi oleh program
    man=0                                                       #untuk menginisiasi variable man supaya terdefinisi oleh program
    for i in range(len(nickname)):                              #melakukan perulangan untuk mengecek tiap kondisi pada program
        if nickname[i]=='a':                                    #menyatakan kondisi ketika variabel nickname indeks ke-i tersebut a maka lady akan increment
            lady+=1
        if nickname[i]=='u':
            lady+=1
        if nickname[i]=='e':
            lady+=1
        if nickname[i]=='t':
            lady+=1
        if nickname[i]=='l':
            lady+=1
        if nickname[i]=='i':
            lady+=1
        if nickname[i]=='b':                                    #menyatakan kondisi ketika variabel nickname indeks ke-i tersebut b maka man akan increment
            man+=1
        if nickname[i]=='d':
            man+=1
        if nickname[i]=='o':
            man+=1
    if man>lady:                                                #menyatakan jika kondisinya nilai man > lady maka akan menampilkan gender "laki laki"
        print("laki-laki")
    else:
        print("perempuan")                                      ##menyatakan jika kondisinya nilai lady > man maka akan menampilkan gender "perempuan"

tebak_gender()                                                  #memanggil fungsi tebak_gender

