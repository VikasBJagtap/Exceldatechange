# read the Excel file
import pandas as pd

# we must need to give source path of our Excel files
file_path = 'E:\\office\\Data.xlsx'

# now we want to read our Excel data sheet
df = pd.read_excel(file_path, sheet_name='Data_Sheet1')
print('Oringinal date format:')
print(df['Date'].head())

# convert the dates to DD-MM-YYYY format
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%d-%m-%y')
print('This is converted date format:')
print(df['Date'].head())

#save the converted data back to Excel

output_path = 'E:\\office\\Converted_Dates.xlsx'

# In my case, I don't need the index in my output file, so index=False helps keep the file clean and focused on the data
df.to_excel(output_path, index=False)
print('File saved as', output_path)