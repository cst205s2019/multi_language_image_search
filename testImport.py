import imageSearch

keyword = 'ocean'
# to write html
# search = imageSearch.imageSearch(keyword, 'w')
# to not write html and include range in init
# search = imageSearch.imageSearch(keyword, '', 0, 5)
# search.searchRange(0, 5)
try:
    print(search.getTnList()[0])
except:
    pass
print(f'wb: {len(search.getWbList())}')
print(f'ln: {len(search.getTnList())}')
