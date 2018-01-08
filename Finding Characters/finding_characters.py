word_list = ['hello','world','my','name','is','Anna']

letter = set('o')

for word in word_list:
    if letter & set(word):
        print word