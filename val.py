try:

    age = 12
    if age <18:

        raise ValueError("AGE for vote 18+")
    else:
        ("elgible for vote")

except ZeroDivisionError as e:
    print("divison not possiblr" + str(e))

except ValueError as e:
    print(str(e))
except:

    print("Exception occured")

else:
    print("executed suceess")
finally:
    print("nava")
