def backwards(s):
    """ returns its parameter string in reverse"""
    rev_str = ''
    if len(s) == 0:
        return rev_str
    else:
        return s[-1] + backwards(s[:-1])
    
print(backwards("Hi there!"))
    