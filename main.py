# https://github.com/gopuu/DeepKey-Algorithm/
import encryptKey
import decryptKey
import messageEncrypt
import messageDecrypt
if __name__ == "__main__":
	i=True
	while i:
		import os
		os.system('cls')
		try:
			print("\n#####  DeepKey Algorithm  #####\n")
			option=int(input("1. Encryption\n2. Decryption\n3. EXIT\nSELECT: "))
			if option==1:
				if os.path.exists('Encrypt.txt'):
					os.remove('Encrypt.txt')
				if os.path.exists('EncryptKey.txt'):
					os.remove('EncryptKey.txt')
				if os.path.exists('PlainKey.txt'):
					os.remove('PlainKey.txt')
				
				txt=input("Enter Message:")
				txt=messageEncrypt.msgEncrypt(txt)
				key=encryptKey.encrypt()
				cipher=key+txt
				#print(cipher)
				with open ('Encrypt.txt','w') as f:
					f.write(cipher)
					f.close()
				print("\nEncrypted Msg Stored in File 'Encrypt.txt' !!")
				        
				input()
			elif option==2:
				if os.path.exists('Decrypt.txt'):
					os.remove('Decrypt.txt')
				if os.path.exists('DecryptKey.txt'):
					os.remove('DecryptKey.txt')

				#txt=input("Enter Cipher Text:")
				#pKey=input("Enter Plain Key:")
				txt=""
				pKey=""
				lines=""

				with open ('Encrypt.txt','r') as f: #get file
					lines=f.readlines()
					f.close()
					#print("\ncipherMsg: ",lines)
					for i in lines:
						#print("\nloop: ",i)
						txt=i

				with open ('PlainKey.txt','r') as f: #get file
					lines=f.readlines(16)
					f.close()
					#print("\npKey: ",line)
					for i in lines:
						#print("\nloop: ",i)
						pKey=i

				cipherMsg=""
				plainMsg=""
				cipherMsg=decryptKey.decrypt(txt,pKey)
				print("\ntxt: ",txt)
				print("\npKey: ",pKey)
				if cipherMsg:
					plainMsg=messageDecrypt.msgDecrypt(cipherMsg)
					print("\nMessage :",plainMsg)
					with open ('Decrypt.txt','w') as f: #store in file
						f.write(plainMsg)
						f.close()
					print("\nDecrypted Msg Stored in File 'Decrypt.txt' !!")     
				else:
					print("invalid key")            
				input()
			elif option==3:
				import sys
				sys.exit()
			else:
				print("error")
			opt=input("do u want to continue [y/n]: ")
			if opt=='n' or option=='N':
				i=0
		except Exception as e:
			raise "Exception"
		else:
			pass
		finally:
			pass
# https://github.com/gopuu/DeepKey-Algorithm/