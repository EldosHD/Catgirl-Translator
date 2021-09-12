import re

def translate(toTranslate, data: dict):

    token = re.split(" |\r\n|\n\r|\r|\n", toTranslate)                    #read input from user and separated into words 
    result = ""
    i = 0                                               #current starting word to check from
    while i < len(token):
        found = False                                   #translation found in dictionary
        for j in range(i,len(token)):                   
            word = " ".join(token[i:j+1])
            temp =  word
            word = word.lower().rstrip(",;:*+-_!.?-~#")        #check for all possible continous combinations starting from i
            end = temp[len(word):]
            if word in data:
                result += data[word]+ end + " "              #translation found
                found = True
                i = j + 1                               #set new starting word after found combination
                j = len(token)                          
        if not found:                       
            result += token[i] + " "                    #no translation found -> keep word as it is
            i += 1
    return result