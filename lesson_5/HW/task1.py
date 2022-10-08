words="авб абв бав абв вба бав вба абв абв абв".split(" ")
srt_word="абв"
res=list((filter(lambda x: srt_word not in x,words)))
print((" ").join(res))
#авб бав вба бав вба