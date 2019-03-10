import sys


def main():
    id=input("enter id: ")
    flag=1
    sum=0
    counter = 0
    for dig in id:
        if counter<8:
            if flag==1:
                sum += int(dig)*1
                flag += 1
            elif flag==2:
                if int(dig)*2<10:
                    sum += int(dig) * 2
                    flag -= 1
                else:
                    num = int(dig)*2
                    num = int(num/10+num%10)
                    sum += num
                    flag -= 1
        else:
            if 10-sum%10==int(dig):
                print("Valid ID")
            else:
                print("Not Valid ID")
        counter += 1

if __name__ == "__main__":
      main()