user_sentence = input("What is your sentence?: ")

user_sentence_split = user_sentence.split() #split() function splits the words into seperate sentences

word_counter = 1

for sentence in user_sentence_split:
    modified_sentence = sentence[:10] # extracting the first 10 letters inn the user's sentence/word
    print(f"{word_counter}. {modified_sentence}")    #word-counter puts numbers on new lines
    word_counter += 1






#for word in user_sentence_split:
    #print(f"{word_counter}. {word}")
    #word_counter +=1