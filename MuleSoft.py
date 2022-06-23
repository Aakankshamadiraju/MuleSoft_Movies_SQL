# Movies Table
# (Name, Actor, Actress, Director, Year of Release )
import sqlite3
# Creating a Database and connecting to Database.
conn = sqlite3.connect("Movies.db")
cursor = conn.cursor()
print("[ + ] Opened database Successfully")

# Creating "MOVIE" Table if not exists 
cursor.execute(''' SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='Movies' ''')

if cursor.fetchone()[0] == 1:
    print("[ * ] Table Exists.")
else:
    cursor.execute(''' CREATE TABLE Movies
             (Id INTEGER PRIMARY KEY AUTOINCREMENT,
             Name TEXT NOT NULL,
             Actor TEXT NOT NULL,
             Actress TEXT NOT NULL,
             Director TEXT NOT NULL,
             YearOfRelease TIMESTAMP NOT NULL
             );''')
    print("[ + ] Table Created Successfully")
print("\n-----------------------  Inserting Data into Table ---------------------------------")
# Inserting data into Table
cursor.execute("INSERT INTO Movies (Name, Actor, Actress, Director, YearOfRelease) VALUES('Sammohanam', 'Sudheer Babu', 'Aditi Rao Hydari', 'Mohana Krishna Indraganti', '2018')")
cursor.execute("INSERT INTO Movies (Name, Actor, Actress, Director, YearOfRelease) VALUES('Venom', 'Tom Hardy', 'Michelle Williams', 'Rube Fleischer', '2018')")
cursor.execute("INSERT INTO Movies (Name, Actor, Actress, Director, YearOfRelease) VALUES('Avatar', 'Samuel Henry', 'Zoe Saldana', 'James Cameron', '2009')")
cursor.execute("INSERT INTO Movies (Name, Actor, Actress, Director, YearOfRelease) VALUES('The Dark Knight', 'Bruce Wayne', 'Myaggie Gyllenhaal', 'Christopher Nolan', '2008')")
cursor.execute("INSERT INTO Movies (Name, Actor, Actress, Director, YearOfRelease) VALUES('The Shawshank Redempt', 'Andy Dufesne', 'Renee Blaine', 'Frank Darabont', '1994')")

print("\n[ + ] Data inserted Successfully \n")


# Fetching all entries from Table
print("-----------------------  Fetching data from Table ---------------------------------\n\n")
cursor.execute("SELECT * FROM Movies")
print("ID |\t Name |\t Actor |\t Actress |\t Director |\t Year")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
for row in cursor:
    print(row[0], "\t|\t", row[1], "\t|\t", row[2], "\t|\t", row[3], "\t|\t", row[4], "\t|\t", row[5])
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n[ + ] Fetched Data Successfully\n")


# Fetching details of an Actor "Tom Hardy"
print("-----------------------  Fetching Actor 'Tom Hardy' details from Table ---------------------------------\n\n")
cursor.execute("SELECT * FROM Movies WHERE Actor='Tom Hardy' ")
print("ID |\t Name |\t Actor |\t Actress |\t Director |\t Year")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
for row in cursor:
    print(row[0], "\t|\t", row[1], "\t|\t", row[2], "\t|\t", row[3], "\t|\t", row[4], "\t|\t", row[5])
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n[ + ] Fetched Tom Hardy Details Successfully")

# Clearing Table
cursor.execute("DELETE FROM Movies")
print("[ + ] Table Cleared Succesfully\n\n")

#Closing Database connection
conn.commit()
conn.close()
print("[ + ] Database Closed Successfully")