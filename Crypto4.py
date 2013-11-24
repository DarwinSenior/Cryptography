import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
def constructing(g, bits,code):
    assert g<256
    assert len(code)+1==bits;
    s="".join('\x00' for i in range(16-bits))+chr(g)+code;
    t="".join('\x00' for i in range(16-bits))+"".join(chr(bits) for i in range(bits));
    return strxor(s,t)

class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding
if __name__ == "__main__":
    po = PaddingOracle()
    cipherText="f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
    blocks=[cipherText.decode('hex')[i*16:(i+1)*16] for i in range(len(cipherText.decode('hex'))/16)]
    print(po.query(cipherText))       # Issue HTTP query with the given argument

def getList(blocks,po):
code="";
count=0
for j in xrange(1,17):
    newCode=code;
    for i in range(256):
        newBlock=blocks[2:4]
        newBlock[0]=strxor(newBlock[0],constructing(i,j,code))
        if(po.query("".join(newBlock).encode('hex'))):
            newCode=chr(i)+code
            count+=1
    code=newCode
print code
code2="The Magic Words are Squeamish Ossifrage"


