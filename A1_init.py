#!/usr/bin/env python3

import os
import random
import hashlib

#var declaration
salt = "salt.txt"
shadow = "shadow.txt"
tries=0


#Create salt and shadow files if not no records exist
if not os.path.exists(salt):

    with open(salt, "w") as f:
        f.write("")
    with open(shadow, "w") as f:
        f.write("")

#Request username input
uname=input("Please enter your username to create an account: ")

#Check if account exists
with open (salt) as f:
    for line in f:
        if line.split(":")[0] == uname:
            print("Username already exists. ")
            break
    else:
        #Create password
        while tries<10:
            tries+=1
            passwd=input("Please enter your password: ")
            if len(passwd) >= 8 and any(char in passwd for char in "$%&_"):

                #Confirm password
                if input("Please confirm password: ")== passwd:
                        
                    #Get clearance
                    clear=input("Please enter the clearance code (0, 1, 2, or 3): ")    
                    if clear in ["0", "1", "2", "3"]:

                        #Generate new salt and add to salt.txt
                        passSalt = ''.join(random.choices("0123456789", k=8))
                        with open(salt, "a") as st:
                            st.write(uname + ":" + passSalt + "\n")
                        
                        #Generate hash and add to shadow.txt (MD5)
                        passSaltHash=passwd + passSalt
                        passSaltHash = hashlib.md5(passSaltHash.encode()).hexdigest()
                        with open(shadow, "a") as s:
                            s.write(uname + ":" + passSaltHash + ":" + clear + "\n")
                        print("Account created successfully.")
                        break

                    else:
                        print("Invalid clearance code.")
                        continue

                else:
                    print("Passwords do not match.")
                    continue

            else:
                #Query user for different password
                print("Password must be at least 8 characters long and contain at least one special character ($, %, &, or _).")
                continue

        if tries >= 10:
            print("Please try again by restarting the program.")
