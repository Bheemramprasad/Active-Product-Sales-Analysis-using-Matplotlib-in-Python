import numpy as np                                #data anlysis of iphone purchases
import pandas as pd 
import matplotlib.pyplot as plt

order_Details=pd.read_csv('order_details-masked.csv')

# here we have taken Transaction
# date column
order_Details['Time']=pd.to_datetime(order_Details['Transaction Date'])
order_Details['Hour']=(order_Details['Time']).dt.hour


# n =24 in this case, can be modified
# as per need to see top 'n' busiest hours
timemost1 = order_Details    ['Hour'].value_counts().index.tolist()[:24] 

timemost2 = order_Details['Hour'].value_counts().values.tolist()[:24]

tmost = np.column_stack((timemost1,timemost2))

print(" Hour Of Day" + "\t" + "Cumulative Number of Purchases \n")
print('\n'.join('\t\t'.join(map(str, row)) for row in tmost))

timemost = order_Details['Hour'].value_counts()
timemost1 = []

for i in range(0,23):
    timemost1.append(i)
    
timemost2 = timemost.sort_index()
timemost2.tolist()
timemost2 = pd.DataFrame(timemost2)

plt.figure(figsize=(20, 10))

plt.title('Sales Happening Per Hour (Spread Throughout The Week)',
          fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)

plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(timemost1, timemost2, color='m')
plt.grid()
plt.show()
