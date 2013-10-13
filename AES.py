def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))
def increment_iv(iv, increment):
	num=int(iv.encode('hex'),16)
	s=hex(num+increment)
	s=s[2:len(s)-1].decode('hex')
	return s

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
key="36f18357be4dbd77f050515c73fcf9f2".decode("hex");
ciphertext="69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc3\
88d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329".decode("hex")
cipher=AES.new(key,AES.MODE_ECB)
iv=ciphertext[:AES.block_size]
ciphertext=ciphertext[AES.block_size:]
ctr=Counter.new(128)
correctCipher=AES.new(key,AES.MODE_CTR,counter=ctr)
encryption=correctCipher.decrypt(ciphertext)
print encryption

vector=iv
remain=ciphertext
plain_text=""
while len(remain)>0:
	block=remain[:AES.block_size]
	print xor_strings(cipher.decrypt(vector),block)
	plain_text=plain_text+xor_strings(cipher.encrypt(vector),block)
	remain=remain[AES.block_size:]
	vector=increment_iv(vector,1)

print "++++++++++++++"
print plain_text
