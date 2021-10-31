import bs4
import pandas as pd
import requests

drug_name = []
brand_name = []
generic_name = []
route = []
dates = []
drug_type = []
dosage_form = []
drug_facts = []
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
    data1 = data1.find_all("p")
    print(data1)
    print(len(data1))
    brand_name.append(data1[0])
    generic_name.append(data1[1])
    drug_type.append(data1[2])
    route.append(data1[3])
    dosage_form.append(data1[4])
    dates.append(data1[5])
    break
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

