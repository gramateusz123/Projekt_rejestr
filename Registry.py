import glob, os, time
file = "nothing"
decision = 0
user_login = "admin"
user_password = "access1"
print("Login: ")
login_provided = input()
print("Password: ")
password_provided = input()

while True:

    if login_provided == user_login and password_provided == user_password:
        print("Welcome to your private registry!")
        print("1. If you want to create your data, type 1 and press enter.")
        print("2. If you want to read your data, type 2 and press enter.")
        print("3. If you want to edit new file with your data, type 3 and press enter.")
        print("4. If you want to delete your files, type 4 and press enter.")
        print("5. If you want to exit.")
        decision = input()

    else:
        print("Wrong password or login!")
        break

    if decision == "1":
        print("Name your file: ")
        file = input()
        file += ".txt"
        data = open(file, "a+")
        print("Name: ")
        name = input()
        data.write("Name: ")
        data.write(name)
        data.write("\n")

        print("Age: ")
        age = input()
        data.write("Age: ")
        data.write(age)
        data.write("\n")


        print("From: ")
        fromx = input()
        data.write("From: ")
        data.write(fromx)
        data.write("\n")

        print("Hobby: ")
        hobby = input()
        data.write("Hobby: ")
        data.write(hobby)
        data.write("\n")
        data.close()
        print("Registry created successfully !")
        time.sleep(2)

    elif decision == "2":
        print("Which file do you want to open?")
        os.chdir(".")
        for files in glob.glob("*.txt"):
            print(files)
        file = input()
        try:
            data = open(file, "r")
            print(data.read())
            data.close()
        except:
                print("This file doesn't exist, or you don't have any files!")
        time.sleep(1)
        print("Do you want to close the program? Y/N")
        choice = input()
        if choice == "Y" or choice == "y":
            print("Bye, bye!")
            break

    elif decision == "5":
        print("Bye, bye!")
        break

    elif decision == "3":
        print("Which file do you want to edit?")
        os.chdir(".")
        for files in glob.glob("*.txt"):
            print(files)
        file = input()
        data = open(file,"r")
        print("This is the registry of", file)
        print(data.read())
        data.close()
        print("Do you want to edit all profile or one information? all/one")
        choice = input()
        if choice == "all":
            os.remove(file)
            print("Rename your file: ")
            file = input()
            file += ".txt"
            data = open(file, "w+")
            print("Name: ")
            name = input()
            data.write("Name: ")
            data.write(name)
            data.write("\n")

            print("Age: ")
            age = input()
            data.write("Age: ")
            data.write(age)
            data.write("\n")

            print("From: ")
            fromx = input()
            data.write("From: ")
            data.write(fromx)
            data.write("\n")

            print("Hobby: ")
            hobby = input()
            data.write("Hobby: ")
            data.write(hobby)
            data.write("\n")
            data.close()
    elif decision == "4":
            print("Which file do you want to delete ? If you don't want to, type 'i'm sorry'. ")
            os.chdir(".")
            for files in glob.glob("*.txt"):
                print(files)
            files = input()
            if files == "i'm sorry":
                break
            else:
                print("Are you sure you want to delete this file ? Y/N")
                decision = input()
                if decision == "Y":
                    os.remove(files)
