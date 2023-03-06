# Import Module
import pdftables_api
# if not installed, then Open Command Prompt and type "pip install git+https://github.com/pdftables/python-pdftables-api.git"
  
# API KEY VERIFICATION
conversion = pdftables_api.Client('pd68j90b3qf8')
  
# PDf to CSV 
# csv() method takes two arguments, first is the name of the PDF file and second is the name of the CSV file to be created.
# if you want to convert multiple PDF files to CSV, then you can use a for loop to iterate over the list of PDF files.
# if your pdf file is not in the same directory as the python file, then you must specify the whole path of the PDF file.
# same with the output CSV file, if you want to save the CSV file in a different directory, then you must specify the whole path of the CSV file.
conversion.csv('Valuation_Statement.pdf', 'Valuation_Statement.csv')