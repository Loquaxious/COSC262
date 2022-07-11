def all_pairs(list1, list2, start_index=0):
    """Returns a list of all tuples that can be made by pairing an item 
    from list1 to list2"""
    
    if start_index == len(list1):
        return []
    else:
        return some_pairs(list1[start_index], list2) + all_pairs(list1, list2, start_index+1)
        
def some_pairs(item, list2, start_index=0):
    """Add the item to each element of the list"""
    
    if len(list2) == start_index:
        return []
    else:
        return [(item, list2[start_index])] + some_pairs(item, list2, \
                                                         start_index+1)
    
print(all_pairs([1, 2], [10, 20, 30]))    