# Mock-File-System
Mock File System implementing BLP Model Access control policy


Compilation instructions:
1. Move both files to the same directory
2. Run the A1_init.py file to create the user
3. Run the A1_access.py file to log into the System

Files can be run on CLI with the python3 <<filename>> command

To run the file by typing "FileSystem" into the system, follow the steps below:
(Note: This method runs on linux)

1. Move both files into the home directory
2. Enter the "source setup.bash" command to run the setup 
3. Enter "FileSystem" or "FileSystem -i" to begin functions



Reduction:
The file is implemented in 2 python files. A1_init handles registration by creating the salt.txt and shadow.txt files if they do not exist first.\

A1_init:
1. The input username is checked against salt.txt to see if it exists, if it does not, a password with length >8 and any char in $,%,&,_ is requested
2. The salt and username are saved into salt.txt while the PassSaltHash is generated with MD5 and saved into shadow.txt along with the username and clearance level.

A1_access:
1. The system begins by asking for a username and checking if it exists in salt.txt
2. If it exists, the system compares the hash with shadow.txt
3. The system allows up to 10 login attempts
4. The files are then loaded into a 2D array containing filename, owner and clearance for each record
5. Options are displayed
6. When a file is created, existing files are checked to make sure the file does not already exist then the file is created
7. When a file is appended or written, the system checks if the file's clearance is higher than or equal to the current user's clearance. If it is then it allows the action in accordance with the no write down policy.
8. When a file is read, the system checks if the file's clearance is less than or equal to the current user's clearance. If it is then it allows the action in accordance with the no read up policy.
9. A list of file names can be displayed
10.The contents of the 2D array can be saved to the Files.store file to overwrite the current contents and save the files.
11.The system repeats until the exit command is entered. 