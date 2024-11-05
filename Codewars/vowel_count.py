def get_count(sentence):
    vowel = ["a", "e", "i", "o", "u"]
    count_vowel = 0
    for x in range(len(sentence)):
        if sentence[x] in vowel:
            count_vowel+=1
    return count_vowel

if __name__ == "__main__":
    print(get_count("aeiou"))