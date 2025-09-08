#Add a bash alias for the A1_access.py script and map to the FileSystem command
echo "alias FileSystem='~/A1_access.py'" >> ~/.bashrc

#Reload the bash file to apply changes to the current terminal
source ~/.bashrc

#for both files to reformat to allow #! to run on linux
sed -i 's/\r$//' A1_access.py
sed -i 's/\r$//' A1_init.py

#Make both files executable
chmod +x A1_init.py
chmod +x A1_access.py
