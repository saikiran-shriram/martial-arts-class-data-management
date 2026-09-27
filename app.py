from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Password",  
        database="martialartsclass"    
    )

@app.route('/')
def index():
    return redirect('/artists')

@app.route('/artists')
def artists():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Martial_Artist")
    all_artists = cursor.fetchall()
    conn.close()
    return render_template('artists.html', artists=all_artists)

@app.route('/artists/add', methods=['GET', 'POST'])
def add_artist():
    if request.method == 'POST':
        artist_id = request.form['artist_id']
        artist_name = request.form['artist_name']
        age = request.form['age']
        belt = request.form['belt']
        mob_no = request.form['mob_no']
        class_id = request.form['class_id']
        email = request.form['email']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Martial_Artist (artist_id, artist_name, age, belt, mob_no , class_id, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (artist_id, artist_name, age, belt, mob_no, class_id, email))
        conn.commit()
        conn.close()
        return redirect('/artists')

    return render_template('add_artist.html')


@app.route('/artists/delete/<int:artist_id>')
def delete_artist(artist_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Martial_Artist WHERE artist_id = %s", (artist_id,))
    conn.commit()
    conn.close()
    return redirect('/artists')

@app.route('/coaches')
def coaches():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Coach")
    all_coaches = cursor.fetchall()
    print(all_coaches)   
    conn.close()
    return render_template('coaches.html', coaches=all_coaches)

@app.route('/coaches/add', methods=['GET', 'POST'])
def add_coach():
    if request.method == 'POST':
        coach_id = request.form['coach_id']
        name = request.form['name']
        age = request.form['age']
        belt = request.form['belt']
        experience = request.form['experience']
        email = request.form['email']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Coach (coach_id, name, age, belt, experience, email)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (coach_id, name, age, belt, experience, email))
        conn.commit()
        conn.close()
        return redirect('/coaches')

    return render_template('add_coach.html')

@app.route('/coaches/delete/<int:coach_id>')
def delete_coach(coach_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Coach WHERE coach_id = %s", (coach_id,))
    conn.commit()
    conn.close()
    return redirect('/coaches')


@app.route('/classes')
def classes():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Dojo_Class")
    all_classes = cursor.fetchall()
    print(all_classes)   
    conn.close()
    return render_template('classes.html', classes=all_classes)

@app.route('/classes/add', methods=['GET', 'POST'])
def add_class():
    if request.method == 'POST':
        class_id = request.form['class_id']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        opening_date = request.form['opening_date']
        no_of_students = request.form['no_of_students']
        style_id = request.form['style_id']
        coach_id = request.form['coach_id']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO Dojo_Class (class_id, address, city, state, opening_date, no_of_students, style_id, coach_id) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
    """, (class_id, address, city, state, opening_date, no_of_students, style_id, coach_id))
        conn.commit()
        conn.close()
        return redirect('/classes')

    return render_template('add_class.html')

@app.route('/classes/delete/<int:class_id>')
def delete_class(class_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Dojo_Class WHERE class_id = %s", (class_id,))
    conn.commit()
    conn.close()
    return redirect('/classes')

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
