import urllib.request as lib
import re
import string
import sys 

def read_article_file(url):
    req = lib.urlopen(url)
    text = req.read()
    text = text.decode("UTF-8")
    return text

def text_to_article_list(text):
    articles = re.split("<NEW ARTICLE>", text)
    for article in articles:
        if article == "":
            articles.remove(article)
    return articles

def split_words(text):
    splitWordsList = []
    for line in text.splitlines():
            for word in line.split(" "):
                if word != '':
                    splitWordsList.append(word)
    return splitWordsList

def scrub_word(text):
    text = text.strip(string.punctuation)
    return text

def scrub_words(text):
    for index, word in enumerate(text):
        word = scrub_word(word)
        word = word.lower()
        text[index] = word
    return text

def build_article_index(article_list):
    article_index = {}
    for index, article in enumerate(article_list):
        words = split_words(article)
        words = scrub_words(words)
        for word in words:
            if word != "":
                if word not in article_index:
                    article_index[word] = set()
                article_index[word].add(index)
    return article_index

def find_words(keywords, index):
    intersect_docs = set()
    keywordsFinal = []
    tempList = []
    for word in keywords:
        keywordsFinal.append(word.lower())
    for word in keywordsFinal:
        # we want to return a set where the key is the word 
        if word in index.keys():
            tempList.append(index[word])
    if len(tempList) > 0:
        intersect_docs = set.intersection(*tempList)
    else:
        return set()
    return intersect_docs

 
if __name__ == '__main__':
    # You will need to use the read_article_file, text_to_article,
    # build_article_index, and find_words functions to 
    # implement this part correctly.

    if sys.argv[2] == 'find':
        text = read_article_file(sys.argv[1])
        articles = text_to_article_list(text)
        article_index = build_article_index(articles)
        words = sys.argv[3].split(" ")
        wordsInSet = find_words(words, article_index)
        for word in wordsInSet:
                print(word, end=" ")
    if sys.argv[2] == 'print':
        text = read_article_file(sys.argv[1])
        articles = text_to_article_list(text)
        print(articles[int(sys.argv[3])])

    wordss = []
    for word in words:
        wordss.append(words.lower())
    for index, word in enumerate(wordss):
        wordss[index] == word.strip(string.punctuation)
