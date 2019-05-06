"""Currently only gets first 100 results"""
"""Pass same number 2 times for start and end if only one result except for first image, 0, 1 is valid to get only first"""
#imported for opening url
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#import this to be able to call ssl
import ssl

import os
import re
#makes class
class imageSearch():
    #start and end are optional parameters
    #make save = w to write scaped html files
    def __init__(self, kw, save = '', start = -1, end = -1):
        self.link_list = []
        self.keyword = kw
        self.site = f'https://www.google.com/search?tbm=isch&q={self.keyword}'
        self.save = save
        self.declareSSL()
        #checks to see if user entered range
        if start >= 0 and end > 0:
            self.searchRange(start, end)

    #add this to bypass ssl error
    def declareSSL(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

    #opens new website (most likely next page in searches)
    def openSearch(self):
        req = Request(self.site, headers={'User-Agent': 'Chrome/11.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'})
        # req = Request(self.site, headers={'User-Agent': 'Chrome'})
        resp = urlopen(req, context = self.ctx)
        self.bs_obj = BeautifulSoup(resp.read(), features='lxml')
        #writes to a file for troubleshooting
        if self.save == 'w':
            try:
                os.mkdir('HTML Scrape Pages')
            except:
                print('Failed to make dir')
            txt_file = open(f'HTML Scrape Pages/scrape.html', 'w')
            txt_file.write(self.bs_obj.prettify())
            txt_file.close()

    #goes to next page during search
    def nextPage(self):
        self.site = f'https://www.google.com/search?tbm=isch&q={self.keyword}'
        self.openSearch()

    #gets links to thumbnails and websites
    def getLinks(self):
        count = 0
        #loops through all boxes with info
        for item in self.bs_obj.findAll('div', attrs={'class': 'rg_meta notranslate'}):
            #looks for links to websites that image is on and adds them to list
            if self.start == self.end and count == self.end:
                self.link_list.append(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', item.text))
                return
            elif count < self.start:
                count += 1
            elif count == self.end:
                return
            else:
                self.link_list.append(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', item.text))
                count += 1

    #changes keyword
    def changeKeyword(self, kw):
        self.keyword = kw
        self.site = f'https://www.google.com/search?tbm=isch&q={self.keyword}'

    #searches user specified range
    def searchRange(self, start, end):
        self.start = start
        self.end = end
        self.openSearch()
        self.getLinks()

    #passes thumbnail list
    def getLinkList(self):
        return self.link_list
