# -*- coding: UTF-8 -*-
import pymysql
from flask import Flask, render_template,request,jsonify,session
from models import *
import datetime
from exts import *
from flask_cors import CORS
from PIL import Image
import os
from recommendation import *





app = Flask(__name__)

CORS(app)


@app.route('/register',methods=['POST','GET'])
def register():
    username =request.json.get('username')
    password =request.json.get('password')
    email = request.json.get('email')
    phone = request.json.get('phone')
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    gender=request.json.get('gender')
    user_obj = User(username=username,password=password,email=email,phone=phone,
                first_name=firstName,last_name=lastName,gender=gender,profile=' ',hobby=' ')
    print(user_obj .password,user_obj .username,user_obj .email,user_obj .profile,user_obj .hobby)

    username_obj = User.query.filter_by(username=username).first()
    if username_obj:
        return jsonify({"message":"The username is already exist!","code":400})
    if phone.isdigit():
        if len(phone) == 10:
            pass
        else:
            return jsonify({"message":"please enter correct phone number！","code":400})
    else:
        return jsonify({"message": "please enter correct phone number！","code":400})

    email_obj = User.query.filter_by(email=email).first()
    if email_obj:
        return jsonify({"message":"The email is already exist!","code":400})
    db.session.add(user_obj)
    db.session.commit()
    return jsonify({"message":"Registered successfully!","code":200})


@app.route('/login',methods=['GET','POST'])
def login():
    username =request.json.get('username')
    password =request.json.get('password')
    username_obj = User.query.filter_by(username = username).first()
    password_obj = User.query.filter_by(password = password).first()


    if username_obj and password_obj:
        return jsonify({"message":"Login successful！","code":200,"username":username_obj.username})

    else:
        return jsonify({"message":"Username or password is incorrect!","code":400})

#
#
@app.route('/release',methods=['GET','POST'])
def newhouse():
    if request.method == 'GET':
        # username = session.get('username')
        username = session['username']
        print('newhouse get and username is '+ username)
    else:

        owner = request.json.get('owner')
        address = request.json.get('address')
        description = request.json.get('desc')
        bathroom = int(request.json.get('num_bathroom'))
        bedroom = int(request.json.get('num_bedroom'))
        parking = int(request.json.get('num_parking'))
        pets = int(request.json.get('pets'))
        wifi = int(request.json.get('wifi'))
        fitness = int(request.json.get('fitness'))
        property_type = request.json.get('property_type')
        price = float(request.json.get('price'))
        seletedoptions = request.json.get('selectedOptions')
        state = seletedoptions[0]
        city = seletedoptions[1]
        start_date = request.json.get('start_date')
        end_date = request.json.get('end_date')
        img_name = request.json.get('img_name')
        img_path = 'src/assets/property_img/' + img_name
        newhouse = Property(property_type=property_type,state=state,
                            city =city,address=address,owner=owner,
                            bedroom=bedroom,bathroom=bathroom,pets=pets,
                            wifi=wifi,fitness=fitness,parking = parking,
                            img_url = img_path
                            )
        db.session.add(newhouse)
        db.session.commit()
        property_id = newhouse.pro_id
        order = Orders(start_date=start_date,
                      end_date=end_date,
                      description=description,
                      owner=owner,
                      property_id=property_id,
                      price = price
                      )
        db.session.add(order)
        db.session.commit()
        return jsonify({"message": "Post new house successfully!", "code": 200})

@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    if request.method == 'GET':
        username = username
        user = User.query.filter(User.username == username).first()
        hobby = user.hobby
        first_name = user.first_name
        last_name = user.last_name
        gender = user.gender
        phone = user.phone
        email = user.email
        data = {"hobby":hobby,"first_name":first_name,"last_name":last_name,
                   "gender":gender,"email":email,"phone":phone}
        return jsonify({"data":data})
    else:
        username = username
        first_name = request.json.get('firstName')
        last_name = request.json.get('lastName')
        gender = request.json.get('gender')
        phone = request.json.get('phone')
        email = request.json.get('email')
        hobby = request.json.get('hobby')
        print({"first_name":first_name,"last_name":last_name})
        message = profile_validate(first_name, last_name, email, phone)
        if 'Successfully' in message:
            db.session.query(User).filter_by(username=username). \
                update({User.first_name: first_name, \
                        User.last_name: last_name, \
                        User.hobby: hobby, \
                        User.gender: gender, \
                        User.email: email, \
                        User.phone: phone})
            db.session.commit()
            return jsonify({"message": message, "code": 200})
        else:
            return jsonify({"message": message, "code": 400})


