from flask import Blueprint, flash, render_template, redirect, url_for, abort, request
from flaskblog import db
from flaskblog.posts.forms import PostForm
from flaskblog.models import Post
from flask_login import current_user, login_required

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Youre post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title="New Post", form=form, legend="New Post")


@posts.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', title="Post", post=post)


@posts.route('/post/<int:id>/update', methods=['GET', 'POST'])
def post_update(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Youre post has been updated!', 'success')
        return redirect(url_for('posts.post', id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title="Post Update", form=form, legend="Update Post")


@posts.route('/post/<int:id>/delete', methods=['POST'])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Youre post has been deleted!', 'success')
    return redirect(url_for('main.home'))
