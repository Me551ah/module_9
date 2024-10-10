def all_variants(text: str):
    for e in range(len(text)):
        for s in range(len(text) - e):
            yield text[s:s + e + 1]


if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)