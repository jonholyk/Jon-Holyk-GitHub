# -----------------------------------------
# PRIOR TO RUNNING THIS SCRIPT
# No addt libraries are required (Pandas, numpy, etc.)
# MySQL or PostgreSQL connection is required
# - MySQL: pip install mysql-connector-python
# - PostgreSQL: pip install psycopg2
# -----------------------------------------

from time import time, ctime

# -----------------------------------------
# DATA QUALITY CHECKS MODULE
# This script provides reusable functions to perform 
# data integrity checks against a database table.
#   Update or extend functions if your data model changes
#   Connection object (conn) is expected to be passed in dynamically
# -----------------------------------------

conn = None  # You can override this with a live DB connection when calling the functions

# ------------------------------------------------
# Main wrapper to run and log any test function
# Reuse this for logging all tests consistently
# Make sure each test function follows the expected interface
# ------------------------------------------------
def run_data_quality_check(**options):
    print("*" * 50)
    print(ctime(time()))
    start_time = time()

    testname = options.pop("testname")  # Descriptive label for this test
    test = options.pop("test")          # Function reference (e.g., check_for_nulls)

    print(f"Starting test {testname}")
    status = test(**options)
    print(f"Finished test {testname}")
    print(f"Test Passed {status}")

    end_time = time()
    options.pop("conn")  # Remove connection from logging display

    print("Test Parameters")
    for key, value in options.items():
        print(f"{key} = {value}")

    print()
    print("Duration : ", str(end_time - start_time))
    print(ctime(time()))
    print("*" * 50)

    return testname, options.get('table'), options.get('column'), status


# ----------------------------------------
# Null Check
# Change column/table when reused
# ----------------------------------------
def check_for_nulls(column, table, conn=conn):
    SQL = f'SELECT count(*) FROM "{table}" WHERE {column} IS NULL'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()
    return bool(row_count)  # Returns True if nulls exist


# ----------------------------------------
# Min/Max Range Check
# Adjust min/max values per field when reused
# ----------------------------------------
def check_for_min_max(column, table, minimum, maximum, conn=conn):
    SQL = f'SELECT count(*) FROM "{table}" WHERE {column} < {minimum} OR {column} > {maximum}'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()
    return not bool(row_count[0])  # Returns True if all values are in range


# ----------------------------------------
# Valid Values Check
# Update valid_values set depending on expected inputs
# ----------------------------------------
def check_for_valid_values(column, table, valid_values=None, conn=conn):
    SQL = f'SELECT DISTINCT({column}) FROM "{table}"'
    cursor = conn.cursor()
    cursor.execute(SQL)
    result = cursor.fetchall()
    actual_values = {x[0] for x in result}
    print(actual_values)  # Useful for debugging unexpected values
    status = [value in valid_values for value in actual_values]
    cursor.close()
    return all(status)  # Returns True only if all values are valid


# ----------------------------------------
# Duplicate Check
# Change column/table for different keys
# ----------------------------------------
def check_for_duplicates(column, table, conn=conn):
    SQL = f'SELECT count({column}) FROM "{table}" GROUP BY {column} HAVING count({column}) > 1'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()
    return not bool(row_count)  # Returns True if no duplicates found