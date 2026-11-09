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

@app.route('/artists/edit/<int:artist_id>', methods=['GET', 'POST'])
def edit_artist(artist_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        artist_name = request.form['artist_name']
        age = request.form['age']
        belt = request.form['belt']
        mob_no = request.form['mob_no']
        class_id = request.form['class_id']
        email = request.form['email']

        cursor.execute("""
            UPDATE Martial_Artist
            SET artist_name = %s, age = %s, belt = %s,
                mob_no = %s, class_id = %s, email = %s
            WHERE artist_id = %s
        """, (artist_name, age, belt, mob_no, class_id, email, artist_id))

        conn.commit()
        conn.close()

        return redirect('/artists')

    cursor.execute(
        "SELECT * FROM Martial_Artist WHERE artist_id = %s",
        (artist_id,)
    )
    artist = cursor.fetchone()
    conn.close()

    return render_template('edit_artist.html', artist=artist)


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

@app.route('/coaches/edit/<int:coach_id>', methods=['GET', 'POST'])
def edit_coach(coach_id):

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        belt = request.form['belt']
        experience = request.form['experience']
        email = request.form['email']

        cursor.execute("""
            UPDATE Coach
            SET name = %s, age = %s, belt = %s,
                experience = %s, email = %s
            WHERE coach_id = %s
        """, (name, age, belt, experience, email, coach_id))

        conn.commit()
        conn.close()

        return redirect('/coaches')

    cursor.execute(
        "SELECT * FROM Coach WHERE coach_id = %s",
        (coach_id,)
    )
    coach = cursor.fetchone()
    conn.close()

    return render_template('edit_coach.html', coach=coach)

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

@app.route('/classes/edit/<int:class_id>', methods=['GET', 'POST'])
def edit_class(class_id):

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        opening_date = request.form['opening_date']
        no_of_students = request.form['no_of_students']
        style_id = request.form['style_id']
        coach_id = request.form['coach_id']

        cursor.execute("""
            UPDATE Dojo_Class
            SET address = %s, city = %s, state = %s,
                opening_date = %s, no_of_students = %s,
                style_id = %s, coach_id = %s
            WHERE class_id = %s
        """, (address, city, state, opening_date,
              no_of_students, style_id, coach_id, class_id))

        conn.commit()
        conn.close()
        return redirect('/classes')

    cursor.execute(
        "SELECT * FROM Dojo_Class WHERE class_id = %s",
        (class_id,)
    )
    class_data = cursor.fetchone()
    conn.close()

    return render_template('edit_class.html', **{'class': class_data})

@app.route('/classes/delete/<int:class_id>')
def delete_class(class_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Dojo_Class WHERE class_id = %s", (class_id,))
    conn.commit()
    conn.close()
    return redirect('/classes')

@app.route('/styles')
def styles():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM martial_art_style")
    all_styles = cursor.fetchall()
    print(all_styles)   
    conn.close()
    return render_template('styles.html', styles=all_styles)

@app.route('/styles/add', methods=['GET', 'POST'])
def add_style():
    if request.method == 'POST':
        style_id = request.form['style_id']
        type = request.form['type']
        origin_country = request.form['origin_country']
        description = request.form['description']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO Martial_Art_Style (style_id, type, origin_country, description) 
        VALUES (%s, %s, %s, %s) 
    """, (style_id, type, origin_country, description))
        conn.commit()
        conn.close()
        return redirect('/styles')

    return render_template('add_style.html')

@app.route('/styles/edit/<int:style_id>', methods=['GET', 'POST'])
def edit_style(style_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        style_type = request.form['type']
        origin_country = request.form['origin_country']
        description = request.form['description']

        cursor.execute("""
            UPDATE Martial_Art_Style
            SET type = %s, origin_country = %s, description = %s
            WHERE style_id = %s
        """, (style_type, origin_country, description, style_id))

        conn.commit()
        conn.close()
        return redirect('/styles')
    cursor.execute(
        "SELECT * FROM Martial_Art_Style WHERE style_id = %s",
        (style_id,)
    )
    style = cursor.fetchone()
    conn.close()
    return render_template('edit_style.html', style=style)

@app.route('/styles/delete/<int:style_id>')
def delete_style(style_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Martial_Art_Style WHERE style_id = %s", (style_id,))
    conn.commit()
    conn.close()
    return redirect('/styles')

@app.route('/tournaments')
def tournaments():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Tournament")
    all_tournaments = cursor.fetchall()
    print(all_tournaments)   
    conn.close()
    return render_template('tournaments.html', tournaments=all_tournaments)

@app.route('/tournaments/add', methods=['GET', 'POST'])
def add_tournament():
    if request.method == 'POST':
        tournament_id = request.form['tournament_id']
        date = request.form['date']
        venue = request.form['venue']
        level = request.form['level']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO Tournament (tournament_id, date, venue, level) 
        VALUES (%s, %s, %s, %s) 
    """, (tournament_id, date, venue, level))
        conn.commit()
        conn.close()
        return redirect('/tournaments')

    return render_template('add_tournament.html')

@app.route('/tournaments/edit/<int:tournament_id>', methods=['GET', 'POST'])
def edit_tournament(tournament_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        date = request.form['date']
        venue = request.form['venue']
        level = request.form['level']

        cursor.execute("""
            UPDATE Tournament
            SET date = %s, venue = %s, level = %s
            WHERE tournament_id = %s
        """, (date, venue, level, tournament_id))

        conn.commit()
        conn.close()
        return redirect('/tournaments')
    cursor.execute(
        "SELECT * FROM Tournament WHERE tournament_id = %s",
        (tournament_id,)
    )
    tournament = cursor.fetchone()
    conn.close()
    return render_template('edit_tournament.html', tournament=tournament)

@app.route('/tournaments/delete/<int:tournament_id>')
def delete_tournament(tournament_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tournament WHERE tournament_id = %s", (tournament_id,))
    conn.commit()
    conn.close()
    return redirect('/tournaments')

@app.route('/participations')
def participations():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM participates_in")
    all_participations = cursor.fetchall()
    print(all_participations)   
    conn.close()
    return render_template('participations.html', participations=all_participations)

@app.route('/participations/add', methods=['GET', 'POST'])
def add_participation():
    if request.method == 'POST':
        artist_id = request.form['artist_id']
        tournament_id = request.form['tournament_id']
        result = request.form['result']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO Participates_in (artist_id, tournament_id, result) 
        VALUES (%s, %s, %s) 
    """, (artist_id, tournament_id, result))
        conn.commit()
        conn.close()
        return redirect('/participations')

    return render_template('add_participation.html')

@app.route('/participations/delete/<int:artist_id>')
def delete_participation(artist_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Participates_in WHERE artist_id = %s", (artist_id,))
    conn.commit()
    conn.close()
    return redirect('/participations')

@app.route('/attendance')
def attendance():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Attendance")
    all_records = cursor.fetchall()
    print(all_records)   
    conn.close()
    return render_template('attendance.html', attendance=all_records)

@app.route('/attendance/add', methods=['GET', 'POST'])
def add_attendance():
    if request.method == 'POST':
        artist_id = request.form['artist_id']
        class_id = request.form['class_id']
        date = request.form['date']
        time = request.form['time']
        status = request.form['status']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO Attendance (artist_id, class_id, date , time , status) 
        VALUES (%s, %s, %s, %s ,%s) 
    """, (artist_id, class_id, date , time , status))
        conn.commit()
        conn.close()
        return redirect('/attendance')

    return render_template('add_attendance.html')

@app.route('/attendance/delete/<int:artist_id><int:class_id>')
def delete_attendance(artist_id,class_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Attendance WHERE artist_id = %s and class_id = %s", (artist_id,class_id))
    conn.commit()
    conn.close()
    return redirect('/attendance')

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
