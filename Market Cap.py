#importing the libraries
import urllib3
import re
#opening the txt file
f=open("C:\\Users\\shash\\OneDrive\\Desktop\\MSBA\\Computing for Business Analytics\\Assignment 5\\dowTickers.txt",'r')
#opening new txt file in write mode
f1=open('output_data.txt','w')
#reading the ticker list in txt file
tickerList=f.readlines()
sum=0
c=0
for i in range(len(tickerList)):
    c+=1
    try:
        address="https://finance.yahoo.com/quote/"
        address=address+tickerList[i].strip()#appending the ticker code to the URL
        http = urllib3.PoolManager()
        response = http.request('GET', address)
        webContent = str(response.data)
        position=webContent.find("Market Cap")
        res=re.findall("\d+\.\d+[B,T]", webContent[position:position+300])
        sum+=float(res[0][:-1])*(1000 if res[0][-1]=='T'else 1)#adding up all the capitals of 30 companies.
    except IndexError:
        continue

print('Combined market cap of 30 comapanies:'+str(sum)+'B')
print('Average of market cap of 30 companies:'+str(sum/len(tickerList))+'B')    
    

