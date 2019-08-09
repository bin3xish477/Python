'''
Alexis Rodriguez
Dictionary example
15 July 2019
'''

playList = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'song1',
        'artist': ['blue'],
        'duration': 2.5},
        {'title': 'song2',
        'artist': ['kitty', 'djcat'],
        'duration': 5.25},
        {'title': 'meowmeow',
        'artist': ['garfield'],
        'duration': 2.0}
    ]
}
totalLength = 0
for song in playList['songs']:
    totalLength += song['duration']
print(totalLength)
