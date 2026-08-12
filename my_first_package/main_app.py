import magic_calc.basic_ops as myops
result = myops.add(10, 5)
print(result)

import magic_calc.basic_ops as adops
result4 = adops.subtract(5,2)
print(result4)

import magic_calc.basic_ops as adops
result5 = adops.multiply(5,2)
print(result5)

import magic_calc.basic_ops as adops
result6 = adops.divide(10,5)
print(result6)



import magic_calc.advanced_ops as adops
result1 = adops.power(2,10)
print(result1)

import magic_calc.advanced_ops as adops
result2 = adops.sqrt(3)
print(result2)

import magic_calc.advanced_ops as adops
result3 = adops.magic_multiply(2)
print(result3)


import magic_calc.basic_ops as adops
import magic_calc.advanced_ops
result = adops.add(10,5)
result1 = magic_calc.advanced_ops.sqrt(10)

#F스트링 3개 연습
result1 = magic_calc.advanced_ops.sqrt(10)
print(f"10+5={result}10의 제곱근은 {result1}입니다")

result3 = magic_calc.advanced_ops.magic_multiply(2)
print(f"10+5={result3}2에 7곱하기는 {result3}입니다")

result = magic_calc.basic_ops.add(10,5)
print(f"10+5={result}10+5는 {result}입니다")

print( 'ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ' )
import magic_calc
result_add = magic_calc.basic_ops.add(10,5)
print(result_add)

from magic_calc import basic_ops, advanced_ops
result_sub = basic_ops.subtract(100, 30)
print(result_sub)

from magic_calc.basic_ops import multiply, divide
from magic_calc.advanced_ops import power
print("\n--- 방법 3: multiply, divide, power 직접 사용 --")

result_mul = multiply(7, 8)
print(f"7 * 8 = {result_mul}")


