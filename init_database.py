import sqlite3
conn=sqlite3.Connection("bus_booking.db")
cur=conn.cursor()

# creating all the tables in database
try:
    cur.execute("""
        create table OPERATOR(
        OPID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NAME TEXT, 
        ADDRESS TEXT, 
        EMAIL TEXT, 
        PHONE INTEGER
        )""")
    cur.execute("""
        create table ROUTE(
        ROUTEID INTEGER,
        SID INTEGER,
        NAME TEXT,
        PRIMARY KEY(ROUTEID, SID)
        )""")
    cur.execute("""create table BUS(
        BUSID INTEGER PRIMARY KEY AUTOINCREMENT,
        TYPE TEXT, 
        CAPACITY INTEGER, 
        FARE INTEGER, 
        OPID INTEGER, 
        ROUTEID INTEGER, 
        CONSTRAINT fk_operator 
        FOREIGN KEY (OPID) 
        REFERENCES OPERATOR(OPID),
        CONSTRAINT fk_route 
        FOREIGN KEY (ROUTEID) 
        REFERENCES ROUTE(ROUTEID)
        )""")
    cur.execute("""create table RUNS(
        BUSID INTEGER, 
        DATE TEXT, SEAT_AVAIL INTEGER, 
        PRIMARY KEY(BUSID, DATE), 
        CONSTRAINT fk_bus 
        FOREIGN KEY (BUSID) 
        REFERENCES BUS(BUSID)
        )""")
    cur.execute("""create table BOOKING_HISTORY(
        REF_NO INTEGER PRIMARY KEY AUTOINCREMENT, 
        NAME TEXT, BUSID INTEGER, 
        SEATS INTEGER, DBOOK TEXT, 
        DSTART TEXT, DEND TEXT, 
        CONSTRAINT fk_bus 
        FOREIGN KEY (BUSID) 
        REFERENCES BUS(BUSID)
        )""")
except:
    pass

# populating the database

# Bus
for i in range(1):
    typ=input("bus type: ")
    cap=input("bus capacity: ")
    fare=input("bus fare: ")
    opid=input("bus opid: ")
    rid=input("bus routeid: ")
    cur.execute("""
    insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
    values(
        '{}', {}, {}, {}, {}
    )
    """.format(typ, cap, fare, opid, rid))
# Operator
for i in range(1):
    typ=input("bus type: ")
    cap=input("bus capacity: ")
    fare=input("bus fare: ")
    opid=input("bus opid: ")
    rid=input("bus routeid: ")
    cur.execute("""
    insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
    values(
        '{}', {}, {}, {}, {}
    )
    """.format(typ, cap, fare, opid, rid))

# Route
for i in range(1):
    typ=input("bus type: ")
    cap=input("bus capacity: ")
    fare=input("bus fare: ")
    opid=input("bus opid: ")
    rid=input("bus routeid: ")
    cur.execute("""
    insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
    values(
        '{}', {}, {}, {}, {}
    )
    """.format(typ, cap, fare, opid, rid))

# Runs
for i in range(1):
    typ=input("bus type: ")
    cap=input("bus capacity: ")
    fare=input("bus fare: ")
    opid=input("bus opid: ")
    rid=input("bus routeid: ")
    cur.execute("""
    insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
    values(
        '{}', {}, {}, {}, {}
    )
    """.format(typ, cap, fare, opid, rid))

# Booking History
for i in range(1):
    typ=input("bus type: ")
    cap=input("bus capacity: ")
    fare=input("bus fare: ")
    opid=input("bus opid: ")
    rid=input("bus routeid: ")
    cur.execute("""
    insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
    values(
        '{}', {}, {}, {}, {}
    )
    """.format(typ, cap, fare, opid, rid))


conn.commit()
conn.close()