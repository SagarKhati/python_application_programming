fp = open('temp.txt', 'r')   # opening
'if temp.txt file not exits, it will throw error.' 
#FileNotFoundError: [Errno 2] No such file or directory: 'temp.txt'
content = fp.read()          # reading
print(content)               # displaying content
fp.close()                   # closing


fob = open('a.txt', 'w')
'if a.txt file not exits, it will create file.'
'if a.txt file exits, it will overwrite content.'
fob.write('hey now brown cow')
fob.close()


fob = open('a.txt', 'r')
'r : read only mode'
print(fob.read(3)) #reads 3bytes only
print(fob.read())  #reads till end of file
fob.close()



############################################################################################



# Opening and Closing file

#opens the file file.txt in read mode  
fileptr = open("file.txt","r")  
if fileptr:  
    print("file is opened successfully")  
#closes the opened file  
fileptr.close()



#Reading the file

#open the file.txt in read mode. causes error if no such file exists.  
fileptr = open("file.txt","r");   
  
#stores all the data of the file into the variable content  
content = fileptr.read(9);   
  
# prints the type of the data stored in the file  
print(type(content))   
  
#prints the content of the file  
print(content)   
  
#closes the opened file  
fileptr.close()



#Read Lines of the file

#open the file.txt in read mode. causes error if no such file exists.  
fileptr = open("file.txt","r");   
  
#stores all the data of the file into the variable content  
content = fileptr.readline();   
  
# prints the type of the data stored in the file  
print(type(content))   
  
#prints the content of the file  
print(content)   
  
#closes the opened file  
fileptr.close() 



#Looping through the file

#open the file.txt in read mode. causes an error if no such file exists.  
fileptr = open("file.txt","r");   
  
#running a for loop   
for i in fileptr:  
    print(i) # i contains each line of the file   
    
    
    
#Writing the file
    
#open the file.txt in append mode. Creates a new file if no such file exists.  
fileptr = open("file.txt","a");   
  
#appending the content to the file  
fileptr.write("Python is the modern day language. It makes things so simple.")  
  
#closing the opened file   
fileptr.close();


#open the file.txt in write mode.  
fileptr = open("file.txt","w");   
  
#overwriting the content of the file  
fileptr.write("Python is the modern day language. It makes things so simple.")  
  
#closing the opened file   
fileptr.close();



#Creating a new file

#open the file2.txt in read mode. creates file if no such file exists. cause error if such file exists  
# fileptr = open("file2.txt","x");   
  
# print(fileptr)  
  
# if fileptr:  
#     print("File created successfully");  
    
    
    
#Using with statement with files
    
with open("file.txt",'r') as f:  
    content = f.read();  
    print(content)  
    
    
    
#File Pointer positions

# open the file file2.txt in read mode  
fileptr = open("file2.txt","r")  
  
#initially the filepointer is at 0   
print("The filepointer is at byte :",fileptr.tell())  
  
#reading the content of the file  
content = fileptr.read();  
  
#after the read operation file pointer modifies. tell() returns the location of the fileptr.
print("After reading, the filepointer is at:",fileptr.tell())



#Modifying file pointer position

# open the file file2.txt in read mode  
fileptr = open("file2.txt","r")  
  
#initially the filepointer is at 0   
print("The filepointer is at byte :",fileptr.tell())  
  
#changing the file pointer location to 10.  
fileptr.seek(10);  
  
#tell() returns the location of the fileptr.   
print("After reading, the filepointer is at:",fileptr.tell())  