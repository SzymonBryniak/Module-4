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
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)
print(d3)
