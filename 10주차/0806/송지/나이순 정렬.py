case = int(input())
case_list = [0 for i in range(case)]

for i in range(case):
    case_list[i] = list(input().split())
    case_list[i][0] = int(case_list[i][0])
    
lam_list = sorted(case_list, key = lambda x: x[0])

for i in range(len(lam_list)):
    print(lam_list[i][0], lam_list[i][1])