#!/usr/bin/env python
# coding: utf-8

# In[87]:


import folium
import pandas as pd
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt


# In[88]:


df = pd.read_csv('./dataSQM/ciwarugaData.csv')
df.head()


# In[123]:


df["Kecerahan"][364]


# In[90]:


df1 = pd.read_csv('./dataSQM/bngData.csv')
df1.head()


# In[91]:


df2 = pd.read_csv('./dataSQM/gatsuData.csv')
df2.head()


# In[126]:


m = folium.Map(location=[-2.003589,113.756127], zoom_start=5.5) #sudah cukup mengcover indonesia

pengukuran1 = MarkerCluster().add_to(m)
pengukuran2 = MarkerCluster().add_to(m)
pengukuran3 = MarkerCluster().add_to(m)

# for index, row in df.iterrows():
#     folium.Marker([row['Latitude'], row['Longtitude']], 
#                   popup=row['Kecerahan'],
#                   icon=folium.Icon(icon='cloud')).add_to(pengukuran1)

folium.Marker([df['Latitude'][364], df['Longtitude'][364]], 
                 popup="Survey 2"+"\n Temperatur:"
                          +str( round(row['Temperature'], 10)) +"\n Kecerahan: "
                          +str(row['Kecerahan']),
                  icon=folium.Icon(icon='cloud')).add_to(pengukuran1)
    
for index, row in df1.iterrows():
    folium.Marker([row['Latitude'], row['Longtitude']], 
                  popup="Survey 2"+"\n Temperatur:"
                          +str( round(row['Temperature'], 10)) +"\n Kecerahan: "
                          +str(row['Kecerahan']),
                  icon=folium.Icon(icon='cloud')).add_to(pengukuran2)
    
for index, row in df2.iterrows():
    folium.Marker([row['Latitude'], row['Longtitude']], 
                  popup="Survey 2"+"\n Temperatur:"
                          +str(round(row['Temperature'], 10)) +"\n kecerahan:"
                          +str(row['Kecerahan']),
                  icon=folium.Icon(icon='cloud')).add_to(pengukuran3)


# In[116]:


m.save("./index2.html")


# In[117]:


#Data Imahnoong
url = "http://twro.kabarlangit.com/data/20210418_imahnoong/2021-04-18_SQMdata.csv"

dfi = pd.read_csv(url)
dfi.head()


# # Gambar Grafik

# In[118]:


plt.rcParams["figure.figsize"] = (10,7)

plt.plot(df["Waktu"],df["Kecerahan"],'.',label="Survey 1")
plt.plot(df1["Waktu"],df1["Kecerahan"],'.',label="Survey 2")
plt.plot(df2["Waktu"],df2["Kecerahan"],'.',label="Survey 3")

#plt.plot(dfi["magnitude"],'.',label="Survey ImahNong")

plt.title("Pengamatan Keceragan Langit Kota Bandung")

plt.axhline(18.38,c='red',label="City Sky")

plt.axhline(20.49,c='magenta',label="Bright Suburban Sky")


plt.xlabel("Waktu (detik)")

plt.ylabel("Kecerahan (mpass)")

plt.legend()

plt.grid()
plt.show()


# In[119]:


#plt.plot(dfi["magnitude"],'.',label="Survey ImahNong")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




