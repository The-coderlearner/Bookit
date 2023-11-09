from flask import jsonify, request
from datetime import datetime
import json
from __init__ import *
from models import *
from tokengenerator import *



@app.route('/login', methods=['POST'])
def login():
    data = request.json
    #print(data)
    username = data['username']
    password = data['password']
    existing_user = USER.query.filter_by(username =  username).first()
    if existing_user:
        if existing_user.password != password:
            return ValueError
  
    #    print(existing_user.username)
        token = gen_token(username)
    #    print(token)
        cur_time=datetime.now()
        log_check = Userlogs.query.filter_by(username = username).first()
        if log_check:
            log_check.timestamp = str(cur_time)
            db.session.add(log_check)
            db.session.commit()
        else:
            new_log = Userlogs(username = data['username'], timestamp = str(cur_time))
            db.session.add(new_log)
            db.session.commit()
        return jsonify({'token':token,'userType':'user'})
    else:
        return KeyError
    




@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    #print(data)
    name = data['name']
    email = data['email']
    password = data['password']
    username = data['username']
    #print(data)
    if len(email)==0 or '@' not in email:
        return jsonify({'success':False,'message':'Not an EMail'}), 201
    existing_user = USER.query.filter_by(email=email).first()
    eu = USER.query.filter_by(username=username).first()
    if existing_user or eu:
        return jsonify({'success':False,'message':'User exists'}), 201
    user = USER( username=username, email=email, password=password,name=name)
    
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'done'})




@app.route('/uservenue/<int:venueID>', methods = ['GET'])
def venuedeets(venueID):
    v = Venue.query.filter_by(ID = venueID).first()
    s = Shows.query.filter_by(venue_id = venueID).all()
    L =[]
    for i in s:
        d={
            'ID': i.ID,
            'imgURL': i.imgURL,
            'Name': i.Name,
            'Description': i.Description
        }
        L.append(d)
    k = [v.ID, v.Name, v.Place, L]
    return k

sv = ''
@app.route('/searchit', methods = ['GET','POST'])
def searchit():
    if request.method == 'POST':
        global sv
        sv = request.json
     #   print(sv)
        return jsonify({'status':'success', 'sv': sv})
    else:
        sv = str(sv)
        L = Shows.query.filter(Shows.Name.like("%" +sv + "%")).all()
        L1 = Shows.query.filter(Shows.Name.like(sv + "%")).all()
        L2 = Shows.query.filter(Shows.Name.like("%" + sv)).all()
        l1 = Shows.query.filter(Shows.Tags.like("%" +sv + "%")).all()
        l2 = Shows.query.filter(Shows.Tags.like(sv + "%")).all()
        l3 = Shows.query.filter(Shows.Tags.like("%" +sv)).all()
        v10 = Venue.query.filter(Venue.Name.like("%" +sv + "%")).all()
        v11 = Venue.query.filter(Venue.Name.like("%" +sv)).all()
        v12 = Venue.query.filter(Venue.Name.like(sv + "%")).all()
        v20 = Venue.query.filter(Venue.Place.like("%" +sv + "%")).all()
        v21 = Venue.query.filter(Venue.Place.like(sv + "%")).all()
        v22 = Venue.query.filter(Venue.Place.like("%" +sv)).all()
        l0 = Shows.query.filter(Shows.Ratings.like("%" +sv + "%")).all()
        l00 = Shows.query.filter(Shows.Ratings.like("%" +sv)).all()
        l000 = Shows.query.filter(Shows.Ratings.like(sv + "%")).all()
        show = list(set(l0+L+l1+L1+ L2 + l2 + l3 + l00+ l000))

        venue = list(set(v10+v11+v12+v20+v21+v22))
        show_list, venue_list = [], []
        for i in show:
            d ={
                'ID': i.ID,
                'Name': i.Name,
                'imgURL':i.imgURL,
                'Tags': str(i.Tags)[1:-1]
            }
            show_list.append(d)
        for v in venue:
            d ={
                'ID': v.ID,
                'Name': v.Name,
                'Place': v.Place,
                'imgURL': v.imgURL,
            }
            venue_list.append(d)
        k = [sv, venue_list, show_list]
        print("k = ", k)
        return k


