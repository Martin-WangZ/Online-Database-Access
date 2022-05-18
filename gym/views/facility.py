from gym import app
from flask import render_template, request, jsonify
from gym.daos.dao_facility import DaoFacility
from gym.daos.dao_employee import DaoEmployee


@app.route('/facility_select',methods=['POST'])
def facility_select():
    fid = request.form.get('fid')
    is_outdoor=request.form.get('is_outdoor')
    dao_facility = DaoFacility()
    if fid == '' and is_outdoor == '':
        all_rows = dao_facility.find_all()
    elif fid!='' and is_outdoor != '':
        all_rows = dao_facility.find_facility(int(fid),int(is_outdoor))
    elif fid!='' and is_outdoor == '':
        all_rows=dao_facility.find_fid(int(fid))
    elif fid=='' and int(is_outdoor)==1:
        all_rows=dao_facility.find_outdoor()
    elif (fid is  None or fid=='') and (int(is_outdoor)==0):
        all_rows = dao_facility.find_indoor()
    return jsonify(all_rows)


@app.route('/facility_insert',methods=['POST'])
def facility_insert():
    fid=int(request.form.get('fid'))
    status_label=request.form.get('status_label')
    manufactory=request.form.get('manufactory')
    manufacture_date=request.form.get('manufacture_date')
    eid=int(request.form.get('eid'))
    is_outdoor=int(request.form.get('is_outdoor'))
    dao_facility=DaoFacility()
    dao_employee=DaoEmployee()
    employee_rows=dao_employee.find_all()
    facility_rows=dao_facility.find_all()
    eid_list=list()
    fid_list=list()
    for e in employee_rows:
        eid_list.append(int(e['eid']))
    for f in facility_rows:
        fid_list.append(int(f['fid']))
    if all((fid not in fid_list, eid in eid_list)):
        dao_facility.insert(fid, status_label, manufactory, manufacture_date, eid, is_outdoor)
        return jsonify(status=1)
    else:
        return jsonify(status=0)



@app.route('/facility_delete',methods=['GET'])  #$.getJson is delivered in get way
def facility_delete():
    fid=int(request.args.get('fid'))
    dao_facility = DaoFacility()
    facility_rows = dao_facility.find_all()
    fid_list = list()
    for f in facility_rows:
        fid_list.append(int(f['fid']))
    if fid in fid_list:
        dao_facility.delete(fid)
        return jsonify(status=1)
    else:
        return jsonify(status=0)



@app.route('/facility_update',methods=['POST'])
def facility_update():
    fid = int(request.form.get('fid'))
    status_label = request.form.get('status_label')
    manufactory = request.form.get('manufactory')
    manufacture_date = request.form.get('manufacture_date')
    eid = int(request.form.get('eid'))
    is_outdoor = int(request.form.get('is_outdoor'))
    dao_facility = DaoFacility()
    dao_employee = DaoEmployee()
    employee_rows = dao_employee.find_all()
    facility_rows = dao_facility.find_all()
    eid_list = list()
    fid_list = list()
    for e in employee_rows:
        eid_list.append(int(e['eid']))
    for f in facility_rows:
        fid_list.append(int(f['fid']))
    if fid in fid_list and eid in eid_list:
        dao_facility.update(status_label, manufactory, manufacture_date, eid, is_outdoor,fid)
        return jsonify(status=1)
    else:
        return jsonify(status=0)

