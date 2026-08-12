import math
def power(base, exp):
    return base ** exp
def sqrt(number):
    if number < 0:
        raise ValueError("음수의 제곱근은 계산할 수 없습니다.")
    return math.sqrt(number)
def magic_multiply(number, magic_factor=7):
    return number * magic_factor
