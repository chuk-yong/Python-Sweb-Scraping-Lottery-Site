import requests
from lxml import html
import csv

# scrape toto result from 2001 to 2016.  This site has the following format
# https://www.somelottry.com/lottery/country/lottery/month/2016-06

url = 'https://www.somelottry.com/lottery/country/lottery/month/'
month = ['01','02','03','04','05','06','07','08','09','10','11','12']

for i in range (2001,2017): #the latest year is 2016, 2017 would not be searched
    for j in month:
        urlnow = url + str(i) + '-' + j
        r = requests.get(urlnow,verify=False) # make request.  verify=False for a https site
        tree = html.fromstring(r.content) # tree contains html file in tree structure
        for table in tree.xpath('//table'): 
            elements = table.xpath('.//tr/td//p//span//text()') #search for numbers
            date = table.xpath('.//time//text()') #search for date of draw
            csvfile = csv.writer(open("lottery.csv", "a", newline="")) #appends to file
            csvfile.writerow(elements + date) #write numbers and date on each row

