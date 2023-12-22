import utility

file = "C:\\Users\Sheetal.Chorsiya\\Downloads\\MyFile.xlsx"

# writing data
utility.write_data(file, "Sheet1", 1, 1, "ID")
utility.write_data(file, "Sheet1", 1, 2, "Name")
utility.write_data(file, "Sheet1", 1, 3, "Age")
utility.write_data(file, "Sheet1", 1, 4, "Address")

utility.write_data(file, "Sheet1", 2, 1, "1")
utility.write_data(file, "Sheet1", 2, 2, "Sheetal")
utility.write_data(file, "Sheet1", 2, 3, "26")
utility.write_data(file, "Sheet1", 2, 4, "Ahmedabad")

utility.write_data(file, "Sheet1", 3, 1, "2")
utility.write_data(file, "Sheet1", 3, 2, "Mayur")
utility.write_data(file, "Sheet1", 3, 3, "28")
utility.write_data(file, "Sheet1", 3, 4, "Surat")

# Fetch rows and column number
print(utility.get_row_count(file, "Sheet1"))
print(utility.get_column_count(file, "Sheet1"))

# fill the green and red colour
utility.fill_red(file, "Sheet1", 1, 1)
utility.fill_red(file, "Sheet1", 1, 2)
utility.fill_red(file, "Sheet1", 1, 3)
utility.fill_red(file, "Sheet1", 1, 4)

utility.fill_green(file, "Sheet1", 2, 1)
utility.fill_green(file, "Sheet1", 2, 2)
utility.fill_green(file, "Sheet1", 2, 3)
utility.fill_green(file, "Sheet1", 2, 4)

utility.fill_green(file, "Sheet1", 3, 1)
utility.fill_green(file, "Sheet1", 3, 2)
utility.fill_green(file, "Sheet1", 3, 3)
utility.fill_green(file, "Sheet1", 3, 4)

# reading data

print(utility.read_data(file, "Sheet1", 1, 1), end=" ")
print(utility.read_data(file, "Sheet1", 1, 2), end=" ")
print(utility.read_data(file, "Sheet1", 1, 3), end=" ")
print(utility.read_data(file, "Sheet1", 1, 4), end=" ")

print(utility.read_data(file, "Sheet1", 2, 1), end=" ")
print(utility.read_data(file, "Sheet1", 2, 2), end=" ")
print(utility.read_data(file, "Sheet1", 2, 3), end=" ")
print(utility.read_data(file, "Sheet1", 2, 4), end=" ")

print(utility.read_data(file, "Sheet1", 3, 1), end=" ")
print(utility.read_data(file, "Sheet1", 3, 2), end=" ")
print(utility.read_data(file, "Sheet1", 3, 3), end=" ")
print(utility.read_data(file, "Sheet1", 3 , 4), end=" ")
