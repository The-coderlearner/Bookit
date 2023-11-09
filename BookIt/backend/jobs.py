from flask_mail import Message, Mail
from celery import Celery
from celery.schedules import crontab
from __init__ import app
from models import USER,Userlogs, Bookings,Shows, Venue
from datetime import *
from flask import current_app, render_template


celery = Celery(
    'jobs',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)
celery.conf.timezone = "Asia/Kolkata"
@celery.task()
def daily_sender():
    with app.app_context(): 
        didnotbook, didnotlogin = usernotify()
        with app.test_request_context(): 
            for user in didnotbook:
                send_the_email(user)
            for user in didnotlogin:
                send_email(user)

def usernotify():
    today = str(date.today())
    flag = False
    k = USER.query.all()
    l, m=[], []
    for j in k:
        flag = True
        kuku = Userlogs.query.filter_by(username = j.username).first()
        booky = Bookings.query.filter_by(Username = j.username).all()
        if kuku.timestamp[:10] != today:
            l.append(kuku.username)
        for i in booky:
            if i.timestamp[:10] == today:
                flag = False
        if flag:
             m.append(j.username)
    print(l,m)
    didnotlogin = []
    didnotbook = []
    for i in l:
        k = USER.query.filter_by(username = i).first()
        didnotlogin.append(k.email)
    for i in m:
        k = USER.query.filter_by(username = i).first()
        if k.email not in didnotlogin:
            didnotbook.append(k.email)
    print(didnotbook, didnotlogin)
    return didnotbook, didnotlogin
    

def send_the_email(email):
    sender = 'sssa.aditi@gmail.com'
    subject = 'Ping!!! BookIt notification!'
    html_body = render_template("daily_notbooked.html")
    msg = Message(subject=subject, sender=sender, recipients=[email], html=html_body)
    with current_app.app_context():
        mail = Mail(current_app)
        mail.send(msg)
    return 'Email Sent Successfully'

def send_email(email):
    sender = 'sssa.aditi@gmail.com'
    subject = 'Ping!!! BookIt notification!'
    html_body = render_template("daily_notvisited.html")
    msg = Message(subject=subject, sender=sender, recipients=[email], html=html_body)

    with current_app.app_context():
        mail = Mail(current_app)
        mail.send(msg)
    return 'Email Sent Successfully'

def monthlymailer(user, b):
    sender = 'sssa.aditi@gmail.com'
    sub = 'BookIt Report'
    if b is None:
        html_body = render_template("monthly_notbooked.html")
        msg = Message(subject=sub, sender=sender, recipients=[user.email], html=html_body)
        with current_app.app_context():
            mail = Mail(current_app)
            mail.send(msg)
        return 'Email Sent Successfully'
    html_body = render_template('monthly_report.html',user=user, b = b)
    msg = Message(subject=sub, sender=sender, recipients=[user.email], html=html_body)
    with current_app.app_context():
        mail = Mail(current_app)
        mail.send(msg)
    return 'Email Sent Successfully'


@celery.task
def monthly_sender():
    with app.app_context(): 
        users = USER.query.all()
        with app.test_request_context(): 
            for user in users:
                bookings = monthlybook(user)
                monthlymailer(user, bookings)

def monthlybook(user):
    
    month = datetime.now() - timedelta(days=30)
    bl =[]
    bookings = Bookings.query.filter_by(Username=user.username).all()
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    for i in bookings:
        k = i.timestamp
        datetime_object = datetime.strptime(k, date_format)
        if datetime_object > month:
            bl.append(i)
    print(bl)
    b =[]
    if len(bl) == 0:
        return None
    for i in bl:
        m =[]
        s = Shows.query.filter_by(ID = i.show_id).first()
        if s==None:
            continue
        v = Venue.query.filter_by(ID = s.venue_id).first()
        if i.Rating is None:
            k = None
        else:
            k = i.Rating
        m = [s.Name, v.Name, v.Place, i.date[1:-1], i.nos, k]
        b.append(m)
    return b

celery.conf.broker_connection_retry_on_startup = True

celery.conf.enable_utc = False
celery.conf.timezone = "Asia/Kolkata"
celery.conf.beat_schedule = {
    'send-daily-emails': {
        'task': 'jobs.daily_sender', 
        'schedule': crontab(hour='23', minute='50'),
    },
    'send-monthly-emails': {
        'task': 'jobs.monthly_sender', 
        'schedule': crontab(day_of_month='23', hour='23', minute='50'),
    },
}

