import os
from shutil import copyfile


path = "C:/Users/sale/Documents/ChemFarmImports/categoryImportExcel/categoryImportExcelInput/All_Files"
copyPath = "C:/Users/sale/Documents/ChemFarmImports/categoryImportExcel/categoryImportExcelInput/testCopy"

for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        if file.find("-") == -1 and file.find("_") == -1:
            copyfile(dirpath.replace("\\", "/") + "/" + file, copyPath + "/" + file)

