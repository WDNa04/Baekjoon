def binom_coeff(n,k):
    a = n
    multi_n = 1
    while a>0:
        multi_n *= a
        a -= 1
    b = n-k
    multi_n_k = 1
    while b > 0:
        multi_n_k *= b
        b -= 1
    c = k
    multi_k = 1
    while c > 0:
        multi_k *= c
        c -= 1
    return int(multi_n / multi_n_k / multi_k)

print(binom_coeff(int(input()),int(input())))