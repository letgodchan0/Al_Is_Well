def s_palin(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def palin(s, left, right):
    if s == s[::-1]:
        return 0
    else:
        while left < right:
            if s[left] != s[right]:
                check_left = s_palin(s, left+1, right)
                check_right = s_palin(s, left, right-1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

t = int(input())
for _ in range(t):
    s = input()
    print(palin(s, 0, len(s)-1))