



try:
    a=10
    b=50
    c= a/b
    print(c)

except ZeroDivisionError as e:

    print("divison not possible by zero")

except:
    print("Exception occured")

else:
    print("executed suceess")
finally:
    print("nava")