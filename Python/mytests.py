# -----------------------------------------
# IMPORT DATA QUALITY CHECK FUNCTIONS
# These functions are defined in the dataqualitychecks module 
#   added in the dataqualitychecks.py file.
# If you add new checks or rename functions in that module,
#   make sure to update the imports here accordingly.
# You can also import other custom checks if needed.
# -----------------------------------------
from dataqualitychecks import check_for_nulls
from dataqualitychecks import check_for_min_max
from dataqualitychecks import check_for_valid_values
from dataqualitychecks import check_for_duplicates

# -----------------------------
# TEST DEFINITIONS
# Each test is a dictionary with:
# - testname: label for the test
# - test: function to call from dataqualitychecks module
# - column: column to test (UPDATE THIS for new table)
# - table: table to test (UPDATE THIS for new dataset)
# - minimum/maximum: used in min-max tests (adjust as needed)
# - valid_values: set of expected values (adjust per context)
# -----------------------------

test1 = {
    "testname": "Check for nulls",
    "test": check_for_nulls,
    "column": "monthid",     # <-- Change column name when using on a new table
    "table": "DimMonth"      # <-- Change table name for your target data
}

test2 = {
    "testname": "Check for min and max",
    "test": check_for_min_max,
    "column": "month",       # <-- Update to new numeric column if reused
    "table": "DimMonth",     # <-- Update table
    "minimum": 1,            # <-- Set appropriate lower bound
    "maximum": 12            # <-- Set appropriate upper bound
}

test3 = {
    "testname": "Check for valid values",
    "test": check_for_valid_values,
    "column": "category",             # <-- Column being validated
    "table": "DimCustomer",           # <-- Target table
    "valid_values": {'Individual', 'Company'}  # <-- Change valid values for new data
}

test4 = {
    "testname": "Check for duplicates",
    "test": check_for_duplicates,
    "column": "monthid",     # <-- Unique key to check for duplication
    "table": "DimMonth"
}

test5 = {
    "testname": "Check for nulls",
    "test": check_for_nulls,
    "column": "year",        # <-- Adjust column name for different date or ID fields
    "table": "DimMonth"
}

test6 = {
    "testname": "Check for min and max",
    "test": check_for_min_max,
    "column": "quarter",     # <-- Change to relevant numeric column
    "table": "DimMonth",
    "minimum": 1,
    "maximum": 4
}

test7 = {
    "testname": "Check for valid values",
    "test": check_for_valid_values,
    "column": "quartername",             # <-- Text column to validate
    "table": "DimMonth",
    "valid_values": {'Q1', 'Q2', 'Q3', 'Q4'}  # <-- Adjust based on expected values
}

test8 = {
    "testname": "Check for duplicates",
    "test": check_for_duplicates,
    "column": "customerid",   # <-- Key column expected to be unique
    "table": "DimCustomer"
}