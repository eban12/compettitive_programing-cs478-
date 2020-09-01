def matchingStrings(strings, queries):
    count = {}
    for string in strings:
        if string in count:
            count[string] += 1
        else:
            count[string] = 1
    
    return [count[query] if query in count else 0 for query in queries]
