import pandas as pd

consume_type = []
med_names = []
brand_name = []

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

df = pd.read_csv('cipla1.csv')
print(len(df))


for i in df['medName']:
    j = containsNumber(i)
    print(j)

# i = 1
# for i in range(len(df)):
#     if i ==0:
#         brand_name.append(df.iloc[i].values)
#         med_names.append(df.iloc[i+1].values)
#         consume_type.append(df.iloc[i+2].values)

#     if i%3 == 0:
#         # print(df.iloc[i])
#         brand_name.append(df.iloc[i].values)
#         med_names.append(df.iloc[i+1].values)
#         consume_type.append(df.iloc[i+2].values)
