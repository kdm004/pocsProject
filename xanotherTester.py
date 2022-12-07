from fuzzyWuzzy import fuzz

def get_ratio(word):
    ratio = fuzz.token_set_ratio(word, 'kevin')
    return ratio


# Works.
word_list = ['hello', 'my', 'name', 'is', 'kevin']
for word in word_list:
    #if word == 'kevin':
    ratio = get_ratio(word)
    if ratio >= 90:
        print(word)

# Works.
word_list = ['hello', 'my', 'name', 'is', 'kevin']
for word in word_list:
    #if word == 'kevin':
    ratio = fuzz.token_set_ratio(word, 'kevin')
    if ratio >= 90:
        print(word)



# Doesn't work.
word_list = ['hello', 'my', 'name', 'is', 'kevin']
for word in word_list:
    #if word == 'kevin':
    if fuzz.token_set_ratio(word, 'kevin') >= .90:
        print(word)






