from calc import add, multiply
print(add(2, 3))  # 5 출력
print(multiply(4, 5))  # 20 출력
print(add(10, 5))

import datetime
print("\n=== 3. datetime (날짜와 시간) ===")
# 현재 컴퓨터의 날짜와 시간을 출력합니다[cite: 2]
print("datetime.now() ->", datetime.datetime.now())

import math
print("math.sqrt(16) ->", math.sqrt(16))

import os
print("\n=== 4. os (운영체제 기능) ===")
print("os.getcwd() ->", os.getcwd())

import random
print("\n=== 2. random (랜덤값 생성) ===")
print("1부터10까지~ ->", random.randint(1, 10))

import sys
print("\n=== 5. sys (시스템 정보) ===")
print("sys.version ->", sys.version)

import time
print("\n=== 6. time (시간 지연) ===")
print("1초 동안 잠시 멈춥니다...")
time.sleep(1)  # 1초 동안 프로그램 실행을 멈춥니다[cite: 2]
print("1초 지났습니다! 끝!")