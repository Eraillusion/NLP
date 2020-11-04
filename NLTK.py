import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
from nltk.corpus import brown
from nltk import word_tokenize,sent_tokenize
tokens = nltk.word_tokenize("Web Mining is the application of data mining techniques to discover
and retrieve useful information and patterns from the World Wide Web documents and services. +
"
"Unlike the Web Content Mining and Web Struture Mining, Web Usage
Mining - automatic discover the patterns in clickstreams and associated data collected or
generated as a + "
"result of user interactions with one or more Web sites. discover
user’s navigation pattern and predict user's behavior，The discovered patterns are usually
represented + "
"as collections of pages, objects, or resources that are frequently
accessed by groups of users with common interests.")
tokens2 = nltk.word_tokenize("Another day has gone, I'm still alone, how could this be? You're
not here with me.You never say goodbye, someone tell me why, did you have to go? And leave my
world so cold + "
"Everyday I sit and ask myself. How did love slip away. Something
whispers in my ear and says. That you are not alone. I am here with you. Though you're far away.
I am here to stay")
tokens3 = nltk.word_tokenize("The fair girl is really fair at the fair, I have to shot a beautiful
shot of this cute girl. If I had to live my life without you near me. The days would all be empty.
The nights would seem so long. + "
"With you I see forever, oh, so clearly. I might have been in love
before. But it never felt this strong. Our dreams are young and we both know. They'll take us
where we want to go. + "
"Hold me now, touch me now. I don't want to live without you.
Nothing's gonna change my love for you. You oughta know by now how much I love you. One thing
you can be sure of. + "
"I'll never ask for more than your love. The world may change my
whole life through. But nothing's gonna change my love for you")
#print("Tokens:", tokens)
#print("Tokens:", tokens2)
print("Parrt of Paragraph 1: ", nltk.pos_tag(tokens))
print("Paragraph 1 ends\n")
print("Parrt of Paragraph 2: ", nltk.pos_tag(tokens2))
print("Paragraph 2 ends\n")
print("Parrt of Paragraph 3:\n Lyrics of Nothing's Gonna Change My Love For You ",
nltk.pos_tag(tokens3))
print("Paragraph 3 ends\n")