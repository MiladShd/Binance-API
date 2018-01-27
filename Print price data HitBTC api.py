
# coding: utf-8

# In[1]:


#Connecting to HitBTC server thtough its public API
#Ploting the data
#Visit https://api.hitbtc.com/ for more details


# In[2]:


import requests #necessary to connect with api
import time #to use sleep function and makes delay


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


apiAddress = 'https://api.hitbtc.com/api/2/public/' #common address
def getRequests(req): #common function
    return requests.get(req).json() #the data are in json format.


# In[5]:


#List of Currencies


# In[6]:


inf = 'currency'
result = getRequests( apiAddress + inf  )
result[1]


# In[7]:


#Candles for BitCoin to USD (BTCUSD)


# In[8]:


result =[]
inf = 'candles/BTCUSD'
limit = '100' #Number of Candles
period = 'M3' #Time Intervals
result = getRequests(apiAddress + inf +'?'+'period='+period+'&limit='+limit)
result[1] #A sample of what we have


# In[9]:


resultDF= pd.DataFrame(result) #convert result to a dataframe


# In[10]:


resultDF= resultDF.reset_index() #add index to the columns


# In[11]:


#Plot together


# In[12]:


#The problem is y axis! look how messi it is


# In[13]:


plt.figure(1)
plt.ylabel('Price')
plt.plot(resultDF['index'], resultDF['close'],resultDF['index'], resultDF['open'],resultDF['index'], resultDF['max'],resultDF['index'], resultDF['min'])
plt.show()


# In[14]:


#To solve messiness just use the yticks/xticks


# In[15]:


plt.figure(2)
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 20))
plt.plot(resultDF['index'], resultDF['close'],resultDF['index'], resultDF['open'],resultDF['index'], resultDF['max'],resultDF['index'], resultDF['min'])
plt.show()


# In[16]:


#Interactive plot -> change the size and surf the coordination


# In[17]:


#method 1:


# In[18]:


from matplotlib import interactive
interactive(True)
plt.figure(3)
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 20))
plt.plot(resultDF['index'], resultDF['close'],resultDF['index'], resultDF['open'],resultDF['index'], resultDF['max'],resultDF['index'], resultDF['min'])
plt.show()
interactive(False)


# In[19]:


#method 2:


# In[20]:


get_ipython().magic('matplotlib notebook')
plt.figure(4)
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 20))
plt.plot(resultDF['index'], resultDF['close'],resultDF['index'], resultDF['open'],resultDF['index'], resultDF['max'],resultDF['index'], resultDF['min'])
plt.show()


# In[21]:


#Plot in 4x1 box


# In[27]:


plt.figure(5) #define a figure

ax= plt.subplot(411)
ax.set_title('close')
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 30))
plt.plot(resultDF['index'], resultDF['close'], 'g')


ax= plt.subplot(412)
ax.set_title('open')
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 30))
plt.plot(resultDF['index'], resultDF['open'] , 'c')


ax= plt.subplot(413)
ax.set_title('max')
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 30))
plt.plot(resultDF['index'], resultDF['max'] , 'b')

ax= plt.subplot(414)
ax.set_title('min')
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 30))
plt.plot(resultDF['index'], resultDF['min'] , 'r')

plt.tight_layout() #makes it tidy with minimum overlap
plt.show()


# In[23]:


#Plot in a 2x2 box


# In[28]:


plt.figure(6) #define a figure

ax= plt.subplot(221)
ax.set_title('close')
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 10))
plt.plot(resultDF['index'], resultDF['close'], 'g')


ax= plt.subplot(222)
ax.set_title('open')
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 10))
plt.plot(resultDF['index'], resultDF['open'] , 'c')


ax= plt.subplot(223)
ax.set_title('max')
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 10))
plt.plot(resultDF['index'], resultDF['max'] , 'b')

ax= plt.subplot(224)
ax.set_title('min')
plt.ylabel('Price')
plt.yticks(np.arange(0, 12500, 10))
plt.plot(resultDF['index'], resultDF['min'] , 'r')

plt.tight_layout() #makes it tidy with minimum overlap
plt.show()


# In[77]:


from matplotlib import interactive
interactive(True)
plt.figure(10)
plt.ylabel('Price')
plt.yticks(np.arange(0, 15000, 20))
plt.plot(resultDF[0:99]['index'], resultDF[0:99]['open'],'go')
plt.plot(resultDF[0:99]['index'], resultDF[0:99]['close'],'yo')
plt.plot(resultDF[0:99]['index'], resultDF[0:99]['min'],'r.')
plt.plot(resultDF[0:99]['index'], resultDF[0:99]['max'],'b*')
plt.show()


# In[79]:


plt.figure(8)
plt.plot(resultDF[0:10]['index'], resultDF[0:10]['min'],'g-')
plt.plot(resultDF[0:10]['index'], resultDF[0:10]['max'],'r-')
plt.plot(resultDF[0:10]['index'], resultDF[0:10]['open'],'y-')
plt.plot(resultDF[0:10]['index'], resultDF[0:10]['close'],'b-')
plt.show()

