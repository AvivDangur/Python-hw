import sys


def main():
    string=input("enter string: ")
    flag=0
    counter=0
    newstring=""
    for c in string:
        if flag==0:
            first=c
            counter+=1
            flag=1
        else:
            if c==first:
                counter+=1
            else:
                newstring+=first
                newstring+=str(counter)
                first = c
                counter = 1

    newstring += first
    newstring += str(counter)
    print(newstring)






if __name__ == "__main__":
      main()