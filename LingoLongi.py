# TODO
# 10. Word classification by Wordlists
# 20. Subtitles filter
# 30. Memorise scripts
# 40. Movie's wordlist filter
# 50. Personal vocabular model

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

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

subs = clear_str(subtext, clear_list)

di = {}
for ii in subs.split():
    p = morph.parse(ii)[0]
    # смотрим только определённые части речи
    if p.tag.POS in ['NOUN','VERB','INFN']:
        i = p.normal_form
        if len(i)>=minlen:
            if di.get(i, -1)<0:
                di[i] = 1
            else:
                di[i] = di[i] + 1


print(di)
