"""EXAMPLE OF HOW TO IMPORT AND RUN THE IMAGE SEARCH CLASS"""

#imageSearchEnhanced.py must be in the same file for this line to work and import correctly
import imageSearchEnhanced as imageSearch

#easier to import the keyword as unicode
keyword = u'海'
# to write html
# put this line and the import line into whatever program you are tryig to integrate into to get the program to work
search = imageSearch.imageSearch(keyword, '', 0, 5)

# to not write html and include range in init
# search = imageSearch.imageSearch(keyword, '', 0, 5)
# search.searchRange(0, 5)
print(len(search.getLinkList()))

try:
    # gets first image in list to get second do [1][0]
    print(f'Full res link: {search.getLinkList()[0][0]}')
    # gets host website link
    print(f'Host website link: {search.getLinkList()[0][1]}')
    # useless link that would take more time to delete than just keep
    print(f'Useless link: {search.getLinkList()[0][2]}')
except:
    pass
