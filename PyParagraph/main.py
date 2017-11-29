#import modules
import os
import csv
import re

sentence = []
word = []

filepath = os.path.join("paragraph_2.txt")

with open(filepath, "r", newline='') as txtfile:
    paragraph = txtfile.read()

    # get the sentence count
    if "\n" in paragraph:
        sentence = re.split(r'\n\n', paragraph)
    else:
        sentence = re.split("(?<=[.!?]) +", paragraph)

    sentence_count = len(sentence)

    # get the word count
    for x in sentence:
        word += x.split()

    word_count = len(word)

    # average letter count per word
    sum_word_len = 0
    for x in word:
        sum_word_len += len(x)

    avg_letter_cnt = sum_word_len/len(word)

    # average sentence length
    avg_sent_len = word_count/sentence_count

path = os.path.join("..\PyParagraph", "Analysis_"+filepath[0:11]+".txt")

print("Paragraph Analysis")
print("_____________________________")
print("Approximate Word Count: "+ str(word_count))
print("Approximate Sentence count: " + str(sentence_count))
print("Average Letter Count: " + str(avg_letter_cnt))
print("Average Sentence Length: " + str(avg_sent_len))
print("_____________________________")

with open(path, "w", newline='') as txtfile:
    txtfile.write("Paragraph Analysis\n")
    txtfile.write("_____________________________\n")
    txtfile.write("Approximate Word Count: "+ str(word_count) + "\n")
    txtfile.write("Approximate Sentence count: " + str(sentence_count) +"\n")
    txtfile.write("Average Letter Count: " + str(avg_letter_cnt) + "\n")
    txtfile.write("Average Sentence Length: " + str(avg_sent_len) + "\n")
    txtfile.write("_____________________________")