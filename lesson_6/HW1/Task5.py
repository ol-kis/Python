
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n=10
joke=[str(random.choice(nouns))+" " + str(random.choice(adverbs))+" "+str(random.choice(adjectives)) for x in range(1,n)]
print(joke)