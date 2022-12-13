#!/usr/bin/env python
# coding: utf-8

# # Grizzly Bear Conservation in BC

# <img src="https://www2.gov.bc.ca/assets/gov/environment/plants-animals-and-ecosystems/wildlife-wildlife-habitat/grizzly-bears/images/grizzly_bear_photo_credit_troy_malish_1140.jpg" width="500" alt="Adult Grizzly Bear" />

# ### Have you ever been to Moricetown?
# I went once, in the summer of 2016. I got to see the fish ladders and the wooden fish huts that the Wet'suwet'en First Nation people used/use for fishing. Often, you'll see grizzly bears there like the one pictured above.

# #### Moricetown Canyon is quite the sight to behold.
# To quote [Eh Canada Travel](https://www.ehcanadatravel.com/british-columbia/northern-bc/smithers/parks-places/5364-moricetown-canyon.html):
# > *Time your visit right and view the Moricetown Canyon at its best (during high run off season) when the Bulkley River is all about white water - crashing and smashing its way down into the canyon creating some fantastic kodak moments.*
# <br>
# 
# Water flow can be calculated like this:<br>
# $$ 0.425\text{ m/s}\times 1\text{ m}\times 0.6\text{ m} = 0.255\text{ m}^3\text{s} $$

# In[1]:


import pandas as pd
import altair as alt
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# read in the raw data
griz_df = pd.read_csv('../data/raw/grizzlybear_2019_conservationranking_results.csv', usecols = ['GBPU', 'Region', 'PopnEst2018', 'Female_Popn_2018', 'Overal_Threat'])

# rename columns
griz_df.columns = ['Population Units', 'Region', 'Population Estimate', 'Female Population', 'Overall Threat']


# In[3]:


# find the grizzly bear population estimate (including a breakout for females) for every region 
griz_pop_reg = griz_df.groupby(['Region']).sum().reset_index()
griz_pop_reg


# In[4]:


# narrow down the search to the Skeena Region 
griz_pop_skeena = griz_pop_reg.loc[griz_pop_reg['Region'] == 'Skeena']
griz_pop_skeena


# If we wanted to answer the question "What percentage of the Skeena Region grizzly bears are female?", we could write code like this:<br>
# ```python
# sk_fem_percent = (int(griz_pop_skeena['Female Population']) / int(griz_pop_skeena['Population Estimate'])) * 100
# sk_fem_percent = round(sk_fem_percent,2)
# print("Females make up " + str(sk_fem_percent) + "% of the Skeena Region grizzly bear population")
# ```

# The equation to calculate the percentage of these two numbers is:<br>
# $$ (2970\div 5400) \times 100 = 55\% $$

# In[5]:


# group the data by overall threat level
griz_threat = griz_df.groupby(['Overall Threat']).size().reset_index(name='Pop. Units').sort_values('Pop. Units')
griz_threat


# In[6]:


# find the population estimate for each overall threat level
reg_threat_levels = griz_df.groupby('Overall Threat')[['Population Estimate']].sum().reset_index()
reg_threat_levels


# In[7]:


# find the grizzly bear population units where the overall threat is high
griz_pu_hthreat = griz_df.loc[griz_df['Overall Threat'] == 'High'].sort_values('Region')
griz_pu_hthreat


# If we wanted to state what population unit(s) were listed as a low overall threat, we could write code like this:
# ```python
# griz_pu_lthreat = griz_df.loc[griz_df['Overall Threat'] == 'Low']
# print("The grizzly bear population unit(s) that have a low overall threat rating are: \n" + griz_pu_lthreat['Population Units'].to_string(index=False))
# ```

# In[8]:


griz_reg_pop_chart = alt.Chart(griz_pop_reg).mark_bar(color = 'brown').encode(
    x=alt.X('Region:O', axis=alt.Axis(labelAngle=-45)),
    y='Population Estimate:Q'
).properties(title='Grizzly Bear Population by Region', width=500, height=300
            ).configure_scale(bandPaddingInner=0.25)

griz_reg_pop_chart


# In[9]:


griz_pop_threat_chart = alt.Chart(reg_threat_levels).mark_bar(color = 'red').encode(
     x=alt.X('Overall Threat:O', axis=alt.Axis(labelAngle=-45)),
     y='Population Estimate:Q'
).properties(title='Grizzly Bear Population by Threat Level', width=500, height=300
            ).configure_scale(bandPaddingInner=0.25)

griz_pop_threat_chart


# <img src="https://www.hellobc.com/content/uploads/2018/01/24670_dbc_1900_px-1900x1000.jpg" width="500" alt="Grizzly Dinner Date" />

# Here is my citation for the grizzly bear dataset {cite}`grizzly_conservation`.

# See this citation for the inspiration behind this grizzly notebook {cite}`griz_inspo`.

# In[ ]:




