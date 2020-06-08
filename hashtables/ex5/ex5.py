# Your code here
cache = {}


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for i in files:
        if i not in cache:
            cache[i] = i

    for y in cache:
        for x in queries:
            if x in y:
                result.append(y)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
