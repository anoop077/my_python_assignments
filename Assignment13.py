#Question1
'''
>>> f=open('//Users//katoch//Desktop//abc//test.txt', 'r')
>>> f.seek(-500,2)
>>> f.read()
'''
#Question2
'''
import re
import string
frequency = {}
document_text = open('//Users//katoch//Desktop//abc//test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print(words, frequency[words])
'''
#Question3
'''
with open("//Users//katoch//Desktop//abc//test.txt","rb")as d:
	var=d.read()

with open("//Users//katoch//Desktop//abc//best.txt","wb")as b:
	b.write(var)

'''
#Question4
'''
>>>f=open('//Users//katoch//Desktop//abc//a.txt',"w")
>>>f.write("Line1 a.txt file")
>>>f.close()
>>>f=open('//Users//katoch//Desktop//abc//a.txt',"a")
>>>f.write("Line2 a.txt file")
>>>f.close()
>>>f=open('//Users//katoch//Desktop//abc//a.txt',"a")
>>>f.write("Line3 a.txt file")
>>>f.close()
>>>f=open('//Users//katoch//Desktop//abc//b.txt',"w")
>>>f.write("Line1 b.txt file")
>>>f.close()
>>>f=open('//Users//katoch//Desktop//abc//b.txt',"a")
>>>f.write("Line2 b.txt file")
>>>f.close()
>>>f=open('//Users//katoch//Desktop//abc//b.txt',"a")
>>>f.write("Line3 b.txt file")
>>>f.close()

>>>with open('//Users//katoch//Desktop//abc//a.txt') as fh1, open('//Users//katoch//Desktop//abc//b.txt') as fh2:
	for line1, line2 in zip(fh1, fh2):
		print(line1+line2)

Line1 a.txt file
Line1 b.txt file

Line2 a.txt file
Line2 b.txt file

Line3 a.txt file
Line3 b.txt file
'''
#Question5
'''
import random
>>> a=[]
>>>for i in range(10):
	a.append(random.randint(0,5))

	
>>> print(a)
>>>f=open('//Users//katoch//Desktop//abc//file1.txt', 'w')
>>> print(a,file=f)
>>> f.close()

>>>f=open('//Users//katoch//Desktop//abc//file1.txt', 'r')
>>> f.readlines()
>>> text=f.readlines()
>>> text.sort()
>>> f.close()


>>> with open('//Users//katoch//Desktop//abc//file1.txt', 'rb') as d:
	var=d.read()

	
>>> with open('//Users//katoch//Desktop//abc//file2.txt','wb') as b:
	b.write(var)
'''
