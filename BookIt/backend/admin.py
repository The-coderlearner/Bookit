from __init__ import *
from models import *
from flask import jsonify, request, Response
import pandas as pd
from tokengenerator import *


@app.route("/admin/addvenue",methods=["POST","GET"])
@jwt_required
def addvenue():
    data = request.json
  #  print(data)
    n,img,c,p = data['Name'],data['imgURL'],int(data['Capacity'].strip()),data['Place']
    ven = Venue.query.filter_by(Name=n).first()
    if ven==None:
        new_ven = Venue(Name=n, Place=p, Capacity=c, imgURL=img )
        db.session.add(new_ven)
        db.session.commit()
    return jsonify(data)



@app.route('/admin/editV/<int:venueID>',methods = ['GET', 'PUT'])
def editvenue(venueID):
   # print(venueID)
    data = request.json
    #print(data)
    venue = Venue.query.filter_by(ID=venueID).first()
    venue.Name=data['Name']
    venue.imgURL=data['imgURL']
    venue.Capacity=data['Capacity']
    venue.Place=data['Place']
    db.session.commit()
    return jsonify({'status': 'Success'})



@app.route('/admin/deletevenue/<int:venueID>',methods=['GET','DELETE'])
@jwt_required
def deletevenue(venueID):
    #print(venueID)
    show = Shows.query.filter_by(venue_id=venueID).all()
    for i in show:
        db.session.delete(i)
        db.session.commit()
    venue = Venue.query.filter_by(ID=venueID).first()
    db.session.delete(venue)
    db.session.commit()
    return jsonify({'status': 'Success'})



@app.route('/adminlogin', methods=['POST'])
def adminlogin():
    data = request.json
    username = data['username']
    password = data['password']
    existing_user = Admin.query.filter_by(Username=username).first()
    if existing_user:
        if existing_user.Password != password:
            return jsonify({'success':False,'message':'No such password'}), 201
  
        #print(existing_user.Username)
        token = genrate_token(username)
        return jsonify({'token':token,'userType':'admin'})
    else:
        return jsonify({'success':False,'message':'No such user exists'}), 201

@app.route('/adminsignup', methods = ['POST'])
def adminsignup():
    data = request.json
    eusername = data['eusername']
    Pass = data['epassword']
    username = data['username']
    password = data['password']
    existing_user = Admin.query.filter_by(Username=username).first()
    if existing_user:
        return jsonify({'success': False,'message': 'Error'}), 201
    s = Admin.query.filter_by(Username=eusername).first()
    if s==None or s.Password!=Pass:
        return jsonify({'success': False,'message': 'Error'}), 201
    user = Admin(Username=username, Password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'success'})



@app.route('/admin/<int:venueID>', methods=['GET','POST'] )
@jwt_required
def getshows(venueID):
    if request.method == 'GET':
        venue = Venue.query.filter_by(ID = venueID).first()
        #print(venue)
        show = Shows.query.filter_by(venue_id = venueID).all()
        #print(show)
        show_list = list()
        for s in show:
            d={
                'ID' : s.ID,
                'Description': s.Description,
                'pos':s.pos,
                'tags':str(s.Tags)[1:-1],
                'Dates':s.Dates,
                'Allseats': str(s.Allseats),
                'Ratings': s.Ratings,
                'imgURL': s.imgURL,
                'name' : s.Name,
                'Capacity': str(s.As)
            }
            #print(s.Name,d)
            show_list.append(d)
        venue_data = {
            'ID': venue.ID,
            'Name': venue.Name,
            'Place': venue.Place,
            'Capacity': venue.Capacity
        }
        return jsonify({'venue':venue_data, 'shows':show_list})
    if request.method =='POST':
        data = request.json
        #print("data",data)
        c, pri, r =None, None, None
        if data['Capacity']:
            c = int(data['Capacity'].strip())
        if data['pos']:
            pri = float(data['pos'])
        if data['Ratings']:
            r = float(data['Ratings'].strip())
        n,img,d= data['Name'],data['imgURL'],data['Description']
        t,dates,v = data['Tags'],data['Dates'],data['venue_id']
        shows = Shows.query.filter_by(venue_id=v)
        Shows.insert_show(n,img,d,r,pri,"[{}]".format(t),"[{}]".format(dates),v,c)
        return jsonify(data)



