import sys


def main():
    sum=0
    list = []
    number = input("enter number:\t")
    while number != "stop":
        list.append(int(number))
        number = input("enter number:\t")
    if list is None:
        print("List is empty")
    else:
        for i in list:
            sum += i
        print("The Sum is: "+str(sum))



if __name__ == "__main__":
    main()