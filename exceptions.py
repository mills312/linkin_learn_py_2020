try:
    u_resp=input("what should I devide by?")
    i = int(u_resp)
    x = 10/i
    print(x)
except ZeroDivisionError as e:
    print("Can't devide by zero", e)
except ValueError as e:
    print("Need a valid number", e)
except:
    print("not working")
finally:
    print("Thank you for dividing")
