import imageSearchEnhanced as imageSearch

keyword = 'ocean'
# to write html
search = imageSearch.imageSearch(keyword, 'w', 0, 5)
# to not write html and include range in init
# search = imageSearch.imageSearch(keyword, '', 0, 5)
# search.searchRange(0, 5)
print(len(search.getLinkList()))
