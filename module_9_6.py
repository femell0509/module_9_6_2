def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)-i):
            yield text[j:j+i+1]

for w in all_variants('abc'):
    print(w)

