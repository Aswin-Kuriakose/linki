from dates import getDates

def getValues():

    dates, sorted_files = getDates()

    values = []
    for file in sorted_files:
        inner_values = []
        with open(f"./dec 2020/00Z/{file}", "r") as txt_file:
            values.append(inner_values)
            for line in txt_file:
                strip_col = line.strip()

                if len(strip_col) > 60:

                    columns = strip_col.split()
                    
                    height = columns[1]
                    humidity = columns[4]

                    inner_values.append( [ float(height), float(humidity) ] )
    return values