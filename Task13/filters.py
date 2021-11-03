import pandas as pd
from pandas.core.algorithms import mode

b_name = []
g_name = []
drug_type = []
route = []
dosage_form = []
dates = []

def extractor(x):
    # temp = x[1]
    try:
        f = x.split('<span>')
        g = f[1]
        g = g.split('</span>')
        g1 = g[0]
        if '<a class="Link"' in g1:
            y = g1.split('>')
            # print(y)
            st1 = y[0]
            st2 = y[1]
            n = st1.split('<a')
            n1 = st2.split('</a')
            stm1 =n[0]
            stm2 =n1[0]
            stm = stm1+stm2
            return stm
        else:
            return g1
    except:
        
        f = x.split('</b>: ')
        g = f[1]
        if '<a class="Link"' in g:
            y = g.split('>')
            st1 = y[0]
            st2 = y[1]
            n = st1.split('<a')
            n1 = st2.split('</a')
            stm1 =n[0]
            stm2 =n1[0]
            stm = stm1+stm2
            return stm
        else:
            return g

def looper_state(x):
    x = str(x)
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.split('</p>')

    for i in range(0,len(x)):
        if '<p><b>Brand Name</b>:' in x[i]:
            g = extractor(x[i])
            b_name.append(g)
        elif ' <p><b>Generic Name</b>:' in x[i]:
            g = extractor(x[i])
            g_name.append(g)
        elif ' <p><b>Drug Type</b>:' in x[i]:
            g = extractor(x[i])
            drug_type.append(g)
        elif ' <p><b>Route</b>:' in x[i]:
            g = extractor(x[i])
            route.append(g)
        elif ' <p><b>Dosage Form</b>:' in x[i]:
            g = extractor(x[i])
            dosage_form.append(g)
        elif ' <p><b>Data Current As Of</b>:' in x[i]:
            g = extractor(x[i])
            dates.append(g)
        else:
            pass
        
    print(len(b_name), len(route))
    if len(b_name) > len(route):
        route.append('NaN')
        print(len(b_name), len(route))
        print('append')
    else:
        pass


df = pd.read_csv('C:\\Users\\aaris\\Desktop\\forinternship\\HSMT-Internship\\health_a_i.csv')
for i in range(0,len(df)):
    x = df.iloc[i].values
    looper_state(x)
    
print(len(b_name),len(g_name),len(drug_type),len(route),len(dosage_form),len(dates))
# print(b_name,g_name,drug_type,route,dosage_form,dates)

sf = pd.DataFrame({
    "Brand Name":b_name,
    "Generic Name":g_name,
    "Drug Type":drug_type,
    "Route":route,
    "Dosage Form":dosage_form,
    "Date":dates,
})

sf.to_csv('aaris_heath_a_i.csv', header=False, mode = 'a')