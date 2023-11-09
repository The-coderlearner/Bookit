from __init__ import db

class Venue(db.Model):
    __tablename__ = "Venue"
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    Place = db.Column(db.String(50), nullable=False)
    Capacity = db.Column(db.Integer, nullable=False)
    imgURL = db.Column(db.String(50))

class Shows(db.Model):
    __tablename__ = "Shows"
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    imgURL = db.Column(db.String(50))
    Description = db.Column(db.String(100))
    Ratings = db.Column(db.Float)
    pos = db.Column(db.Float, nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.ID'))
    Tags = db.Column(db.ARRAY(db.String(50)),nullable=False)
    venue = db.relationship("Venue", backref="showsven")
    Dates = db.Column(db.ARRAY(db.TIMESTAMP(timezone=True)), nullable=False)
    As=db.Column(db.Integer, nullable=False)
    Allseats=db.Column(db.Integer, nullable=False)
    def insert_show(name,imgurl,desc,r,pos,tag,date,venid,As):
        Z=Venue.query.filter_by(ID=venid).first()
        Z.Capacity=int(Z.Capacity)-int(As)
        new_show = Shows(Name=name, Ratings=r, Description=desc, Tags=tag, pos=pos,imgURL=imgurl,Dates=date,venue_id=venid,As=As,Allseats=As)
        db.session.add(new_show)
        db.session.commit()


class Userlogs(db.Model):
    __tablename__="Userlogs"
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.String(50), nullable=False)

class Admin(db.Model):
    __tablename__="Admin"
    Username = db.Column(db.String(50), unique=True, nullable=False,primary_key=True)
    Password = db.Column(db.String(50))

class USER(db.Model):
    __tablename__ = "USER"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50))

class Bookings(db.Model):
    __tablename__="Bookings"
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    timestamp = db.Column(db.String(50), nullable=False)
    Username = db.Column(db.String(50), nullable=False)
    show_id= db.Column(db.Integer, nullable=False)
    nos=db.Column(db.Integer, nullable=False)
    price=db.Column(db.Float, nullable=False)
    date= db.Column(db.String(50),nullable=False)
    Rating = db.Column(db.Float)
