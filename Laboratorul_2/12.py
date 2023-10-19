def rhymes(words):
    rhyming_groups = {}
    for word in words:
        rhyme_ending = word[-2:]
        if rhyme_ending in rhyming_groups:
            rhyming_groups[rhyme_ending].append(word)
        else:
            rhyming_groups[rhyme_ending] = [word]
    grouped_words = list(rhyming_groups.values())
    return grouped_words

word_list = ['ana', 'banana', 'carte', 'arme', 'parte']
result = rhymes(word_list)
print(result)
