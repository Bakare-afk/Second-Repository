import pandas
# scores = pandas.Series([85,75,87,98] ,index  = ["Amina", "David" , "Ola","Chika"])
# print(scores["David"])

# calories={"day1:420","day2:56", "day3:24"}
# myseries=pandas.Series(calories)
# print(myseries)
# # print(myseries["day1","day2"])

# #  How to create a series
# myseries=pandas.Series([7,6,5,5,4], index = ["Ade","Bola","Taiwo","Bakare","Daniel"])
students={
    "Name":["Ade","Bola","Taiwo","Bakare","Daniel"],
    "Age":[12,12,34,33,45],
    "Score":[12,32,43,54,65]


}
df =pandas.DataFrame(students)
print(df[["Name","Score"]])


data=[
    {"Name":"David","Score":91},
    {"Name":"CHIKA","Score":332}

]

df = pandas.DataFrame(data)
print(df)

pd  = pandas.read_csz("pandas.py"/"student.csv")