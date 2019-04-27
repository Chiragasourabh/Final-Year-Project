from flaskext.mysql import MySQL

def dbInit(app):
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'FYPCS'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'tXsDi9pEJ8M6tmk'
    app.config['MYSQL_DATABASE_DB'] = 'FYPCS'
    app.config['MYSQL_DATABASE_HOST'] = 'FYPCS.mysql.pythonanywhere-services.com'
    mysql.init_app(app)
    try:
        conn = mysql.connect()
        cursor =conn.cursor()
        return cursor
    except:
        print("Database Error")
        return None
    return None

# cursor.execute("SELECT * from User")
# data = cursor.fetchone()