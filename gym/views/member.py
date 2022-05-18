from gym import app
from flask import request, jsonify
from gym.daos.dao_member import DaoMember
from gym.daos.dao_membership import DaoMemebership
from gym.daos.dao_branch import DaoBranch

@app.route('/member_insert',methods=['POST'])
def member_insert():
    mid=int(request.form.get('mid'))
    username=request.form.get('username')
    password=request.form.get('password')
    phone=request.form.get('phone')
    bid=int(request.form.get('bid'))
    mtype=request.form.get('mtype')
    dao_member=DaoMember()
    dao_membership=DaoMemebership()
    dao_branch=DaoBranch()
    all_member=dao_member.find_all()
    all_membership=dao_membership.find_all()
    all_branch=dao_branch.find_all()
    member_list=list()
    membership_list=list()
    branch_list=list()
    for i in all_member:
        member_list.append(int(i['mid']))
    for i in all_membership:
        membership_list.append(i['mtype'])
    for i in all_branch:
        branch_list.append(int(i['bid']))
    if all((mid not in member_list,mtype in membership_list,bid in branch_list)):
        dao_member.insert(mid,phone,bid,mtype,password,username)
        return jsonify(status=1)
    else:
        return jsonify(status=0)


@app.route('/member_delete',methods=['GET'])
def member_delete():
    mid=int(request.args.get('mid'))
    dao_member = DaoMember()
    all_member = dao_member.find_all()
    for item in all_member:
        if mid==int(item['mid']):
            dao_member.delete(mid)
            return jsonify(status=1)
    else:
        return jsonify(status=0)


@app.route('/member_update',methods=['POST'])
def member_update():
    mid = int(request.form.get('mid'))
    username = request.form.get('username')
    password = request.form.get('password')
    phone = request.form.get('phone')
    bid = int(request.form.get('bid'))
    mtype = request.form.get('mtype')
    dao_member = DaoMember()
    dao_membership = DaoMemebership()
    dao_branch = DaoBranch()
    all_member = dao_member.find_all()
    all_membership = dao_membership.find_all()
    all_branch = dao_branch.find_all()
    member_list = list()
    membership_list = list()
    branch_list = list()
    for i in all_member:
        member_list.append(int(i['mid']))
    for i in all_membership:
        membership_list.append(i['mtype'])
    for i in all_branch:
        branch_list.append(int(i['bid']))
    if all((mid in member_list,bid in branch_list,mtype in membership_list)):
        dao_member.update(mid,phone,bid,mtype,password,username)
        return jsonify(status=1)
    else:
        return jsonify(status=0)


@app.route('/member_select',methods=['GET'])
def member_select():
    mid=request.args.get('mid')
    dao_member = DaoMember()
    if mid=='':
        all_rows=dao_member.find_insurance()
        return jsonify(all_rows=all_rows,status=1)
    else:
        mid_list=list()
        all_member=dao_member.find_all()
        for item in all_member:
            mid_list.append(int(item['mid']))
        if int(mid) in mid_list:
            all_rows=dao_member.find_specific_insurance(int(mid))
            return jsonify(all_rows=all_rows,status=1)
        else:
            return jsonify(status=0)









