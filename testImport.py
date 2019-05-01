import imageSearchEnhanced as imageSearch

keyword = 'ocean'
# to write html
search = imageSearch.imageSearch(keyword, 'w', 0, 1)

# to not write html and include range in init
# search = imageSearch.imageSearch(keyword, '', 0, 5)
# search.searchRange(0, 5)
print(len(search.getLinkList()))
# gets first image in list to get second do [1][0]
print(f'Full res link: {search.getLinkList()[0][0]}')
# gets host website link
print(f'Host website link: {search.getLinkList()[0][1]}')
# useless link that would take more time to delete than just keep
print(f'Useless link: {search.getLinkList()[0][2]}')
