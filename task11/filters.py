import pandas as pd

df = pd.read_csv('task11\chat3.csv')
# print(df['Questions'])
# print(df['Options'])
q, o, d= [],[],[]
for i, j in zip(df['Questions'], df['Options']):
    d.append('Heart Attack')
    q.append(i)
    o.append(j)
jf = pd.DataFrame({
    "Disease": d,
    "Questions":q,
    "Options": o
})
jf.to_csv('mfine_chat.csv', mode = 'a', header= False)