from django.views.decorators.csrf import *
from django.shortcuts import *
from django.contrib import messages
from django.http import *
from datetime import date
import time
import datetime
import pymysql
import razorpay



def connection():
    return pymysql.connect(host="localhost", user="root", password="", database="tiffin_service")


def index(request):
    return render(request, "index.html")

def adminDashboard(request):
    return render(request, "adminDashboard.html")

def adminlogout(request):
    del request.session['admin']
    return redirect(adminlogin)


def adminlogin(request):
    if request.method == 'GET':
        return render(request, "adminlogin.html")
    else:
        email = request.POST['email']
        password = request.POST['password']
        q = f"select * from admin where email='{email}' and password='{password}'"
        conn = connection()
        cr = conn.cursor()
        cr.execute(q)
        result = cr.fetchone()
        if result is None:
            return redirect(adminlogin)
        else:
            request.session['admin'] = {'email':email, 'password':password}
            return redirect(adminDashboard)



@csrf_protect
def addadmin(request):
    if 'admin' in request.session:
        if request.method == "POST":
            conn = connection()
            cr = conn.cursor()
            email = request.POST["email"]
            password = request.POST["password"]
            role = request.POST["role"]
            query = "select email from admin where email='"+email+"'"
            cr.execute(query)
            answer = cr.fetchone()
            try:
                if len(answer) > 0:
                    messages.warning(request, "Duplicate email address!")
            except:
                query = "insert into admin values ('"+email+"', '"+password+"', '"+role+"')"
                cr.execute(query)
                conn.commit()
                conn.close()
                messages.success(request, "Admin added successfully.")
        return render(request, "addadmin.html")
    else:
        return redirect(adminlogin)


def viewadmin(request):
    if 'admin' in request.session:
        conn = connection()
        cr = conn.cursor()
        query = "select email, role from admin"
        cr.execute(query)
        answer = cr.fetchall()
        admindetails = []
        for row in answer:
            d = {"email": row[0], "role": row[1]}
            admindetails.append(d)
        return render(request, "viewadmin.html", {"ar": admindetails})
    else:
        return redirect(adminlogin)



def deleteadmin(request):
    if 'admin' in request.session:
        if request.method == "GET":
            conn = connection()
            cr = conn.cursor()
            email = request.GET["selectedvalue"]
            query = "delete from admin where email='"+email+"'"
            cr.execute(query)
            conn.commit()
            conn.close()
            messages.success(request, "Admin deleted successfully.")
            return render(request, "viewadmin.html")
    else:
        return redirect(adminlogin)



@csrf_protect
def editadmin(request):
    if 'admin' in request.session:
        if request.method == "GET":
            conn = connection()
            cr = conn.cursor()
            email = request.GET["selectedvalue"]
            query = "select * from admin where email='"+email+"'"
            cr.execute(query)
            answer = cr.fetchone()
            admindetails = {"email": answer[0], "password": answer[1], "role": answer[2]}
            return render(request, "editadmin.html", {"ar": admindetails})
    else:
        return redirect(adminlogin)



@csrf_protect
def saveadmin(request):
    if request.method == "POST":
        conn = connection()
        cr = conn.cursor()
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]
        query = "update admin set password='"+password+"', role='"+role+"' where email='"+email+"'"
        cr.execute(query)
        conn.commit()
        conn.close()
        messages.success(request, "Admin updated successfully.")
        return redirect('viewadmin')


################################################################################


@csrf_protect
def addarea(request):
    if 'admin' in request.session:
        if request.method == "POST":
            conn = connection()
            cr = conn.cursor()
            aid = request.POST["aid"]
            area = request.POST["area"]
            city = request.POST["city"]
            state = request.POST["state"]
            query = "select area_id from location where area_id='"+aid+"'"
            cr.execute(query)
            answer = cr.fetchone()
            try:
                if len(answer) > 0:
                    messages.warning(request, "Area already exists!")
            except:
                query = "insert into location values('"+aid+"', '"+area+"', '"+city+"', '"+state+"')"
                cr.execute(query)
                conn.commit()
                conn.close()
                messages.success(request, "Area added successfully.")
        return render(request, "addarea.html")
    else:
        return redirect(adminlogin)



