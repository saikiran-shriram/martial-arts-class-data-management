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
            INSERT INTO Martial_Artist (artist_id, artist_name, age, belt, mob_no, class_id, email)
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

if __name__ == '__main__':
    app.run(debug=True)
