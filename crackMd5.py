import hashlib
def crackMd5(dst):
    dst = dst.lower()
    print(dst)
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    word = str(a) + str(b)+ str(c)+str(d)
                    tmp =  hashlib.md5(word).hexdigest()
                    if dst == tmp:
                       return word
    return None

def de_md5Code(md5Code):
    for i in range(0,10000):
     num = str(i)
     code = hashlib.md5(num).hexdigest()
     if(code==md5Code):
      return num
    else:
     return "0000"
if __name__=="__main__":
    raw_input(de_md5Code("d785bf9067f8af9e078b93cf26de2b54"))

