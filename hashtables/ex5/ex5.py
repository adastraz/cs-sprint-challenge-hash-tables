# Your code here
cache = {}


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    
    for i in files:
        filename = i.split('/')[-1]
        # print(something[-1])
        if filename not in cache:
            cache[filename] = []
        
        cache[filename].append(i)

    for x in queries:
        if x in cache:
            result += cache[x]

    return result


if __name__ == "__main__":
    files = ['/dir256/dirb256/file256',
            '/dir256/file256', '/dir3490/dirb3490/file3490',
            '/dir3490/file3490', '/dir8192/dirb8192/file8192',
            '/dir8192/file8192']
    queries = [
            "file3490",
            "file256",
            "file999999",
            "file8192"
        ]
    print(finder(files, queries))
