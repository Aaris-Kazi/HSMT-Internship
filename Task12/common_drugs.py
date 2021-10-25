import pandas as pd
import time

start = time.time()
one_mg = list(pd.read_excel('Task12\D-F_1mg.xlsx')['Product Name'])

pharmeasy = list(pd.read_excel('Task12\D-F_netmeds.xlsx')['Medname'])

netmeds = list(pd.read_excel('Task12\D-F_Pharmeasy.xlsx')['medName'])

end = time.time()
print("Time needed = ",end - start)
print("---------------------------------------------------")

List = []
count = 1
for i in one_mg:
    if i in pharmeasy or i in netmeds:
        print(count, " : ", i)
        List.append(i)
        count += 1

dic = {"Common Drugs": List}

df = pd.DataFrame(dic)
df.to_csv('Common_DrugsD-F.csv')
