#file_name =  # path to file + file name
#sheet =  # sheet name or sheet number or list of sheet numbers and names
file_name = "C:\\Users\cgarcia\\Documents\\_APRENDER\\CLIENTES\\TOUS\\Tous.xlsx"
sheet = "Conversion Rate"

import pandas as pd
df = pd.read_excel(io = file_name, sheet_name = sheet)
print(df.head(5))  # print first 5 rows of the dataframe

df_transform = df.drop(columns =['Latitude','Longitude'])
print(df_transform.head(5))

df_export = df_transform.groupby(['Year','Date','Store','Store Location','City','Country'])["Nr of Visitors","Nr of Purchases"].apply(lambda x : x.astype(float).sum())
print(df_export.head(5))

df_export.to_excel("C:\\Users\cgarcia\\Documents\\_APRENDER\\CLIENTES\\TOUS\\output.xlsx", sheet_name= "Conversion Rate" )