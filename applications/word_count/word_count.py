def word_count(s):
    # Your code here

    #create a dict
    count = dict()
    #split the word up into individual strings
    words = s.split()
    #loop through entire string
    for word in words:
        # if the word is in words(s)
        if word in count:
            #count each occurrence
            count[word] += 1
        else:
            count[word] = 1
        # return the count
    return count

    



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat . And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))