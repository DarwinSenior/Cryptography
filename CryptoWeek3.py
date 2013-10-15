from Crypto.Hash import SHA256

fileName='file2.mp4'
block_size=1024
file=open(fileName)
stream=file.read()
tail=len(stream)%block_size

print len(stream)

hash=SHA256.new()
pos=len(stream)
block=stream[pos-tail:]
pos=pos-tail
hash.update(block)
value=hash.digest()

while pos>0:
	block=stream[pos-block_size:pos]
	hash=SHA256.new()
	hash.update(block+value)
	value=hash.digest()
	pos=pos-block_size

print value.encode("hex")