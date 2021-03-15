class solution:
    '''
    ///////////////////////////////////////////
    // 1.1 Is Unique
    '''
    def isUnique(s: str) -> bool:
        if len(s) > 128: return False
        char_set = [False for i in range(128)]
        for i in range(len(s)):
            val = ord(s[i])
            if char_set[val] == True:
                return False
            char_set[val] = True
        return True

    # Assumption: The string uses the lowercase letters a through z. => reduce space
    def isUnique1(s: str) -> bool:
        checker = 0;
        for i in range(len(s)):
            val = ord(s[i])
            if checker & (1 << val) > 0: return False
            checker |= (1 << val)
        return True

    # O(n^2) time, O(1) space
    def isUnique2(s: str) -> bool:
        if len(s) > 128: return False
        for i in range(len(s)):
            for j in range(i):
                if(s[j]==s[i]): return False
        return True

    # O(n log(n)) time
    def isUnique3(s: str) -> bool:
        t = sorted(s)
        print(t)
        u = ''.join(t)
        print(u)
        for i in range(len(t)-1):
            if(t[i]==t[i+1]): return False
        return True

    '''
    ///////////////////////////////////////////
    // 1.2 Check Permutation
    '''
    def sort(s: str) -> str:
        return ''.join(sorted(s))

    def permutation(s: str, t:str) -> bool:
        if len(s)!=len(t): return False
        return solution.sort(s) == solution.sort(t)

    def permutation2(s: str, t:str) -> bool:
        if len(s)!=len(t): return False # Permutation must be same length
        letters = [0 for i in range(128)]   # Assumption: ASCII
        for i in range(len(s)):
            letters[ord(s[i])] += 1
        for i in range(len(t)):
            letters[ord(t[i])] -= 1
            if letters[ord(t[i])] < 0: return False
        return True # letters has no no neg values, and therefore no pos values either.

    '''
    ///////////////////////////////////////////
    // 1.3 Check Permutation
    '''
    def replaceSpace(s: bytearray, trueLength: int):
        spaceCount = 0
        for i in range(trueLength):
            if s[i] == ' ': spaceCount += 1
        index = trueLength + spaceCount * 2
        if trueLength < len(s): s[trueLength] = '\0'

        for i in range(trueLength-1, -1, -1):
            if s[i] == ' ':
                s[index-1] = '0'
                s[index-2] = '2'
                s[index-3] = '%'
                index = index - 3
            else:
                s[index-1] = s[i]
                index -= 1
        return

'''
# 1.1 Is Unique
str_in = "abcdb"
print(solution.isUnique(str_in))
print(solution.isUnique1(str_in))
print(solution.isUnique2(str_in))
print(solution.isUnique3(str_in))
'''
'''
# 1.2 Check Permutation
str1 = "god"
str2 = "dog"
print(solution.permutation(str1, str2));
print(solution.permutation2(str1, str2));
'''
# 1.3 URLify
str_in = "Mr John Smith    "
ba_in = bytearray(str_in, 'utf-8')
solution.replaceSpace(ba_in, 13);
