from pymongo import MongoClient, collection

client = MongoClient('localhost', 27017)
db = client['mydatabase']


students_collection = db['Students']
advisors_collection = db['Advisors']
student_advisor_collection = db['Student_Advisor']


students_data = [
    {"student_id": 1, "name": "John Doe"},
    {"student_id": 2, "name": "Alice Smith"},
    {"student_id": 3, "name": "Michael Johnson"},
    {"student_id": 4, "name": "Emily Brown"},
    {"student_id": 5, "name": "David Wilson"},
    {"student_id": 6, "name": "Sarah Taylor"},
    {"student_id": 7, "name": "Daniel Martinez"},
    {"student_id": 8, "name": "Emma Anderson"},
    {"student_id": 9, "name": "James Garcia"},
    {"student_id": 10, "name": "Olivia Lee"}
]
students_collection.insert_many(students_data)

advisors_data = [
    {"advisor_id": 101, "name": "Dr. Smith"},
    {"advisor_id": 102, "name": "Prof. Johnson"},
    {"advisor_id": 103, "name": "Dr. Williams"},
    {"advisor_id": 104, "name": "Prof. Brown"},
    {"advisor_id": 105, "name": "Dr. Wilson"},
    {"advisor_id": 106, "name": "Prof. Taylor"},
    {"advisor_id": 107, "name": "Dr. Martinez"},
    {"advisor_id": 108, "name": "Prof. Anderson"},
    {"advisor_id": 109, "name": "Dr. Garcia"},
    {"advisor_id": 110, "name": "Prof. Lee"}
]
advisors_collection.insert_many(advisors_data)

student_advisor_data = [
    {"student_id": 1, "advisor_id": 101},
    {"student_id": 2, "advisor_id": 102},
    {"student_id": 3, "advisor_id": 103},
    {"student_id": 4, "advisor_id": 104},
    {"student_id": 5, "advisor_id": 105},
    {"student_id": 6, "advisor_id": 106},
    {"student_id": 7, "advisor_id": 107},
    {"student_id": 8, "advisor_id": 108},
    {"student_id": 9, "advisor_id": 109},
    {"student_id": 10, "advisor_id": 110}
]
student_advisor_collection.insert_many(student_advisor_data)

pipeline = [
    {"$lookup": {
        "from": "Student_Advisor",
        "localField": "advisor_id",
        "foreignField": "advisor_id",
        "as": "students"
    }},
    {"$project": {
        "_id": 0,
        "advisor_id": 1,
        "name": 1,
        "num_students": {"$size": "$students"}
    }}
]

results = advisors_collection.aggregate(pipeline)
for result in results:
    print(f"id of advisor: {result['advisor_id']}, Name of advisor: {result['name']}, Number of students: {result['num_students']}")

client.close()
