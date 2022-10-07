import json
import sqlite3
conn=sqlite3.connect('dbfilw.sqlite')
consl=conn.cursor()
consl.executescript('''
drop table if exists users;
drop table if exists member;
drop table if exists course;
create table users(
    id integer not null primary key autoincrement unique,
    name text unique
);
create table course(
    id integer not null primary key autoincrement unique,
    title text unique
);
create table member(
    user_id integer,
    course_id integer,
    role integer,
    primary key (user_id,course_id)
)
''')
flname=input("Enter file name: ")
if len(flname)<1:
    flname="sampledata.json"
str_data=open(flname).read()
json_data=json.loads(str_data)
for entry in json_data:
    name=entry[0]
    title=entry[1]
    print(name,title)
    consl.execute('''
    insert or ignore into users(name)
    values(?)
    ''',(name,))
    consl.execute('''
    select id from users where name=?
    ''',(name,))

    user_id= consl.fetchone()[0]
    consl.execute('''
    insert or ignore into course(title)
    values(?)
    ''',(title,))
    consl.execute('''
    
    ''')
