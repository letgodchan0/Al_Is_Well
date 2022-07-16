n = int(input())
nums = []
num = ''
for _ in range(n):
    word = input()
    for i in range(len(word)):
        if '0' <= word[i] <= '9':
            num += word[i]
            
        else:
            if num == '0':
                nums.append(int(num))
                num = ''
            elif num != '':
                num = num.lstrip('0')
                if num == '':
                    nums.append(0)
                else:
                    nums.append(int(num))
                num = ''
    if num != '':
        if num == '0':
                nums.append(int(num))
                num = ''
        else:
            num = num.lstrip('0')

            if num == '':
                nums.append(0)
            else:
                nums.append(int(num))
            num = ''
nums.sort()
for i in range(len(nums)):
    print(nums[i])