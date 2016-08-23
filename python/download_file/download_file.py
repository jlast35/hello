#!/usr/bin/env python

import urllib2

url_of_file_to_download = "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1__SX1377_SY720_.jpg"

image_file = urllib2.urlopen(url_of_file_to_download)

output_file = open("matrix.jpg","wb")
output_file.write(image_file.read())
output_file.close()

# wow - it actually worked! i just downloaded an image file from an image file link using python!
# now, if I can just find a command line tool to resize the image and convert to png...