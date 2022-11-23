from datetime import datetime
import faker
from random import randint, sample, choice
import sqlite3

FAKE_DATA = faker.Faker("uk_UA")

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 5
NUMBER_TEACHERS = 3
NUMBER_GRADES = 20
SUBJECTS = []
with open("subjects.txt", "r", encoding="utf-8") as fh:
    SUBJECTS = fh.read().split("\n")


def generate_fake_data(
    number_groups, number_students, number_subjects, number_teachers
) -> tuple():
    fake_groups = []
    fake_students = []
    fake_subjects = []
    fake_teachers = []

    for _ in range(number_groups):
        fake_groups.append(FAKE_DATA.pystr_format()[:2].upper())

    for _ in range(number_students):
        fake_students.append(FAKE_DATA.first_name() + " " + FAKE_DATA.last_name())

    for subject in sample(SUBJECTS, k=number_subjects):
        fake_subjects.append(subject)

    for _ in range(number_teachers):
        if randint(0, 1):
            fake_teachers.append(
                FAKE_DATA.prefix_male()
                + " "
                + FAKE_DATA.first_name_male()
                + " "
                + FAKE_DATA.last_name_male()
            )
        else:
            fake_teachers.append(
                FAKE_DATA.prefix_female()
                + " "
                + FAKE_DATA.first_name_female()
                + " "
                + FAKE_DATA.last_name_female()
            )

    return fake_groups, fake_students, fake_subjects, fake_teachers


def prepare_data(fake_groups, fake_students, fake_subjects, fake_teachers) -> tuple():

    for_teachers = []
    for teacher in fake_teachers:
        for_teachers.append((teacher,))

    for_subjects = []
    for subject in fake_subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_groups = []
    for group in fake_groups:
        for_groups.append((group,))

    for_students = []
    for student in fake_students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    students_subjects = {}
    for student_id in range(1, NUMBER_STUDENTS + 1):
        students_subjects[student_id] = sample(
            list(range(1, NUMBER_SUBJECTS + 1)), k=NUMBER_SUBJECTS - 1
        )

    for_students_subjects = []
    for student_id, subject_ids in students_subjects.items():
        for subject_id in subject_ids:
            for_students_subjects.append((student_id, subject_id))

    for_grades = []
    for student_id in students_subjects:
        for _ in range(NUMBER_GRADES):
            for_grades.append(
                (
                    student_id,
                    choice(students_subjects[student_id]),
                    randint(1, 12),
                    FAKE_DATA.date_this_year(before_today=True, after_today=False),
                )
            )

    return (
        for_teachers,
        for_subjects,
        for_groups,
        for_students,
        for_students_subjects,
        for_grades,
    )


def insert_data_to_db(
    for_teachers,
    for_subjects,
    for_groups,
    for_students,
    for_students_subjects,
    for_grades,
) -> None:

    with sqlite3.connect("education.db") as con:

        cur = con.cursor()

        sql_to_teachers = """INSERT INTO teachers(full_name)
                               VALUES (?)"""
        cur.executemany(sql_to_teachers, for_teachers)

        sql_to_subjects = """INSERT INTO subjects([name], teacher_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, for_subjects)

        sql_to_groups = """INSERT INTO groups([name])
                               VALUES (?)"""
        cur.executemany(sql_to_groups, for_groups)

        sql_to_students = """INSERT INTO students(full_name, group_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, for_students)

        sql_to_students_subjects = """INSERT INTO students_subjects(student_id, subject_id)
                                        VALUES (?, ?)"""
        cur.executemany(sql_to_students_subjects, for_students_subjects)

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, date_of)
                                        VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, for_grades)

        con.commit()


if __name__ == "__main__":
    fake_groups, fake_students, fake_subjects, fake_teachers = generate_fake_data(
        NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_TEACHERS
    )
    (
        for_teachers,
        for_subjects,
        for_groups,
        for_students,
        for_students_subjects,
        for_grades,
    ) = prepare_data(fake_groups, fake_students, fake_subjects, fake_teachers)
    insert_data_to_db(
        for_teachers,
        for_subjects,
        for_groups,
        for_students,
        for_students_subjects,
        for_grades,
    )
