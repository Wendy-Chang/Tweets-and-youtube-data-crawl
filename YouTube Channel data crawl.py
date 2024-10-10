#!/usr/bin/env python
# coding: utf-8

# In[1]:


from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
import argparse
import pafy
import numpy as np
import csv
from urllib import error
from urllib import request
import sys
import seaborn as sns

import matplotlib.pyplot as plt


# In[2]:


api_key='your key'
#channel_id = ''
channel_ids = [] #your channel list
youtube = build('youtube','v3',developerKey=api_key)
pafy.set_api_key("your key")


# In[3]:


def get_channel_stats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(part= 'snippet,contentDetails, statistics',
                                     id=','.join(channel_ids))
    response = request.execute()
    
    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Channel_id = response['items'][i]['id'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
                
    return all_data


# In[4]:


channel_statistics = get_channel_stats(youtube, channel_ids)


# In[5]:


channel_data = pd.DataFrame(channel_statistics)


# In[6]:


channel_data 


# In[7]:


channel_data.info()


# In[8]:


channel_data.to_csv('channels_data.csv')


# In[17]:


channel_data = pd.read_csv('channel_data.csv')


# In[18]:


channel_data


# In[19]:


channel_data["Subscribers"] = pd.to_numeric(channel_data["Subscribers"])
channel_data["Views"] = pd.to_numeric(channel_data["Views"])
channel_data["Total_videos"] = pd.to_numeric(channel_data["Total_videos"])


# In[20]:


channel_data.describe()


# In[21]:


stat2 = channel_data.describe()
stat2.loc['var'] = stat2.loc['std']/stat2.loc['mean']


# In[22]:


stat2


# In[23]:


stat = channel_data.describe() #保存基本统计量
stat.loc['range'] = stat.loc['max']-stat.loc['min']#极差
stat.loc['dis'] =stat.loc['75%']-stat.loc['25%'] #四分位数间距
stat.loc['var'] = stat2.loc['std']/stat2.loc['mean']


# In[24]:


stat


# In[25]:


corr = channel_data.corr()
sns.heatmap (corr, xticklabels = corr.columns, yticklabels = corr.columns)


# In[34]:



# create a bar chart with a logarithmic y-axis
channel_data.plot.bar(x='Channel_name', y=[ 'Total_videos','Subscribers', 'Views'], color=['purple','green','blue'], edgecolor='black')
plt.xlabel('Channel_name')
plt.xticks(rotation=120)
plt.ylabel('Values')
plt.yscale('log')
plt.title('The 6 Seed channels information visualization_YouTube')
plt.xticks(rotation =45)
plt.legend(title='categories', loc=2, bbox_to_anchor=(1.01, 1.0),borderaxespad=0.)

plt.savefig("E:/thesis pictures/Seed channels information visualization_YouTube.png")
plt.show()


# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# create a sample DataFrame
data = {'Column 1': [190000, 1000000, 68900]}
df = pd.DataFrame(data)

# create a density plot
sns.kdeplot(df['Column 1'], shade=True, color='purple')
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Gaussian Distribution of Values')
plt.show()


# In[2]:


import seaborn as sns

# 数据
data = [1,2,3,4,5,6,7,8,9,10]

# 画图
sns.kdeplot(data)


# In[ ]:




