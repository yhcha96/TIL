#!/usr/bin/env python
# coding: utf-8

# # 1226 6일차

# ### 1. Class : 객체를 표현하기 위한 개념
# 
# ex) 게임 - 기사, 궁수, 마법사 등 직업별로 클래스가 생성
# 
#     웹브라우저 - 스크롤바, 버튼, 체크박스 등 구성요소가 모두가 클래스
# 
# 1. 기사 클래스로 홍길동 객체(캐릭터)를 생성
# 2. 체력, 마나, 공격력,... 초기값 설정 = 속성(속성이 필요)
# 3. 달리기, 베기, 찌르기,....동작 스킬 = 메서드
# 
# **=> 클래스는 속성과 메서드로 구성된다**

# In[6]:


res = 0
def add(num):
    global res
    res += num
    return res

print(add(3))
print(add(4))


# In[7]:


def add(num):
    res = 0
    res += num
    return res

print(add(3))
print(add(4))


# In[10]:


# 계산기 2대
res1 = 0
res2 = 0

def add1(num):
    global res1
    res1 += num
    return res1

def add2(num):
    global res2
    res2 += num
    return res2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))


# In[25]:


# 메모리에 만들어짐
class Calc: # 변수이름 규치과 같음
    def __init__(self): # 객체를 초기화하는 역할(객체가 만들어진 시점으로)
        self.res = 0
        print('초기화')
    def add(self,num):
        self.res += num
        return self.res
    def sub(self,num):
        self.res -= num
        return self.res


# In[26]:


# hgd = Calc() # 객체 = 클래스()
cal1 = Calc() # 꼐산기1
cal2 = Calc() # 계산기2

print(cal1.add(3))
print(cal1.add(4))

print(cal2.add(3))
print(cal2.add(7))


# In[ ]:


'''
붕어빵 기계 = class, 속성(특징)과 메서드(동작)
붕어빠 = 객체(object)

'''


# In[28]:


class FishBread:
    pass # 아무기능도없는 클래스 정의 가능


# In[29]:


a = FishBread()
print(type(a))


# In[47]:


# 사칙연사 클래스
class FourCal:
    def __init__(self):
        self.res = 0
    def setData(self,first,second):
        self.first = first
        self.second = second
# self : 지금 만들어진 객체
# self.first : 지금 만들어지고 있는 객체의 first 속성
    
    def add(self):
        self.res = self.first + self.second
        return self.res
    def sub(self):
            self.res = self.first - self.second
            return self.res
    def mul(self):
        self.res = self.first * self.second
        return self.res
    def div(self):
        self.res = self.first / self.second
        return self.res


# In[49]:


# 변수 = 클래스명()
# 변수는 클래스로부터 만들어진 객체를 나타냄

# 붕어빵 = 붕어빵기계()
a = FourCal() # FourCal클래스로부터 객체 생성
b = FourCal()

# 붕어빵.내용물을 정한다(단팥)
a.setData(4,2) # 숫자 4,2를 a에 지정 : first에 4, second에 2 저장
b.setData(1,2)


print(a.add()) # 6 리턴
print(b.add())
# print(a.sub())
# print(a.mul())
# print(a.div())


# In[51]:


# MoreFourCal은 FourCal의 자식
class MoreFourCal(FourCal):
    pass
# 상속 => class 자식 클래스명(부모클래스명):
# MoreFourCal클래스는 FourCal클래스를 상속했으므로, FourCal클래스의 모든 기능을 사용할 수 있음


# In[52]:


A = MoreFourCal()
A.setData(4,2)
A.add()


# In[63]:


class MoreFourCal(FourCal):
    def pow(self):
        res = self.first ** self.second
        return res


# In[64]:


B = MoreFourCal()
B.setData(2,3)
B.pow()


# In[66]:


# 매서드 오버라이딩(overriding): 부모 클래스로부터 상속받은 매서드를 자식이 변경

myObj = FourCal()
myObj.setData(4,2)
myObj.div()


# In[67]:


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 1:
            print("Don't divide by 1")
            return
        else:
            return self.first/self.second


# In[70]:


sfc = SafeFourCal()
sfc.setData(4,1)
print(sfc.div())


# In[81]:


class Person:
    def __init__(self,name,age,home):
        self.name = name
        self.age = age
        self.home = home
    def greeting(self):
        print("안녕하세요. 나는 %s입니다" %self.name)
    def name(self):
        return self.name
    def age(self):
        return self.age
    def home(self):
        return self.home


# In[82]:


ps = Person("홍길동",25,"서울시 역삼동")
ps.greeting() # 안녕하세요. 나는 홍길동입니다.
print("Name : ",ps.name)
print("Age : ",ps.age)
print("Home : ",ps.home)


# In[85]:


class Person2:
    def __init__(self,*args):
        self.name = args[0]
        self.age = args[1]
        self.home = args[2]
    def greeting(self):
        print("안녕하세요. 나는 %s입니다" %self.name)
    def name(self):
        return self.name
    def age(self):
        return self.age
    def home(self):
        return self.home


# In[86]:


ps2 = Person2("홍길동",25,"서울시 역삼동")
ps2.greeting() # 안녕하세요. 나는 홍길동입니다.
print("Name : ",ps2.name)
print("Age : ",ps2.age)
print("Home : ",ps2.home)


# In[ ]:




