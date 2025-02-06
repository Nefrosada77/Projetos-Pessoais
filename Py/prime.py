def comp_prime(n: int,a: list):
    if n >= 1000:
        return a
    prime = True
    for num in a:
        if n % num == 0:
            prime = False
            break
    if prime == True:
        a.append(n)
    return comp_prime(n+1,a)

a = []

print(comp_prime(2,a))
