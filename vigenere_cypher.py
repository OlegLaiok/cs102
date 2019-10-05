def encrypt_vigenere(s, k):
    s1=''
    k1=k
    n=int
    if len(k)<len(s):
        while len(k1)<len(s):
            k1=k1+k
    'cгенерировали ключ'

    for i in range(0,len(s)):
        if (ord(s[i])>=ord('a') and ord(s[i])<=ord('z')) or (ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')):
            c=s[i].islower()
            if c==True:
                n=ord(s[i])+(ord(k1[i])-ord("a"))
                if n>ord('z'):
                    while n>ord('z'):
                        n=(n-ord('z'))+(ord('a')-1)
            else:
                n=ord(s[i])+(ord(k1[i])-ord("A"))
                if n>ord('Z'):
                    while n>ord('Z'):
                        n=(n-ord('Z'))+(ord('A')-1)
            s1=s1+chr(n)
        else:
            s1=s1+s[i]
    return s1  

def decrypt_vigenere(s, k):
    s1=''
    k1=k
    n=int
    if len(k)<len(s):
        while len(k1)<len(s):
            k1=k1+k
    'cгенерировали ключ'

    for i in range(0,len(s)):
        if (ord(s[i])>=ord('a') and ord(s[i])<=ord('z')) or (ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')):
            c=s[i].islower()
            if c==True:
                n=ord(s[i])-(ord(k1[i])-ord("a"))
                if n<ord('a'):
                    while n<ord('a'):
                        n=(ord('z')+1)-(ord('a')-n)
            else:
                n=ord(s[i])-(ord(k1[i])-ord("A"))
                if n<ord('A'):
                    while n<ord('A'):
                        n=(ord('Z')+1)-(ord('A')-n)
            s1=s1+chr(n)
        else:
            s1=s1+s[i]
    return s1

print("Шифр Вижнера")   
s=input('Введите шифруемое сообщение ')
k=input("ВВедите ключ")
s1=encrypt_vigenere(s,k)
print('Зашифрованное сообщение:',s1)
print('Дешифрованное сообщение:',decrypt_vigenere(s1,k))