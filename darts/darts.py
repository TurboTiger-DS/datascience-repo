# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


'''Import data'''
df = pd.read_csv('data.csv')

''' Columns '''
df['Percentage'] = df['Made']/df['Attempts']



df['Field'] = df['Field'].apply(str)
df = df.set_index('Field')



'''Plot'''

c = plt.cm.Reds

group_names=['20', '1', '18','4','13','6','10','15','2','17','3','19','7','16','8','11','14','9','12','5']
group_size=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


final_list=[]
for i in group_names:
    x = df.loc[i,'Percentage']
    final_list.append(c(x))

fig2, ax2 = plt.subplots()
ax2.axis('equal')
mypie, _ = ax2.pie(group_size, radius=2, labels=group_names, startangle=100, colors=final_list,counterclock=False)
plt.setp( mypie, width=1.95, edgecolor='white')


plt.show()


    
