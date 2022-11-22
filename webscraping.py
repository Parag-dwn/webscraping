
# In[1]:


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[2]:


url = "https://www.amazon.in/s?k=samsung&rh=n%3A1389401031&ref=nb_sb_noss"
ur = uReq(url)
read = ur.read()
ur.close()
page = soup(read,"html5lib")


# In[3]:


cont = page.findAll("div",{"class" : "a-section a-spacing-small a-spacing-top-small"})
lis = []

dic = {"Name":[],"Price":[],"rating":[]}


# In[4]:


for i in cont:
    name = i.findAll("span",{"class" : "a-size-medium a-color-base a-text-normal"})
    names=""
    if len(name)!=0:
        Name = name[0].text
        for item in Name:
            if item !="(":
                names = names + item
            else:
                break
        rating =  i.findAll("span",{"class" :"a-icon-alt"})
        if len(rating)!=0:
            Rating = rating[0].text[:3]
            price = i.findAll("span",{"class" :"a-price-whole"})
            Price = price[0].text
            dic["Name"].append(names)
            dic["Price"].append(Price)
            dic["rating"].append(Rating)


# In[5]:


df = pd.DataFrame(dic)
df.to_csv("amazon.csv")


# In[6]:


table = pd.read_csv('amazon.csv')


# In[7]:


table


# In[8]:


maximum = table["Price"].max()
print("Maximum Price is : \t",table["Price"].max())
for i in range(len(table)):
    if table.loc[i]['Price'] == maximum:
        print("Mobile: ",table.loc[i][["Name"]])


# In[9]:


print("\n")
maximum1 = table['Price'].min()
print("Minimum Price is : \t",maximum1)
for i in range(len(table)):
    if table.loc[i]['Price'] == maximum:
        print("Mobile: ",table.loc[i][["Name"]])
        break


# In[ ]:




