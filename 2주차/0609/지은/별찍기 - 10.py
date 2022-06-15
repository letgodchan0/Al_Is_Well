def draw(n):
    if n == 3:
        return ['***','* *','***']

    stars = draw(n//3)
    answer = []

    for star in stars:
        answer.append(star*3)

    for star in stars:
        answer.append(star+' '*(n//3)+star)

    for star in stars:
        answer.append(star*3)

    return answer

n = int(input())
print('\n'.join(draw(n)))