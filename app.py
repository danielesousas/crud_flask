from flask import Flask, render_template, request, url_for, redirect, flash
import sqlite3 as sql


app = Flask(__name__)

@app.route('/')


@app.route('/index')
def index():
    con = sql.connect('form_db.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return render_template('index.html', data=data)

@app.route('/add_user', methods=['POST','GET'])
def add_user():
    if request.method=="POST":
        nome = request.form['nome'],
        idade = request.form['idade'],
        endereco = request.form['endereco'],
        numero = request.form['numero'],
        cidade = request.form['cidade'],
        estado = request.form['estado'],
        email = request.form['email']
        con = sql.connect('form_db.db')
        cur = con.cursor()
        cur.execute("insert into users(NOME, IDADE, ENDEREÇO, NUMERO, CIDADE, ESTADO, EMAIL) values (?,?,?,?,?,?,?)", (nome, idade, endereco, numero, cidade, estado, email))
        con.commit()
        flash('Dados Cadastrados!', 'success')
        return redirect(url_for("index"))
    return render_template('add_user.html')

@app.route('/edit_user/<string:id>', methods=["POST", "GET"])
def edit_user(id):
    if request.method=="POST":
        nome = request.form['nome'],
        idade = request.form['idade'],
        endereco = request.form['endereco'],
        numero = request.form['numero'],
        cidade = request.form['cidade'],
        estado = request.form['estado'],
        email = request.form['email']
        con = sql.connect('form_db.db')
        cur = con.cursor()
        cur.execute("update users set NOME=?, IDADE=?, ENDEREÇO=?, NUMERO=?, CIDADE=?, ESTADO=?, EMAIL=? where ID=?",(nome, idade, endereco, numero, cidade, estado, email))
        con.commit()
        flash('Dados Atualizados com Sucesso!', 'success')
        return redirect(url_for('index'))
    con=sql.connect('form_db.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where ID=?",(id))
    data=cur.fetchone()
    return render_template('index.html', data=data)


@app.route('/delete_user<string:id>', methods=['GET'])
def delete(id):
    if request.method=="POST":
        con = sql.connect('form_db.db')
        cur = con.cursor()
        cur.execute("delete users where ID=?", (id))
        con.commit()
        flash('Dados Deletados', 'warning')
        return redirect(url_for('index'))
    

if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)