def calcBills():
    myBills = {
        'Electric': 120.00,
        'Rent': 1200.00,
        'Water_Sewer': 60.00,
        'Car_Ins': 75.00,
        'Phone': 65.00
    }
    total = 0
    for bill in myBills:
        total += myBills[bill]
    owedStr = 'The total owed for bills this month is: ${}.'.format(total)
    return owedStr