def viewarea(request):
    if 'admin' in request.session:
        conn = connection()
        cr = conn.cursor()
        query = "select area_id, area_name, city, state from location"
        cr.execute(query)
        answer = cr.fetchall()
        areadetails = []
        for row in answer:
            d = {"aid": row[0], "areaname": row[1], "city": row[2], "state": row[3]}
            areadetails.append(d)
        return render(request, "viewarea.html", {"ar": areadetails})
    else:
        return redirect(adminlogin)



def deletearea(request):
    if request.method == "GET":
        conn = connection()
        cr = conn.cursor()
        aid = request.GET["selectedvalue"]
        query = "delete from location where area_id='"+aid+"'"
        print(query)
        cr.execute(query)
        conn.commit()
        conn.close()
        messages.success(request, "Area deleted successfully.")
        return redirect(viewarea)


def editarea(request):
    if request.method == "GET":
        conn = connection()
        cr = conn.cursor()
        aid = request.GET["selectedvalue"]
        query = "select * from location where area_id='"+aid+"'"
        cr.execute(query)
        answer = cr.fetchone()
        areadetails = {"aid": answer[0], "areaname": answer[1], "city": answer[2], "state": answer[3]}
        return render(request, "editarea.html", {"ar": areadetails})


@csrf_protect
def savearea(request):
    if request.method == "POST":
        conn = connection()
        cr = conn.cursor()
        aid = request.POST["aid"]
        areaname = request.POST["areaname"]
        city = request.POST["city"]
        state = request.POST["state"]
        query = "update location set area_name='"+areaname+"', city='"+city+"', state='"+state+"' where area_id='"+aid+"' "
        cr.execute(query)
        conn.commit()
        conn.close()
        messages.success(request, "Area updated successfully.")
        return redirect(viewarea)


##################################################################################################


@csrf_protect
def addmenu(request):
    if 'admin' in request.session:
        if request.method == "POST":
            conn = connection()
            cr = conn.cursor()
            mealid = request.POST["mealid"]
            mealtype = request.POST["mealtype"]
            date = request.POST["date"]
            year, month, day = date.split('-')
            day_name = datetime.date(int(year), int(month), int(day))
            dayname = day_name.strftime("%A")
            description = request.POST["description"]
            price = request.POST["price"]
            query = "select meal_id from menu where meal_id='"+mealid+"'"
            cr.execute(query)
            answer = cr.fetchone()
            try:
                if len(answer) > 0:
                    messages.warning(request, "Meal ID already exists!")
            except:
                query = "insert into menu values('"+mealid+"', '"+mealtype+"', '"+date+"', '"+dayname+"', '"+description+"', '"+price+"')"
                cr.execute(query)
                conn.commit()
                conn.close()
                messages.success(request, "Meal added successfully.")
        return render(request, "addmenu.html")
    else:
        return redirect(adminlogin)



def viewmenu(request):
    if 'admin' in request.session:
        conn = connection()
        cr = conn.cursor()
        query = "select meal_id, meal_type, date, description, price from menu"
        cr.execute(query)
        answer = cr.fetchall()
        menudetails = []
        for row in answer:
            d = {"mealid": row[0], "mealtype": row[1], "date": row[2], "description": row[3], "price": row[4]}
            menudetails.append(d)
        return render(request, "viewmenu.html", {"ar": menudetails})
    else:
        return redirect(adminlogin)



def deletemenu(request):
    conn = connection()
    cr = conn.cursor()
    mealid = request.GET["selectedvalue"]
    query = "delete from menu where meal_id='"+mealid+"'"
    cr.execute(query)
    conn.commit()
    conn.close()
    messages.success(request, "Menu deleted successfully.")
    return redirect(viewmenu)


