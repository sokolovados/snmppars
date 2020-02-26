def rangedef(item): 
    myiter = iter(item) 
    start = next(myiter) 
    end = start 
    for num in myiter: 
        if num == end +1: 
            end = num 
        else: 
            yield(start,end) 
            start = num 
            end = num 
    yield (start,end) 

