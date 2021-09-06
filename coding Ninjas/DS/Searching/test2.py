def VowelConsonantSequence(str):
    n = len(str)
    ans = []
    prev = isVowel(str[0])
    for i in range(1,n-1):
        if isVowel(str[i]) != prev:
            ans.append(prev)
            prev = isVowel(str[i])
    ans.append(isVowel(str[-1]))
    
    print(ans)



def isVowel(char):
    if char == 'a' or char == 'o' or char == 'e' or char == 'i' or char == 'u':
        return 'V'
    else:
        return 'C'

VowelConsonantSequence('whereabouts')
