from gym import app
from flask import render_template, request, jsonify
from gym.daos.dao_branch import DaoBranch
from gym.daos.dao_location import DaoLocation


@app.route('/branch_select',methods=['POST'])
def branch_select():
    bid=request.form.get('bid')
    dao_branch=DaoBranch()
    if bid is None or bid == '':
        all_rows = dao_branch.find_all()
    else:
        all_rows=dao_branch.find_specific_branch(int(bid))
    return jsonify(all_rows)


@app.route('/branch_insert',methods=['POST'])
def branch_insert():
    bid=int(request.form.get('bid'))
    bname=request.form.get('bname')
    email=request.form.get('email')
    phone=request.form.get('phone')
    postcode=request.form.get('postcode')
    dao_branch = DaoBranch()
    dao_location=DaoLocation()
    all_branch=dao_branch.find_all()
    all_location=dao_location.find_all()
    post_list=list()
    bid_list=list()
    for row in all_location:
        post_list.append(row['postcode'])
    for row in all_branch:
        bid_list.append(int(row['bid']))
    if bid in bid_list or postcode not in post_list:
        return jsonify(status=0)
    elif bid not in bid_list and postcode in post_list:
        dao_branch.insert(bid, bname, email, phone, postcode)
        return jsonify(status=1)




@app.route('/branch_delete',methods=['GET'])  #$.getJson is delivered in get way
def branch_delete():
    bid=int(request.args.get('bid'))
    dao_branch = DaoBranch()
    all_rows=dao_branch.find_all()
    status=0
    for row in all_rows:
        if bid==int(row['bid']):
            dao_branch.delete(bid)
            status=1
        else:
            continue
    else:
        return jsonify(status=status)


@app.route('/branch_update',methods=['GET'])
def branch_update():
    bid = int(request.args.get('bid'))
    bname = request.args.get('bname')
    email = request.args.get('email')
    phone = request.args.get('phone')
    postcode = request.args.get('postcode')
    dao_branch = DaoBranch()
    dao_location=DaoLocation()
    all_branch = dao_branch.find_all()
    all_location = dao_location.find_all()
    post_list = list()
    bid_list = list()
    for row in all_location:
        post_list.append(row['postcode'])
    for row in all_branch:
        bid_list.append(int(row['bid']))
    if bid not in bid_list or postcode not in post_list:
        return jsonify(status=0)
    elif bid in bid_list and postcode in post_list:
        dao_branch.update(bname,email,phone,postcode,bid)
        return jsonify(status=1)



















