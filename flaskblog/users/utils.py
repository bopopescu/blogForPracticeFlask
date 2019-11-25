import os
from flaskblog import mail
from flask import url_for,current_app
from PIL import Image
import secrets
from flask_mail import Message


def safe_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/img', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='nurlantukenbayev@gmail.com', recipients=[user.email])
    msg.body = f'''To reset password, visit the following link: 
    {url_for('users.reset_token', token=token, _external=True)}
    If you did not the make this request simply ignore this email.
    '''
    mail.send(msg)
