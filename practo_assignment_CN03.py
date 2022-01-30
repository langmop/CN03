import sys
import os
import requests
import time
inputArr = sys.argv
    
index = -1
try:
	index = inputArr.index('-f')
	search = '_'.join(inputArr[1:index])
	fileName = " ".join(inputArr[index+1:])
	reqReturn = requests.get('https://en.wikipedia.org/wiki/'+search)
	if reqReturn.status_code==200:
		if fileName=='':
			fileName = "defaultFile.log"
		file1 = open(fileName, 'a+')
		os.system('cls||clear')
		file1.write('https://en.wikipedia.org/wiki/'+search+"\n")
		loading = ''
		for x in range(11):
			print(loading+' '+str(x*10))
			loading+='_ '
			time.sleep(1)
			os.system('cls||clear')
			
		sys.stdout.write('https://en.wikipedia.org/wiki/'+search+"\n")
		
		print('data saved in ',fileName)
		
	else:
	    print('bad request')
		
except Exception as e:
	if e.args==("'-f' is not in list",):
		search = "_".join(inputArr[1:]) 
		fileName = "defaultFile.log"
		file1 = open(fileName, 'a+')
		os.system('cls||clear')
		file1.write('https://en.wikipedia.org/wiki/'+search+"\n")
		loading = ''
		for x in range(11):
			print(loading+' '+str(x*10))
			loading+='_ '
			time.sleep(1)
			os.system('cls||clear')
			
		sys.stdout.write('https://en.wikipedia.org/wiki/'+search+"\n")
		
		print('data saved in ',fileName)
	else:
		print(e)
