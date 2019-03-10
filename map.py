import sys


def main():
    list = [1,2 ,3]
    map(f,list)

def f(t):
    return t*2
def map(f,l):
    for i in l:
        i = f(i)
        print(i)


if __name__ == "__main__":
      main()