@app.route("/admin/home", methods=["GET"])
def adminhome():
    v = Venue.query.all()
    #print("v =",v)
    venueid_list = list()
    for venue in v:
        d={
            'ID' : venue.ID,
            'place': venue.Place,
            'imgURL': venue.imgURL,
            'name' : venue.Name,
            'capacity': str(venue.Capacity)
        }
        venueid_list.append(d)
    #print(venueid_list)
    return jsonify(venueid_list)


@app.route('/admin/summary', methods =['GET'])
def summary():
    V = Venue.query.all()
   # print(V)
    vlist =[]
    for v in V:
        d ={
            'ID': v.ID,
            'Name': v.Name
        }
        vlist.append(d)
    return jsonify({'venues' : vlist})



@app.route('/generate_csv/<int:v>', methods=['GET'])
def generate_csv(v):
    try:
        venue = Venue.query.filter_by(ID = v).first()
        #print(venue)
        venue_name = venue.Name
        #print(venue_name)
        s = Shows.query.filter_by(venue_id = v).all()
        data =[]
        #print(s)
        for si in s:
            d = Bookings.query.filter_by(show_id = si.ID).all()
            c = len(d)
            k, m = 0, 0
            for i in d:
                k += i.price
                m += int(i.nos)
            d = {
                'Show ID': si.ID,
                'Show Name': si.Name,
                'Shows Ratings': si.Ratings,
                'Capacity': si.As,
                'Number of tickets booked': m,
                'Number of Bookings done': c,
                'Price per Seat': si.pos,
                'Total earnings': k
                
            }
            data.append(d)
        df = pd.DataFrame(data)
       # print("df = ",df)
        csv_data = df.to_csv(index=False)
        response = Response(csv_data, content_type='text/csv')
        k = "attachment; filename=" + venue_name + "_summary.csv"
       # print(k)
        response.headers['Content-Disposition'] = k

        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/admin/editS/<int:v>/<name>', methods=['PUT'])
def editShow(v,name):
  #  print("name = ",name)
    data = request.json
    #print('Data = ', data)
    As = data['Capacity']
    s=Shows.query.filter_by(venue_id=v).all()
    for i in s:
        if i.Name == name:
            show=i
            break
    ven=Venue.query.filter_by(ID=show.venue_id).first()
    if int(show.As)!=int(As):
        if int(show.As)>int(As):
            k=int(ven.Capacity)+(int(show.As)-int(As))
            ven.Capacity=k
            db.session.commit()
        else:
            k=int(ven.Capacity)-(int(As)-int(show.As))
            ven.Capacity=k
            db.session.commit()
    show.Name=data['Name']
    show.imgURL=data['imgURL']
    show.Description=data['Description']
    show.Ratings = data['Ratings']
    show.pos = data['pos']
    show.Tags = "[{}]".format(data['tage'])
    show.As=data['Capacity']
    show.Allseats = data['Capacity']
    if data['Dates']:
        show.Dates="[{}]".format(data['Dates'])
    db.session.commit()
    return

@app.route('/admin/deleteshow/<int:venueID>/<int:showID>', methods = ['DELETE'])
@jwt_required
def deleteshow(showID, venueID):
    V=Venue.query.filter_by(ID=venueID).first()
    show = Shows.query.filter_by(ID=showID).first()
    V.Capacity=V.Capacity+show.Allseats
    db.session.commit()
    db.session.delete(show)
    db.session.commit()
    return

