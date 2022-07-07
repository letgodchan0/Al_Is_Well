def solution(s):
    name = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    i = 0
    while i < len(s):
        if not s[i].isdigit():
            now = s[i:i + 3]
            if now not in name:
                now += s[i + 3]
            if now not in name:
                now += s[i + 4]
            s = s.replace(now, str(name.index(now)))
        i += 1
          
    return int(s)