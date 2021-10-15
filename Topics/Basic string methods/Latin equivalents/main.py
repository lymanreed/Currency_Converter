def normalize(name):

    name_dict = {
        'é': 'e',
        'ë': 'e',
        'á': 'a',
        'å': 'a',
        'œ': 'oe',
        'æ': 'ae'
    }

    new_name = ''
    for c in name:
        if c in name_dict:
            new_name = name.replace(c, name_dict[c])

    return new_name


print(normalize(input()))
