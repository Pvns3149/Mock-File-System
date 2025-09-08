#!/usr/bin/env python3

import os
import hashlib
import sys
import subprocess

#Define arg function to handle -i CLI argument
def arg():
    if len(sys.argv) > 1 and sys.argv[1] == "-i":
        # Run A1_Init
        subprocess.run([sys.executable,"A1_init.py"])
        exit()

#Run arg if it is called directly to check for arguments
if __name__ == "__main__":
    arg()


#var declaration
salt = "salt.txt"
shadow = "shadow.txt"
filesPath = "Files.store"
count=0
found=False

#Check if salt and shadow files exist
if not os.path.exists(salt) or not os.path.exists(shadow):
    print("Salt and/or shadow file does not exist. Please run A1_init.py first.")
    exit()

#Test output
print("MD5 (This is a test) = " + hashlib.md5("This is a test".encode()).hexdigest())

while count < 10:

    #Request username and password input
    uname = input("Please enter your username to log in: ")
    passwd = input("Please enter your password to log in: ")

    #Check if account exists
    with open (salt) as f:
        for line in f:
            if line.split(":")[0] == uname:
                print(uname + " found in " + salt)
                passSalt = line.split(":")[1].strip()
                print ("Salt retrieved: " + passSalt)

                #Hashing 
                print("Hashing ...")
                passSaltHash = passwd + passSalt
                passSaltHash = hashlib.md5(passSaltHash.encode()).hexdigest()
                print("Hash value: " + passSaltHash)

                #Compare against shadow.txt records
                with open(shadow) as s:
                    for line in s:
                        if line.split(":")[0] == uname and line.split(":")[1] == passSaltHash:
                            print("Login successful.")
                            found=True

                            #Assign clearance
                            clear=line.split(":")[2].strip()
                            break
                break

        if not found:
            print("Incorrect username or password.")
            count += 1

        else:
            break
        

if count >= 10:
    print("Maximum login attempts exceeded.")
    exit()

#Verify authentication
print("Authentication for user " + uname + " complete.")
print("The clearance for " + uname + " is: " + clear + ".")

#Load Files.store and create if not exist
files = []

if not os.path.exists(filesPath):
    with open(filesPath, "w") as f:
        f.write("")
else:
    with open(filesPath) as fp:
        for line in fp:
            files.append([line.split(":")[0],line.split(":")[1],line.split(":")[2].strip()])

#Display menu
while True:
    found = False
    choice = input("Options: (C)reate, (A)ppend, (R)ead, (W)rite, (L)ist, (S)ave or (E)xit \n ")
    
    if choice in ["C", "c"]:

        #Search for file
        filename = input("Filename: ")
        for f in files:
            if f[0] == filename:
                print("File already exists.")
                found = True
                break
        
        if not found :

            #Create file
            files.append([filename, clear, uname])
            print("File created.")

        continue

    elif choice in ["A", "a","W", "w"]:

        #Request filename and check for clearance (No write down)
        filename = input("Filename: ")
        for f in files:
            if f[0] == filename:
                print("File found.")
                found = True
                if f[1] >= clear:
                    print("Action Successful.")
                else:
                    print("Action Denied.")
                break

        if not found :
            print("File not found.")
        continue

    elif choice in ["R", "r"]:

        #Request filename and check for clearance (No read up)
        filename = input("Filename: ")
        for f in files:
            if f[0] == filename:
                found = True
                print("File found.")
                if f[1] <= clear:
                    print("Action Successful.")
                else:
                    print("Action Denied.")
                break

        if not found :
            print("File not found.")
        continue
    
    elif choice in ["L", "l"]:

        #List all files
        print("Files: ")
        if files.__len__() > 0:
            for f in files:
                print(f[0])
        else:
            print("No files found.")
        continue

    elif choice in ["S", "s"]:


        #Save changes to file
        with open(filesPath, "w") as fp:
            for f in files:
                fp.write(f[0] + ":" + f[1] + ":" + f[2] + "\n")
        print("Changes saved." )
        continue

    elif choice in ["E", "e"]:
        choice = input("Shut down the FileSystem? (Y)es or (N)o \n")
        if choice in ["Y", "y"]:
            exit()
        else:
            continue
    