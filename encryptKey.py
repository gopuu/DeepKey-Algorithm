# https://github.com/gopuu/DeepKey-Algorithm/
class Encrypt:
    aa,keys=[0,3,4,7],[]
    arr=[[],[],[],[],[],[],[],[]]
    size=""
    def __init__(self,text):
        #text="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz@#"
        self.text=text    

        #declaring array & storing string into 2D-Array
        self.size=len(self.arr)

    def toArray(self):
        #array 8*8
        self.text=list(self.text)
        j=-1
        for i in range(len(self.text)):
            if i%8==0:
                j+=1
            self.arr[j].append(self.text[i])
    #--------------- show array -----------------
    def show_array(self):
        print("")
        for n in self.arr:
            print(n)

    def generate_key(self,arr): # generate Key, from 4 rows & merge it------
        key=""
        for n in range(len(self.arr)):      #row
            for i in self.aa:
                if i==n:
                    for m in range(len(self.arr[n])):      #col
                        for j in self.aa:
                            if j==m:
                                key=key+self.arr[n][m]
        self.keys.append(key)
        return key      # // generate Key -----------------

    def round_1(self):      # round 1 ------------------------
        n=self.generate_key(self.arr)
        with open ('PlainKey.txt','w') as f:
            f.write(n)

    def round_2(self):      # round 2 ---------------------
        for n in range(self.size):
            last=(int(float(self.size/2))-1)
            if n==0 or n==last+1:
                self.arr[n],self.arr[n+last]=self.arr[n+last],self.arr[n]
        n=self.generate_key(self.arr)

    def round_3(self):      # round 3 ---------------------
        for n in range(self.size):
            last=(int(float(self.size/2))-1)
            for m in range(self.size):
                if m==0 or m==last+1:
                    self.arr[n][m],self.arr[n][m+last]=self.arr[n][m+last],self.arr[n][m]
        n=self.generate_key(self.arr)

    def round_4(self):      # round 4 ---------------------
        for n in range(int(float(self.size/2))):
            self.arr[n],self.arr[self.size-(n+1)]=self.arr[self.size-(n+1)],self.arr[n]
        n=self.generate_key(self.arr)

    def round_5(self):      # round 5 ---------------------
        for n in range(self.size):
            size_n=len(self.arr)
            for m in range(int(float(size_n/2))):
                self.arr[n][m],self.arr[n][size_n-(m+1)]=self.arr[n][size_n-(m+1)],self.arr[n][m]
        n=self.generate_key(self.arr)

    def round_6(self):      # round 6 ---------------------
        for n in range(int(float(self.size/2))):
            self.arr[n],self.arr[n+4]=self.arr[n+4],self.arr[n]
        n=self.generate_key(self.arr)
        
    def round_7(self):      # round 7 ---------------------
        for n in range(len(self.arr)):
            for m in range(int(float(len(self.arr[n])/2))):
                self.arr[n][m],self.arr[n][m+4]=self.arr[n][m+4],self.arr[n][m]
        n=self.generate_key(self.arr)

    def round_8(self):      # round 8 ---------------------
        for n in range(int(float(self.size/2))):
            for m in range(int(float(self.size/2))):
                self.arr[n][m]=chr(ord(self.arr[n][m])+1)
        n=self.generate_key(self.arr)

    def round_9(self):      # round 9 ---------------------
        for n in range(int(float(self.size/2))):
            for m in range(int(float(self.size/2)),self.size):
               self.arr[n][m]=chr(ord(self.arr[n][m])+2)
        n=self.generate_key(self.arr)
   
    def round_10(self):      # round 10 ---------------------
        for n in range(int(float(self.size/2)),self.size):
            for m in range(int(float(self.size/2))):
                self.arr[n][m]=chr(ord(self.arr[n][m])+1)
        n=self.generate_key(self.arr)
   
    def round_11(self):      # round 11 ---------------------
        for n in range(int(float(self.size/2)),self.size):
            for m in range(int(float(self.size/2)),self.size):
               self.arr[n][m]=chr(ord(self.arr[n][m])+2)
        n=self.generate_key(self.arr)
   
    def round_12(self):      # round 12 ---------------------
        for n in range(int(float(self.size/2)),self.size):
            for m in range(int(float(self.size/2)),self.size):
               self.arr[n][m]=chr(ord(self.arr[n][m])+2)
        n=self.generate_key(self.arr)
     
    def SaveToFile(self):        
        ##### STORING KEY, get 192 BYTE  #####   
        finalKey=""
        for n in range(len(self.keys)): #swap positions 1st with 3rd & 4th with last
            if n==0 or n==6:
                self.keys[n],self.keys[n+(int(float(len(self.keys)/2)-1))]=self.keys[n+(int(float(len(self.keys)/2)-1))],self.keys[n]
        for n in range(len(self.keys)): #merge keys to 1 key
            finalKey+=self.keys[n]
        #print("\nENCRYPTED KEY:",finalKey)
        key_length=len(finalKey)
        #print("\nLength:",key_length)

        with open ('EncryptKey.txt','w') as f:
            f.write(finalKey)
            f.close()
        print("\nEncrypted Key & PlainText key Stored in \nFile 'EncryptKey.txt' & 'PlainKey.txt' !!")
        return finalKey

#=========== ENCRYPION =========
def encrypt():
    #---- Generating Random Strings ----
    #Using random.choices() 
    import string 
    import random 
    # initializing size of string 
    N = 64
    # using random.choices() to generate random strings 
    res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase+'@#', k = N)) 
    # print result
    text=str(res)
    #print("The generated random string : " + text)
    #print("LEN:",len(text))
    #---- // Generating Random Strings ----

    encrypt=Encrypt(text)
    encrypt.toArray()
    encrypt.round_1()
    encrypt.round_2()
    encrypt.round_3()
    encrypt.round_4()
    encrypt.round_5()
    encrypt.round_6()
    encrypt.round_7()
    encrypt.round_8()
    encrypt.round_9()
    encrypt.round_10()
    encrypt.round_11()
    encrypt.round_12()
    return encrypt.SaveToFile()
    
#===========// ENCRYPTION =========
# https://github.com/gopuu/DeepKey-Algorithm/