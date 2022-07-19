a = int(input())

for _ in range(a):
    n = input()

    if n == n[::-1]:
        print(0)
    else:
        for i in range(len(n)):
            new = n[:i] + n[i + 1:]
            if new == new[::-1]:
                print(1)
                break
        else:
            print(2)
