'''
<접근방법>
1. nPr로 2가지문자 다구해서 하려다가 포기

2. set 자료형 이용
A = set(str1)
B = set(str2)
A_inter = A.intersection(B)
처럼 set자료형의 함수를 사용하면 중복되는 요소를 삭제하기 때문에 '다중집합'에 해당되지 않는다

<새로안거>
collection 패키지
['AA', 'AA'] ['AA', 'AA', 'AA'] 를 Counter 객체로 변환을 해주면
Counter({'AA': 2}) Counter({'AA': 3})
각각의 리스트를 해당 원소의 key값으로 하고, 원소의 개수를 value값으로 하는 딕셔너리 구조이다.
교집합은 Counter({'AA':2}) 을 원소로 가져온 리스트
합집합은 Counter({'AA':3}) 을 원소로 가져온 리스트
각각은 &, |로 표현가능하다

<출제자의 의도>
merge sort 응용이라는데..
'''

from collections import Counter
# 단어를 두글자씩 끊어서 집합을 만듬
def sets(strs):
    # 영문자로 된 글자쌍만 가능
    # 기타 공백, 숫자, 특수문자는 pass
    arr = []
    i = 0
    while i < len(strs)-1:
        if 'A' <= strs[i] <= 'Z' and 'A' <= strs[i+1] <= 'Z':
            arr.append(strs[i:i+2])
            i += 1
        else:
            i += 1
    return arr

# 대문자로 변환 => .upper() , .lower() 같은거 사용할 수 있었음
'''
def capital(strs):
    res = ""
    for i in strs:
        if 'a' <= i <= 'z':
            res += chr(ord(i)-32)
        else:
            res += i
    return res
'''
str1 = "aa1+aa2"
str2 = "AAAA12"

A = sets(str1.upper())
B = sets(str2.upper())
print(A,B)
C1 = Counter(A)
C2 = Counter(B)
print((C1 & C2))
inter = list((C1 & C2).elements())
union = list((C1 | C2).elements())

if len(inter) == 0 and len(union) == 0:
    answer = 1
else:
    answer = (len(inter)/len(union))

print(int(answer * 65536))
