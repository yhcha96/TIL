'''
모듈 : 함수나 변수, 클래스들을 모아 놓은 파일
다른 파이썬 프로그램에서 모듈을 사용하기 편하게 하기 위해서
확장자가 py가 붙은 파일
'''

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

# __name__ == '__main__'을 사용하면
# __name__ == '__main__'조건이 참이됨
# 따라서 if문에 있는 문장을 수행
# 그런데 외부 파일에서
# 이 모듈을 불러와서 실행할때는 __name__ != '__main__'이므로, if문이 실행이 안됨


if __name__== '__main__':
    print(add(2,3))
    print(sub(4,3))

