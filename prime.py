def is_prime(num):
    prime = True
    for c in range(2, num + 1):
        if num == c:
            continue
        elif num % c == 0:
            prime = False

    return prime


is_prime(18)
# Write your code here.
#
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()