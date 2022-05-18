import os
from gym import app
from flask import render_template, request, jsonify
from gym.daos.dao_home import DaoHome
from gym.daos.dao_employee import DaoEmployee
from gym.daos.dao_branch import DaoBranch
from gym.models.model_home import ModelHome


@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    dao_home = DaoHome()
    all_rows = dao_home.find_all()
    home_list = list()
    for row in all_rows:
        home_model = ModelHome(row['id'], row['title'], row['content'], os.path.join(r'..\static\images', row['image']))
        home_list.append(home_model)
    return render_template('/home.html', home_list=home_list)


@app.route('/login', methods=['POST','GET'])
def login():
    username = str(request.form.get('username'))
    password = str(request.form.get('password'))
    if all((username.strip(), password.strip())):
        dao_employee = DaoEmployee()
        all_rows = dao_employee.find_all()
        for item in all_rows:
            if all((username == item['username'], password == item['password'])):
                return jsonify(status=1)
        return jsonify(status=0)
    else:
        return jsonify(status=2)


@app.route('/success', methods=['GET'])
def success():
    username = str(request.args.get("username"))
    return render_template('/login_success.html', username=username)


@app.route('/register_form', methods=['GET'])
def register_form():
    return render_template('/register_form.html')


@app.route('/register', methods=['POST'])
def register():
    eid = request.form.get('eid')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    salary = request.form.get('salary')
    gender = request.form.get('gender')
    mid = request.form.get('mid')
    bid = request.form.get('bid')
    password = request.form.get('password')
    is_internship = request.form.get('employee')  # 1 stands for internship  0 is not
    username = request.form.get('username')
    dao_employee = DaoEmployee()
    dao_branch=DaoBranch()
    all_rows = dao_employee.find_all()
    all_records = dao_branch.find_all()
    bid_list=list()
    mid_list=list()
    for employee in all_rows:
        mid_list.append(int(employee['eid']))
    for branch in all_records:
        bid_list.append(int(branch['bid']))
    for row in all_rows:
        if int(eid) == int(row['eid']):
            return render_template('/register_information.html',url='/register_form',message='the eid has been existed please try again!')
        if int(mid) not in mid_list or int(bid) not in bid_list:
            return  render_template('/register_information.html',url='/register_form',message='please input existed mid or bid, try again!')
    else:
        dao_employee.insert(int(eid), fname, lname, email, phone, int(salary), gender, int(mid), int(bid), password, int(is_internship), username)
        return render_template('/register_information.html',url='/home', message='register success! click here to login')

