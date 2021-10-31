


import bs4
import pandas as pd
import requests

Type=[]
Name=[]
Phone=[]
Address=[]
City=[]
State=[]
Pincode=[]
Country=[]
Timings=[]
Mode_of_Payment=[]
Currency=[]
Link_to_profile=[]

url = "https://www.healthgrades.com/drugs/a-z/alpha-a"
resp = requests.get(url)
resp.status_code
resp.reason
soup = bs4.BeautifulSoup(resp.content)
# print(soup)
data = soup.find_all("li", attrs={"class":"DrugSectionList-items-item"} )

for tags in data:
    l = tags.a['href']
    print(l)
    # link = "https:"+l
    Link_to_profile.append(l)
    response = requests.get(l)
    soup1 = bs4.BeautifulSoup(response.content)

    data1 = soup1.find("section", attrs={"id":"basics"})
    # data1 = soup1.find_all("span")
    print(data1)
#     data2 = data1[0].find_all('dd')
#     Type.append("Pharmacy")
#     Name.append(data2[0].text)
#     Address.append(data2[1].text)
#     City.append(data2[2].text)
#     Pincode.append(data2[3].text)
#     Country.append(data2[4].text)
#     Phone.append(data2[5].text)
#     Currency.append(data2[6].text)
#     Timings.append(data2[7].text)
#     Mode_of_Payment.append(data2[8].text)
print("Site Scrapped Succesfully")

# dataset = {
#     "Type":Type,
#     "Name":Name,
#     "Phone":Phone,
#     "Address":Address,
#     "City":City,
#     "Pincode":Pincode,
#     "Country":Country,
#     "Timings":Timings,
#     "Mode_of_Payment":Mode_of_Payment,
#     "Currency":Currency,
#     "Link_to_profile":Link_to_profile, 
# }

# datum = pd.DataFrame(dataset)
# datum.to_csv("lucknow_aaris_kazi.csv")

