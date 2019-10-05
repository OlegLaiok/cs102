"шифратор"

def encrypt_caesar(s):
    x=int(input("Введите сдвиг "))
    i=int
    s1=""
    for i in range(0,len(s)):
        if (ord(s[i])>ord('a') and ord(s[i])<ord('z')) or (ord(s[i])>ord('A') and ord(s[i])<ord('Z')):
            c=s[i].islower()
            if c==True:
                q=ord(s[i])+x
                if q>ord('z'):
                    while q>ord('z'):
                        q=(q-ord('z'))+(ord('a')-1)
            else:
                q=ord(s[i])+x
                if q>ord('Z'):
                    while q>ord('Z'):
                        q=(q-ord('Z'))+(ord('A')-1)
            s1=s1+chr(q)
        else:
            s1=s1+s[i]      
    return s1


"дешифратор"
def decrypt_caesar(s):
    x=int(input("ВВедите сдвиг"))
    i=int
    s1=""
    for i in range(0,len(s)):
        if (ord(s[i])>ord('a') and ord(s[i])<ord('z')) or (ord(s[i])>ord('A') and ord(s[i])<ord('Z')):
            c=s[i].islower()
            if c==True:
                q=ord(s[i])-x
                if q<ord("a"):
                    while q<ord("a"):
                        q=(ord('z')+1)-(ord('a')-q)
            else:
                q=ord(s[i])-x
                if q<ord("A"):
                    while q<ord("A"):
                        q=(ord('Z')+1)-(ord('A')-q)
            s1=s1+chr(q)
        else:
            s1=s1+s[i]
    return s1
print("Шифр цезаря")   
s=input('Введите шифруемое сообщение')
s1=encrypt_caesar(s)
print('Зашифрованное сообщение:',s1)
print('Дешифрованное сообщение:',decrypt_caesar(s1))