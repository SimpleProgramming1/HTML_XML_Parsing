
#Importing Library 

from bs4 import BeautifulSoup
import urllib.request


#Extracting content from HTML page

page= urllib.request.urlopen('https://statecancerprofiles.cancer.gov/quick-profiles/index.php?statename=newjersey')


# Applying BeautifulSoup object to page variable and applying HTML parser

soup=BeautifulSoup(page,'html.parser')


# printing the object

print(soup)


# Extracting content from XML page and storing it in webpage variable 

webpage= urllib.request.urlopen('https://data.lacity.org/api/views/nxs9-385f/rows.xml?accessType=DOWNLOAD')


# Applying BeautifulSoup object to webpage variable and applying XML parser

soup1=BeautifulSoup(webpage,'lxml')


# printing the object

print(soup1.prettify())


# Extracting relevant tags

zip_code=soup1.find_all('zip_code')

zip_code




