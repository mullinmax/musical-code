def the_name_game(name):
    name = name.strip()
    if not name:
        return "Please enter a valid name."

    name_lower = name.lower()
    vowels = "aeiou"

    # Remove leading consonants up to the first vowel for the rhyme part
    if name_lower[0] in vowels:
        short_name = name_lower
    else:
        for i, char in enumerate(name_lower):
            if char in vowels:
                short_name = name_lower[i:]
                break
        else:
            short_name = name_lower  # fallback, no vowels found

    # Special case: if short_name starts with a banned consonant sound
    def avoid_double_sound(prefix):
        return '' if short_name.startswith(prefix) else prefix

    b = avoid_double_sound('b')
    f = avoid_double_sound('f')
    m = avoid_double_sound('m')

    print(f"{name}, {name}, bo-{b + short_name}")
    print(f"Banana-fana fo-{f + short_name}")
    print(f"Fee-fi-mo-{m + short_name}")
    print(f"{name}!")
