d, num = input().split()
d = int(d)
x, y = map(int, input().split())

def find_coordinate(num, idx, r, c, size):  
    if size == 0:
        global num_r,num_c
        num_r,num_c = r, c
        return

    if num[idx] == '1':
        find_coordinate(num, idx+1, r, c+size, size//2)
    elif num[idx] == '2':
        find_coordinate(num, idx+1, r, c, size//2)
    elif num[idx] == '3':
        find_coordinate(num, idx+1, r+size, c, size//2)
    elif num[idx] == '4':
        find_coordinate(num, idx+1, r+size, c+size, size//2)

def make_answer(num_r, num_c, size, ans):
    if size == 0:
        print(ans)
        return

    if 0 <= num_r < size and size <= num_c < 2*size:
        make_answer(num_r, num_c-size, size//2, ans+'1')
    elif 0 <= num_r < size and 0 <= num_c < size:
        make_answer(num_r, num_c, size//2, ans+'2')
    elif size <= num_r < 2*size and 0 <= num_c < size:
        make_answer(num_r-size, num_c, size//2, ans+'3')
    elif size <= num_r < 2*size and size <= num_c < 2*size:
        make_answer(num_r-size, num_c-size, size//2, ans+'4')

num_r = num_c = 0
find_coordinate(num,0,num_r,num_c,(2**d)//2)    #좌표를 찾아낸다
num_r -= y      #이동
num_c += x
if 0 <= num_r < 2**d and 0 <= num_c < 2**d:
    make_answer(num_r,num_c,(2**d)//2,'')   #사분면 방식으로 다시 만든다
else:
    print(-1)