import sys



def main():
    code = "1234"
    balance = 500
    user_code = input("Enter Your Secret Code:\t")
    while not code_checking(user_code, code):
        user_code = input("Enter Your Secret Code:\t")
    while True:
        print("enter A to check your balance")
        print("enter B to withdraw money")
        print("enter C to change your secret code")
        print("enter D to quit")
        choice = input()
        if choice == "A":
            user_code = input("Enter Your Secret Code:\t")
            while not code_checking(user_code, code):
                user_code = input("Enter Your Secret Code:\t")
            print(balance)

        elif choice == "B":
            user_code = input("Enter Your Secret Code:\t")
            while not code_checking(user_code, code):
                user_code = input("Enter Your Secret Code:\t")
            print("enter 1 to withdraw 20,enter 2 to withdraw 50"
                  " or enter 3 to select the amount")
            choice = input()
            if choice == "1":
                balance = withdraw(balance, 20)
            elif choice == "2":
                balance = withdraw(balance, 50)
            elif choice == "3":
                amount = int(input("enter the amount you want to withdraw:\t"))
                if amount > 0:
                    balance = withdraw(balance, amount)
                else:
                    print("amount must be greater than 0")

        elif choice == "C":
            user_code = input("Enter Your Secret Code:\t")
            while not code_checking(user_code, code):
                user_code = input("Enter Your Secret Code:\t")
            new_code = input("enter new secret code:\t")
            code = new_code

        elif choice == "D":
            sys.exit()


def code_checking(user_code, code):
    if user_code == code:
        return True
    return False


def withdraw(balance, amount):

      balance -= amount
      print("Success")
      return balance




if __name__ == "__main__":
    main()

