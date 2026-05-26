
# 1. Verificar se número é par ou ímpar
def par_ou_impar(n):
    return "Par" if n % 2 == 0 else "Ímpar"

# 2. Fatorial
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# 3. Verificar se é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testes
print(par_ou_impar(4))    # Par
print(fatorial(5))         # 120
print(eh_primo(7))         # True