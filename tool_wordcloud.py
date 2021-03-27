#!/usr/bin/env python

from wordcloud import WordCloud

with open("Hack/Facebook.txt", encoding="utf-8")as file:
    text = file.read()                              # 1. Read the text content
    # 2. Set the background color, width and height of the word cloud, and the number of words
    wd = WordCloud(background_color="black", width=600, height=300, max_words=50).generate(text)
    image = wd.to_image()                               # 3. Generate picture
    image.show()                                        # 4. Show picture
    wd.to_file('wordcloud.png')

