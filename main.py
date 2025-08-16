from Objects.Person import Person
from PersonFunctions import customGreet
from DatabaseConnections.OracleDB import getData



data = getData("artisan")
for row in data:
    print(row)
