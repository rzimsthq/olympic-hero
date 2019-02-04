# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)

data.rename(index=str,columns={'Total':'Total_Medals'},inplace=True)
data.head()

#Code starts here



# --------------
#Code starts here

#Creating new column 'Better_Event'
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'] , 'Both', data['Better_Event'])

#Finding the value with max count in 'Better_Event' column
better_event=data['Better_Event'].value_counts().index.values[0]

#Printing the better event
print('Better_Event=', better_event)

    
#Code ends here    


# --------------
#Code starts here




d={'Country_Name':data['Country_Name'],'Total_Summer':data['Total_Summer'],'Total_Winter':data['Total_Winter'],'Total_Medals':data['Total_Medals']}
top_countries=pd.DataFrame(data=d)
top_countries.drop(top_countries.index[-1],inplace=True)

def top_ten(top_countries,x):
    ds=top_countries.nlargest(10,x)
    country_list=list(ds['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

common=list(set(top_10_summer).intersection(top_10_winter).intersection(top_10))



# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

plt1=summer_df.plot('Country_Name','Total_Summer',kind='bar',rot=45)
plt1.set_xlabel('Country Name')
plt1.set_ylabel('Number of Medals')
plt1.get_legend().remove()
plt1.set_title('Summer')

plt2=winter_df.plot('Country_Name','Total_Summer',kind='bar',rot=45)
plt2.set_xlabel('Country Name')
plt2.set_ylabel('Number of Medals')
plt2.get_legend().remove()
plt2.set_title('Winter')

plt3=top_df.plot('Country_Name','Total_Summer',kind='bar',rot=45)
plt3.set_xlabel('Country Name')
plt3.set_ylabel('Number of Medals')
plt3.get_legend().remove()
plt3.set_title('Top')


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df['Country_Name'][summer_df['Golden_Ratio'].idxmax()]

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df['Country_Name'][winter_df['Golden_Ratio'].idxmax()]

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df['Country_Name'][top_df['Golden_Ratio'].idxmax()]




# --------------
#Code starts here
data_1=data[:-1]



data_1['Total_Points']=(data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']*1)
most_points=data_1['Total_Points'].max()
best_country=data_1['Country_Name'][data_1['Total_Points'].idxmax()]


# --------------
#Code starts here
best=data.loc[data['Country_Name']==best_country]
col_list=['Gold_Total','Silver_Total','Bronze_Total']
best=best[col_list]
ax=best.plot.bar(stacked=True,rot=45)
ax.set_xlabel('United States')
ax.set_ylabel('Medals Tally')


