from itertools import count
import string
#I am Reilly Prescott and this is my program to split a string of text into a list, remove all punctuation from the text, and break down the amount of words containing 'e' in the string. 

global text
text = """And so, does the destination matter? Or is it the path we take? I declare that no accomplishment has substance nearly as great as the road used to achieve it.
We are not creatures of destinations. 
It is the journey that shapes us. Our callused feet, our backs strong from carrying the weight of our travels, our eyes open with the fresh delight of experiences lived.
In the end, I must proclaim that no good can be achieved by false means.
For the substance of our existence is not in the achievement, but in the method."""

def main(text):

    #Removing punctuation
    text_without_punct = ""
    for letter in text:
        if letter not in string.punctuation:
            text_without_punct += letter
    text = text_without_punct
    #Splitting the text
    wds = text.split()
    text = wds
    length = len(text)
    #Counting words with e in the list
    es = 0
    for word in text:
        if "e" in word:
            es += 1


    float(length)
    float(es)
    
    print("Your text is ",length," words long. Out of those ", length, "words ",es," contain the letter 'e'.", "That is ",(es/length)*100, "% of your text")

    return text

main(text)

