def tebak_gender():
    gdr=(["female","male"])
    pil= input("masukkan sebuah nama : ")
    i=0
    if (i > 1 ):
        if ('a' or 'u' or  'e' or 't' or 'l' > 1 ):
            if ('b' or 'd' or 'o' <= 1):
                print("female")
            else:
                print ("male")
        elif ('a' or 'u' or 'e' or 't' or 'l' <= 1 ):
            if ('b' or 'd' or 'o' <= 1):
                print("male")
            else:
                print ("male")
    elif (i <= 1):
        if ('a' or 'u' or  'e' or 't' or 'l' > 1 ):
            if ('b' or 'd' or 'o' <= 1):
                print ("female")
            else:
                print ("male")
        elif ('a' or 'u' or  'e' or 't' or 'l' <= 1):
            if ('b' or 'd' or 'o' <= 1):
                print("male")
            else:
                print ("male")
    else :
        print ("male")
tebak_gender()

