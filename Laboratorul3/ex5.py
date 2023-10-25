def validate_dict(rules, dictionary):
    # stocam cheile in 2 multimi => elemente distincte
    valid_keys = set(rule[0] for rule in rules)
    dictionary_keys = set(dictionary.keys())
    rule_dict = {rule[0]: rule[1:] for rule in rules}
    #creaza un dictionar cu cheia rule[o] si valoare restul de ce mai este

    if valid_keys.intersection(dictionary_keys) != dictionary_keys:
        return False
    for key, value in dictionary.items():
            prefix, middle, suffix = None, None, None
            prefix, middle, suffix = rule_dict[key]
            if prefix and suffix:
                if not value.startswith(prefix):
                    return False
                if middle and middle not in value[1:-1]: #value[1:-1] scoate primul si ultimul character din value
                    return False
                if not value.endswith(suffix):
                    return False

    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {
    "key1": "come inside, it's too cold out",
    "key2": "start middle winter",
    "key3": "this is not valid"
}

result = validate_dict(rules, dictionary)
print(result)
