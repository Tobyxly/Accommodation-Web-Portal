import csv
import numpy as np
import pymysql
from models import *
from exts import *

def read_db():
    list1=[(0,"")]
    list2=[(0,0,0.0)]
    property = db.session.query(Property).all()
    for property_item in property:
        list1.append((property_item.pro_id,property_item.address))
    results=db.session.query(Orders.order_id,Orders.rating,Orders.tenant,User.user_id).join(User,Orders.tenant==User.username).all()
    for r in results:
        # print(r.order_id,r.rating,r.user_id)
        if r.rating != None:
            list2.append((r.user_id,r.order_id,r.rating))
    list1 = sorted(list1, key=lambda x:x[0])
    list2 = sorted(list2, key=lambda x: (x[0],x[1]))
    return list1, list2


def processing():
    list1 = [(0, "")]
    list2 = [(0, 0, 0.0)]
    property1 = db.session.query(Property).all()
    for property_item in property1:
        list1.append((property_item.pro_id, property_item.address))
    results = db.session.query(Orders.order_id, Orders.rating, Orders.tenant,Orders.property_id,User.user_id).join(User,
                                                                                                 Orders.tenant == User.username).all()
    list_pro=[]
    for r in results:
        # print(r.order_id,r.rating,r.user_id)
        if r.rating != None and (r.user_id,r.property_id) not in list_pro:
            list2.append((r.user_id, r.property_id, r.rating))
            list_pro.append((r.user_id,r.property_id))
    list1 = sorted(list1, key=lambda x: x[0])
    list2 = sorted(list2, key=lambda x: (x[0], x[1]))
    # print(list1)
    # print(list2)
    print("now processing the model")
    dataset=list1
    #dataset = csv.reader(open('./housedata/houses.csv', encoding='utf-8'))
    house = {}
    kk = 0
    for row in dataset:
        if kk == 0:
            kk = kk + 1
            continue
        za = str(row[0])
        zb = row[1]
        house[za] = zb
    dataset=list2
    #dataset = csv.reader(open('./housedata/ratings.csv', encoding='utf-8'))
    nhouse = 0
    nman = 0
    kk = 0
    dicman = {}
    dichouse = {}
    for row in dataset:
        if kk == 0:
            kk = kk + 1
            continue
        if row[0] not in dicman:
            dicman[str(row[0])] = nman
            nman = nman + 1
        if row[1] not in dichouse:
            dichouse[row[1]] = nhouse
            nhouse = nhouse + 1
    rating = [[0 for i in range(nhouse)] for j in range(nman)]

    kk = 0
    #dataset = csv.reader(open('./housedata/ratings.csv', encoding='utf-8'))
    zz = [[] for i in range(nman)]
    for row in dataset:
        if kk == 0:
            kk = kk + 1
            continue
        za = dicman[str(row[0])]
        zb = dichouse[row[1]]
        dd = float(row[2])
        rating[za][zb] = dd
        zz[za].append(zb)
    rating = np.array(rating)
    corr = np.corrcoef(rating, rowvar=0)
    corr = 0.5 + corr * 0.5
    print(corr)
    return zz,dicman,dichouse,nhouse,rating,corr,house



def processing1(input,zz,dicman,dichouse,nhouse,rating,corr,house):
    newman = {v: k for k, v in dicman.items()}
    newhouse = {v: k for k, v in dichouse.items()}
    #print("model completed!,input your id")
    per = str(input)
    # print(dichouse)
    #while int(per) != -100:
    #print(dicman)
    print(dicman)
    person = dicman[per]
    now = {}
    hasrate = []
    for i in range(nhouse):
        s = 0
        if rating[person][i] != 0:
            hasrate.append(i)
        else:
            for j in range(len(zz[person])):
                s = s + rating[person][zz[person][j]] * corr[i][zz[person][j]]
        now[i] = s

    k = sorted(now.items(), key=lambda item: item[1], reverse=True)
    print('person ' + str(per) + ' has rate the house with houseid: ')
    rate_list=[]
    for i in range(len(hasrate)):
        print(newhouse[hasrate[i]], end='  ')
        rate_list.append(newhouse[hasrate[i]])
    print()
    print('The next houses we recommand for him is: ')
    id_list=[]
    name_list=[]
    for i in range(min(10, len(k))):
        #print('id:  ' + newhouse[k[i][0]], '      /////////name:   ' + house[newhouse[k[i][0]]])
        # print('id:  ' + str(newhouse[k[i][0]]))
        # id_list.append(str(newhouse[k[i][0]]))
        if str(newhouse[k[i][0]]) in house:
            print('id:  ' + str(newhouse[k[i][0]]))
            id_list.append(str(newhouse[k[i][0]]))
            print(house[str(newhouse[k[i][0]])])
            name_list.append(house[str(newhouse[k[i][0]])])
    print()
    print("input -100 to finish recommand or input another person id")
    #per = input()
    return rate_list,id_list,name_list


zz,dicman,dichouse,nhouse,rating,corr,house=processing()
#
# print('-------------')

#processing1(4,zz,dicman,dichouse,nhouse,rating,corr,house)


# zz,dicman,dichouse,nhouse,rating,corr,house=processing()
#
# print('-------------')
# processing1(2,zz,dicman,dichouse,nhouse,rating,corr,house)
# list1, list2=read_db()
# print(list2)
#
# print('-------------')
#processing1(3,zz,dicman,dichouse,nhouse,rating,corr,house)