def editmenu(request):
    conn = connection()
    cr = conn.cursor()
    mealid = request.GET["selectedvalue"]
    query = "select meal_id, meal_type, date, description, price from menu where meal_id='"+mealid+"'"
    cr.execute(query)
    answer = cr.fetchone()
    menudetails = {"mealid": answer[0], "mealtype": answer[1], "date": answer[2], "description": answer[3], "price": answer[4]}
    return render(request, "editmenu.html", {"ar": menudetails})


@csrf_protect
def savemenu(request):
    conn = connection()
    cr =conn.cursor()
    mealid = request.POST["mealid"]
    mealtype = request.POST["mealtype"]
    date = request.POST["date"]
    description = request.POST["description"]
    price = request.POST["price"]
    query = "update menu set meal_type='"+mealtype+"', date='"+date+"', description='"+description+"', price='"+price+"' where meal_id='"+mealid+"'"
    cr.execute(query)
    conn.commit()
    conn.close()
    messages.success(request, "Menu updated successfully.")
    return redirect(viewmenu)


##############################################################################################


def usersignup(request):
    if request.method == "POST":
        conn= connection()
        cr = conn.cursor()
        email = request.POST["email"]
        password = request.POST["password"]
        fullname = request.POST["fullname"]
        query = "select email from sign_up where email='"+email+"'"
        cr.execute(query)
        answer = cr.fetchone()
        try:
            if len(answer) > 0:
                messages.warning(request, "Email already exists!")
        except:
            if len(password) >= 8:
                query = "insert into sign_up(email, password, name) values('"+email+"', '"+password+"', '"+fullname+"') "
                cr.execute(query)
                conn.commit()
                conn.close()
                return render(request, "user-personal.html", {"email": email})
            else:
                messages.success(request, "Password should be at least 8 characters long")
    return render(request, "usersignup.html")


def deliveryareas(request):
    conn = connection()
    cr = conn.cursor()
    query = "select area_name, city, state from location"
    cr.execute(query)
    answer = cr.fetchall()
    areadetails = []
    for row in answer:
        d = {"areaname": row[0], "city": row[1], "state": row[2]}
        areadetails.append(d)
    return render(request, "deliveryareas.html", {"ar": areadetails})


def personaldetails(request):
    if request.method == "POST":
        conn = connection()
        cr = conn.cursor()
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        house_no = request.POST["houseno"]
        area = request.POST["area"]
        city = request.POST["city"]
        state = request.POST["state"]
        query = "update sign_up set mobile='"+mobile+"', house_no='"+house_no+"', area='"+area+"', city='"+city+"', state='"+state+"' where email='"+email+"'"
        cr.execute(query)
        print(house_no, area)
        conn.commit()
        conn.close()
        return render(request, "index.html")
    return render(request, "userlogin.html")


def userlogin(request):
    userdata = []
    if request.method == "POST":
        conn = connection()
        cr = conn.cursor()
        email = request.POST["email"]
        password = request.POST["password"]
        query = "select * from sign_up where email='"+email+"' and password='"+password+"'"
        cr.execute(query)
        answer = cr.fetchone()
        try:
            if len(answer) > 0:
                d = {"email": answer[0], "name": answer[2], "mobile": answer[3], "houseno": answer[4], "area": answer[5], "city": answer[6], "state": answer[7]}
                userdata.append(d)
                request.session["user"] = userdata
                if userdata[0]["mobile"] == "":
                    return render(request, "user-personal.html", {"email": email})
                else:
                    return redirect(userdashboard)

        except:
            messages.warning(request, "Invalid email/password")
    # if the user is already logged in, then redirect to dashboard \
    if "user" in request.session:
        return redirect(userdashboard)
    return render(request, "userlogin.html")


