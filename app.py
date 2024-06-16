master_pwd = input("Master Password?: ")

def view():
    pass


def add():
    name = input("Account Name: ")
    pwd =  input("Password: ")
    #open file in a mode , w will clear entire file and make a new one, r will read the file cant edit or destroy file, a mode append mode allows to add to end of existing file or create new file if that file does not exist
    with open("passwords.txt", 'a') as f:
        f.write(name + '|' + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add)?, press q to quit  ").lower()
    if mode =='q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
        #brings them to top of while loop
        continue