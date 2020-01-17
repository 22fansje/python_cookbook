import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = ["January", "February", "March", "Arpil", "May", "June", "July", "August", "September", "Obtober", "November", "December"]
    colors = ["blue", "pink", "green", "cyan", "purple", "yellow", "orange", "brown", "cyan", "black", "grey", "white"]
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)


    print(dates)
    print(colors)

    # I need to ,ake sure i remember these lists.

    whatColor = input('What color do you wish to know the date of?:')
    coldex = colors.index(whatColor)
    theDate = dates[coldex]
    print('The date of',whatColor,'is:',theDate)
