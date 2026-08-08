# Write a program to find out whether a given post is talking about “Harry” or not



post = input ("Enter your post : ")

word = "harry"
if word.lower() in post :
    print ("This post talking about Harry")

else :
    print ("This post does not talking about Harry") 