from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import AddMemberForm, AddBookForm
import os

# Flask app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for WTForms
db = SQLAlchemy(app)

# Import models
from models import Member, Book

# Home route
@app.route('/')
def home():
    members = Member.query.all()
    books = Book.query.all()
    return render_template('home.html', members=members, books=books)

# CRUD for Members
@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    form = AddMemberForm()
    if form.validate_on_submit():
        new_member = Member(name=form.name.data, email=form.email.data)
        db.session.add(new_member)
        db.session.commit()
        flash('Member added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_member.html', form=form)

@app.route('/edit_member/<int:id>', methods=['GET', 'POST'])
def edit_member(id):
    member = Member.query.get_or_404(id)
    form = AddMemberForm(obj=member)
    if form.validate_on_submit():
        member.name = form.name.data
        member.email = form.email.data
        db.session.commit()
        flash('Member updated successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('edit_member.html', form=form, member=member)

@app.route('/delete_member/<int:id>')
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    flash('Member deleted successfully!', 'danger')
    return redirect(url_for('home'))

# CRUD for Books
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data, author=form.author.data)
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_book.html', form=form)

@app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    form = AddBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        db.session.commit()
        flash('Book updated successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('edit_book.html', form=form, book=book)

@app.route('/delete_book/<int:id>')
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully!', 'danger')
    return redirect(url_for('home'))

if __name__ == '__main__':
    if not os.path.exists('library.db'):
        db.create_all()  # Create database if it doesn't exist
    app.run(debug=True)