@app.route('/change_password/<username>',methods=['GET','POST'])
def change_password(username):
    username = username
    password = request.json.get('confirmedPassword')

    if len(password) < 6:
        return jsonify({"message":'password cannnot shorter than 6',"code":400})
    elif len(password) > 20:
        return jsonify({"message":'password cannot longer than 20',"code":400})
    else:
        db.session.query(User).filter_by(username=username).update({User.password: password})
        db.session.commit()
        return jsonify({"message":"Successfully Reset Password","code":200})



# @app.route('/properties',methods=['GET'])
# def get_all_order():
#     property_item = []
#     property = db.session.query(Property).all()
#     # print(property)
#     for pro_item in property:
#         # print(pro_item.pro_id)
#         order = Orders.query.filter(Orders.property_id==pro_item.pro_id).first()
#         item={"img_url": pro_item.img_url,
#                   # "src/assets/property_img/"+ str(pro_item.pro_id) + ".jpg",
#               "address":pro_item.address,
#               "state": pro_item.state,
#               "city":pro_item.city,
#               "price":order.price,
#               "bedroom":pro_item.bedroom,
#               "bathroom":pro_item.bathroom,
#               "parking": pro_item.parking,
#               "order_id": order.order_id
#               }
#         property_item.append(item)
#     return jsonify({"property_item": property_item, "code": 200})

@app.route('/properties',methods=['POST','GET'])
def get_all_order():
    property_item = []

    property = db.session.query(Property).all()
    # username = request.json.get('username')
    # user_obj = User.query.filter(User.username == username).first()
    # print(username)


    for pro_item in property:
        # print(pro_item.pro_id)
        order = Orders.query.filter(Orders.property_id==pro_item.pro_id).all()
        for e in order:

            status1 = ''
            if e.status == 0:
                status1 = 'Availble'
            elif e.status == 1:
                status1 = 'Booked'
            item={"img_url": pro_item.img_url,
                      # "src/assets/property_img/"+ str(pro_item.pro_id) + ".jpg",
                  "address":pro_item.address,
                  "state": pro_item.state,
                  "city":pro_item.city,
                  "price":e.price,
                  "bedroom":pro_item.bedroom,
                  "bathroom":pro_item.bathroom,
                  "parking": pro_item.parking,
                  "order_id": e.order_id,
                  "status":status1
                  }
            if e.status == 0:
                property_item.append(item)
    return jsonify({"property_item": property_item})


@app.route('/recommend',methods=['POST','GET'])
def get_recommend_order():
    recommend_item=[]
    property = db.session.query(Property).all()
    username = request.json.get('username')
    if username:
        user_obj = User.query.filter(User.username == username).first()
        zz, dicman, dichouse, nhouse, rating, corr, house = processing()
        rate_list, id_list, name_list=processing1(user_obj.user_id, zz, dicman, dichouse, nhouse, rating, corr, house)
        for pro_item in property:
            # print(pro_item.pro_id)
            order = Orders.query.filter(Orders.property_id==pro_item.pro_id).all()
            for e in order:

                status1 = ''
                if e.status == 0:
                    status1 = 'Availble'
                elif e.status == 1:
                    status1 = 'Booked'
                item={"img_url": pro_item.img_url,
                          # "src/assets/property_img/"+ str(pro_item.pro_id) + ".jpg",
                      "address":pro_item.address,
                      "state": pro_item.state,
                      "city":pro_item.city,
                      "price":e.price,
                      "bedroom":pro_item.bedroom,
                      "bathroom":pro_item.bathroom,
                      "parking": pro_item.parking,
                      "order_id": e.order_id,
                      "status":status1
                      }
                if str(pro_item.pro_id) in id_list[:3] and e.status == 0:
                    recommend_item.append(item)
    else:
        sorted_property = db.session.query(Orders.property_id, func.avg(Orders.rating)).group_by(Orders.property_id).all()
        sorted_property = sorted(sorted_property,key=lambda x:(x[1],x[0]),reverse=True)
        high_rating_id = sorted_property[:3]
        print(high_rating_id)
        for item2 in high_rating_id:
            for pro_item in property:
                # print(pro_item.pro_id)
                order = Orders.query.filter(Orders.property_id == pro_item.pro_id).all()
                for e in order:

                    status1 = ''
                    if e.status == 0:
                        status1 = 'Availble'
                    elif e.status == 1:
                        status1 = 'Booked'
                    item = {"img_url": pro_item.img_url,
                            # "src/assets/property_img/"+ str(pro_item.pro_id) + ".jpg",
                            "address": pro_item.address,
                            "state": pro_item.state,
                            "city": pro_item.city,
                            "price": e.price,
                            "bedroom": pro_item.bedroom,
                            "bathroom": pro_item.bathroom,
                            "parking": pro_item.parking,
                            "order_id": e.order_id,
                            "status": status1
                            }
                    if item2[0] == pro_item.pro_id and e.status == 0:
                        recommend_item.append(item)


    return jsonify({"recommend_item":recommend_item,"code": 200})









