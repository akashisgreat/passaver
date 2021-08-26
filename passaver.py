# Python 3.7
# Author - akashisgreat
# Purpose - Auto generate Random Passwords and save it with UserName and CompanyName in text form.

import random
#import clipboard

print("\n\t\t** Your PASSWORD Saver. **\n")
password_length = 10     # Change no. with your desired passwd length.
file_name = ".Docsys.sysImport.txt" # Change the file name which you want to keep in.
                                    # Remember! file name should be starting with "."(dot) because, in linux it is called hidden file.
                                    # e.g. ".filename.tXX"
value = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@#$%&*-+()![]\|\,.*:;/?_"
password = random.sample(value, password_length)
password = "".join(password)
print("Your password is:>> ",password)
#clipboard.copy(password)
#print("* its Copied and use it :)\n")

asksave = input("Do you want to save this(y/n): ")
print("")
asksave = asksave.lower()
if asksave=="y":
    text_file = open(file_name,'a')
    user = input("Enter User Name: ")
    if user=="":
        text_file.write("[Not entered]")
    else:
        text_file.write(user)
    text_file.write(" || ")
    campany = input("Enter Company Name (e.g. fb,insta): ")
    if campany=="":
        text_file.write("[Not entered]")
    else:
        text_file.write(campany)
    text_file.write(" || ")
    text_file.write(password)
    text_file.write("\n")
    text_file.close()
    print("\n\tYour password has been saved.\n")
elif asksave=="n":
    print("\tPassword not saved.\n\tDone.\n")
    exit()
else:
    print("\tPassword not saved.\n\texit\n")
    exit()
