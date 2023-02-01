'''import pandas as pd
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'D:\Storage\secure-connect-dataset-store.zip'
}
auth_provider = PlainTextAuthProvider('tTGPMMnUYfDggFKwbufrzlQJ', 'Nz7,xX4SxU5l3Rw0H4dFFZL3JJU2jH-PLgyEm.OWOE3vI4OgEzd71kWqZDlnzREkt_ethMxfofLucyqM0RROh2bLbh.ZhvbI8rD5DaMemFEbQ44s-LF9GrD7ZYGbrR.K')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")

row = session.execute("use tostoredatasets")'''

import csv
with open("D:\Storage\4701229_9B6UWIIW.csv","r") as data:
    next(data)
    data_csv = csv.reader(data)
    for i in data_csv:
        print(i)
print("finished")

'''dataset = pd.read_excel(r"D:\Storage\Data_Train.xlsx")
json_data = dataset.to_json()
for i in json_data:
    print(i)'''



