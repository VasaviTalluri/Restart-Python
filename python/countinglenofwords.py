#calculate length of each word in a sentence
a=input("Enter the sentence : ")
words = a.split()
for i in words:
    print(i,":",len(i))