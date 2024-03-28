def is_prime(num):
    if num<=1:
        return False
    elif num==2 or num==3:
        return num
    elif num%2==0 or num%3==0:
        return False
    else:
        return num

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
