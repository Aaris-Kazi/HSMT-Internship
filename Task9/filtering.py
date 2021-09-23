import pandas as pd
links, price_usd, price_inr, room_count, km, rating, hotel_name, hosp = [], [], [], [], [], [], [], []
df = pd.read_csv('hotels_hosp.csv')
# print(df)
def gsplit(value):
    m,n = value.split('\n')
    return n
for i in range(len(df)):
    try:
        if "HOTEL'S NAME: " in df['Hotels'][i] or "HOTEL'S DISTANCE FROM HOSPITAL (IN KM):" in df['Hotels'][i]:
            x = df['Hotels'][i]
            y = df['Hospitals'][i]
            m, n = x.split('\nSTAR RTAING:')
            m = gsplit(m)
            hotel_name.append(m)
            hosp.append(y)
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
            m, n = n.split("\nHOTELS LINK:")
            m = gsplit(m)
            price_usd.append(m)
            # print(m)
            n = gsplit(n)
            if n == '' or n == None:
                links.append('NAN')
            else:
                links.append(n)
            # print(n)
            # print(df.iloc[i].values)
            
    except Exception as e:
        # print(e)
        pass
print(len(hosp))
print(len(hotel_name))
print(len(rating))
print(len(km))
print(len(room_count))
print(len(price_usd))
print(len(price_inr))
print(len(links))
# df = pd.DataFrame({
#     'Hospital': hosp,
#     'Hotels': hotel_name,
#     'Ratings': rating,
#     'KM Range': km,
#     'Room Count': room_count,
#     'Price USD': price_usd,
#     'Price INR': price_inr,
#     # 'Links': links
# })
# df.to_csv("hosp_hotel4.csv", mode="a")
# df.to_csv("hosp_hotel3.csv", mode="a", header= False)

