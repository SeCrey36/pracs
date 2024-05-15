import hashlib
import time

start_time = time.time()

alf = 'a1b2c3d4e5f6g7h8i9j0klmnopqrstuvwxyz.,:-!? '

key = 'key'
message = 'hi'

key_let=[]
key_num=[]
key_int = []

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

while len(message) > len(key_int): f_hash()

word = ''
key_int_index = 0

for letter in message:
    for alf_letter in alf:
        if letter == alf_letter:
            letter_code_index = (key_int[key_int_index] + alf.find(alf_letter)) % len(alf)
            key_int_index = key_int_index + 1
            word += alf[letter_code_index]
print(word)
print(len(message))
print("--- %s seconds ---" % (time.time() - start_time))