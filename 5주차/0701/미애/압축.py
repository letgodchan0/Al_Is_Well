answer = []
alpha = {}
n = 27
for i in range(0, n-1):
    alpha[chr(i+65)] = i+1
msg = "KAKAO"
# msg = list(msg) - 문자열일 때와 길이 같기 때문에 안해도됨

start, end = 0, 0

while 1:
    # 있으면 그 다음단어 확인(end+=1)
    end += 1
    if end == len(msg):
        answer.append(alpha[msg[start:end]])
        break

    # 만약 start부터 end+1 까지의 단어가 없으면 추가
    if msg[start:end+1] not in alpha:
        alpha[msg[start:end+1]] = n
        n += 1
        answer.append(alpha[msg[start:end]])

        # 시작단어 이동
        start = end

print(answer)
