def lcs(s1, s2):
    """Takes two strings and returns the longest common subsequence, using the
    simplistic recursion given in lecture notes
    """
    memo = {}
    
    def lcs_memo(s1, s2):
        if (s1, s2) not in memo:
            if s1 == '' or s2 == '':
                memo[(s1, s2)] = ''
                return memo[(s1, s2)]
            elif s1[-1] == s2[-1]: # last chars are the same
                memo[(s1, s2)] = lcs_memo(s1[:-1], s2[:-1]) + s1[-1]
                return memo[(s1, s2)]
            else:
                # Drop last char of each string in turn
                # Choose best outcome
                sln1 = lcs_memo(s1[:-1], s2)
                sln2 = lcs_memo(s1, s2[:-1])
                
                if len(sln1) > len(sln2):
                    memo[(s1, s2)] = sln1
                    return memo[(s1, s2)]
                else:
                    memo[(s1, s2)] = sln2
                    return memo[(s1, s2)]
        else:
            return memo[(s1, s2)]
        
    return lcs_memo(s1, s2)
    
## A simple test that should run without caching
#s1 = "abcde"
#s2 = "qbxxd"
#lcs = lcs(s1, s2)
#print(lcs)

#s1 = "Look at me, I can fly!"
#s2 = "Look at that, it's a fly"
#print(lcs(s1, s2))

#s1 = "abcdefghijklmnopqrstuvwxyz"
#s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
#print(lcs(s1, s2))

s1 = "balderdash!"
s2 = "balderdash!"
print(lcs(s1, s2))
