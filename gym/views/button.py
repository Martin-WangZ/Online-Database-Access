from gym import app
from flask import render_template, request, jsonify


@app.route('/branch',methods=['GET'])
def branch():
    username=request.args.get('username')
    return render_template('/branch.html',username=username)


@app.route('/employee',methods=['GET'])
def employee():
    username=request.args.get('username')
    return render_template('/employee.html',username=username)


@app.route('/facility',methods=['GET'])
def facility():
    username=request.args.get('username')
    return render_template('/facility.html',username=username)


@app.route('/member',methods=['GET'])
def member():
    username=request.args.get('username')
    return render_template('/member.html',username=username)


@app.route('/private_coach',methods=['GET'])
def private_coach():
    username=request.args.get('username')
    return render_template('/private_coach.html',username=username)


@app.route('/section',methods=['GET'])
def section():
    username=request.args.get('username')
    return render_template('/section.html',username=username)


