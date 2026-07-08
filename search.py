# word="python"
# with open("exercise.txt","r") as f:
#         data=f.read()
#         if data.find(word)==-1:
#                 print("not found")
#         else:
#                 print("found")        

# with function
def search_word():
    word="like"
    with open("exercise.txt","r") as f:
         data=f.read()
    if data.find(word)==-1:
                 print("not found")
    else:
                 print("found") 
search_word()                

# checking in which line

def search_word_line():
    word="like"
    data=True
    line_no = 1
    with open("exercise.txt","r") as f:
           while data:
                   data=f.readline()
                   if word in data:
                           print(line_no)
                           return
                   line_no += 1                                  
    return -1
search_word_line()           