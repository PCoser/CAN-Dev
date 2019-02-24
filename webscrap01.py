
# coding = B
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
from bs4 import BeautifulSoup
from urllib import request
import operator
import nltk
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords

s = ""
paragraphs = []

stop_words = set(stopwords.words('english')) 

urlstring  = "https://www.ask.com/web?o=0&l=dir&qo=pagination&q=first%20nations%20issues%20site%3Acbc.ca&qsrc=998&page=4"
def urlGetter(urlstring):
   url = urlstring
   page = request.Request(url)
   info = request.urlopen(page).read().decode('utf-8')
   soup = BeautifulSoup(info, 'lxml')
   titles = soup.find_all('a')
   listOfUrls = []
   print(soup)


   for a in soup.find_all('a', href=True):
       print("Found the URL:", a['href'])
       if 'cbc.ca/' in a['href']:
        listOfUrls.append(a['href'])


   print (listOfUrls)
   return listOfUrls

def keyWordGetter(urlstring):
  
# Parse html using BeautifulSoup, you can use a different parser like lxml if present
  try: 
    page = requests.get(urlstring)
    soup = BeautifulSoup(page.text, 'lxml')
    text = soup.find_all('p')
    print(type(text))
    print("THIS IS TYPE")
    for x in text:
      paragraphs.append(str(x))

    print(text)
  except:
    print('usuck')


listresultofurls  = urlGetter(urlstring)

print("THIS IS RESULT")
#for url1 in listresultofurls:
  #print(url1)

for x in range(len(listresultofurls)):
  print("BEGINNING OF ARTICLE")
  print()
  print()
  print()
  keyWordGetter(listresultofurls[x])


for par in paragraphs:
  for word in par:
    print("word IS")
    print(word)

  s+=par+ " "

# import re
# data = s.split()
# from collections import Counter
# c2 = Counter(data)
# print (c2)

wordcount={}

words = s.split()
span = 4
twoWordsSplit =  [" ".join(words[i:i+span]) for i in range(0, len(words), span)]


for word in twoWordsSplit:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print (k, v)


sorted_map = sorted(wordcount.items(), key=operator.itemgetter(1))

print(sorted_map)

for url2 in listresultofurls:
  print(url2)
print(len(listresultofurls))
# with open(r"C:\Python\test\111.txt", "w") as file:
#     for title in titles:
#         file.write("answer"+ title.get('href') + '\n\n')
