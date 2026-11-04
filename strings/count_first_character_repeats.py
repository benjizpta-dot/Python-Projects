def countFirst(text):
    text = text.lower()
    if not text:
        return 0
    return text[1:].count(text[0])

if __name__ == "__main__":
    for text in ["Benji", "DDDDD"]:
        print(repr(text), countFirst(text))
