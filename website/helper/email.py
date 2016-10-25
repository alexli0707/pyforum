from threading import Thread

from config import MAIL_DEFAULT_SENDER
from flask import render_template, current_app
from flask_mail import Message
from website.app import mail


def send_async_email(app, msg):
    """异步发送"""
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    """发送邮件"""
    app = current_app._get_current_object()
    msg = Message(subject, sender=MAIL_DEFAULT_SENDER, recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
