import urllib
from bs4 import BeautifulSoup
import os

soup = BeautifulSoup(urllib.urlopen('http://jamespotterseries.com').read())
command = 'pdfunite'

for i in range(1, 25):
	url = soup.find_all('a')[i].get('href')
	urllib.urlretrieve(url, '%s.pdf' % str(i))
	command += ' %s.pdf' % str(i)

command += ' final.pdf'
os.system(command)

print "All done! Deleting unnecessary files."
for i in range(1, 25):
	os.remove('%s.pdf' % i)

