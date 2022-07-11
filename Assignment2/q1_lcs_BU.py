def lcs(s1, s2):
    """A Bottom Up approach to the lcs algorithm"""
    n1 = len(s1) + 1
    n2 = len(s2) + 1
    
    table = [[None for _ in range(n2)] for _ in range(n1)]
    
    for i in range(n1):
        for j in range(n2):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])
                
    n = len(s1) 
    m = len(s2) 
    result = ''
    while (table[n][m] != 0):
        if s1[n-1] == s2[m-1]:
            result = s1[n-1] + result
            n -= 1
            m -= 1
        else:
            if table[n-1][m] >= table[n][m-1]:
                n -= 1
            else:
                m -= 1
    
    return result

#s1 = "Look at me, I can fly!"
#s2 = "Look at that, it's a fly"
#print(lcs(s1, s2))

#s1 = "abcdefghijklmnopqrstuvwxyz"
#s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
#print(lcs(s1, s2))

#s1 = "balderdash!"
#s2 = "balderdash!"
#print(lcs(s1, s2))

#s1 = 1500 * 'x'
#s2 = 1500 * 'y'
#print(lcs(s1, s2))

s1 = "mac_adress = data[macAddress]"
s2 = "mac_adress = data[mac_address]"
print(lcs(s1, s2))