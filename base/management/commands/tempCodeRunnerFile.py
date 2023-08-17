import psycopg2
  
conn = psycopg2.connect(database="gymtrack",
                        user='postgres', password='Rishabh422@', 
                        host='127.0.0.1', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()
  
sql2 = '''COPY exercise(body_part, muscle_name, exercise_name, sets, reps)
FROM /Users/rishabhtiwari/Desktop/gymtrack/base/management/commands/Workout.csv
DELIMITER ','
CSV HEADER;'''
  
cursor.execute(sql2)
  
sql3 = '''select * from exercise;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
  
conn.commit()
conn.close()