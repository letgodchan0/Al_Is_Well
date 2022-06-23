def solution(m, musicinfos):
    answer = '(None)'
    answer_time = 0
    
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    
    for info in musicinfos:
        lst = info.strip('"').split(',')
        befhour, befminute = map(int, lst[0].split(':'))
        afthour, aftminute = map(int, lst[1].split(':'))
        
        time = (afthour - befhour) * 60 + aftminute - befminute
        music = lst[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        
        if len(music) <= time:
            music = music * (time // len(music)) + music[:(time % len(music))]
            
        if m in music and time > answer_time:
            answer = lst[2]
            answer_time = time
            
    return answer