import hashlib

alf = 'a1b2c3d4e5f6g7h8i9j0klmnopqrstuvwxyz.,:-!? '

encoded_mess = input('Input encoded message: ')
key = input("Key input: ")

key_int = []
key_index = 0
message = ''
key_let=[]
key_num=[]

def f_hash():
    global key
    global hex_dig
    hash_object = hashlib.sha1(key.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    
    for i in hex_dig:
       if i not in ('0','1','2','3','4','5','6','7','8','9'):
          key_let.append(i) 
       else: key_num.append(int(i))
    
    while len(key_let) < len(key_num): key_num.pop()
    while len(key_let) > len(key_num): key_let.pop()

    for i in range(0, len(key_let)):
        if i%2 == 0:
           key_int.append(alf.find(key_let[i])+key_num[i])
        else:
           key_int.append(len(alf) - (alf.find(key_let[i])+key_num[i]))
    
    key = ''
    key = ''.join(hex_dig)
    
f_hash()

while len(encoded_mess) > len(key_int): f_hash()

for letter in encoded_mess:
    for alf_letter in alf:
        if letter == alf_letter:
            letter_mess_code = (alf.find(alf_letter) - key_int[key_index]) % len(alf)
            if letter_mess_code < 0:
                letter_mess_code = (letter_mess_code + len(alf)) % len(alf)
            key_index = key_index + 1
            message += alf[letter_mess_code]
print(message)