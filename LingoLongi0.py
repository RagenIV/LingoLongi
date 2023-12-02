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

#nltk.download('stopwords')

#from nltk.corpus import stopwords
#stop_words = set(stopwords.words('english'))
#from nltk.stem.wordnet import WordNetLemmatizer

# replace symbols from text
clear_list = ['.',',',':','»','«', '"']
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

#subs = clear_str(subtext, clear_list)
#subs = word_tokenize(subtext)
#print(nltk.pos_tag(subs))

import text_normalizer



'''
di = {}
for ii in subs.split():
    #print(ii)
    
    # смотрим только определённые части речи
    if p.tag.POS in ['NOUN','VERB','INFN']:
        i = p.normal_form
        if len(i)>=minlen:
            if di.get(i, -1)<0:
                di[i] = 1
            else:
                di[i] = di[i] + 1


print(di)
'''
