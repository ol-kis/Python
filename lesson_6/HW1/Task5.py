
import random
count=int(input("Enter count of joke: "))
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
joke=[str(random.choice(nouns))+" " + str(random.choice(adverbs))+" "+str(random.choice(adjectives)) for x in range(1,count)]
print(joke)