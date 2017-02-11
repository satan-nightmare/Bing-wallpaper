#!/usr/bin/python
import urllib
import urllib2
import os
from bs4 import BeautifulSoup

imageurl='http://www.bing.com'
page=urllib2.urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-IN/')
xml=page.read()
soup=BeautifulSoup(xml,'xml')
imageurl += soup.url.string
imageurl=imageurl[:-12]+'1920x1080.jpg'
print imageurl
try:
	urllib.urlretrieve(imageurl, "wallpaper1.jpg")
	if os.path.isfile('wallpaper.jpg'):
		os.remove('wallpaper.jpg')
	os.rename('wallpaper1.jpg','wallpaper.jpg')
except Exception as e:
	pass
os.system("gsettings set org.gnome.desktop.background picture-uri file:///media/sumit/New\ Volume/Python/wallpaper.jpg")