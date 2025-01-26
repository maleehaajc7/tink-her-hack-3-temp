import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("files.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

#for modification purpose to drop the table and recreate(to add a new column: description)

cursor.execute("DROP TABLE IF EXISTS Notes")
cursor.execute("DROP TABLE IF EXISTS Syllabus")

# Create the Notes table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL,
    module_number TEXT NOT NULL,
    drive_link TEXT NOT NULL,
    description TEXT NOT NULL     
);
""")



# Create the Syllabus table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Syllabus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL,
    scheme TEXT NOT NULL,
    drive_link TEXT NOT NULL,
    description TEXT NOT NULL     
);
""")


# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")