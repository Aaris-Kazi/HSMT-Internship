import pandas as pd

df = pd.read_csv('Task9\hotel.csv')
# print(df)
for i in range(len(df)):
    try:
        if "HOTEL'S NAME: " in df['Hotels'][i] or "HOTEL'S DISTANCE FROM HOSPITAL (IN KM):" in df['Hotels'][i]:
            x = df['Hotels'][i]
            m = x.strip('\nSTAR RTAING:')
            print(m)
            # print(df.iloc[i])
            
    except Exception:
        pass

# if "HOTEL'S NAME: " in df["Hotels"][184] or "HOTEL'S DISTANCE FROM HOSPITAL (IN KM):" in df["Hotels"][184]:
#     print(df["Hotels"][184])
# x= "HOTEL'S NAME: OYO 10667 Prakash Guest House STAR RTAING: 2 HOTEL'S DISTANCE FROM HOSPITAL (IN KM): 1.0 35 1800 PRICE RANGE (USD): 24 HOTELS LINK: oyorooms.com"
# if "HOTEL'S NAME: " in x:
#     print(x)

# print(df.iloc[128])
# print(df.iloc[129])
# if 'APPOINTMENT ' in df.iloc[129]:
#     print(df.iloc[129])
# if "HOTEL'S " in df.iloc[128]:
#     print(df.iloc[129])
# if "APPOINTMENT LINK\n- not available -" == df.iloc[0]:
#     print(df.iloc[0])

# x = df[df['Hotels'] == "APPOINTMENT LINK\n- not available -"]
# print(x)

# y = df['APPOINTMENT ' in df['Hotels']]
# print(y)