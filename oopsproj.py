class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("Welcome to ChatBook!! How would like you to proceed\n" \
        "1. Press 1 to signup\n" \
        "2. Press 2 to signin\n" \
        "3. Press 3 to write a post\n" \
        "4. Press 4 to message a friend\n" \
        "5. Press any other key to exit ")

        if user_input == "1":
            self.signup()
        if user_input == "2":
            self.signin()
        if user_input == "3":
            pass
        if user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Set up your email : ")
        pwd = input("Set up your password : ")
        self.username = email
        self.password = pwd 
        print("You have signed up succesfully!!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("Please signin by pressing 1 in menu")
        else:
            uname = input("Enter your email : ")
            pwd1 = input("Enter your password : ")
            if self.username==uname and self.password==pwd1:
                print("You have signed in succesfully!!")
                self.loggedin = True
            else:
                print("Please input correct credentials\n")
                self.signin()

        print("\n")
        self.menu()

        

        


obj = chatbook()