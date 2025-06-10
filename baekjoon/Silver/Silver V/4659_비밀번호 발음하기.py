def ok_pwd2(test): #chat
    vowels = ['a', 'e', 'i', 'o', 'u']
    has_vowel = False

    for i in range(len(test)):
        if test[i] in vowels:
            has_vowel = True

        # 같은 글자 두 번 연속 체크 (ee, oo는 예외)
        if i > 0:
            if test[i] == test[i-1] and test[i] not in ['o', 'e']:
                return False
        
        # 3개 연속 모음 or 자음 체크
        if i >= 2:
            check = test[i-2:i+1]
            if all(c in vowels for c in check) or all(c not in vowels for c in check):
                return False
    
    return has_vowel

def ok_pwd(test):
    vowel = ['a', 'e', 'i', 'o', 'u']
    has_vowel = 0

    for i in range(len(test)):
        if test[i] == test[i-1] and test[i] not in ['e', 'o']:
            return False
    
    for v in vowel:
        if v in test:
            has_vowel = 1
            i = 0
            while i+2 < len(test):
                check = test[i:i+3]
                cnt = 0
                for v in vowel:
                    if v in check:
                        cnt +=1
                i = i +1
                
                if 1<= cnt <=2:
                    continue
                else:
                    return False
            
    if has_vowel == 0:
        return False
    else:
        return True
    
test_case = []
while True:
    test = input()
    if test == 'end':
        break
    else:
        test_case.append(test)

for test in test_case:
    if ok_pwd(test) == True:
        print(f'<{test}> is acceptable.')
    else:
        print(f'<{test}> is not acceptable.')