import os

# Joshua Taylor
# May 14, 2020
# This week we will create a program that performs file processing activities.
# Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.

directory = input("Enter the directory that you want to save the file : ")

filename = input("Enter the filename : ")

name = input("Enter your name : ")

address = input("Enter your address : ")

phone_number = input("Enter your phone number : ")
def main():
#checking if the directory exists

    if os.path.isdir(directory):

        #createing and opening the file to write

        writeFile = open(os.path.join(directory,filename),'w')

        #writing the data by comma seperated

        writeFile.write(name+','+address+','+phone_number+'\n')

        #close the file after writing is done

        writeFile.close()

        print("File contents:")

        #reading the file for proof of storing

        readFile = open(os.path.join(directory,filename),'r')

        for line in readFile:
            print(line)

    else:
        print("Sorry that directory is not exists...")


    readFile.close()

main()