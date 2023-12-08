import sqlite3

with sqlite3.connect('Register.db') as db:
    cursor = db.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS [Должности](
        id INTEGER PRIMARY KEY,
        name TEXT(50),
        salary REAL,
        cab INTEGER
    );
    
    CREATE TABLE IF NOT EXISTS [Услуги](
        id INTEGER PRIMARY KEY,
        name TEXT(50),
        price REAL,
        time_sec TEXT(50),
        position INTEGER,
        FOREIGN KEY (position) REFERENCES [Должности] (id)
    );
    
    CREATE TABLE IF NOT EXISTS [Сотрудники](
        id INTEGER PRIMARY KEY,
        fio TEXT(50),
        date_of_birth TEXT,
        tel TEXT,
        position INTEGER,
        FOREIGN KEY (position) REFERENCES [Должности] (id)
    );
    
    CREATE TABLE IF NOT EXISTS [Клиенты](
        id INTEGER PRIMARY KEY,
        fio TEXT(50),
        tel TEXT,
        date_of_birth DATATIME,
        comment TEXT
    );
    
    CREATE TABLE IF NOT EXISTS [Оказанные услуги](
        id INTEGER PRIMARY KEY,
        time TEXT(50),
        client INTEGER,
        employee INTEGER,
        service INTEGER,
        FOREIGN KEY (client) REFERENCES [Клиенты] (id),
        FOREIGN KEY (employee) REFERENCES [Сотрудники] (id),
        FOREIGN KEY (service) REFERENCES [Услуги] (id)
    )
    """

    cursor.executescript(query)

    cursor.execute("INSERT INTO [Услуги] VALUES(NULL, 'Освидетельствование', 50, 95, 5)")
    cursor.execute("INSERT INTO [Должности] VALUES(NULL, 'Психиатр', 2405.2, 107)")
    cursor.execute("INSERT INTO [Сотрудники] VALUES(NULL, 'Кенеди Д.М.', '13.04.1955', '+375445558127', 5)")
    cursor.execute("INSERT INTO [Клиенты] VALUES(NULL, 'Панин А.А.', '+375447179024', '01.11.1971', 'Мне нравится!')")
    cursor.execute("INSERT INTO [Оказанные услуги] VALUES(NULL, 11, 5, 5, 5)")
