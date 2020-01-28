#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pymongo
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from pprint import pprint


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = ('https://mars.nasa.gov/news/')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# # Scraping

# In[4]:


# print(soup.prettify())


# # NASA Mars News

# In[5]:


# title from website
title = soup.find('div', class_="content_title").text

# body from website
body = soup.find('div', class_="rollover_description").text
print(title)
print(body)


# # JPL Mars Space Images - Featured Image

# In[6]:


url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[7]:


base_link = soup.find('div', class_='jpl_logo').a['href'].rstrip('/')
img_link = soup.find('div',class_='carousel_container').article.footer.a['data-fancybox-href']
featured_image_url = "https:"+ base_link + img_link
featured_image_title = soup.find('h1', class_="media_feature_title").text.strip()
print(featured_image_url)
print(featured_image_title)


# # Mars Weather

# In[8]:


url = ('https://twitter.com/marswxreport?lang=en')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[9]:


# print(soup.prettify())


# In[10]:


contents = soup.find_all("div",class_="content")
# print(contents)


# In[11]:


weather_mars = []
for content in contents:
    tweet = content.find("div", class_="js-tweet-text-container").text
    weather_mars.append(tweet)
# print(weather_mars)


# In[12]:


mars_weather = weather_mars[3]
print(mars_weather)


# # Mars Facts

# In[13]:


mars_facts_url = "https://space-facts.com/mars/"
table = pd.read_html(mars_facts_url)
table[0]


# In[14]:


df = table[0]
df.columns = ["Facts", "Value"]
df.set_index(["Facts"])
df


# In[15]:


facts_html = df.to_html()
facts_html = facts_html.replace("\n","")
facts_html


# # Mars Hemipshere

# In[16]:


hemisphere_image_urls = []


# ### Cerberus Hemispheres

# In[17]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[18]:


# print(soup.prettify())


# In[19]:


cerberus_img = soup.find_all('div', class_="wide-image-wrapper")
print(cerberus_img)


# In[20]:


for img in cerberus_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
cerberus_title = soup.find('h2', class_='title').text
print(cerberus_title)
cerberus_hem = {"Title": cerberus_title, "url": full_img}
print(cerberus_hem)


# ### Schiaparelli Hemisphere

# In[21]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[22]:


# print(soup.prettify())


# In[23]:


shiaparelli_img = soup.find_all('div', class_="wide-image-wrapper")
print(shiaparelli_img)


# In[24]:



for img in shiaparelli_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
shiaparelli_title = soup.find('h2', class_='title').text
print(shiaparelli_title)
shiaparelli_hem = {"Title": shiaparelli_title, "url": full_img}
print(shiaparelli_hem)


# ### Syrtis Hemisphere

# In[25]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[26]:


syrtris_img = soup.find_all('div', class_="wide-image-wrapper")
print(syrtris_img)


# In[27]:



for img in syrtris_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
syrtris_title = soup.find('h2', class_='title').text
print(syrtris_title)
syrtris_hem = {"Title": syrtris_title, "url": full_img}
print(syrtris_hem)


# ### Valles Marineris Hemisphere

# In[28]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[29]:


valles_marineris_img = soup.find_all('div', class_="wide-image-wrapper")
print(valles_marineris_img)


# In[30]:


for img in valles_marineris_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
valles_marineris_title = soup.find('h2', class_='title').text
print(valles_marineris_title)
valles_marineris_hem = {"Title": valles_marineris_title, "url": full_img}
print(valles_marineris_hem)


# In[33]:


hemisphere_image_urls.append(cerberus_hem)
hemisphere_image_urls.append(shiaparelli_hem)
hemisphere_image_urls.append(syrtris_hem)
hemisphere_image_urls.append(valles_marineris_hem)
hemisphere_image_urls


# In[ ]:




