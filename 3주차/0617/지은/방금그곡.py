def solution(m, musicinfos):
    answer = ''
    substi = {'C':'H', 'D':'I',  'F':'J',  'G':'K',  'A':'L', 'E':'M'}
    ##이 들어간 음들을 처리해주기 위한 딕셔너리. 문제 조건에는 E#이 없었으나 런타임에러가 나서 찾아보고 추가함...
    m_changed = ''  #substi를 m에도 적용시키기 위함
    infos = []
    
    for musicinfo in musicinfos:    #음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
        song_changed = []
        start_time, end_time, title, song = musicinfo.split(',')
        start_hour, start_min = map(int, start_time.split(':'))
        end_hour, end_min = map(int, end_time.split(':'))
        time = (end_hour - start_hour) * 60 + end_min - start_min   #시간구하기
        
        for i in range(len(song)):  ##들어간 음표 처리해주기
            if song[i]=='#':
                continue
            if i < len(song)-1 and song[i+1]=='#':
                song_changed.append(substi[song[i]])
            else:
                song_changed.append(song[i])

        played = song_changed * (time//len(song_changed)) + song_changed[:time%len(song_changed)]    #그 시간동안 재생되었던 음악
        infos.append((title, ''.join(played)))

    #재생된 시간으로 내림차순으로 정렬하기
    infos = sorted(infos, key=lambda x: len(x[1]), reverse=True)

    for j in range(len(m)):
        if m[j]=='#':
                continue
        if j < len(m)-1 and m[j+1]=='#':
            m_changed += substi[m[j]]
        else:
            m_changed += m[j]

    for info in infos:
        if m_changed in info[1]:
            answer = info[0]
            break
    
    if answer=='':
        answer="(None)"

    return answer 

print(solution("ABCDEFG", 	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", 	["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", 	["12:00,12:04,WORLD1,ABC", "13:00,13:04,WORLD,ABC", "12:00,12:04,WOfRLD,ABC"]))

