import sys


def main():
    list = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for i in list:
        for j in range(0, 3):
            i[j] = int(input("enter num:\t"))
    print(check_line(list))

def print_list(l):
    for i in l:
        print("\n")
        for j in i:
            print(str(j)+",")
def check_line(l):
    flag=0
    for i in l:
        if flag!=0:
            return flag
        for j in i:
            first=i[0]
            if i[j]==first:
                flag=first
            else:
                flag=0
    return flag

def check_cross(l):
    flag=0
    for i in l:
        if flag!=0:
            return flag
        for j in i:
            first = i[j]
            if i[j + 1] == first:
                flag = first
            else:
                flag=0
    return flag


if __name__ == "__main__":
      main()