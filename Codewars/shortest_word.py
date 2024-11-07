"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be emptyand you do not need to account for different data types.
"""
def find_short(s):
    # your code here
    list_words = s.split()
    len_words = []
    for x in range(len(list_words)):
        len_words.append(len(list_words[x]))
    len_words.sort()
    return len_words[0] # l: shortest word length

def find_shortv2 (s):
    return min(len(x) for x in s.split())

if __name__ == "__main__":
    find_short("Hello World, this is me")