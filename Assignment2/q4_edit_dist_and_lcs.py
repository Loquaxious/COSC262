def line_edits(s1, s2):
    """ Takes two strings as parameters representing the previous and current 
    versions of the code file. It uses the edit distance algorithm with whole 
    lines as the comparison elements, to determine which lines to delete, insert
    alter or just copy. The output will be a list of 3-element tuples 
    (op, left_line, right_line) that will correspond line for line wiht the 
    output table"""
    
    result = []
    split1 = s1.splitlines()
    split2 = s2.splitlines()
    n = len(split1) 
    m = len(split2)
    
    table = pop_table(split1, split2)
    
    while (n != 0 or m != 0):
        if n == 0 or m == 0:
            if n == 0 and m == 0:
                return result
            elif n == 0:
                result = [('I', '', split2[m-1])] + result
                m -= 1
            else:
                result = [('D', split1[n-1], '')] + result
                n -= 1
        elif split1[n-1] == split2[m-1]:
            result = [('C', split1[n-1], split2[m-1])] + result
            n -= 1
            m -= 1
        elif table[n-1][m-1] <= table[n-1][m] and table[n-1][m-1] <= table[n][m-1]:
            result = subs_line(split1[n-1], split2[m-1]) + result 
            n -= 1
            m -= 1        
        elif table[n-1][m] < table[n][m-1] and table[n-1][m] < table[n-1][m-1]:
            result = [('D', split1[n-1], '')] + result
            n -= 1
        elif table[n][m-1] < table[n-1][m] and table[n][m-1] < table[n-1][m-1]:
            result = [('I', '', split2[m-1])] + result
            m -= 1
    return result


def subs_line(line1, line2):
    """ If a subsitute operation happsn in the line edits method this is called
    to check mark what characters have been changed"""
    line_lcs1 = lcs(line1, line2)
    line_lcs2 = line_lcs1[:]
    result1 = ''
    result2 = ''
    
    for char1 in line1:
        if (line_lcs1 != None and line_lcs1 != '') and line_lcs1[0] == char1:
            result1 += line_lcs1[0]
            line_lcs1 = line_lcs1[1:]
        else:
            result1 += '[[' + char1 + ']]'
    
    for char2 in line2:
        if (line_lcs2 != None and line_lcs2 != '') and line_lcs2[0] == char2:
            result2 += line_lcs2[0]
            line_lcs2 = line_lcs2[1:]
        else:
            result2 += '[[' + char2 + ']]'
    
    return [('S', result1, result2)]

   
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


def pop_table(split1, split2):
    """Populates the table for the bottom up version of the edit distance 
    algorithm"""
    n1 = len(split1) + 1
    n2 = len(split2) + 1
    
    table = [[None for _ in range(n2)] for _ in range(n1)]
    
    for i in range(n1):
        for j in range(n2):
            if i == 0 and j == 0:
                table[i][j] = 0
            elif i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif split1[i-1] == split2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
    return table 

s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)