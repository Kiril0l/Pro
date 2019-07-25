import json
import sys
import sqlite3
import os

def create_db(path):
    if not os.path.isfile(path):
        with open(path, "wb") as file:
            pass
    return

def get_connect(path):
    connect = sqlite3.connect(path)
    return connect

def create_table(connect):
    sql = """CREATE TABLE IF NOT EXISTS "location" (
        	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        	"contry"	TEXT NOT NULL UNIQUE,
        	"city"	TEXT NOT NULL,
        	"lat"	REAL NOT NULL,
        	"lon"	REAL NOT NULL
        );"""
    cursor = connect.cursor()
    cursor.execute(sql)
    connect.commit()

def get_date(path):
    json_file = open(path, "r")
    data = json.load(json_file)
    json_file.close()
    return data

if __name__ == "__main__":
    if len(sys.argv) > 2:
        path = os.path.join(sys.argv[1], sys.argv[2])
        create_db(path)
        connection = get_connect(path)
        create_table(connection)
        data = get_date("city.list.json")
        print(data[0])
        print("OK")
    else:
        print("Not arguments")

    # if len(sys.argv) > 2:
    #     file = open("city.list.json", "r")
    #     cities = json.load(file)
    #     print(len(cities))
    # else:
    #     print("Нет аргументов")
    #     exit(1)
