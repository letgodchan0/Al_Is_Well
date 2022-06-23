def solution(files):
    answer = []
    head, number, tail = '', '', ''

    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]

                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                answer.append([head, number, tail])
                head, number, tail = '', '', ''
                break
    answer = sorted(answer, key=lambda x : (x[0].lower(), int(x[1])))

    return [''.join(i) for i in answer]