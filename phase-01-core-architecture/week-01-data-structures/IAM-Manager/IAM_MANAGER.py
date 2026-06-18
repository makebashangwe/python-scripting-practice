import random

class User:
    def __init__(self, user_ID:int, username:str, clearance_level:str, is_active:bool=True):
        self.clearance_level = clearance_level
        self.is_active = is_active
        self.username= username
        self.user_ID= user_ID

    def get_username(self):
        return self.username

    def get_clearance_level(self):
        return self.clearance_level

    def get_status(self):
        return self.is_active
    def get_user_ID(self):
        return self.user_ID

class IAM_Manager:
    def __init__(self):
        self._userbook = {}

    def verify_user_ID(self,user_ID):
        if user_ID in self._userbook:
            return True
        else:
            return False
    def onboard_user(self,user_ID, username, clearance_level):
        if not self.verify_user_ID(user_ID):
            self._userbook[user_ID] = User(user_ID, username, clearance_level)
            return True
        else:
            return False

    def changeUsername(self,username,new_username):
        for user in self._userbook.values():
            if user.get_username() == username:
                user_ID = user.get_user_ID()
                if self.verify_user_ID(user_ID):
                    self._userbook[user_ID].username = new_username
                    return True
                else:
                    return False
        else:
            return False
    def deactivate_user(self,username):
        for user in self._userbook.values():
            if user.get_username() == username:
                user_ID = user.get_user_ID()
                if self.verify_user_ID(user_ID):
                    if self._userbook[user_ID].get_status():
                        self._userbook[user_ID].is_active = False
                        return True
                    else:
                        return False
            else:
                continue
        return False #if can't find user after all

    def get_active_usernames(self):
        active_user_list = []
        for user in self._userbook.values():
            if user.get_status():
                active_user_list.append(user.get_username())

        return active_user_list

    def get_active_users(self):
        active_user_list = []
        for user in self._userbook.values():
            if user.get_status():
                active_user_list.append(user)

        return active_user_list
    #driver

def show_choices():
    return (f"1. Create Users\n"
            f"2. Show Users\n"
            f"3.Deactive Users\n"
            f"4.Change Username\n"
            f"5.Quit")
def main():
    manager = IAM_Manager()

    while True:
        print(show_choices()) #almost forgot to print it!
        while True:
            try:
                option = int(input("Please select an option: "))
                break
            except ValueError:
                print("Please enter a number")
            except UnboundLocalError:
                print("Please enter a valid option!")

        match option:
            case 1:
                while True:
                    try:
                        creation_num = int(input("How many users would you like to create?"))
                        break
                    except ValueError:
                        print("Please enter a number")
                for i in range(creation_num):
                    user_ID = random.randint(0000, 9000)
                    while True:
                        username = input("Username: ")
                        if username in manager.get_active_usernames():
                            print(f"User {username} already exists!")
                        elif username == "":
                            print("Please enter a valid username!")
                        else:
                            break
                    clearance_level = input("Clearance level: ")
                    success = manager.onboard_user(user_ID, username, clearance_level)
                    if success:
                        print(f"Created {username}!")
                    else:
                        print(f"Failed to create {username}.")

            case 2:

                if len(manager.get_active_usernames())<=0:
                    print("No active users!")
                else:
                    for user in manager.get_active_users() :
                        print(f"Username: {user.get_username()} | clearance level: {user.get_clearance_level()} ")
            case 3:
                if len(manager.get_active_usernames()) <= 0:
                    print("No active users!")
                else:
                    for user in manager.get_active_users():
                        print(f"Username: {user.get_username()} | clearance level: {user.get_clearance_level()} ")
                    username_for_deactivation = input("Please enter the username you want to deactivate: ")
                    if username_for_deactivation in manager.get_active_usernames():
                        status = manager.deactivate_user(username_for_deactivation)
                        if status:
                            print(f"Deactivated {username_for_deactivation}!")
                        else:
                            print("Failed to deactivate user!")
                    else:
                        print("User does not exist!")
            case 4:
                username_canidate= input("Please enter the username you want to change: ")
                if username_canidate in manager.get_active_usernames():
                    new_username = input("Please enter the new username: ")
                    manager.changeUsername(username_canidate, new_username)
                else:
                    print("This username does not exist!")
            case 5:
                print("Quitting...")
                break
            case _:
                print("Please enter a valid option!")

main()