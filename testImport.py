import imageSearch

keyword = 'ocean'
search = imageSearch.imageSearch(keyword)
search.searchRange(0, 5)
try:
    print(search.getTnList()[0])
except:
    pass
print(f'wb: {len(search.getWbList())}')
print(f'ln: {len(search.getTnList())}')
