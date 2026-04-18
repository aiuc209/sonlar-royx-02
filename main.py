def eng_yaqin_fibonacci(son):
    a, b = 0, 1
    while a < son:
        a, b = b, a + b
    if abs(a - son) < abs(b - son):
        return a
    else:
        return b

def sonlarni_fibonacciga_aylantir(sonlar):
    fibonaccilar = []
    for son in sonlar:
        fibonaccilar.append(eng_yaqin_fibonacci(son))
    return fibonaccilar

sonlar = [10, 20, 30, 40, 50]
print(sonlarni_fibonacciga_aylantir(sonlar))
