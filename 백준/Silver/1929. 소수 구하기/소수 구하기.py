# ------ 에라토스테네스의 체 알고리즘 사용 ------ #
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers

M, N = map(int, input().split())

# N까지의 모든 소수를 한 번만 계산합니다.
primes = sieve_of_eratosthenes(N)

# [M, N] 범위 내의 소수를 필터링하여 출력합니다.
for prime in primes:
    if prime >= M:
        print(prime)