from flask_app.models.model_user import User
from flask_app.models.model_post import Post

from flask_app import app
from flask import render_template, redirect, flash, session, request

@app.route('/ideas')
def list_user_posts():
    if 'user_id' not in session:
        return redirect('/login')
    # Collects all the posts from the database and their users
    posts = Post.get_all_posts()
    print(posts)
    return render_template('ideas.html', posts = posts)
    
@app.route('/add_blog', methods=['POST'])
def add_post():
    if 'user_id' not in session:
        return redirect('/login')
    data = {
        'title' : request.form['title'],
        'content' : request.form['content'],
        'user_id' : session['user_id']
    }

    Post.add_blog(data)
    return redirect('/ideas')

@app.route('/delete_blog/<int:blog_id>')
def delete_blog(blog_id):
    data = {
        'blog_id' : blog_id
    }

    Post.delete(data)
    return redirect('/ideas')

@app.route('/update_blog/<int:blog_id>')
def update_blog(blog_id):
    if 'user_id' not in session:
        return redirect('/login')
    data = {
        'blog_id' : blog_id
    }
    post = Post.get_post(data)
    return render_template('update_blog.html', post = post)
    
@app.route('/update', methods=["POST"])
def update():
    data = {
        'blog_id' : request.form['blog_id'],
        'title' : request.form['title'],
        'content' : request.form['content']
    }

    Post.update_the_blog(data)
    return redirect('/ideas')