import os

os.chdir("..")
data_dir = os.getcwd()
folder_list = ['/grafana',
               '/kafka/data',
               '/kafka/secrets',
               '/nifi/conf',
               '/nifi/database_repository',
               '/nifi/flowfile_repository',
               '/nifi/logs',
               '/nifi/provenance_repository',
               '/nifi/state',
               '/nifi/utils',
               '/timescaledb',
               '/zookeeper/data',
               '/zookeeper/datalog'
               ]

for folder in folder_list:
    folder_path = data_dir + folder
    os.makedirs(folder_path)