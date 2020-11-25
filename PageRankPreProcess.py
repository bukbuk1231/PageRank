import os
import pandas as pd

def calculate_all_pages(folder_name):
    outbound = {}
    inbound = {}
    files = set()

    for file in os.listdir(folder_name):
        file_name = int(file.split('.')[0])
        files.add(file_name)

    for file in os.listdir(folder_name):
        file_name = int(file.split('.')[0])

        # add in file index number into dictionary
        if file_name not in outbound:
            outbound[file_name] = 0
        if file_name not in inbound:
            inbound[file_name] = []

        data = pd.read_csv(folder_name + '/' + file)
        data_dict = data.to_dict()['outlinks'][0][1:-1]
        #print(data.to_dict())
        #data_dict = data.to_dict()['link_to_urls'][0][1:-1]
        data_list = data_dict.split(',')

        # convert strings into ints
        data_list = [int(x) for x in data_list]

        for num in data_list:
            # modify outbound counts
            if num in files and file_name != num:
                outbound[file_name] = outbound[file_name] + 1

            # modify inbound items
            if num in files:
                if num not in inbound:
                    inbound[num] = []
                old_list = list(inbound[num])
                if file_name != num:
                    old_list.append(file_name)
                inbound[num] = old_list


    return (outbound, inbound)
