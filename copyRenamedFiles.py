import xlrd
import os
from shutil import copyfile

path = "C:/Users/sale/Documents/testInput"
copyPath = "C:/Users/sale/Documents/testOutput"

file_location = "C:/Users/sale/Documents/ChemFarmImports/AobiousToChemfarm/Output/"
output = "output.xlsx"

# reads the imageIDKey
workbook = xlrd.open_workbook(file_location + output)
sheet = workbook.sheet_by_index(0)


image_id = sheet.col_values(0,1)
aobious_id = sheet.col_values(1,1)
name = sheet.col_values(2,1)
chemfarm_id = sheet.col_values(3,1)

for i in range(0,len(image_id)):
    file = str(int(image_id[i])) + ".jpg"
    currChemFarmID = int(chemfarm_id[i])
    if os.path.isfile(path + "/" + file) and currChemFarmID != -1:
        newName = str(currChemFarmID) + ".jpg"
        copyfile(path.replace("\\", "/") + "/" + file, copyPath + "/" + newName)

print("done :)")
