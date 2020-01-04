Q1 파이썬 키워드에 대한 질문 추출

```python
url = "https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

# 페이지에서 질문 제목 추출
for link in soup.select("ul.type01 dt.question a"):
    print(link.text)
```



Q2 1페이지에 있는 질문 모두 추출

```python
url = "https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

# 페이지에 있는 각 질문 페이지로 가는 url 추출
links =[]
for link in soup.select('ul.type01 dt.question a'):
    links.append(link.attrs['href'])

# 각 질문 페이지로 가서 질문 추출
for link in links:
    response = requests.get(link)
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    print("\nQuestion\n")
    for x in soup.select("div.title"): # 질문 제목에서 질문 추출
        print(x.text)
    for x in soup.select("div.c-heading__content"): # 질문 본문에서 질문 추출
        print(x.text)
    print("="*40)
```



Q3  1~10페이지에 있는 질문 모두 추출

```python
url = "https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

#총 질문 수 추출
num_sentence = soup.select_one("span.title_num").text
num = int(num_sentence[7:10]+num_sentence[11:14]) # 총 질문 수 str -> int
page_num = num//10 + 1 # 페이지 수 구하기


for i in range(10): #10페이지만 하니깐 range(10) 전체페이지하려면 page_num
    print("%d 페이지의 질문입니다."%(i+1))
    url = "https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&c_id=&c_name=&sm=tab_pge&kin_start="+str(10*(i+1)+1)
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    
    # 페이지에 있는 질문 10개의 url 저장
    links =[]
    for link in soup.select('ul.type01 dt.question a'):
        links.append(link.attrs['href'])
	
    # 각 질문의 질문과 답변 추출
    for link in links:
        response = requests.get(link)
        text = response.text
        soup = BeautifulSoup(text,'html.parser')
        
        # 질문 제목에 있는 것과 본문에 있는 것 모두 추출
        print("\nQuestion\n")
        for x in soup.select("div.title"):
            print(x.text)
        for x in soup.select("div.c-heading__content"):
            print(x.text)
        print("="*40)
```





Q4  1~10페이지에 있는 질문/답변 모두 추출

```python
url = "https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')


for i in range(10): 
    print("%d 페이지의 질문입니다."%(i+1))
    url = "https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&c_id=&c_name=&sm=tab_pge&kin_start="+str(10*(i+1)+1)
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    
    # 페이지에 있는 질문 10개의 url 저장
    links =[]
    for link in soup.select('ul.type01 dt.question a'):
        links.append(link.attrs['href'])
	
    # 각 질문의 질문과 답변 추출
    for link in links:
        response = requests.get(link)
        text = response.text
        soup = BeautifulSoup(text,'html.parser')
        
        # 질문 제목에 있는 것과 본문에 있는 것 모두 추출
        print("\nQuestion\n")
        for x in soup.select("div.title"):
            print(x.text)
        for x in soup.select("div.c-heading__content"):
            print(x.text)
        
        print("\nAnswer\n")
        i = 1 # 답변이 여러개 일때가 있어서 답변 구분용도
        for x in soup.select("div.se-main-container"):
            print("답변%d"%i)
            print(x.text)
            i += 1
        print("="*40)
```



Q5 추출한 전체 결과에 대해 '초보'라는 단어가 등장한 횟수 출력

```python
url = "https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

total = 0 # '초보'단어가 나온 총 수
for i in range(10):
    url = "https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&c_id=&c_name=&sm=tab_pge&kin_start="+str(10*(i+1)+1)
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    
    links =[]
    for link in soup.select('ul.type01 dt.question a'):
        links.append(link.attrs['href'])

    for link in links:
        response = requests.get(link)
        text = response.text
        soup = BeautifulSoup(text,'html.parser')
        for x in soup.select("div.title"):
            c1 = len(re.findall('초보',x.text)) # 질문 제목에서 '초보'가 나온 횟수
        for x in soup.select("div.c-heading__content"):
            c2 = len(re.findall('초보',x.text)) # 질문 본문에서 '초보'가 나온 횟수
        for x in soup.select("div.se-main-container"):
            c3 = len(re.findall('초보',x.text)) # 답변에서 '초보'가 나온 횟수
        total += c1+c2+c3

print("'초보'라는 단어는 총%d번 나왔습니다."%total)
```

