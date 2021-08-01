import pandas as pd

consume_type = []
med_names = []
brand_name = []

df = pd.read_csv('med_data.csv')
print(len(df))
i = 1
for i in range(len(df)):
    if i ==0:
        brand_name.append(df.iloc[i].values)
        med_names.append(df.iloc[i+1].values)
        consume_type.append(df.iloc[i+2].values)

    if i%3 == 0:
        # print(df.iloc[i])
        brand_name.append(df.iloc[i].values)
        med_names.append(df.iloc[i+1].values)
        consume_type.append(df.iloc[i+2].values)
# print(consume_type)
# print(df.iloc[6])
df = pd.DataFrame({
    "Brand Name": brand_name,
    "Molecules": med_names,
    "Dosage Form": consume_type
})
df.to_csv('cipla.csv')