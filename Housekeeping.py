import os

#print(os.getcwd()) #To know the current working dirctory
#print(os.listdir())  #Listing te content of current directory

try:
    # Changing the current path to the path where housekeepin needs to be performed
    os.chdir(r"C:\Users\Anjika")

    # printing the present directory
    print(os.getcwd())
    l = os.listdir()
    print(l)

    #Removing the files whose names endswith .security.txt
    for i in range(len(l)):
        if l[i].endswith(".security.txt"):
            os.remove(l[i])
        else:
            pass

    # cross-checking the files
    print(l)

except FileNotFoundError:
    print("path does not exist")
finally:
    print("code completed")

