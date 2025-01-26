import sqlite3

# Connect to the database
conn = sqlite3.connect("files.db")
cursor = conn.cursor()

# Insert sample data
cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '1', 'https://drive.google.com/uc?export=download&id=1Hxz9hNQ1XWPOd5wTFkgClNWKnc-ZCsKr','MODULE 1 KTU NOTE');
""")
cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '2', 'https://drive.google.com/uc?export=download&id=1pDhEUt9GqnK0z6o1mQBSVjhITuiwkQ_y','MODULE 2 KTU NOTE');
""")

cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '3', 'https://drive.google.com/uc?export=download&id=1pDhEUt9GqnK0z6o1mQBSVjhITuiwkQ_y','MODULE 3 KTU NOTE');
""")

cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '4', 'https://drive.google.com/uc?export=download&id=1qwsyrTObotTRRiM-MhnSBujI3zCaLq5O', 'MODULE 4 KTU NOTE');
""")

cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '5', 'https://drive.google.com/uc?export=download&id=1-T4a_jqLszfMRSdlq1WLY9vgJOf0_lKl','MODULE 5 KTU NOTE');
""")

cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '1', 'https://drive.google.com/uc?export=download&id=1NI5kfgl1vQMLssIbH6JT_nsP0inBX4KU','MODULE 1 Kerala NOTE');
""")
cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '2', 'https://drive.google.com/uc?export=download&id=1nsAt1rB665vbhr9zxXu0HzOROsdz3DfO','MODULE 2 Kerala NOTE');
""")

cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '3', 'https://drive.google.com/uc?export=download&id=1gwx7FBM3IE5TrnGRZ6Xa7yOpKIGVrPiw','MODULE 3 Kerala NOTE');
""")
cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '4', 'https://drive.google.com/uc?export=download&id=1bWRqNQ_OkWehMqUuoLIPekNd3pTysq9m','MODULE 4 Kerala NOTE');
""")

cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('EST102', '5', 'https://drive.google.com/uc?export=download&id=1JoGSh0zqMss74BksKk_wmvSVrpnzWg55','MODULE 5 Kerala NOTE');
""")

cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('ENG1', 'A02', 'https://drive.google.com/uc?export=download&id=1lhf3ytSrXNxIkvScFrk7kb23tYs2BGk0','ALL MODULE BA-ENG CU NOTE');
""")

cursor.execute("""
INSERT INTO Notes (course_code, module_number, drive_link, description)
VALUES ('POL1', 'B01', 'https://drive.google.com/uc?export=download&id=1hXgk9ZbuLR_SDNc11I8MO47-XVbzLzqv','ALL MODULE BA-POL CU NOTE');
""")

cursor.execute("""
INSERT INTO Syllabus (course_code, scheme, drive_link, description)
VALUES ('EST102', '2015', 'https://drive.google.com/uc?export=download&id=1HnYfNkzenFhSVwxbgJUO7KfVIWzlbi4t','2015 scheme EST102');
""")

cursor.execute("""
INSERT INTO Syllabus (course_code, scheme, drive_link, description)
VALUES ('EST102', '2019', 'https://drive.google.com/uc?export=download&id=1Z-mI07F7PtxccRvd1fYmfHcjVvMCBkTC','2019 scheme EST102');
""")

cursor.execute("""
INSERT INTO Syllabus (course_code, scheme, drive_link, description)
VALUES ('BE100', '2015', 'https://drive.google.com/uc?export=download&id=1HI45YL3Nv1Pjc7vPwukUOmfDKEh6xrhw','2015 scheme BE100');
""")

cursor.execute("""
INSERT INTO Syllabus (course_code, scheme, drive_link, description)
VALUES ('ENG1_A02', '2022', 'https://drive.google.com/uc?export=download&id=1_lVLA7uYWV9Xq0NmNnkmUgMcfAeir6Ag','2022 scheme ENG1 A02');
""")

cursor.execute("""
INSERT INTO Syllabus (course_code, scheme, drive_link, description)
VALUES ('POL1_B01', '2023', 'https://drive.google.com/uc?export=download&id=1f05T9xbfvRbrUaMyEnULJRu1asB7japD','2022 scheme POL1 B01');
""")


# Commit and close
conn.commit()
conn.close()

print("Data inserted successfully.")
