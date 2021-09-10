import pandas as pd
links, price_usd, price_inr, room_count, km, rating, hotel_name = [], [], [], [], [], [], []
df = pd.read_csv('Task9\hotel.csv')
# print(df)
def gsplit(value):
    m,n = value.split('\n')
    return n
for i in range(len(df)):
    try:
        if "HOTEL'S NAME: " in df['Hotels'][i] or "HOTEL'S DISTANCE FROM HOSPITAL (IN KM):" in df['Hotels'][i]:
            x = df['Hotels'][i]
            m, n = x.split('\nSTAR RTAING:')
            m = gsplit(m)
            hotel_name.append(m)
            # print(m)
            # print(n)
            m, n = n.split("\nHOTEL'S DISTANCE FROM HOSPITAL (IN KM):")
            m = gsplit(m)
            rating.append(m)
            # print(m)
            # print(n)
            m, n = n.split("\nROOM COUNT:")
            m = gsplit(m)
            km.append(m)
            # print(m)
            m, n = n.split("\nPRICE RANGE (INR):")
            m = gsplit(m)
            room_count.append(m)
            # print(m)
            m, n = n.split("\nPRICE RANGE (USD):")
            m = gsplit(m)
            price_inr.append(m)
            # print(m)
            # m, n = n.split("\nPRICE RANGE (USD):")
            # m = gsplit(m)
            # print(m)
            m, n = n.split("\nHOTELS LINK:")
            m = gsplit(m)
            price_usd.append(m)
            # print(m)
            n = gsplit(n)
            links.append(n)
            # print(n)
            # print(df.iloc[i].values)
            
    except Exception as e:
        # print(e)
        pass
df = pd.DataFrame({
    'Hotels': hotel_name,
    'Ratings': rating,
    'KM Range': km,
    'Room Count': room_count,
    'Price USD': price_usd,
    'Price INR': price_inr,
    'Links': links,
})
# df = pd.DataFrame(dic)
df.to_csv("hosp_hotel.csv", mode="a")


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