
#TASK TO BE DONE 
#TASK 1. Creating a file & adding backslash (\) before every double quote in the ﬁle contents.
#TASK 2. Reading That file 
#TASK 3. write it to another ﬁle in the same folder.
#TASK 4. print the contents of both  ﬁles.
print("Name :Mrinal Mayank")
print("UID :19BCS1605")

Write1=open('TEXTFILE1.txt','a')
Write1.write("Hello , I am  \"MRINAL \", my hobby is painting") #TASK 1
Write1.close()

Read1= open('TEXTFILE1.txt','r')
print("READING TEXTFILE1 :",Read1.read())                       #TASK 2
Read1.close()

COPIED_FROM =open('TEXTFILE1.txt','r') 
COPIED_TO   =open('TEXTFILE2.txt','a') 
for i in COPIED_FROM :
    COPIED_TO.write(i)                                          #TASK 3
COPIED_FROM.close() 
COPIED_TO.close()

Read2= open('TEXTFILE1.txt','r')
Read3= open('TEXTFILE2.txt','r')
print("DISPLAY TEXTFILE1 :",Read2.read())                       #TASK 4
print("DISPLAY TEXTFILE2 :",Read3.read())
Read2.close()
Read3.close()