@app.route('/<int:showid>/<int:seats>/<username>/<int:p>', methods =['POST'])
def bookshow(showid, seats, username,p):
    #print(seats)
    sh = Shows.query.filter_by(ID = showid).first()
    d = sh.Dates [1:-1]
    if int(seats) == 0:
        return jsonify({'status': 'failure'})
    cur_time=datetime.now()
    s = Bookings(timestamp = str(cur_time), Username=username, show_id=showid, nos=seats, price=p, date= d )
    #print(s)
    db.session.add(s)
    #print(sh.As)
    db.session.commit()
    sh.As = sh.As - seats
    #print(sh.As)
    db.session.commit()

    return jsonify({'status': 'success'})



@app.route('/<int:showid>')
def showshow(showid):
    s = Shows.query.filter_by(ID = showid).first()
    #print(s.Name)
    vename = Venue.query.filter_by(ID = s.venue_id).first()
    d = s.Dates[1:-1].split()
    l = [vename.Place, vename.Name, s.Ratings, s.Name, s.As, s.pos, s.Tags[1:-1], d]
    #print(l)
    return l


@app.route('/', methods =['GET'])
def home():
    ven = Venue.query.all()
    venue_list = []
    for venue in ven:
        d ={
            'ID' : venue.ID,
            'place': venue.Place,
            'imgURL': venue.imgURL,
            'name' : venue.Name,
            'capacity': str(venue.Capacity)
        }
        venue_list.append(d)
    #print("venues: -" , venue_list, "\n\n")
    show = Shows.query.all()
    show_list = list()
    for s in show:
        d={
            'ID' : s.ID,
            'Description': s.Description,
            'pos':s.pos,
            'tags':str(s.Tags)[1:-1],
            'Dates':s.Dates,
            'Allseats': s.Allseats,
            'Ratings': s.Ratings,
            'imgURL': s.imgURL,
            'name' : s.Name,
            'capacity': s.As,
            'venue_id': s.venue_id
        }
     #   print(d)
        show_list.append(d)

    return jsonify({'venues':venue_list, 'shows':show_list})

@app.route('/<username>/profile', methods =['GET','PUT'])
def userprofile(username):
    if request.method == 'GET':
        try:

            b = Bookings.query.filter_by(Username = username).all()
            k,l = [], []
            for j in b:
                i = Shows.query.filter_by(ID = j.show_id).first()
                if i is None:
                    continue
                V = Venue.query.filter_by(ID = i.venue_id).first()
                date_format = "%Y-%m-%dT%H:%M"
                datetime_object = datetime.strptime(i.Dates[1:-1], date_format)
                m = j.Rating
                if m is None:
                    m=i.Ratings
                d ={
                        'ID': i.ID,
                        'Name': i.Name,
                        'Venue': V.Name,
                        'Date': i.Dates[1:-1],
                        'imgURL': i.imgURL,
                        'nos': j.nos,
                        'Total': j.price,
                        'Rating': m
                    }
                if datetime.now() < datetime_object:
                    l.append(d)
                    #print(l)
                else:
                    k.append(d)
                    #print(d)
            redis_cli.setex('profile', 1800, json.dumps({'shows': k, 'showsdone': l}))
            return jsonify({'shows': k, 'showsdone': l})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        data = request.json
        show_id = data['ID']
        i = Shows.query.filter_by(ID = show_id).first()
        j = Bookings.query.filter_by(Username = username).first()
        j.Rating = float(data['Rating'])
        rating = (i.Ratings + float(data['Rating']))/2
        i.Ratings = round(rating, 1)
        db.session.commit()
        return jsonify({'status': 'success'})
  