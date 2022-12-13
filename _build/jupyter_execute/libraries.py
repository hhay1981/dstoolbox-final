#!/usr/bin/env python
# coding: utf-8

# # An Ode to Libraries 

# <img src="https://2.bp.blogspot.com/-2s3zgBhRZ3Y/XIQBWYb14aI/AAAAAAAAH00/kBqlSexZx2M2CRltougzJ7j5F-dklLlvgCPcBGAYYCw/s1600/Quote-6.png" width="500" alt="Library Quote" />

# Here is my citation for the library quotes {cite}`lib_quotes`.

# ### Librarians are smart.<br>
# Maybe they can't tell you what **this** means: <br>
# $$ \overline{x} = \frac{x_1 + x_2 + \cdots + x_n}{n} = \frac{1}{n}\left(\sum_{i=1}^{n} x_{i} \right)$$
# <br>
# **but** they most certainly can tell you where to find books in *any* library that will teach you more about mathmatics!

# Let's say, like me, you have a middle-schooler at home. Perhaps they've been tasked to find out more about the *Pythagorean Theorum*, which expresses itself as: <br><br>
# $$ x^2 + y^2 = z^2 $$ <br>
# A librarian might direct them to [this book](https://gvpl.ent.sirsidynix.net/client/en_US/default/search/detailnonmodal/ent:$002f$002fSD_ILS$002f0$002fSD_ILS:254024/ada?qu=pythagorean+theorum&d=ent%3A%2F%2FSD_ILS%2F0%2FSD_ILS%3A254024%7EILS%7E2&h=8) for more information

# In[1]:


import pandas as pd
import altair as alt
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# read in the raw data
lib_df = pd.read_csv('../data/raw/2002-2020-bc-public-libraries-open-data-csv-v20.csv', usecols = ['Period','2 Short Name of Library System', '101 Library Symbol', '3 Type of Library System', '802 Facility Owner', '960 Total computers available for public use'])

# rename columns
lib_df.columns = ['Year', 'Library System Name', 'Library Symbol', 'Library System Type', 'Facility Owner', 'Computers Available']


# In[3]:


# find the number of computers available at each library by their library symbol
lib_sym_comp = lib_df.groupby(['Library Symbol', 'Computers Available']).Year.min().reset_index()
lib_sym_comp.head()


# If we wanted to answer the question "What libraries were owned by the Regional District in 2020?", we could write code like this:<br>
# ```python
# lib_sys_owner = lib_df.groupby(['Library System Name', 'Facility Owner']).Year.min().reset_index()
# lib_sys_owner = lib_sys_owner.loc[(lib_sys_owner['Year'] == 2020) & (lib_sys_owner['Facility Owner'] == 'Regional District')]
# lib_sys_owner
# ```

# Furthermore, if we wanted to state how *many* libraries were owned by the Regional District in 2020, we could write code like this:
# ```python
# rd_2020_count = len(lib_sys_owner)
# print("There were " + str(rd_2020_count) + " libraries owned by the Regional District in 2020")
# ```

# In[4]:


# filter the number of computers available by library symbol for the Greater Victoria Public Library
lib_gvpl = lib_sym_comp.loc[lib_sym_comp['Library Symbol'] == 'BVI'].sort_values('Year')
lib_gvpl = lib_gvpl.astype({'Computers Available':'int'})
lib_gvpl.head()


# In[5]:


# rename cell values for library system types for consistency
lib_df['Library System Type'] = lib_df['Library System Type'].replace({'A': 'Public Library Association', 'I': 'Integrated Library System', 'M': 'Municipal Library', 'R': 'Regional Library System'})
lib_df['Library System Type'].fillna('Not Listed',inplace=True)


# In[6]:


# group library data by year and system type
lib_sys_yr = lib_df.groupby(['Year', 'Library System Type']).size().reset_index(name='count').sort_values('Year')
lib_sys_yr = lib_sys_yr.loc[lib_sys_yr['Year'] == 2020].sort_values('Library System Type')
lib_sys_yr = lib_sys_yr.loc[lib_sys_yr['Year'] == 2020].sort_values('Library System Type')
lib_sys_yr


# In[7]:


lib_gvpl_chart = alt.Chart(lib_gvpl).mark_bar().encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45)),
    y='Computers Available:Q'
).properties(title='Public Computers Available at GVPL', width=500, height=300
            ).configure_scale(bandPaddingInner=0.25)

lib_gvpl_chart


# In[8]:


lib_sys_yr_chart = alt.Chart(lib_sys_yr).mark_bar().encode(
    x=alt.X('Library System Type:O', axis=alt.Axis(labels=False)),
    y=alt.Y('count:Q', title='Number of Systems'),
    color='Library System Type'
).properties(title='BC Library Systems in 2020', width=500, height=300
            ).configure_scale(bandPaddingInner=0.25)

lib_sys_yr_chart


# <img src="https://i1.wp.com/deasillustration.com/blog/wp-content/uploads/2011/02/GVPL_Octopus.jpg?w=435" width="500" alt="New GVPL Library Card Design" />

# Here is my citation for the library dataset {cite}`bcpl_stats`.

# In[ ]:




