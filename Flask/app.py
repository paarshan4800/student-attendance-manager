from flask import Flask, render_template, redirect, request, url_for, jsonify
import cx_Oracle
import json

app = Flask(__name__)
roll_no = 0
faculty_id = 0
var ={} 

app.config['DB_USER'] = ''
app.config['DB_PWD'] = ''
app.config['DB_HOST'] = ''
app.config['DB_DATABASE'] = ''


@app.route('/')
def index():
    return render_template("index.html")

# redirecting to staff or student
@app.route('/user', methods=["POST"])
def user():
    x = request.form["user"]

    if x == "STAFF":
        return render_template("staff.html")
    if x == "STUDENTS":
        return render_template("student.html")


@app.route('/student')
def student():
    return render_template("student_login.html")

# receiving,validating student login
@app.route('/student_login', methods=["POST", "GET"])
def student_login():
    global roll_no
    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()

    roll_no = request.form["roll_no"]
    pass_word = request.form["pass_word"]

    sql = """SELECT roll_no FROM students"""
    cur.execute(sql)
    student_list = [row[0] for row in cur.fetchall()]
    for x in student_list:
        if x == int(roll_no):
            sql = """SELECT pass_word FROM students WHERE roll_no=:xroll_no"""
            cur.execute(sql, ({'xroll_no': roll_no}))
            y = cur.fetchone()

            if pass_word == y[0]:

                cur.callproc("dbms_output.enable")
                cur.callproc('all_att', [roll_no])
                z = []
                textVar = cur.var(str)
                statusVar = cur.var(int)
                while True:
                    cur.callproc("dbms_output.get_line", (textVar, statusVar))
                    if statusVar.getvalue() != 0:
                        break

                    y = textVar.getvalue()
                    x = list(y.split('\t'))
                    for i in x:
                        if '' in x:
                            x.remove('')
                    length = len(x)
                    z = z+x

               # print(z)
               # print(length)
             #   for i in range(len(z)):
                   # print(z[i])

                return render_template("student_welcome.html", length=length, att_list=z, roll_no=roll_no)
    cur.close()
    return render_template("student_login.html", error="Invalid Roll No/Password")


@app.route('/faculty')
def faculty():
    return render_template("faculty_login.html")


@app.route('/faculty_login', methods=["POST"])
def faculty_login():
    global faculty_id
    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()

    faculty_id = request.form["faculty_id"]
    pass_word = request.form["pass_word"]

    cur.execute("""SELECT faculty_id FROM faculty""")
    faculty_list = [row[0] for row in cur.fetchall()]
 #   print("HELOOOOO")
  #  print(faculty_list)
    for x in faculty_list:
        if x == int(faculty_id):
            sql = """SELECT pass_word FROM faculty WHERE faculty_id=:xfaculty_id"""
            cur.execute(sql, ({'xfaculty_id': faculty_id}))
            y = cur.fetchone()

            if pass_word == y[0]:
                conn = cx_Oracle.connect(
                    "doom/doom@localhost/orcl")
                cur = conn.cursor()

                sql = """SELECT c.course_id,c.course_name from teaches t inner join course c on t.course_id=c.course_id and faculty_id = :x_faculty_id"""
                cur.execute(sql, ({'x_faculty_id': faculty_id}))
                faculty_course = cur.fetchall()
             #   print(faculty_course)
                cur.close()
                return render_template("faculty_welcome.html", faculty_id=faculty_id, faculty_course=faculty_course)
    cur.close()
    return render_template("faculty_login.html", error="Invalid Faculty ID/Password")


@app.route('/logout')
def logout():
    return render_template("index.html")


@app.route('/student_details')
def student_details():
    global roll_no
  #  print(roll_no)
    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()

    sql = """SELECT roll_no,first_name,last_name,initials,email_id,to_char(dob,'DD-MM-YYYY'),age from students where roll_no = :x_roll_no"""
    cur.execute(sql, ({'x_roll_no': roll_no}))
    student_info = cur.fetchall()
   # print(student_info)
    return render_template("student_details.html", student_info=student_info)


@app.route('/faculty_details')
def faculty_details():
    global faculty_id

    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()

    sql = """SELECT faculty_id,first_name,last_name,initials,email_id from faculty where faculty_id = :x_faculty_id"""
    cur.execute(sql, ({'x_faculty_id': faculty_id}))
    faculty_info = cur.fetchall()
   # print(faculty_info)
    return render_template("faculty_details.html", faculty_info=faculty_info)


