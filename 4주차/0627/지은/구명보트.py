from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0

    while people:
        answer += 1
        boat = []
        boat.append(people.pop())
        while people:
            boat.append(people.popleft())
            if sum(boat)>limit:
                people.appendleft(boat.pop())
                break
            elif sum(boat)==limit:
                break

    return answer