import sys
import tabula
# prerequisites: 
#  1. Install java from: https://www.oracle.com/in/java/technologies/downloads/#java8
#  2. Add java installation folder (C:\Program Files\Java\jre1.8.0_251\bin) to the environment path variable
#  3. Restart the computer, if needed
#  4. Install tabula-py using pip: pip install tabula-py


# Usage: python pdfToCSV.py <input_pdf_file_path> <output_csv_file_path>
# Example: python pdfToCSV.py "C:\Users\user\Downloads\pdfToCSV\pdfToCSV\input\input.pdf" "C:\Users\user\Downloads\pdfToCSV\pdfToCSV\output\output.csv"
# You can omit the output path, in which case the output file will be saved in the same folder as the input file with the same name as the input file
if len(sys.argv) == 1:
    print("No arguments provided")
    sys.exit()

elif len(sys.argv) == 2:
    path = sys.argv[1]
    tabula.convert_into(path, f'{path}.csv', output_format="csv", pages='all')
    print("Conversion Successful")

elif len(sys.argv) == 3:
    path = sys.argv[1]
    output_path = sys.argv[2]
    tabula.convert_into(path, output_path, output_format="csv", pages='all')
    print("Conversion Successful")
