def solution(files):
    answer = []
    for file in files:
        result = []
        for i in range(len(file)):
            if file[i].isdigit():
                result.append(file[:i])
                start = i
                break
        for i in range(start, len(file)):
            if len(file[start:]) == 1:
                result.append(file[start:])
                break

            if i-start >= 5:
                result.append(file[start:i])
                result.append(file[i:])
                break
            if not file[i].isdigit():
                result.append(file[start:i])
                result.append(file[i:])
                break

            if i == len(file)-1:
                result.append(file[start:i+1])
                break

        answer.append(result)

    answer.sort(key = lambda x: (x[0].upper(), int(x[1])))
    answer = list(map(lambda x : ''.join(x), answer))
    return answer

