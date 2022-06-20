# #코드 바꿔주기
def change_code(m):
    return m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

# 시간 체크
def timecheck(time1, time2):
    time1 = int(time1[:2]) * 60 + int(time1[3:])
    time2 = int(time2[:2]) * 60 + int(time2[3:])
    return time2 - time1

# 결과 반환
def solution(m, musicinfos):
    m = change_code(m)
    check = []
    code = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    for info in musicinfos:
        information = info.split(',')
        time = timecheck(information[0], information[1])
        song = information[2]
        play = change_code(information[3])
        if len(play) > time:
            play = play[:time]
        else:
            play = play * (time // len(play)) + play[:(time % len(play))]

        if m in play:
            check.append((song, time))

    if len(check) == 0:
        return "(None)"

    return sorted(check, key = lambda x: x[1], reverse = True)[0][0]