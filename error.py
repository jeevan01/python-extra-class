try:
   a = int(input("Enter a number"))
   b = int(input("Enter another number"))
   ans = a/b
   print(ans)
except ZeroDivisionError as ex :
    print("you cannot divide a number by 0")
except KeyboardInterrupt as kex:
    print("\nProgram exited by user")