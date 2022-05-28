# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    #reading the files
     with open("./story.txt", "r") as openfile:
     read_file = openfile.read()
     print (read_file)
     print("This file is true")
  #  return "Hello World"


def count_words():
   # text = read_file_content("./story.txt")
    # [assignment] Add your code here
 text = readfile("./story.txt")
    split_text= text.split()
    #print(split_text)
    count ={}
    for i in split text:
    if i in count:
    count[i]+= 1
   else:
       count =1

print(countwords())
    #return {"as": 10, "would": 20}
   
   #  file = open("story.txt" ,"r")
   #  count=0
  #   for line in file:
  #       words = line.split(" ")
 #        count += len (words)
         #file.close()
  #   print("Number of words in a Text File : ", count)