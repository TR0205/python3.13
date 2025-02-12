# 素数かを判定

n = 54

def is_prime(n: int) -> bool:
    """nが素数かを判定する"""
    # 1以下の場合は素数ではない
    if n < 2:
        return False
    # 2,3は素数
    if n in (2, 3):
        return True
    # 2,3で割り切れる数は素数ではない
    if n % 2 == 0 or n % 3 == 0:
        return False       
    # 25以降の判定
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(n))