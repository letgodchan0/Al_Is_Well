def solution(m, musicinfos):
    answer = ''
    pos = []
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('E#', 'e')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    m = m.replace('A#', 'a')
    m = m.replace('B#', 'b')
    for music in musicinfos:
        start, end, title, note = music.split(',')
        sh, sm = map(int, start.split(':'))
        eh, em = map(int, end.split(':'))
        minute = eh * 60 + em - sh * 60 - sm
        # 실제 재생된 시간보다 길면
        note = note.replace('C#', 'c')
        note = note.replace('D#', 'd')
        note = note.replace('E#', 'e')
        note = note.replace('F#', 'f')
        note = note.replace('G#', 'g')
        note = note.replace('A#', 'a')
        note = note.replace('B#', 'b')
        if len(note) > minute:
            r_note = note[:minute]
        elif len(note) == minute:
            r_note = note
        else:
            r_note = note * (minute//len(note)) + note[:minute%len(note)]




        if m in r_note:
            pos.append([title, minute])

        # n = list(map(str, r_note.split(f'{m}')))
        # print(n)
        # if len(n) == 1:
        #     continue
        # # m 으로 나눠지기만 하면
        # else:
        #     # 배열 첫번째 꺼는 무시 가능
        #     for i in range(1, len(n)):
        #         if n[i] == '':
        #             pos.append([title, minute])
        #             break
        #         elif n[i][0] != '#':
        #             pos.append([title, minute])
        #             break
        #     # else:
            #     for i in range(1, len(n)):
            #         if n[i][0] != '#':
            #             pos.append([title, minute])
            #             break

        # if m in r_note and m+'#' not in r_note:
        #     pos.append([title, minute])
    print(r_note)
    if not pos:
        answer = '(None)'
    else:
        pos.sort(key=lambda x : x[1], reverse=True)
        answer = pos[0][0]

    
    return answer


a = 'ABC'
b = list('DABCABC#'.split('ABC#'))
b ='ABC#B#C#'.replace('C#', 'c')
print(b)


m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution("AB", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
