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
if __name__=="__main__":
    raw_input(crackMd5("d785bf9067f8af9e078b93cf26de2b54"))
    # crackMd5("d785bf9067f8af9e078b93cf26de2b54")