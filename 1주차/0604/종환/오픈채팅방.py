"""
I
record
- "Enter <uid(string)> <username(string)>"  /  각 단어는 알파벳 대소문자를 구별하며, 알파벳과 숫자로만 이루어져 있다.
- "Leave <uid> <username>"
- "Change <uid> <username>"

O
변경된 최종 닉네임으로 "<닉네임>님이 들어왔습니다/나갔습니다" 출력할 것

- 아이디와 닉네임은 1자 이상, 10자 이하

풀이
출입1기록 리스트로
[
    ["Enter", uid],
    ["Leave", uid],
    ...
]
와 같이 기록하고,
닉네임 딕셔너리로
{
    "uid": "username",
    "uid": "username",
    ...
}
와 같이 기록해서 출입1기록 리스트를 출력할 때 uid로 닉네임을 조회하며 출력한다.
"""
def solution(record):
    io = []
    nickname = dict()

    # 입력
    for line in record:
        tmp = list(line.split(" "))
        if tmp[0] == "Enter":
            io.append([tmp[0], tmp[1]])
            if (tmp[1] not in nickname) or (nickname[tmp[1]] != tmp[2]):
                nickname[tmp[1]] = tmp[2]
        elif tmp[0] == "Leave":
            io.append([tmp[0], tmp[1]])
        elif tmp[0] == "Change":
            nickname[tmp[1]] = tmp[2]

    # 출력
    answer = []
    for line in io:
        if line[0] == "Enter":
            answer.append(f"{nickname[line[1]]}님이 들어왔습니다.")
        elif line[0] == "Leave":
            answer.append(f"{nickname[line[1]]}님이 나갔습니다.")

    return answer