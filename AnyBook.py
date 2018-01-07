#download any book just give exact name and textbook  or fiction


import requests
import bs4
import urllib
from bs4 import BeautifulSoup
#import urllib3
#import urllib.request
#from urllib.request import urlretrieve


def textbook_download(textbook):
        #print ('Enter a textbook name')
        book = textbook
        print ()
        #search in data base and get thhe searched page
        url = 'http://gen.lib.rus.ec/search.php?req='+book+'&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def'

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')

        #finding the first result in searched page
        for td in soup.find_all('td',{'width':500}):
                link_fbook = td.find('a')['href']
                print (link_fbook)
                #getting the first result link
                book_page = 'http://gen.lib.rus.ec/'+link_fbook
                break

        #download page of the book
        def book_dpage(book_url):
            print ('result')
            source_code = requests.get(book_url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text,'lxml')
            for tr in soup.find_all('td',{'rowspan':22}):
                dpage=tr.find('a')['href']
                print (dpage)
        return dpage
                
        book_dpage(book_page)
        #getting download link found by giving book page into book download page
        book_dlink=book_dpage(book_page)

        #finding the download link
        def book_d(down):
            print(2)
            source_code = requests.get(down)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text,'lxml')
            for td in soup.find_all('td',{'align':'center'}):
                dlink=td.find('a')['href']
                dlink='http://libgen.io'+dlink
                print (dlink)
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


def fiction_book(fiction):
        #print ('Enter a Fiction book name')
        book = fiction
        print ()
        format_book=input("enter the format you want mobi epub pdf")
        #search in data base and get thhe searched page
        url = 'http://gen.lib.rus.ec/foreignfiction/index.php?s='+book+'&f_lang=English&f_columns=1&f_ext='+format_book+'&f_group=1'

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')

        #finding the first result in searched page
        for td in soup.find_all('a',{'id':'mlink'}):
                #link_fbook = td.find('a')['href']
                #print (td['href'])
                link_fbook=td['href']
                #getting the first result link
                book_page = 'http://libgen.io/'+link_fbook
                print (book_page)
                break


book_s=input("Enter a book name")
print ()
book_type=input("Enter 't' for textbook or 'f' for fiction")
if book_type=='t':
        textbook_download(book_s)
elif book_type=='f':
        fiction_book(book_s)
else:
        print("Enter 't' for textbook or 'f' for fiction")
        
