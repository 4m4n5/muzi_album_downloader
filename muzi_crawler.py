__author__ = 'aman'

import urllib
import requests

# enter album id here
# (it is displayed after /album/ in the url when you click at the album to expand it)
id = raw_input('Enter Album id : ')

number_of_songs = input('Enter no of songs you want to download: ')

url = 'https://sdslabs.co.in/muzi/ajax/album/?id=' + id

source_code = requests.get(url)

json_data = source_code.json()

album = json_data[u'name']
names_of_album = [album, album.replace(' [Deluxe]','')]

artist = json_data[u'band']
for name_of_album in names_of_album:
    print 'Possible Names of the album : ' + name_of_album
print 'Name of Band : ' + artist

def download(down_link, name):
    code = urllib.urlopen(down_link)
    if (code.getcode() == 200):
        print down_link
        urllib.urlretrieve(down_link, name)


for i in range(0, number_of_songs):
    track = json_data[u'tracks'][i][u'title']
    track_id = json_data[u'tracks'][i][u'track']
    print track
    base_download_url = 'https://music.sdslabs.co.in/English/'
    # after track id and before track
    seperators = [' ', ' - ', '. ', ' . ', '. '+artist+' - ', ' '+artist+' - ']
    # check song extension
    song_extensions = ['.mp3', '.m4a']
    # include or exclude 0
    numbers = ['0', '']
    for name_of_album in names_of_album:
        for sep in seperators:
            for ext in song_extensions:
                if(int(track_id)<=9):
                    for num in numbers:
                        download_url = base_download_url + artist + '/' + name_of_album + '/' + num + track_id + sep + track + ext
                        download(download_url, track+'.mp3')
                else:
                    download_url = base_download_url + artist + '/' + name_of_album + '/' + track_id + sep + track + ext
                    download(download_url, track+'.mp3')

