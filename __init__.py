import re

def separate(close_text: str):
    regex = r"{{c(\d)::.+?}}"
    matches = re.finditer(regex, close_text, re.MULTILINE)

    new = list(close_text)

    for matchNum, match in enumerate(matches, start=1):
        new[match.start(1):match.end(1)] = [str(matchNum)]

    return "".join(new)

if __name__ == "__main__":
    print(separate("{{c1::thing}} stuff {{c1::thing2}}"))