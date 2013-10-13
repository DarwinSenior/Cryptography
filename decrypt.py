from Crypto.Cipher import AES
def increment_iv(iv, increment):
	num=int(iv.encode('hex'),16)
	s=hex(num+increment)
	s=s[2:len(s)-1].decode('hex')
	return s
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))
def decryptWithCBC(key, ciphertext):
	cipher=AES.new(key,AES.MODE_ECB)
	iv=ciphertext[:AES.block_size]
	ciphertext=ciphertext[AES.block_size:]
	vector=iv
	remain=ciphertext
	plain_text=""
	while len(remain)>=AES.block_size:
		block=remain[:AES.block_size]
		vector=xor_strings(vector,cipher.decrypt(block))
		print vector
		plain_text=plain_text+vector
		vector=block;
		remain=remain[AES.block_size:]
	return plain_text
def decryptWithCRT(key, ciphertext):
	cipher=AES.new(key,AES.MODE_ECB)
	iv=ciphertext[:AES.block_size]
	ciphertext=ciphertext[AES.block_size:]
	vector=iv
	remain=ciphertext
	plain_text=""
	while len(remain)>0:
		block=remain[:AES.block_size]
		print xor_strings(cipher.decrypt(vector),block)
		plain_text=plain_text+xor_strings(cipher.encrypt(vector),block)
		remain=remain[AES.block_size:]
		vector=increment_iv(vector,1)
