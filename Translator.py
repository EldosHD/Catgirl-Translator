def translate(toTranslate):

    #initialise dictionary
    data = {}

    #open text file with translations in form of:
    #normal (1+ words separated by single space) + double space + furry (1+ words separated by single space)
    infile = open("Catgirl-Translator\\dictionary.txt").readlines()
    for line in infile:
        trans = line.split(" -> ")                      #read line and separate normal and furry
        data[trans[0]] = trans[1].replace("\n", "")     #save translation into dictionary

    token = toTranslate.split(" ")                    #read input from user and separated into words 
    result = ""
    i = 0                                               #current starting word to check from
    while i < len(token):
        found = False                                   #translation found in dictionary
        for j in range(i,len(token)):                   
            word = " ".join(token[i:j+1])
            temp =  word
            word = word.lower().rstrip("!.?-~#")                                           #check for all possible continous combinations starting from i
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