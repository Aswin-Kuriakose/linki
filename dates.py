import os

def getDates():
    dates_list = []

    folder = os.listdir("./dec 2020/00Z")

    sorted_files = sorted(folder)

    for files in sorted_files:
        date = files.split()
        year = date[3].split(".")[0]
        dates_list.append(f"{date[1]}-{date[2]}-{year}")
    return (dates_list, sorted_files)