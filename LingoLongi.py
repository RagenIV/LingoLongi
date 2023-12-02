# TODO
# 10. Word classification by Wordlists
# 20. Subtitles filter
# 30. Memorise scripts
# 40. Movie's wordlist filter
# 50. Personal vocabular model

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize

#from nltk.corpus import stopwords
#stop_words = set(stopwords.words('english'))
#from nltk.stem.wordnet import WordNetLemmatizer

# replace symbols from text
clear_list = ['.',',',':','»','«', '"', '/','-',"'"]
def clear_str(s1, li):
    s2 = s1
    for iii in li:
        s2 = s2.replace(iii,'')
    return s2.lower()


# import subtitles
# TODO menu of srt with request to https://my-subs.co/
subf = open("./srt/twilight.srt")
subtext = subf.read()
subf.close()
words = set()
subs = clear_str(subtext, clear_list)
subs = word_tokenize(subs)
for word in nltk.pos_tag(subs):
    if len(word[1]) > 1 and word[1] not in ["CD", "JJ"]:
        words.add(word[0])
#print(words)

# import wordlist
import xlwings as xw

print("""Choose your level:
0) Pre A1
1) A1
2) A2
3) B1
4) B2+""")
KNOWN = dict()
L = int(input())
# Open the worksheet
for lev in range(L):
    app = xw.App(visible=False)
    # Specifying a sheet
    w = xw.Book("./wordlevels/levels.xlsx")
    ws = w.sheets[str(lev)]
     
    # Selecting data from
    # a single cell
    v1 = ws.range("A1:A3333").value
    v2 = ws.range("B1:B3333").value
    w.close()
    app.quit()
    res = set([i for i in v1 if i is not None])
    KNOWN = KNOWN | dict(zip(v1, v2))

# Filter Subtitles
LEARN = list(words - res)
print("You should learn totally", len(LEARN), "words")
print("So, how much of them you would like learn now?")
print("type 0 to show all of them")
k = int(input())
if k > 0:
    import random
    LEARN = random.choices(LEARN, k=k)


# Learn technique
print(LEARN)
