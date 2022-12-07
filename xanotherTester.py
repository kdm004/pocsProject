from fuzzyWuzzy import fuzz

def get_ratio(word):
    ratio = fuzz.token_set_ratio(word, 'kevin')
    return ratio






word_list = ['hello', 'my', 'name', 'is', 'kevin']
for word in word_list:
    #if word == 'kevin':
    ratio = get_ratio(word)
    if ratio >= 90:
        print(word)








