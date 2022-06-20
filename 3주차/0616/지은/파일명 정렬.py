import re

def solution(files):
    heads = []
    nums = []
    answer = []

    for file in files:          #NUMBER로 정렬
        num = re.findall(f'\d+', file)
        nums.append((int(num[0]), file))
    nums = sorted(nums, key=lambda x : x[0])
    #sorted(nums)를 하면 첫번째 인자가 같을 시 두 번째 인자도 비교하여 정렬함
    _, srtd_files = zip(*nums)   #*연산자 써서 분해하기

    
    for srtd_file in srtd_files:  #HEAD로 정렬
        head = re.split(f'\d+', srtd_file)[0]
        print(head)
        heads.append((head, srtd_file))
    print(heads)
    heads = sorted(heads, key=lambda x : x[0].lower())
    _, answer = zip(*heads)

    return list(answer)

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F5 Freedom Fighter", "B50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
