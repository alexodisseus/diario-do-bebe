from apps.post import blueprint
from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound

from apps.post.models import Post



from apps.post.forms import PostForm



@blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        Post.create_post(title=form.title.data, content=form.content.data, author=current_user)
        flash('Your post has been created!', 'success')
        return redirect(url_for('post_blueprint.index'))

    return render_template('post/create_post.html', title='New Post', form=form)



@blueprint.route('/view/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    print(post)
    return render_template('post/post.html', title=post.title, post=post)




@blueprint.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    """
    if post.author != current_user:
        abort(403)
    """
    print(post)
    form = PostForm()
    if form.validate_on_submit():
        post.update_post(title=form.title.data, content=form.content.data)
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post_blueprint.index', id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('post/create_post.html', title='Update Post', form=form)



@blueprint.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user:
        abort(403)
    post.delete_post()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('post_blueprint.index'))


# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""



@blueprint.route('/')
#@login_required
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    #return render_template('list_posts.html', posts=posts)
    return render_template('post/index.html' , posts=posts)

"""
@blueprint.route('/ver/<id>')
#@login_required
def view(id):
    cotista = view_id_cotistas(id)
    return render_template('cotistas/view.html' , cotista=cotista)
"""
