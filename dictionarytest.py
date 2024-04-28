# def fun(a):
#     if a > 30:
#         return 1
#     else:
#         return a + fun(a + 3)
#
#
# print(fun(25))
# tuple_1 = (1, 2, 4, 8)
# tuple_2 = 1., .5, .25, 125

# print(tuple_1)
# print(tuple_2)
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except ValueError:
        print("Wrong value.")
    except ZeroDivisionError:
        print("Sorry. I cannot divide by zero.")
    except:
        print("I don't know what to do...")