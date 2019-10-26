def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(0, len(plaintext)):
        if ('a' <= plaintext[i] <= 'z') or ('A' <= plaintext[i] <= 'Z'):
            c = plaintext[i].islower()
            if c == True:
                q = ord(plaintext[i])+3
                if q > ord('z'):
                    while q > ord('z'):
                        q = (q-ord('z'))+(ord('a')-1)
            else:
                q = ord(plaintext[i])+3
                if q > ord('Z'):
                    while q > ord('Z'):
                        q = (q-ord('Z'))+(ord('A')-1)
            ciphertext = ciphertext+chr(q)
        else:
            ciphertext = ciphertext+plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    i = int
    plaintext = ""
    for i in range(0, len(ciphertext)):
        if ('a' <= plaintext[i] <= 'z') or ('A' <= plaintext[i] <= 'Z'):
            c = ciphertext[i].islower()
            if c == True:
                q = ord(ciphertext[i])-3
                if q < ord("a"):
                    while q < ord("a"):
                        q = (ord('z')+1)-(ord('a')-q)
            else:
                q = ord(ciphertext[i])-3
                if q < ord("A"):
                    while q < ord("A"):
                        q = (ord('Z')+1)-(ord('A')-q)
            plaintext = plaintext+chr(q)
        else:
            plaintext = plaintext+ciphertext[i]
    return plaintext
