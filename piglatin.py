def get_piglatin(text):
    if type(text)==type(" "):
        words = text.split()
        new_words = []
        for word in words:
            if word.isalpha():
                new_word = word[1:] + word[0] + "a"
                new_words.append(new_word)
            else:
                new_words.append(word)
        return " ".join(new_words)
    else:
        raise ValueError("Input type should be string")

if __name__=="__main__":
    s=input("Enter the string")
    print(get_piglatin(s))
   



