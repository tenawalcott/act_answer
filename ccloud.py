import os
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

path = 'D:\web crawler\\actmi\python'
files = os.listdir(path)
s = ""
for file in files:
    with open(path+"\\"+file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            s += str(line)
k = jieba.cut(s)
stop = [word for word in open("停词.txt", encoding="utf-8")]
pattern = r'[\u4e00-\u9fa5]+'
stop = [re.findall(pattern, s) for s in stop]
stopWord = []
for s in stop:
    try:
        stopWord.append(s[0])
    except:
        continue
text = " ".join([word for word in k if word not in stopWord])
wordcloud = WordCloud(font_path="SIMYOU.TTF").generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
