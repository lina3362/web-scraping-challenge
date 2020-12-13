#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import os


# In[38]:


#site navigation
executable_path = {"executable_path": "C:\Program Files\chromedriver_win32\chromedriver"}
browser = Browser('chrome', **executable_path, headless=False)


# NASA Mars News

# In[39]:


#open url
mars_url = "https://mars.nasa.gov/news/"
browser.visit(mars_url)
#using bs to write it into html
html = browser.html
soup = bs(html, "html.parser")


# In[40]:


mars_title = soup.find_all('div', class_='content_title')[0].text
mars_paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
print(mars_title)
print(mars_paragraph)


# In[ ]:





# JPL Mars Space Images - Featured Image

# In[43]:


#Open browser to url for JPL Featured Space Image
browser.visit("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
html = browser.html
soup = bs(html, "html.parser")


# In[49]:


image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + image
print(featured_image_url)


# In[ ]:





# Mars Facts

# In[56]:


# Use Pandas to scrape data
mars_facts = pd.read_html('https://space-facts.com/mars/')
#put mars facts into a table
df = mars_facts[0]
# Rename columns and set index
df.columns=['Parameter', 'Number']
df


# In[57]:


#convert the data to a HTML table string
mars_facts_table = [df.to_html(classes='data table table-borderless', index=False, header=False, border=0)]
mars_facts_table


# In[ ]:





# Mars Hemispheres

# In[58]:


# Open browser to USGS Astrogeology site
hemisphere.img_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
html = browser.html
soup = bs(html, 'html.parser')


# In[75]:


mars_hemispheres = []
results = soup.find_all('div', class_='item')

# find the image url to the full resolution image
for result in results:
    mars_dict = {}
    titles = result.find('h3').text
    individual_link = result.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + individual_link
    browser.visit(image_link)

    print(titles)
    print(image_link)
    


# In[79]:


#Add hemisphere title to dictionary
mars_dict['title']= titles
# Add image url to dictionary
mars_dict['image_url'] = image_link
# Append the list with dictionaries
mars_hemispheres.append(mars_dict)

mars_hemispheres