@app.route('/search', methods=['POST'])
def search():
    state = request.json.get('state')
    city = request.json.get('city')
    address = request.json.get('address')
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    pets = request.json.get('pets')
    wifi = request.json.get('wifi')
    fitness = request.json.get('fitness')
    bedroom = request.json.get('num_bedroom')
    bathroom = request.json.get('num_bathroom')
    parking = request.json.get('num_parking')
    property_type = request.json.get('type')

    results = db.session.query(Property.address, Orders.status,Orders.price,Orders.order_id,Property.img_url,Property.bathroom,Property.bedroom,Property.parking,Property.state,Property.city). \
        join(Orders, Orders.property_id == Property.pro_id). \
        filter(Property.state == state,
               Property.city == city,
               Property.bedroom >= bedroom,
               Property.bathroom >= bathroom,
               Property.parking >= parking,
               Property.address.contains(address) if address is not None else "",
               Property.pets ==1 if pets is not False else "",
               Property.wifi ==1 if wifi is not False else "",
               Property.fitness ==1 if fitness is not False else "",
               Property.property_type ==property_type if property_type is not None else "",
               Orders.start_date <= start_date if start_date !="" else "",
               Orders.end_date >= end_date if start_date !="" else ""
               ).distinct().all()
    property_item = []
    status = ''
    for r in results:
        if r.status == 1:
            status = 'Booked'
        elif r.status == 0:
            status = 'Availble'
        item = {"address": r.address,
                "price": r.price,
                "img_url": r.img_url,
                "bathromm": r.bathroom,
                "bedroom": r.bedroom,
                "parking": r.parking,
                "state": r.state,
                "city": r.city,
                "order_id":r.order_id,
                "status": status
                }
        if r.status == 0:
            property_item.append(item)
    print(property_item)
    if property_item:
        return jsonify({"property_item": property_item})
    else:
        return jsonify({"messga": "no reasonable results", "code": 200})




@app.route("/upload", methods=['post', 'get'])
def upload():
    f = request.files['file']
    print(f.filename)
    f.save(f.filename)

    image_file = Image.open(f.filename)  # open colour image
    # image_file = image_file.convert('1')  # convert image to black and white
    # w, h = image_file.size
    # print(w,h)
    out_img = image_file.resize((245,165))
    path = '/Users/xiongluyuan/Desktop/group_vue/src/assets/property_img/'
    out_img.save(path+f.filename)
    filepath = path + '/' + f.filename
    return filepath

@app.route("/delete_img",methods=['POST'])
def delete_img():
    filename = request.json.get('filename')
    my_file = '/Users/xiongluyuan/Desktop/group_vue/src/assets/property_img/'+filename
    if os.path.exists(my_file):
        os.remove(my_file)
        return jsonify({"code":200})
    else:
        return jsonify({"code":400})

@app.route("/detail",methods=['GET','POST'])
def detail():
    order_id = request.args.get('order_id')
    result = db.session.query(Property.owner,Property.state, Property.city, Property.address, Orders.price, Orders.property_id,
                              Property.fitness,Orders.description,Property.img_url, Property.bathroom, Property \
                               .bedroom, Property.pets,Property.wifi,Property.parking,Orders.start_date,Orders.end_date). \
        join(Orders, Orders.property_id == Property.pro_id). \
        filter(Orders.order_id == order_id)
    item = {}
    for r in result:
        if r.pets == 0:
            pets = "Not allowed"
        else:
            pets = "Allowed"
        if r.fitness == 0:
            fitness = "No fitness"
        else:
            fitness = "Have free fitness"
        if r.wifi == 0:
            wifi = "No wifi"
        else:
            wifi = "Have free wifi"
        item = {"address": r.address,
                "price": r.price,
                "img_url": r.img_url,
                "bathroom": r.bathroom,
                "bedroom": r.bedroom,
                "parking": r.parking,
                "state": r.state,
                "city": r.city,
                "desc":r.description,
                "pets": pets,
                "fitness": fitness,
                "wifi": wifi,
                "start_date": r.start_date,
                "end_date": r.end_date,
                "owner":r.owner
                }
    return jsonify({"property_item":item})


# @app.route("/new_order",methods=['POST','GET'])
# def new_order():
#     tenant_name = request.json.get('username')
#     order_id = int(request.json.get('order_id'))
#     result = db.session.query(Orders).filter_by(order_id=order_id).first()
#     print(result.tenant)
#     if result.tenant is not None:
#         return jsonify({"message": "This property was already booked!"})
#     elif result.owner == tenant_name:
#         return jsonify({"message":"You can not book your own property"})
#     else:
#         db.session.query(Orders).filter_by(order_id=order_id).update({Orders.tenant: tenant_name,Orders.status:1})
#         db.session.commit()
#         return jsonify({"message":"Booking successfully!"})

