from pdf2image import convert_from_path
import os
import pymupdf

poppler_path = r"C:\Users\User\Downloads\Release-24.02.0-0\poppler-24.02.0\Library\bin"
target_folder = r"C:\Users\User\Documents\data_projects\table-luis\imgs"
pdf_file = r"C:\Users\User\Documents\data_projects\table-luis/E-M_Subs_2014-2016.pdf"
filename = "E-M_Subs_2014-2016.pdf"
def main():
    root_folder = os.getcwd()
    file = convert_from_path(pdf_file, poppler_path=poppler_path)
    for i in range(len(pdf_file)-1):
        file[i].save(f"{target_folder}/{filename[:-4]}_page_{str(i)}.jpg","JPEG")


if __name__ == "__main__":
    main()