def userdashboard(request):
    if "user" in request.session:
        conn = connection()
        cr = conn.cursor()
        lunch = "lunch"
        query = "select date, day, description from menu where meal_type='"+lunch+"'"
        cr.execute(query)
        answer = cr.fetchall()
        lunch_details = []
        for row in answer:
            menu_list = row[2].split(', ')
            d = {"day": row[0], "date": row[1], "description": menu_list}
            lunch_details.append(d)
        dinner = "dinner"
        query1 = "select date, day, description from menu where meal_type='"+dinner+"'"
        cr.execute(query1)
        answer1 = cr.fetchall()
        dinner_details = []
        for row in answer1:
            menu_list = row[2].split(', ')
            d = {"day": row[0], "date": row[1], "description": menu_list}
            dinner_details.append(d)
        return render(request, "userdashboard.html", {"lunch": lunch_details, "dinner": dinner_details})
    else:
        return redirect(userlogin)


def changeuserpassword(request):
    if request.method == "POST":
        conn = connection()
        cr = conn.cursor()
        oldpassword = request.POST["oldpassword"]
        newpassword = request.POST["newpassword"]
        # confirmpassword = request.POST["confirmpassword"]
        user = request.session['user']
        email = user[0]['email']
        query = "select password from sign_up where email='"+email+"'"
        cr.execute(query)
        answer = cr.fetchone()
        try:
            if (oldpassword == answer[0]):
                query = "update sign_up set password='"+newpassword+"' where email='"+email+"'"
                cr.execute(query)
                conn.commit()
                conn.close()
                messages.success(request, "Password updated successfully.")
                return redirect(userdashboard)
        except:
            messages.warning(request, "Invalid password.")
    return render(request, "changeuserpassword.html")


def changeuserdetails(request):
    if request.method == "POST":
        conn = connection()
        cr = conn.cursor()
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        houseno = request.POST["houseno"]
        area = request.POST["area"]
        city = request.POST["city"]
        query = "update sign_up set mobile='"+mobile+"', house_no='"+houseno+"', area='"+area+"', city='"+city+"' where email='"+email+"'"
        cr.execute(query)
        conn.commit()
        conn.close()
        request.session.save()
        return redirect(userdashboard)
    return render(request, "changeuserdetails.html")


def userlogout(request):
    request.session.modified = True
    del request.session["user"]
    return redirect(index)


#########################################################################


def userbooking(request):
    return render(request, "userbooking.html")


def checkout(request):
    if request.method == "POST":
        conn = connection()
        cr = conn.cursor()
        bookfor = request.POST["bookfor"]
        startdate = request.POST["date"]
        # year, month, day = startdate.split('/')
        # day_name = datetime.date(int(year), int(month), int(day))
        # dayname = day_name.strftime("%A")
        mealtype = request.POST["mealtype"]
        houseno = request.POST["houseno"]
        area = request.POST["area"]
        city = request.POST["city"]
        state = request.POST["state"]
        payment = request.POST["paymentoption"]
        query = "select price from menu where meal_type='" + mealtype + "'"
        cr.execute(query)
        answer = cr.fetchone()
        price = answer[0] * 6

        discountprice, tiffincost, billamount = 0, 0, 0

        if bookfor == "one-week":
            discountprice = price - (price * (5/100))       #5% discount
            tiffincost = discountprice + 200                #200 delivery
            billamount = tiffincost + (tiffincost * 5/100)  #5% gst
        else:
            price = price * 4
            discountprice = price - (price * (10 / 100))
            tiffincost = discountprice + 800
            billamount = tiffincost + (tiffincost * 5 / 100)


        # Create RazorPay order
        if payment == "Online":
            client = razorpay.Client(auth=("rzp_test_CY2r3FNtRbPFhE", "rnxE7qw0KIwZg8p0nzFJ9OlA"))

            order_amount = int(billamount)*100
            order_currency = 'INR'
            order_receipt = time.time() # unique receipt id

            order_data = {
                "amount": order_amount,
                "currency": order_currency,
                "receipt": str(order_receipt),
            }
            razorpay_create_response = client.order.create(data=order_data)
            orderid = razorpay_create_response["id"]

            d = {"bookfor": bookfor, "startdate": startdate, "mealtype": mealtype, "paymentoption": payment, "billamount": billamount, "orderid": orderid}
            return render(request, "checkout-new.html", {"ar": d})

        else:
            d = {"bookfor": bookfor, "startdate": startdate, "mealtype": mealtype, "paymentoption": payment, "billamount": billamount}
            return render(request, "cod-new.html", {"ar": d})

    return render(request, "checkout-new.html")