@app.route("/new_order",methods=['POST','GET'])
def new_order():
    tenant_name = request.json.get('username')
    order_id = int(request.json.get('order_id'))
    start = request.json.get('start_date_user')
    end = request.json.get('end_date_user')
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    start = start.date()
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    end = end.date()
    # divide the order
    order = Orders.query.filter(Orders.order_id == order_id).first()
    if (order.start_date >start or order.end_date < end or end <= start):
        return jsonify({"message": "Please select appropriate date","code":400})
    elif order.tenant is not None:
        return jsonify({"message": "This property was already booked!","code":400})
    elif order.owner == tenant_name:
        return jsonify({"message":"You can not book your own property","code":400})
    else:
        status = order.status
        price = order.price
        start_date = order.start_date
        end_date = order.end_date
        description = order.description
        tenant = order.tenant
        owner = order.owner
        property_id = order.property_id
        ord_date = order.ord_date
        rating = order.rating
        review = order.review
        # renew order
        tenant = tenant_name
        status = 1
        db.session.query(Orders).filter_by(
            order_id = order_id). \
            update({Orders.tenant: tenant,
                    Orders.status: status,
                    Orders.start_date: start,
                    Orders.end_date: end
                    })
        db.session.commit()

        if start > start_date:
            # add a new (start_date,start)
            order1 = Orders(start_date=start_date,
                           end_date=start,
                           description=description,
                           owner=owner,
                           property_id=property_id,
                           price=price,
                           rating=rating
                           )
            db.session.add(order1)
            db.session.commit()
        if end < end_date:
            # add a new(end,end_date)
            order2 = Orders(start_date=end,
                           end_date=end_date,
                           description=description,
                           owner=owner,
                           property_id=property_id,
                           price=price,
                           rating=rating
                           )
            db.session.add(order2)
            db.session.commit()
    return jsonify({"message": "Booking successfully!", "code": 200})
    # print(order.order_id)
    # print(order_id)


@app.route('/my_order', methods=['GET','POST'])
def my_order():
    order_item1 = []
    username = request.json.get('username')
    tenant = username
    order_1 = db.session.query(Property.state, Property.city, Property.address, Orders.price,Orders.start_date,Orders.end_date,Orders.order_id,Orders.owner). \
        join(Orders, Orders.property_id == Property.pro_id). \
        filter(Orders.tenant == username)
    for o in order_1:
        item = {
            "order_id": o.order_id,
            "state": o.state,
            "city": o.city,
            "address": o.address,
            "price": o.price,
            "start_date": o.start_date,
            "end_date": o.end_date,
            "owner": o.owner,
        }
        order_item1.append(item)
    print(order_item1)
    return jsonify({"order_item": order_item1, "code": 200})

@app.route('/my_house', methods=['GET','POST'])
def my_house():
    house_item = []
    username = request.json.get('username')
    house = db.session.query(Property.state, Property.city, Property.property_type,Property.address, Orders.price, Orders.start_date,
                               Orders.end_date,Orders.status,Orders.order_id, Orders.owner). \
        join(Orders, Orders.property_id == Property.pro_id). \
        filter(Orders.owner == username)
    for o in house:
        if o.status == 0:
            status = 'Has not been rented'
        else:
            status = 'Has been rented'
        item = {
            "order_id": o.order_id,
            "state_city": o.state+'/'+o.city,
            "address": o.address,
            "price": o.price,
            "type" : o.property_type,
            "start_date": o.start_date,
            "end_date": o.end_date,
            "status": status
        }
        house_item.append(item)
    return jsonify({"house_item": house_item, "code": 200})


@app.route('/delete_order', methods=['GET','POST'])
def delete_order():
    order_id = request.json.get('order_id')
    print(order_id)
    order_obj = Orders.query.filter_by(order_id=order_id).first()
    print(order_obj.status)
    if order_obj.status != 0:
        return jsonify({"message": "This order was already booked, you can not delete it now!"})
    else:
        db.session.delete(order_obj)
        db.session.commit()
        return jsonify({"message": "Delete order successfully!"})

@app.route('/new_review', methods=['GET','POST'])
def new_review():
    username = request.json.get('username')
    order_id = request.json.get('order_id')
    review = request.json.get('review')
    rating = request.json.get('rating')
    # print("--------------------")
    # print(username,order_id,review,rating)
    order_obj=Orders.query.filter_by(order_id=order_id).first()
    if order_obj.rating is not None:
        return jsonify({"message": "This order was already reviewed, you can not review it now!"})
    else:
        db.session.query(Orders).filter_by(order_id=order_id).update({Orders.review: review, Orders.rating: rating})
        db.session.commit()
        return jsonify({"message": "Review order successfully!"})





if __name__ == '__main__':
    app.run()
