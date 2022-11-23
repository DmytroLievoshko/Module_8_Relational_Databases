import sqlite3
from pprint import pprint


def main():
    with sqlite3.connect("education.db") as con:

        cur = con.cursor()
        for i in range(12):
            with open(f"select{str(i + 1)}.sql", encoding="utf-8") as fh:
                print(fh.readline())
                sql_text = fh.read()
                res = cur.execute(sql_text)
                pprint(res.fetchall())
                print("---------------------------------------------------\n")


if __name__ == "__main__":
    main()
