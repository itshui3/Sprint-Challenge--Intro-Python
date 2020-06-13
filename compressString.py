# write an algo to compress a given String. If compressed string is same length or greater than original string, return original string

myString = 'aaabcddddef'

def compress(s):

    prev = None
    counter = 1

    compressed = ''

    for l in s:
        if prev == None:
            prev = l
        elif prev == l:
            counter+=1
        elif prev != l:

            compressed += prev
            compressed += str(counter)

            prev = l
            counter = 1

    compressed += s[-1]
    compressed += str(counter)

    if len(compressed) < len(s):
        return compressed
    else:
        return s

print(compress(myString))