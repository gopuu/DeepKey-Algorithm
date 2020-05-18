# https://github.com/gopuu/DeepKey-Algorithm/
class Decrypt:
    key=""
    arr=[[],[],[],[]]
    size=0

    ##### DECRYPTION #####
    def __init__(self,finalKey):
        self.finalKey=list(finalKey)        
        key_length=len(self.finalKey)

        #convert to 12*16 array
        tmp_arr=[[],[],[],[],[],[],[],[],[],[],[],[]]
        j=-1
        #print("\ninit: ",self.finalKey)
        for i in range(len(self.finalKey)):
            if i%16==0:
                j+=1
            tmp_arr[j].append(self.finalKey[i])
     
        self.size=len(tmp_arr)
        #print("\ntmp_err size: ",self.size)
        for n in range(len(tmp_arr)): #swap positions 1st with 3rd & 4th with last
            last=(int(float(self.size/2))-1)
            if n==0 or n==last+1:
                tmp_arr[n],tmp_arr[n+last] = tmp_arr[n+last],tmp_arr[n]
        #display tmp-array
        for i in range(len(tmp_arr)):
            self.key=tmp_arr[i]
        #print("\ninit-key: ", self.key)
        print("\ninit-array:\n")        
        for i in range(len(tmp_arr)):
            print(tmp_arr[i])

    def KeyToArray(self,key):        # key-to-1D.array conversion ------
        #array 4*4
        arr=[[],[],[],[]]
        self.key=list(key)
        print("\nkey2arr: ",self.key)
        print("\nkey-len: ",len(self.key))
        
        print("\narr: ",arr)

        j=-1
        for i in range(len(self.key)):
            if i%4==0 and i<=len(self.key):
                j+=1
            arr[j].append(self.key[i])
        self.arr=arr
    def show_array(self):
        #for n in range(len(self.arr)):
            print(self.arr)
        
    def reverse_round_12(self):     # reverse of round 12 ---------
        self.KeyToArray(self.key)
        self.size=len(self.arr)
        print("\nr-12")
        self.show_array()

        for n in range(int(float(self.size/2)),self.size):
            for m in range(int(float(self.size/2)),self.size):
                self.arr[n][m]=chr(ord(self.arr[n][m])-2)

    def reverse_round_11(self):     # reverse of round 11 ---------
        self.show_array()
        for n in range(int(float(self.size/2)),self.size):
            for m in range(int(float(self.size/2)),self.size):
                self.arr[n][m]=chr(ord(self.arr[n][m])-2)
            
    def reverse_round_10(self):     # reverse of round 10 ---------
        self.show_array()
        for n in range(int(float(self.size/2)),self.size):
            for m in range(int(float(self.size/2))):
                self.arr[n][m]=chr(ord(self.arr[n][m])-1)
            
    def reverse_round_9(self):     # reverse of round 9 ---------
        self.show_array()
        for n in range(int(float(self.size/2))):
            for m in range(int(float(self.size/2)),self.size):
                self.arr[n][m]=chr(ord(self.arr[n][m])-2)
            
    def reverse_round_8(self):     # reverse of round 8 ---------
        self.show_array()
        for n in range(int(float(self.size/2))):
            for m in range(int(float(self.size/2))):
                self.arr[n][m]=chr(ord(self.arr[n][m])-1)
            
    def reverse_round_7(self):     # reverse of round 7 ---------
        self.show_array()
        for n in range(self.size):
            for m in range(int(float(self.size/2))):
                self.arr[n][m],self.arr[n][m+2]=self.arr[n][m+2],self.arr[n][m]
            
    def reverse_round_6(self):     # reverse of round 6 ---------
        self.show_array()
        for n in range(int(float(self.size/2))):
            self.arr[n],self.arr[n+2]=self.arr[n+2],self.arr[n]
            
    def reverse_round_5(self):     # reverse of round 5 ---------
        self.show_array()
        for n in range(self.size):
            for m in range(int(float(self.size/2))):
                self.arr[n][m],self.arr[n][self.size-(m+1)]=self.arr[n][self.size-(m+1)],self.arr[n][m]
            
    def reverse_round_4(self):     # reverse of round 4 ---------
        self.show_array()
        for n in range(int(float(self.size/2))):
            self.arr[n],self.arr[self.size-(n+1)]=self.arr[self.size-(n+1)],self.arr[n]
            
    def reverse_round_3(self):     # reverse of round 3 ---------
        self.show_array()
        for n in range(self.size):
            for m in range(len(self.arr[n])):
                if m==0 or m==2:
                    self.arr[n][m],self.arr[n][m+1]=self.arr[n][m+1],self.arr[n][m]
            
    def reverse_round_2(self):     # reverse of round 2 ---------
        self.show_array()
        for n in range(len(self.arr)):
            if n==0 or n==2:
                self.arr[n],self.arr[n+1]=self.arr[n+1],self.arr[n]
            
    def reverse_round_1(self,pKey):     # reverse of round 1 ---------
        self.show_array()
        s=self.list2Arr(self.arr)
        #if s==pKey or pKey==encryptKey.encrypt():
        if s==pKey:
            with open ('DecryptKey.txt','w') as f:
                f.write(s+'\n')
                f.close()
            print("\nDecrypted Key Stored in File 'DecryptKey.txt' !!")
            return 1
        else:
            print("sKey: ",s,"\npKey: ",pKey)
            return 0
    def list2Arr(self,arr):
        s=""
        for n in range(len(self.arr)):
            for m in range(len(self.arr[n])):
                s+=self.arr[n][m]
        return s
#============= DECRYPTION =========
def decrypt(txt,pKey):
    #finalKey=input("Enter Encrypted Key: ")
    cipherMsg=list(txt)
    finalKey=""
    cipherTxt=""
    for n in range(len(cipherMsg)):
        if n<192:
            finalKey+=cipherMsg[n]
        else:
            cipherTxt+=cipherMsg[n]
              
    #print("\nfinalKey: ",finalKey)
    #print("\nLength: ",len(finalKey))
    decrypt=Decrypt(finalKey)
    decrypt.reverse_round_12()
    decrypt.reverse_round_11()
    decrypt.reverse_round_10()
    decrypt.reverse_round_9()
    decrypt.reverse_round_8()
    decrypt.reverse_round_7()
    decrypt.reverse_round_6()
    decrypt.reverse_round_5()
    decrypt.reverse_round_4()
    decrypt.reverse_round_3()
    decrypt.reverse_round_2()
    tmp=decrypt.reverse_round_1(pKey)
    if tmp:
        return cipherTxt
    else:
        return tmp
#===========// DECRYPTION =========
# https://github.com/gopuu/DeepKey-Algorithm/