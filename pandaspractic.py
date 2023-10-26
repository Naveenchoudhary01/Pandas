# import pandas as pd

# mydata = {
#         'car':['bmw','audi','merc'],
#         'value':[30,42,48]   
# }
# var = pd.DataFrame(mydata)
# print(var)
#-----------Series---------------------------------
# import pandas as pd
# a=[1,2,3,4,5]
# var=pd.Series(a)
# print(var)
#--------------lables---------------------------
# import pandas as pd
# a=[9,4,5,8]
# var=pd.Series(a)
# print(var[0])
# print(var[1])
# print(var)
#--------------create own lables---------------------
# import pandas as pd
# a=[9,8,7,5,2,5,11]
# var=pd.Series(a,index=['a','b','c','c','d','e','f'])
# print(var)
# print(var['d'])
#-------------key and value srise---------------------
# import pandas as pd
# a={'naveen':20, 'kumar':30,'chaudhary':50}
# var=pd.Series(a)
# #var=pd.Series(a,index=['naveen','kumar']) # crate only two 
# print(var)
#--------------data frame--------------------
# data={ 
#     'a':[10,20,30],
#     'b':[1,2,3]}
# var=pd.DataFrame(data)
# #print(var)
# print(var.loc[[0,1,2]])  # use loc finde specifed row and colums 
#------------index---------------------------------
# data = {
#     'a': [10, 20, 30],
#     'b': [1, 2, 3]}
# var=pd.DataFrame(data,index=['day1','day2','day3'])
# #print(var)
# print(var.loc['day2'])  # locate index by name
#-----------load files in data frame----------------
# df=pd.read_excel('diffrence.xls')
# print(df.to_string())
# print(pd.options.display.max_rows)
# pd.options.display.max_rows = 9999 # u can increse rows in your system
#-----------read JSON file-----------------------
# df=pd.read_json('naveen.JSON')
# print(df.to_string())  # use to print entire data fame
# ------------head method---bydefault 5 rows-----------------------
#df=pd.read_csv('kumar.csv')
# print(df.head(20))
#-----------tail--------same as head----------------
# print(df.tail())
#---------info-----------------------
# print(df.info())
#-----------cleaning data-----------------
# df.dropna(inplace=True) # remove al null valuse
# df.dropna()             # return a new data frame
# df.fillna()             # replce empty cells with value
#-----------replace using mean median or mode-------------
#-----------convert to correct formet-------------------
# df['date']=pd.to_datetime(df['date'])
# print(df.to_string())

