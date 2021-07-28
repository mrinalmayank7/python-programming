#MODES
#''r' is for read, ti is the default mode 
#'w' is for write from the first line 
#'a' write from the end of file , if file doest not exist it will create a new file 
#'x' is for create a file , if  file exist then it will return error 
#'t' is text
#'b' is for binary 

f= open('file1.txt','w+') #w+ is for both read write 
f1=open('file1.txt','a')
for i in range(3):
    f.write('New Line %d\n'% (i+1))
    f1.write('Append Line %d\n'% (i+2))
f.close()
f1.close()

f2= open('file1.txt','r')
print(f2.readline()) #readline reads one line
if f2.mode=='r':
    readfile=f2.read()  #read all lines
    print(readfile)
f2.close()

