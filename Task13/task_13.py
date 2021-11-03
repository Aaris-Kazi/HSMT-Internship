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
data_all = []
Link_to_profile=[]

url = "https://www.healthgrades.com/drugs/fda/a-z/alpha-i"
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
    data2 = soup1.find_all("td")
    if '/drugs/' in l:
        data1 = data1.find_all("p")
        # print(data1)
        # print(data2)
        print(len(data1))
        data_all.append(data1)
        # brand_name.append(data1[0])
        # generic_name.append(data1[1])
        # drug_type.append(data1[2])
        # route.append(data1[3])
        # dosage_form.append(data1[4])
        # dates.append(data1[5])
    else:
        pass
        # drug_facts.append(data2[0])
        # break
print("Site Scrapped Succesfully")

dataset = {
    # "Brand Name":brand_name,
    # "Generic Name":generic_name,
    # "Drug Type":drug_type,
    # "Route":route,
    # "Dosage Form":dosage_form,
    # "Dates":dates,
    "Data to be filtered": data_all
}

datum = pd.DataFrame(dataset)
datum.to_csv("health_a_i.csv")

