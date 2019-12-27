# 예외처리

#예외상황
# f = open("없는 파일.txt","r")
# print(2/0)

try:
    print(2/0)
# print(2/0)문장을 수행하는 과정에서 예외상황이 발생할 경우
# 만약 ZeroDivisionError 예와상황이면 아래와 같은 문장을 수행해라
except ZeroDivisionError as e:
    print("0으로 나누면 안됩니다")
    print(e)