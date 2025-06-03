def divide_numbers():
    try:
        num1=int(input("enter numerator"))
        num2=int(input("Enter denominator"))
        result=num1/num2
    except ValueError:
        print("pls enter only numbers")
    except ZeroDivisionError:
        print("Denominator cannot be zero")
    else:
        print("resul:",result)
    finally:
        print("operation success")
divide_numbers()

def read_file():
    filename = input("enter the file name")
    try:
        with open(filename,"r") as f:
            content=f.read()
            print("file content",content)
    except FileNotFoundError:
        print("The files not exists,pls check once")
    except PermissionError:
        print("tou dont have permission to read this")
    else:
        print("file read success")
    finally:
        print("operation success")
read_file()

