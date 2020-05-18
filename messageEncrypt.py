# https://github.com/gopuu/DeepKey-Algorithm/
#============= MSG ENCRYPTION ==========
def msgEncrypt(txt):
    str1=list(txt)
    str2=""
    for n in str1:
        str2+=chr(ord(n)+2)
    #print(str2)
    #reverse-----------------------
    str2=list(str2[::-1])
    str2="".join(str2)
    return str2
    
#=========== // MSG ENCRYPTION =========
# https://github.com/gopuu/DeepKey-Algorithm/