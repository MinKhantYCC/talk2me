# import libraries
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from s2t2s import listen, SpeakText
import re
import os
os.environ['HF_HOME'] = 'cache/'

tokenizer = AutoTokenizer.from_pretrained("model_B/model_B")
model = AutoModelForCausalLM.from_pretrained("model_B/model_B")
model.to("cuda")
mytext = ""
while mytext != "quit":
    # print("Listening....")
    # mytext = listen()
    mytext = input("What's on your mind: ")
    print(mytext)
    mytext = f"<startofstring>{mytext}<bot>"
    encoded = tokenizer(mytext, return_tensors="pt")
    encoded = {k:v.to("cuda") for k, v in encoded.items()}
    gen_text = model.generate(**encoded,
                            top_p=0.9, do_sample=True,# temperature=0.9,
                            max_length=1024,num_beams=12,
                            no_repeat_ngram_size = 1,
                            pad_token_id = tokenizer.eos_token_id,
                            eos_token_id = tokenizer.eos_token_id,
                            bos_token_id = tokenizer.bos_token_id,)
    gen_text = gen_text[0]
    gen_text = tokenizer.decode(gen_text, skip_special_tokens=True)
    idx = re.search("<bot>:", gen_text)
    if not(idx is None):
        gen_text = gen_text[idx.start():]
    print(gen_text)
    SpeakText(gen_text)