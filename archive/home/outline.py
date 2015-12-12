# -*- coding: utf-8 -*-
#Notes and outlines for the home page functionality

"""


1. Access file from external drive
2. Untar file -> D0000001P.pdf, D0000001F.tiff, D0000001T.txt, D0000001M.txt
3. Store pdf, txt and meta.txt to database
4. Tie 3 files together somehow (Is file name enough)
5. Throw away .tiff file



N. Get next file.
loop to end


Noun extraction routine

import nltk
essays = u 'text here'
tokens = nltk.word_tokenize(essays)
tagged = nltk.pos_tag(tokens)
nouns = [word for word,pos in tagged \
     if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')
into_string = str(nouns)

output = open("output.txt", "w")
output.write(joined)
output.close()

"""
