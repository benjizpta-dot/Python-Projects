def countFirst(text):
    text = text.lower()
    if not text:
        return 0
    return text[1:].count(text[0])

for text in ["Benji", "DDDDD"]:
    print(repr(text), countFirst(text))