# WHY ......................................... ? 

def solution(files):
    new_files = []
    
    for j in range(len(files)):
        
        cat = cat2 = num = 0
        
        for i in range(len(files[j])):
            try:
                if int(files[j][i]) > -1 and not cat:
                    cat = i
                    num += 1
                elif num < 5:
                    num += 1
                else:
                    cat2 = i
                    break
            except:
                if cat:
                    cat2 = i
                    break
                pass
            
        new_files.append([files[j][:cat]])
        
        if cat2:
            new_files[j].append(files[j][cat:cat2])
            new_files[j].append(files[j][cat2:])
        else:
            new_files[j].append(files[j][cat:])
    
    print(new_files)
    new_files = sorted(new_files, key=lambda x:(x[0].upper(), int(x[1].lstrip('0'))))
    
    print(new_files)
    
    for i in range(len(new_files)):
        new_files[i] = ''.join(new_files[i])
        
    return new_files