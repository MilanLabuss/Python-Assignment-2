#author milan labus SD2B
#First Function accepting
def functionOne(myList):
    print("Question mark check")
    for x in myList:
        if '?' in x:
            print(x + "Contains Question Mark")


def functionTwo(myList):
    num = {}  #this will store all of the characters found in the list
    #looping through the entire list
    for i in myList:
        for s in i:   #s will go through all character of the list
            if s in num:
                num[s] +=1    #increaing the amount of this character by 1 in count
            else:
                num[s] = 1
        for j in num:
            if num[j] > 1:
               print("character " + j + "  appears in all items")
               print(str(i) + "contains " + j + " " +  str(num[j]) + "times")



myList = ["barack", "obar?ma", "?america?", "war", "russia?", "mak?er"]
functionOne(myList)
print(myList.count("a"))
functionTwo(myList)





