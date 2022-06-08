# 사분면
def find(number, idx, r, c, size):
    if size == 0:
        global num_r, num_c
        num_r, num_c = r, c
        return
    
    if number[idx] == '1':
        find(number, idx + 1, r, c + size, size // 2)
    elif number[idx] == '2':
        find(number, idx + 1, r, c, size // 2)
    elif number[idx] == '3':
        find(number, idx + 1, r + size, c, size // 2)
    elif number[idx] == '4':
        find(number, idx + 1, r + size, c + size, size // 2)

def answer(num_r, num_c, size, ans):
    if size == 0:
        print(ans)
        return
    
    if 0 <= num_r < size and size <= num_c < 2 * size:
        answer(num_r, num_c - size, size // 2, ans + '1')
    elif 0 <= num_r < size and 0 <= num_c < size:
        answer(num_r, num_c, size // 2, ans + '2')
    elif size <= num_r < 2 * size and 0 <= num_c < size:
        answer(num_r - size, num_c, size // 2, ans + '3')
    elif size <= num_r < 2 * size and size <= num_c < 2 * size:
        answer(num_r - size, num_c - size, size // 2, ans + '4')

dimension, number = input().split()
dimension = int(dimension)
x, y = map(int, input().split())

num_r = num_c = 0
find(number, 0, num_r, num_c, (2**dimension) // 2)
num_r -= y
num_c += x

if 0 <= num_r < 2 ** dimension and 0 <= num_c < 2 ** dimension:
    answer(num_r, num_c, (2 ** dimension) // 2, '')
else:
    print(-1)