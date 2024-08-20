# PARA ESTE CODIGO SE ENTIENDE QUE LA BASE DE DATOS "FinalDB.db" ya se encuentra creada y rellenada
# Si no es así, revisar código de JupyterNotebook

import pandas as pd
import sqlite3

#db_path = r"T6M5\Final_Project\FinalDB.db"
#conn = sqlite3.connect(db_path)
conn = sqlite3.connect(r"T6M5\Final_Project\FinalDB.db")
cursor_obj = conn.cursor()

# PROBLEM 1 ----------------------------------------------------------------
# Find the total number of crimes recorded in the CRIME table.

# Query
total_crimes_query = "SELECT COUNT(*) FROM CRIME_TABLE"
# Execute query
cursor_obj.execute(total_crimes_query)
total_crimes = cursor_obj.fetchone()
# Print value
print("PROBLEM 1")
print("."*40)
print(total_crimes[0])
print()

# PROBLEM 2 ----------------------------------------------------------------
# List community area names and numbers with per capita income less than 11000

# Col names are: COMMUNITY_AREA_NUMBER, COMMUNITY_AREA_NAME and PER_CAPITA_INCOME
# Query
capita_limit_query = """
SELECT COMMUNITY_AREA_NUMBER, COMMUNITY_AREA_NAME 
FROM CENSUS_TABLE 
WHERE PER_CAPITA_INCOME < 11000
"""
# Execution
cursor_obj.execute(capita_limit_query)
results = cursor_obj.fetchall()

# Print results
print("PROBLEM 2")
print("."*40)
print("Community Area Number | Community Area Name")
print("-"*50)
for row_all in results:
    print(f"{row_all[0]} | {row_all[1]}")

# PROBLEM 3 ----------------------------------------------------------------
# List all case numbers for crimes involving minors?(children are not considered minors for the purposes of crime analysis) 
minors_query = """SELECT CASE_NUMBER 
FROM CRIME_TABLE 
WHERE DESCRIPTION LIKE '%MINOR%'
"""
cursor_obj.execute(minors_query)
results = cursor_obj.fetchall()

# Print results
print("PROBLEM 3")
print("."*40)
for all_rows in results:
    print(all_rows[0])
print()

# PROBLEM 4 ----------------------------------------------------------------
# List all kidnapping crimes involving a child?
kidnapping_query = """SELECT * FROM CRIME_TABLE
WHERE PRIMARY_TYPE = 'KIDNAPPING' """
cursor_obj.execute(kidnapping_query)

results = cursor_obj.fetchall()
# Print results
print("PROBLEM 4")
print("."*40)
for all_rows in results:
    print(all_rows)
print()

# PROBLEM 5 ----------------------------------------------------------------
# List the kind of crimes that were recorded at schools. (No repetitions)
schools_crimes_query = """SELECT DISTINCT PRIMARY_TYPE 
FROM CRIME_TABLE
WHERE LOCATION_DESCRIPTION
LIKE '%SCHOOL%'"""

cursor_obj.execute(schools_crimes_query)
results = cursor_obj.fetchall()

# Print results
print("PROBLEM 5")
print("."*40)
for all_rows in results:
    print(all_rows[0])
print()

# PROBLEM 6 ----------------------------------------------------------------
# List the type of schools along with the average safety score for each type.
average_safety_query = """SELECT "Elementary, Middle, or High School", AVG(SAFETY_SCORE) AS Average_Safety_Score 
FROM SCHOOL_TABLE 
GROUP BY "Elementary, Middle, or High School" 
"""
cursor_obj.execute(average_safety_query)
results = cursor_obj.fetchall()

# Print results
print("PROBLEM 6")
print("."*40)
print("Type of School | Avg. Safety Score")
print("-"*40)
for all_rows in results:
    print(f"{all_rows[0]} | {all_rows[1]} ")
print()
    
# PROBLEM 7 ----------------------------------------------------------------
# List 5 community areas with highest % of households below poverty line

households_query = """SELECT COMMUNITY_AREA_NUMBER, COMMUNITY_AREA_NAME, PERCENT_HOUSEHOLDS_BELOW_POVERTY
FROM CENSUS_TABLE
ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC
LIMIT 5
"""

cursor_obj.execute(households_query)
results = cursor_obj.fetchall()

# Print results
print("PROBLEM 7")
print("."*40)
print("Area Number | Area Name | Households below poverty (%)")
print("-"*40)
for all_rows in results:
    print(f"{all_rows[0]} | {all_rows[1]} | {all_rows[2]}")
print()

# PROBLEM 8 ----------------------------------------------------------------
# Which community area is most crime prone? Display the coumminty area number only.

crime_prone_query = """ SELECT COMMUNITY_AREA_NUMBER
FROM CRIME_TABLE
GROUP BY COMMUNITY_AREA_NUMBER
ORDER BY COUNT(*) DESC
LIMIT 1
"""

cursor_obj.execute(crime_prone_query)
result = cursor_obj.fetchone()

print("PROBLEM 8")
print("."*40)
print("Community Area Number most crime prone:")
print("-" * 40)
print(result[0])
print()

# PROBLEM 9 ----------------------------------------------------------------
# Use a sub-query to find the name of the community area with highest hardship index
hardship_query = """ SELECT COMMUNITY_AREA_NAME
FROM CENSUS_TABLE
WHERE HARDSHIP_INDEX = (
    SELECT MAX(HARDSHIP_INDEX)
    FROM CENSUS_TABLE
)
"""

cursor_obj.execute(hardship_query)
result = cursor_obj.fetchone()

print("PROBLEM 9")
print("."*40)
print("Community Area with the Highest Hardship Index:")
print("-" * 40)
print(result[0])
print()

# PROBLEM 10 ----------------------------------------------------------------
# Use a sub-query to determine the Community Area Name with most number of crimes
crime_query = """
SELECT COMMUNITY_AREA_NAME
FROM CENSUS_TABLE
WHERE COMMUNITY_AREA_NUMBER = (
    SELECT COMMUNITY_AREA_NUMBER
    FROM CRIME_TABLE
    GROUP BY COMMUNITY_AREA_NUMBER
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
"""
cursor_obj.execute(crime_query)
result = cursor_obj.fetchone()

print("PROBLEM 10")
print("."*40)
print("Community Area with the Most Number of Crimes:")
print("-" * 40)
print(result[0])

# FINAL EXAM QUESTION 2 ----------------------------------------------------------------
# Write and execute a SQL query to list all crimes that took place at a school. Include case number, crime type, and community name.
# How many rows were returned upon execution of this query?
crime_school_query = """
SELECT COUNT(*) FROM CRIME_TABLE
WHERE LOCATION_DESCRIPTION LIKE '%SCHOOL%'
"""
cursor_obj.execute(crime_school_query)
result = cursor_obj.fetchone()

print("FINAL EXAM. QUESTION 2")
print("."*40)
for all_rows in result:
    print(all_rows)