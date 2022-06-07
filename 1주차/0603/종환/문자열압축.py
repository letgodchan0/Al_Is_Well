"""
문자열을 1개 단위로 잘라서 압축해본다.
문자열을 2개 단위로 잘라서 압축해본다.
문자열을 3개 단위로 잘라서 압축해본다.
...
문자열을 전체 길이(len(s))의 1/2개 단위로 잘라서 압축해본다.

방식: 변수에 넣고 다음 문자열과 비교하기 (  같으면 배수 변수 += 1
    다르면 배수변수가 1일 경우 문자열 길이만큼 결과에 + 하고 2 이상일 경우 (len(str(배수변수)) + 문자열 길이) 만큼 결과에 +  )


"""

def solution(s):
    answer = len(s) # 초기값(생 데이터)
    max_len = len(s)
    half_len = int(max_len / 2)
    store = ''
    # times = 0
    for joint in range(1, max_len + 1):
        tmp = 0     # 임시 answer
        start = 0   # 시작 인덱스
        
        # 마디를 지정
        while start <= half_len:
            store = s[start:start+joint]  # 마디 저장
            times = 1
            x = True
            # 마디마다, 다음 마디와 자신을 비교
            while x:
                start += joint
                if s[start:start+joint] == store:
                    times += 1
                else:
                    # 다음 마디가 일치하지 않으면, 스타트 부분은 그대로 두고 다음 탐색해야 함
                    x = False
                    if times == 1:
                        tmp += len(store)
                    else:
                        tmp += len(str(times)) + len(store)
        
        if tmp < answer:
            answer = tmp

    return answer

# 문제: xabcabc와 같은 상황에서 x2abc같은 정답을 끌어내지 못한다.
# 무조건 같은 간격으로만 점프하며 확인하고 있다.
# 그런데 결과값은 정답보다 낮게 나온다 