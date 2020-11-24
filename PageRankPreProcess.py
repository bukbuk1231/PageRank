# import csv
# import os

# def calculate_all_pages(folder_name):
#     inbound_outbound = {}
#     inbound = {}
#     for file in os.listdir(folder_name):
#         file_name = file.split('.')[0]
#         if file_name not in inbound_outbound:
#             inbound_outbound[file_name] = [0, 0]
#         with open(folder_name + '/' + file, newline='') as csvfile:
#             reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#             for row in reader:
#                 for i in range(len(row)):
#                     if i != 0:
#                         # modify outbound counts
#                         inbound_outbound[file_name][1] = inbound_outbound[file_name][1] + 1
#                         # modify inbound items
#                         if row[i] not in inbound:
#                             inbound[row[i]] = []
#                         old_list = list(inbound[row[i]])
#                         old_list.append(file_name)
#                         inbound[row[i]] = old_list
#     # modify inbound counts
#     for key in inbound:
#         inbound_outbound[key][0] = len(inbound[key])
#     print(inbound_outbound)
#     print(inbound)
#     print('\n')

#     return (inbound_outbound, inbound)

# calculate_all_pages('testcsv')

import os
import pandas as pd

def calculate_all_pages(folder_name):
    outbound = {}
    inbound = {}
    for file in os.listdir(folder_name):
        file_name = int(file.split('.')[0])

        # add in file index number into dictionary
        if file_name not in outbound:
            outbound[file_name] = 0
        if file_name not in inbound:
            inbound[file_name] = []

        data = pd.read_csv(folder_name + '/' + file)
        data_dict = data.to_dict()['outlinks'][0][1:-1]
        data_list = data_dict.split(',')

        # convert strings into ints
        data_list = [int(x) for x in data_list]

        for num in data_list:
            # modify outbound counts
            outbound[file_name] = outbound[file_name] + 1

            # modify inbound items
            if num not in inbound:
                inbound[num] = []
            old_list = list(inbound[num])
            old_list.append(file_name)
            inbound[num] = old_list

    # print(outbound)
    # print(inbound)
    return (outbound, inbound)
