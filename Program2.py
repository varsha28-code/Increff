s="The sun sets in the west"

def longest(s):

    words=s.split()

    vowels = {'a','e','i','o','u'}

    res="00"

    ml=0

    for word in words:

        if len(word)%2==0 and word[0] in vowels:

            if len(word)>ml:

                ml=len(word)

                res=word

    print(res)

longest(s)
