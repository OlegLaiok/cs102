def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    k1 = keyword
    if len(keyword) < len(plaintext):
        while len(k1) < len(plaintext):
            k1 = k1+keyword

    for i in range(0, len(plaintext)):
        if ('a' <= plaintext[i] <= 'z') or ('A' <= plaintext[i] <= 'Z'):
            c = plaintext[i].islower()
            if c == True:
                n = ord(plaintext[i])+(ord(k1[i])-ord("a"))
                if n > ord('z'):
                    while n > ord('z'):
                        n = (n-ord('z'))+(ord('a')-1)
            else:
                n = ord(plaintext[i])+(ord(k1[i])-ord("A"))
                if n > ord('Z'):
                    while n > ord('Z'):
                        n = (n-ord('Z'))+(ord('A')-1)
            ciphertext = ciphertext+chr(n)
        else:
            ciphertext = ciphertext+plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    plaintext = ''
    k1 = keyword
    n = int
    if len(keyword) < len(ciphertext):
        while len(k1) < len(ciphertext):
            k1 = k1+keyword
    'cгенерировали ключ'

    for i in range(0, len(ciphertext)):
        if ('a' <= plaintext[i] <= 'z') or ('A' <= plaintext[i] <= 'Z'):
            c = ciphertext[i].islower()
            if c == True:
                n = ord(ciphertext[i])-(ord(k1[i])-ord("a"))
                if n < ord('a'):
                    while n < ord('a'):
                        n = (ord('z')+1)-(ord('a')-n)
            else:
                n = ord(ciphertext[i])-(ord(k1[i])-ord("A"))
                if n < ord('A'):
                    while n < ord('A'):
                        n = (ord('Z')+1)-(ord('A')-n)
            plaintext = plaintext+chr(n)
        else:
            plaintext = plaintext+ciphertext[i]
    return plaintext
