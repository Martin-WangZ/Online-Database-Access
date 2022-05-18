from gym import app
from flask import render_template
from gym.daos.dao_home import DaoHome
from gym.models.model_home import ModelHome


@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    dao_home=DaoHome()
    all_rows=dao_home.find_all()
    home_list=list()
    for row in all_rows:
        home_model=ModelHome(row['id'],row['title'],row['content'],row['image'])
        home_list.append(home_model)
    return render_template('/home.html',home_list=home_list)
