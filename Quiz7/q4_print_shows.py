def print_shows(show_list):
    """Takes an list of show tuples and prints in order of start time
    a list of shows to maximise the amount of shows you can watch"""
    sorted_shows = sorted(show_list, key=lambda shows: shows[1] + shows[2])
    last = 0
    n = len(show_list)
    
    for i in range(n):
        if sorted_shows[i][1] >= last:
            last = sorted_shows[i][1] + sorted_shows[i][2]
            print(str.format("{} {} {}",sorted_shows[i][0], \
                             sorted_shows[i][1], last))
            

# The example from the lecture notes
print_shows([
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4), 
    ('h', 8, 3)])