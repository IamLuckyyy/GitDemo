#[ https://www.programiz.com/python-programming/writing-csv-files ]

# import csv
# try:
#     with open("MyFile.csv",mode='w',encoding='UTF-8') as lucy:
#         x = csv.writer(lucy,delimiter="|")
#         data = [['STOCK','SALES','PRICE'],
#                 ['100','90','$90'],
#                 ['300','280','$280'],
#                 ['400','200','$200']]
#         x.writerows(data) #Writing row by row
#         print("CSV file created successfully")
# except IOError:
#     print("Sorry csv file unable to create")
#     print("Disk write protected")
# finally:
#     print("Finally block success")


# import csv
# try:
#     with open("MyFile.csv",mode='a',encoding='UTF-8') as lucy:
#         x = csv.writer(lucy,delimiter="|")
#         data = [['200','110','$350'],
#                 ['220','70','$500']]
#         x.writerows(data)
#         print("CSV file append successfully")
# except IOError:
#     print("Sorry csv file unable to append")
#     print("File is read only format")
# finally:
#     print("Finally block success")


# try:
#     with open("MyFile.csv",mode='r',encoding='UTF-8') as lucy:
#         for data in lucy:
#             print(data)
#         print("CSV file read successfully")
# except IOError:
#     print("Sorry csv file unable to read")
# finally:
#     print("Finally block success")


import csv
with open("MyFile.csv", 'r') as lucy:
    a = csv.reader(lucy)
    data = []
    for row in a:
        if len(row) != 0:
            data = data+[row]
print(data)