@app.route('/bunk_details', methods=["POST"])
def bunk_details():
    global roll_no
    x = dict(request.form)
    #x =  {"course_id":"CS6106"}

   # print(x['course_id'])
    bunk_course_id = x['course_id']

    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()

    cur.callproc("dbms_output.enable")
    cur.callproc('remain_bunk', [roll_no, bunk_course_id])

    textVar = cur.var(str)
    statusVar = cur.var(int)
    while True:
        cur.callproc("dbms_output.get_line", (textVar, statusVar))
        if statusVar.getvalue() != 0:
            break
        y = textVar.getvalue()

   # print(y)
   # y = json.dumps(y)
    cur.close()
    return {"msg": y}


@app.route('/attendance_shortage')
def attendance_shortage():
    global faculty_id

    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()

    sql = """SELECT c.course_id,c.course_name from teaches t inner join course c on t.course_id=c.course_id and faculty_id = :x_faculty_id"""
    cur.execute(sql, ({'x_faculty_id': faculty_id}))
    faculty_course = cur.fetchall()
    #print(faculty_course)
    cur.close()
    return render_template("faculty_attendance_shortage.html", faculty_id=faculty_id, faculty_course=faculty_course)


@app.route('/attendance_shortage_student_details',methods=["POST"])
def attendance_shortage_student_details():
    global faculty_id
    x = dict(request.form)
    #x =  {"course_id":"CS6106"}

  #  print(x['course_id'])
    bunk_course_id = x['course_id']
   # print(bunk_course_id)
    #print(faculty_id)
    #print(type(bunk_course_id))
    faculty_id=int(faculty_id)
    #print(type(faculty_id))
    
    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()

    cur.callproc("dbms_output.enable")
    cur.callproc('att_shortage', [bunk_course_id, int(faculty_id)])

    z = []
    textVar = cur.var(str)
    statusVar = cur.var(int)
    while True:
        cur.callproc("dbms_output.get_line", (textVar, statusVar))
        if statusVar.getvalue() != 0:
            break

        y = textVar.getvalue()
        print(y)
        x = list(y.split('\t'))
        for i in x:
            if '' in x:
                x.remove('')
            length = len(x)
        z = z+x

        print(z)
    return {"len":length,"list":z}


@app.route('/mark_attendance')
def mark_attendance():
    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()

    sql = """SELECT c.course_id,c.course_name from teaches t inner join course c on t.course_id=c.course_id and faculty_id = :x_faculty_id"""
    cur.execute(sql, ({'x_faculty_id': faculty_id}))
    faculty_course = cur.fetchall()
#   print(faculty_course)
    cur.close()
    return render_template("mark_attendance.html", faculty_id=faculty_id, faculty_course=faculty_course)
    cur.close()

@app.route('/marking_attendance',methods=['POST'])
def marking_attendance():   
    global faculty_id
    global zzz
    global var
    var=request.get_json()
    print(var)
    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()
    print(faculty_id,var['course_id'])
    sql = """select sf.roll_no,s.first_name,s.last_name from student_faculty sf inner join students s on s.roll_no = sf.roll_no and sf.faculty_id = :x_faculty_id and sf.course_id = :x_course_id"""
    cur.execute(sql,{"x_faculty_id":int(faculty_id),"x_course_id": var['course_id'] })
    zzz=cur.fetchall()
    print(zzz)

    return {"values": zzz}

@app.route('/start_mark_attendance')
def start_mark_attendance():
    
    return render_template('start_mark_attendance.html',student_list=zzz,hour=var['hour'])   

@app.route('/insert_attendance',methods=["POST"])
def insert_attendance():
    global faculty_id
    global var
    result=dict(request.form)
    print(result)
    conn = cx_Oracle.connect("{}/{}@{}/{}".format(app.config['DB_USER'],app.config['DB_PWD'],app.config['DB_HOST'],app.config['DB_DATABASE']))
    cur = conn.cursor()
    #print(result['present[]'])
    if 'present[]' in result:
        for i in result['present[]']:
            print (i)
            sql= """insert into attendance_log(roll_no,course_id,faculty_id,hour) values(:1,:2,:3,:4)"""
            x = var['course_id']
            print(x)
            y = int(result['hour'][0])
            print(y)
            print(faculty_id)
            cur.execute(sql,[i,x,faculty_id,y])
    if 'absent[]' in result:
        for i in result['absent[]']:
            print (i)
            sql= """insert into attendance_log(roll_no,course_id,faculty_id,hour) values(:1,:2,:3,:4)"""
            x = var['course_id']
            print(x)
            y = -1*int(result['hour'][0])
            print(y)
            print(faculty_id)
            cur.execute(sql,[i,x,faculty_id,y])
    conn.commit()
    cur.close()
    return {"hello":"Heloooooooooooo"}

if __name__ == "__main__":
    app.run(debug=True)
