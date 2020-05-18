# https://github.com/gopuu/DeepKey-Algorithm/
#============= MSG DECRYPTION ==========
def msgDecrypt(txt):
    str1=""
    str2="".join(txt)
    str2=list(str2[::-1])
    for n in str2:
        str1+=chr(ord(n)-2)    
    return str1
    
#=========== // MSG DECRYPTION =========
# https://github.com/gopuu/DeepKey-Algorithm/