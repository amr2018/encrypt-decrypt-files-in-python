
from cryptography.fernet import Fernet
from os import remove


# #generate the key 
# key = Fernet.generate_key()
# print(key)



f = Fernet(key)

def encrypt(fname):
	with open(fname, 'rb') as f1:
		with open(fname + '.enc', 'wb') as f2:
			f2.write(f.encrypt(f1.read()))

	remove(fname)

def decrypt(fname):
	with open(fname, 'rb') as f1:
		with open(fname.replace('.enc', ''), 'wb') as f2:
			f2.write(f.decrypt(f1.read()))

	remove(fname)

