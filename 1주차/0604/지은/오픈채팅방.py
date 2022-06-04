def solution(record):
    answer = []
    final_id = {}
    for rec in record:  #최종 id 딕셔너리 생성
        rec = rec.split()
        if rec[0]=="Enter" or rec[0]=="Change":   #닉네임이 바뀌는 Enter이거나 Change이면 저장
            state, user_id, nickname = rec
            final_id[user_id] = nickname

    for rec in record:
        rec = rec.split()
        if rec[0]=="Enter" or rec[0]=="Change":     #Enter이거나 Change일 때
            state, user_id, nickname = rec
        else:   #Leave일 때
            state, user_id = rec

        if state == "Enter":
            answer.append(f"{final_id[user_id]}님이 들어왔습니다.")
        elif state == "Leave":
            answer.append(f"{final_id[user_id]}님이 나갔습니다.")

    return answer
