#downloading textbook using python



import requests
import bs4
import urllib
from bs4 import BeautifulSoup
#import urllib3
#import urllib.request
#from urllib.request import urlretrieve



print ('Enter a textbook name')
book = input()
print ()
#search in data base and get thhe searched page
url = 'http://gen.lib.rus.ec/search.php?req='+book+'&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def'

source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')

#finding the first result in searched page
for td in soup.find_all('td',{'width':500}):
        link_fbook = td.find('a')['href']
        
        #getting the first result link
        book_page = 'http://gen.lib.rus.ec/'+link_fbook
        break

#download page of the book
def book_dpage(book_url):
    
    source_code = requests.get(book_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    for tr in soup.find_all('td',{'rowspan':22}):
        dpage=tr.find('a')['href']
        
        return dpage
        
book_dpage(book_page)
#getting download link found by giving book page into book download page
book_dlink=book_dpage(book_page)

#finding the download link
def book_d(down):
    
    source_code = requests.get(down)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    for td in soup.find_all('td',{'align':'center'}):
        dlink=td.find('a')['href']
        dlink='http://libgen.io'+dlink
        print (dlink)
        print ("THIS IS THE DOWNLOAD LINK COPY AND PASTE IN BROWSER")
        return(dlink)
        
book_d(book_dlink)

#getting the book name found by our code
def book_name(name):
    source_code = requests.get(name)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    for tr in soup.find_all('title'):
        print (tr.text)
#def book_attr(book_attr):
 #   source_code = requests.get(book_attr)
  #  plain_text = source_code.text
   # soup = BeautifulSoup(plain_text,'lxml')
    #for td in soup.find_all('td','b'):
     #       print (td.text)
#book_attr(book_page)
book_name(book_page)

#downlods the book without any extension with a random name(will be printed by our 'u')
#book path will be printed by 'u'
#change the extension appropriatly can be a pdf epub etc
a=input("enter y to download")
if a=='y':
    u=urllib.request.urlretrieve(book_d(book_dlink),)
    print (u)
    #f=u.open(movie_download(movie_dl),'lol.pdf')
    #print (f)
    #open("dosk.jpg","w").write(f.read())
