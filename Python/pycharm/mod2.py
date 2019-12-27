# import 모듈이름
import mod1
import urllib


# from mod1 import add
from mod1 import *

print(mod1.add(10,20))

# 모듈에는 1개 이상의 함수, 변수, 클래스 등이 올 수 있다



#case1
#import 패키지명. 모듈명
import pack1.pack1_first

#패기지명.모듈명.함수명()
pack1.pack1_first.prn()


#case2
#from 패키지명.모듈명 impor 함수명
from pack1.pack1_first import prn
prn()


#case3
#from 패키지명 import 모듈명
from pack1 import pack1_first
pack1_first.prn()