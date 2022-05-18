from gym import app
from flask import render_template, request, jsonify
from gym.daos.dao_employee import DaoEmployee


@app.route('/employee_select', methods=['POST'])
def employee_select():
    eid = request.form.get('eid')
    dao_employee = DaoEmployee()
    if eid is None or eid == '':
        all_rows = dao_employee.find_all()
    else:
        all_rows = dao_employee.find_employee(int(eid))
    return jsonify(all_rows)


@app.route('/employee_delete', methods=['GET'])
def employee_delete():
    eid=int(request.args.get('eid'))
    dao_employee = DaoEmployee()
    all_rows=dao_employee.find_all()
    status=0
    for row in all_rows:
        if eid==int(row['eid']):
            dao_employee.delete(eid)
            status=1
            break
        else:
            continue
    else:
        status=0

    return jsonify(status=status)


@app.route('/employee_update', methods=['GET'])
def employee_update():
    eid=int(request.args.get('eid'))
    username=request.args.get('username')
    email=request.args.get('email')
    phone=request.args.get('phone')
    salary=int(request.args.get('salary'))
    is_internship=int(request.args.get('is_internship'))
    password=request.args.get('password')
    dao_employee = DaoEmployee()
    all_rows = dao_employee.find_all()
    for row in all_rows:
        if eid==int(row['eid']):
            dao_employee.update(email,phone,salary,password,is_internship,username,eid)
            status=1
            break
        else:
            continue
    else:
        status=0

    return jsonify(status=status)


