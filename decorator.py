import sys


def main():


 def memorize(function):
      memo = {}

      def wrapper(*args):
            if args in memo:
                  return memo[args]
            else:
                  rv = function(*args)
                  memo[args] = rv
                  return rv

      return wrapper

if __name__ == "__main__":
      main()