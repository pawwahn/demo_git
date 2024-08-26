def div(a,b):

    try:
        res = a/b
    except ZeroDivisionError:
        print("Why are you dividing it by zero :(")
    else:
        print(f"Division is successful and the res is {res}")
    finally:
        print("This block runs no matter what")

div(10,0)