@csrf_exempt
# def paymentAction(request):
#     # return render(request, "index.html")
#     if request.method == "POST":
#
#         conn = connection()
#         cr = conn.cursor()
#         # invoice_date = str(date.today())
#         # email = request.POST["email"]
#         # houseno = request.POST["houseno"]
#         # area = request.POST["area"]
#         # start_date = request.POST["startdate"]
#         # bill_amount = request.POST["billamount"]
#         # query = "insert into customer_order(invoice_date, email, house_no, area, start_date, total_price) values ('"+invoice_date+"', '"+email+"', '"+houseno+"', '"+area+"', '"+start_date+"', '"+bill_amount+"')"
#         # print(query)
#         # cr.execute(query)
#         # conn.commit()
#
#
#         name = request.POST["name"]
#         email = request.POST["email"]
#         houseno = request.POST["houseno"]
#         area = request.POST["area"]
#         city = request.POST["city"]
#         state = request.POST["state"]
#         price = request.POST["billamount"]
#         # aid = request.POST["aid"]
#         # mid = request.POST["mid"]
#         # total = request.POST["total"]
#         date1 = str(date.today())
#         query = f"INSERT INTO `booking`(`invoice_date`, `total_price`, `email`, `address`, `area_id`, `area_name`,`city`, `state`) VALUES ('{date1}','{price}','{email}','{address}','{aid}','{aname}','{city}','{state}')"
#         print(query)
#         cr.execute(query)
#         conn.commit()
#         id = cr.lastrowid
#         # x = request.session['cart']
#         # print(id)
#
#         # for row in x:
#         query = f"INSERT INTO `booking_details`(`delivery_date`, `meal_id`, `price`, `booking_id`) VALUES ('{date1}', '{mid}', '{price}', '{id}')"
#         cr.execute(query)
#         conn.commit()
#         return JsonResponse({'billid': id})
#
#


@csrf_exempt
def paymentsuccess(request):
    conn = connection()
    cr = conn.cursor()

    invoice_date = str(date.today())
    email = request.POST["email"]
    houseno = request.POST["houseno"]
    area = request.POST["area"]
    start_date = request.POST["startdate"]
    bill_amount = request.POST["billamount"]

    query = "insert into customer_order(invoice_date, email, house_no, area, start_date, total_price) values ('" + invoice_date + "', '" + email + "', '" + houseno + "', '" + area + "', '" + start_date + "', '" + bill_amount + "')"
    # print(query)

    cr.execute(query)
    conn.commit()
    order_no = cr.lastrowid
    print(type(order_no))
    order_no = str(order_no)
    meal_type = request.POST['mealtype']
    book_for = request.POST['bookfor']
    query1 = "insert into booking_details(email, order_no, invoice_date, meal_type, meal_duration, start_date, total_price) values ('" + email + "', '" + order_no + "', '"+invoice_date+"', '" + meal_type + "', '" + book_for + "', '" + start_date + "', '" + bill_amount + "')"
    cr.execute(query1)
    conn.commit()
    return render(request, "paymentsuccess.html")


def user_subscription(request):
    if "user" in request.session:
        conn = connection()
        cr = conn.cursor()
        user = request.session['user']
        # print("**************************************************")
        email = user[0]['email']
        query = "select * from booking_details where email='"+email+"' order by order_no desc"
        cr.execute(query)
        answer = cr.fetchall()
        # print(answer)
        booking_list = []
        for row in answer:
            d = {"orderno" : row[2], "invoicedate": row[3], "mealtype" : row[4], "duration" : row[5], "startdate" : row[6], "totalprice" : row[7]}
            booking_list.append(d)
        return render(request, "subscriptions.html", {"ar" : booking_list})
    return redirect(index)


####################################################################################


def aboutus(request):
    return render(request, "aboutus.html")


def whyus(request):
    return render(request, "whyus.html")


def howitworks(request):
    return render(request, "howitworks.html")