import pandas as pd
def making_to_csv():
    f = open('document.txt', 'r')
    line = f.readlines()
    doc_name = []
    position = []
    pos = ''
    temp = ''
    for i in line:
        if '"' in i:
            pos = i.split()
            temp = i
            break

    for i in pos:
        if '"' in i:
            pos = i.replace('"', '')
            pos = pos.replace('\n', '')
    for i in line:
        if 'Dr. ' in i:
            doc_name.append(i.replace('\n',''))

    for i in line:
        if temp in i:
            continue
        elif pos in i:
            i = i.replace('\n', '')
            position.append(i)

    # print(len(doc_name), len(position))
    # print(doc_name, position)

    df = pd.DataFrame({
        "Doctor Name": doc_name,
        "Position": position
    })
    df.to_csv('doctors.csv')