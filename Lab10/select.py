import psycopg2
from config import config

# Get database connection parameters
params = config()

# Connect to the PostgreSQL database
db = psycopg2.connect(**params)

# Create a new cursor
current = db.cursor()

# SQL query
sql = """
    SELECT * FROM PhoneBook;
"""

# Execute the query
current.execute(sql)

# Fetch all the results
result = current.fetchall()

# Print the results
print(result)

# Close the cursor and commit the transaction
current.close()
db.commit()

# Close the database connection
db.close()
