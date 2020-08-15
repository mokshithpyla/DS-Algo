def getScore(s):
    # returns score
    score = 0
    for i in range(len(s)):
        score += 26 * i + ord('a') - ord(s[i])
    return score

def getString(score):
    # returns corresponding character
    # 27
    string = ''
    if score < 26:
        return chr(ord('a') + score - 1)
    while score != 0:
        rem = score % 26
        string += chr(ord('a') + rem - 1)
        score = rem
    return string

def getBooks (str):
    # Write your code here

    questionCount = str.count('?')
    # lex = {}

    # a aa ab
    library = {}
    maxScore = float('-inf')
    for i in range(len(str)):
        string = str[i]
        score = getScore(string)
        maxScore = max(maxScore, score)
        library[score] = True
    print(maxScore)
    q = 0
    books = []
    for i in range(1, maxScore + 1):
        if q == questionCount:
            break
        if i not in library:
            q += 1
            books.append(getString(i))
    q = 0
    print(books)
    for i in range(len(str)):
        if str[i] == '?':
            str[i] = books[q]
            q += 1
    return str



N = int(input())
str = []
for _ in range(N):
    str.append(input())

out_ = getBooks(str)
for i_out_ in out_:
    print (i_out_)