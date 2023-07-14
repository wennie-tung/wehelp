def find_and_print(messages):
    key_words = ['18 years old', 'college student', 'legal age', 'vote']

    for key, value in messages.items():
        contains_key_words = any(key_word in value for key_word in key_words)
        if contains_key_words:
            print(key)

find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})
