# This program allows a user to enter a student's 
# year in school (1 through 4)
# and number of cans collected
year = 0
cans = 0
SIZE = 4
QUIT = 9
collected = [0, 0, 0, 0]
HEADER1 = "Can Recycling Report"
HEADER2 = "Year   Cans Collected"

#Simple value error checking method. Just need to implement.
#def isInt(value):
#    try:
#        int(value)
#        return True
#    except:
#        return False

year = input("Enter year of student (1-4) or 'QUIT' to quit: ")
while not(str(year) == "QUIT"):
    cans = int(input("Enter number of cans collected: "))
    collected[int(year) - 1] += cans
    year = input("Enter year of student (1-4) or 'QUIT' to quit: ")

print()
print(HEADER1)
print(HEADER2)
year = 0
while (year < SIZE):
    print(year + 1, "     ", collected[year])
    year += 1


