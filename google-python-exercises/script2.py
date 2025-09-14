""" import re

text = "123 words"
pattern = r"(\d+)\s(words)"   # raw string, regex pattern

m = re.match(pattern, text)
if m:
    print("Full match:", m.group(0))  # '123 words'
    print("Digits:   ", m.group(1))  # '123'
    print("Word:     ", m.group(2))  # 'words' """


import re

# Regex pattern: one or more digits
pattern = r"\d+"  # \d = digit, + = one or more of previous token
texts = ["1", "12", "123", "abc", "a1b2c3"]

print(f"Pattern: {pattern}\n")

for text in texts:
    match = re.match(pattern, text)
    if match:
        print(f"Text: {text} -> Matched: {match.group()}")
    else:
        print(f"Text: {text} -> No match")

