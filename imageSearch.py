"""DO NOT USE"""
"""USE ENHANCED VERSION FOR BETTER RESULTS"""

#imported for opening url
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#import this to be able to call ssl
import ssl

import os

#makes class
class imageSearch():
    #start and end are optional parameters
    #make save = w to write scaped html files
    def __init__(self, kw, save = '', start = -1, end = -1):
        self.tnlink_list = []
        self.wblink_list = []
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
        req = Request(self.site, headers={'User-Agent': 'Chrome'})
        resp = urlopen(req, context = self.ctx)
        self.bs_obj = BeautifulSoup(resp.read(), features='lxml')
        #writes to a file for troubleshooting
        if self.save == 'w':
            try:
                os.mkdir('HTML Scrape Pages')
            except:
                print('Failed to make dir')
            txt_file = open(f'HTML Scrape Pages/scrape{self.page}.html', 'w')
            txt_file.write(self.bs_obj.prettify())
            txt_file.close()
        self.page += 1

    #goes to next page during search
    def nextPage(self):
        self.site = f'https://www.google.com/search?tbm=isch&q={self.keyword}&start={self.page*20}'
        self.openSearch()

    #gets links to thumbnails and websites
    def getLinks(self):
        added = 0
        #loops through all boxes with info
        for item in self.bs_obj.findAll('td'):
            #looks for links to websites that image is on and adds them to list
            for link in item.findAll('a'):
                if 'url?q=' in link['href']:
                    wblink = link['href']
                    wblink = wblink.replace('/url?q=', '')
                    wblink = wblink[:wblink.find('&sa=')]
                    self.wblink_list.append(wblink)
                    added += 1
                if len(self.wblink_list) == (self.end - (int(self.start/20)*20)):
                    break
            #adds thumbnail to list
            for tn in item.findAll('img'):
                self.tnlink_list.append(tn['src'])
                if len(self.tnlink_list) == (self.end - (int(self.start/20)*20)):
                    return

            #stops duplicates
            if added == 20 and len(self.tnlink_list) < (self.end - (int(self.start/20)*20)):
                self.nextPage()
                self.getLinks()
                return

            elif added == 20:
                return

    #changes keyword
    def changeKeyword(self, kw):
        self.keyword = kw
        self.site = f'https://www.google.com/search?tbm=isch&q={self.keyword}'

    #searches user specified range
    def searchRange(self, start, end):
        self.start = start
        self.end = end
        self.page = int(start/20) + 1
        self.site += f'&start={int(self.start/20)*20}'
        self.openSearch()
        self.getLinks()
        temp_start = self.start
        if start != 0:
            while temp_start > 20:
                temp_start -= 20
            for spot in range(temp_start):
                del self.tnlink_list[spot]
                del self.wblink_list[spot]

    #passes thumbnail list
    def getTnList(self):
        return self.tnlink_list

    #passes redirect list
    def getWbList(self):
        return self.wblink_list
