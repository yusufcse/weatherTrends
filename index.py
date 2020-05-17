import pandas as pd
import matplotlib.pyplot as plt


df_city = pd.read_csv("berlin_temp_avg.csv") 

df_global = pd.read_csv("world_temp_avg.csv") 

#print(df_city['year'][0])
total_elements = len(df_city)
print(len(df_city))

# for index, row in df_city.iterrows():
#     print(index,index+1,index+2,index+3,index+4,index+5,index+6)
#     print(row['year'],row['avg_temp'])

#average = 0

ma_temp_city = []
ma_temp_year = []

ma_temp_global = []


for i in range(len(df_city)-6):
    average = (df_city['avg_temp'][i]+df_city['avg_temp'][i+1]+df_city['avg_temp'][i+2]+df_city['avg_temp'][i+3]+df_city['avg_temp'][i+4]+df_city['avg_temp'][i+5]+df_city['avg_temp'][i+6])
    ma_temp_city.append(round(average/7,2))
    ma_temp_year.append(df_city['year'][i+6])
   
print(ma_temp_city)
    

for i in range(len(df_global)-6):
    average = (df_global['avg_temp'][i]+df_global['avg_temp'][i+1]+df_global['avg_temp'][i+2]+df_global['avg_temp'][i+3]+df_global['avg_temp'][i+4]+df_global['avg_temp'][i+5]+df_global['avg_temp'][i+6])
    ma_temp_global.append(round(average/7,2))
    
print(ma_temp_year,ma_temp_global)


# plt.plot(ma_temp_year,ma_temp_city,color='green')
# plt.plot(ma_temp_year,ma_temp_global,color='orange')
# plt.xlabel('Years')
# plt.ylabel('Temperature $^\circ$C')
# plt.title('Berlin vs Global Avg Temperature 1750 to 2013 ')
# plt.legend(['Berlin','Global'])
# plt.show()

# list1, list2 = (list(t) for t in zip(*sorted(zip(ma_temp_global, ma_temp_year))))

# plt.plot(ma_temp_year,ma_temp_city,color='green')
# plt.plot(ma_temp_year,ma_temp_global,color='orange')
# plt.plot(list2[0],list1[0],'b*')
# plt.xlabel('Years')
# plt.ylabel('Temperature $^\circ$C')
# plt.title('Berlin vs Global Avg Temperature 1750 to 2013 ')
# plt.legend(['Berlin','Global','Global lowest temp '+str(list1[0])+' in '+str(list2[0])])
# plt.show()

list1, list2 = (list(t) for t in zip(*sorted(zip(ma_temp_global, ma_temp_year),reverse=True)))

plt.plot(ma_temp_year,ma_temp_city,color='green')
plt.plot(ma_temp_year,ma_temp_global,color='orange')
plt.plot(list2[0],list1[0],'r*')
plt.xlabel('Years')
plt.ylabel('Temperature $^\circ$C')
plt.title('Berlin vs Global Avg Temperature 1750 to 2013 ')
plt.legend(['Berlin','Global','Global highest Temp '+str(list1[0])+' in '+str(list2[0])])
plt.show()
