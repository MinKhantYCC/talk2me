# import libraries
from transformers import pipeline
from s2t2s import listen, SpeakText
import re
import os
os.environ['HF_HOME'] = 'cache/'

pipe = pipeline("translation", model="minkhantycc/translation-en-ja", device="cuda")
mytext = ""
while mytext != "また":
    mytext = listen(lang='ja-JP')
    gen_text = pipe(mytext, top_p=1, do_sample=True,
                    max_length=50, temperature = 0.9,
                    no_repeat_ngram_size = 1)
    gen_text = gen_text[0]['translation_text']
    gen_text = gen_text.replace('\n', ' ')
    gen_text = gen_text.replace('<bot>', ' ')
    print(gen_text)
    SpeakText(gen_text)