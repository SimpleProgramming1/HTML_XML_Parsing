
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
import urllib.request


# In[5]:

page= urllib.request.urlopen('https://statecancerprofiles.cancer.gov/quick-profiles/index.php?statename=newjersey')


# In[6]:

soup=BeautifulSoup(page,'html.parser')


# In[7]:

print(soup)


# In[8]:

webpage= urllib.request.urlopen('https://data.lacity.org/api/views/nxs9-385f/rows.xml?accessType=DOWNLOAD')


# In[9]:

soup1=BeautifulSoup(webpage,'lxml')


# In[11]:

print(soup1.prettify())


# In[12]:

zip_code=soup1.find_all('zip_code')


# In[13]:

zip_code


# In[ ]:



