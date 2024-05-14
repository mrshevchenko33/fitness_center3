from flask import Flask

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def get_register():
    if request.method == 'POST':
        return 'new ser register'
    else:
        return 'please sign to registartion'

@app.route('/login', methods=['GET', 'POST'])
def get_login():
    if request.method == 'POST':
        return 'user logged in'
    else:
        return 'please enter your credentials'

@app.route('/user', methods=['GET', 'POST', 'PUT'])
def get_user():
    if request.method == 'POST':
        return 'user data modified'
    elif request.method == 'PUT':
        return 'user info is succes updated'
    else:
        return 'user info'

@app.route('/funds', methods= ['GET', 'POST'])
def get_funds():
    if request.method == 'POST':
        return 'user account was succecfully funded'
    else:
        return 'user deposit value'

@app.route('/fitness_center/<gym_id>/services/', methods=['GET'])
def get_services(gym_id):
    return  f'fitness center {gym_id} services list'

@app.route('/fitness_center/<gym_id>/services/<service_id>', methods=['GET'])
def service_id(gym_id, service_id):
    return  f'fitness center {gym_id} service {service_id} info'

@app.route('/fitness_center/<gym_id>/trainer', methods=['GET'])
def get_trainer(gym_id):
    return  f'fitness center {gym_id} trainers list'

@app.route('/fitness_center/<gym_id>/services/<trainer_id>', methods=['GET'])
def trainer_id(gym_id, trainer_id):
    return  f'fitness center {gym_id} trainer {trainer_id} info'

@app.route('/fitness_center/<gym_id>/trainer/<trainer_id>/rating', methods=['GET','POST', 'PUT'])
def trainer_rating(gym_id, trainer_id):
    if request.method == 'POST':
        return  f'rewiew of {trainer_id} in {gym_id} has been added'
    elif request.method == 'PUT':
        return  f'rewiew of {trainer_id} in {gym_id} has been edited'
    else:
        return f'rating of {trainer_id} in {gym_id}'

@app.route('/user/reservations', methods=['GET', 'POST'])
def user_reservations():
    if request.method == 'GET':
        return 'get user reservations'
    elif request.method == 'POST':
        return 'create user reservation'

@app.route('/user/reservations/<reservation_id>', methods=['GET', 'PUT', 'DELETE'])
def user_reservation(reservation_id):
    if request.method == 'GET':
        return f'get reservation with id {reservation_id}'
    elif request.method == 'PUT':
        return f'update reservation with id {reservation_id}'
    elif request.method == 'DELETE':
        return f'delete reservation with id {reservation_id}'

@app.route('/user/checkout', methods=['GET', 'POST', 'PUT'])
def user_checkout():
    if request.method == 'GET':
        return 'get user checkout information'
    elif request.method == 'POST':
        return 'create user checkout'
    elif request.method == 'PUT':
        return 'update user checkout'

@app.route('/fitness_center', methods=['GET'])
def fitness_centers():
    return 'get all fitness centers'

@app.route('/fitness_center/<id>', methods=['GET'])
def fitness_center(id):
    return f'get fitness center with id {id}'

@app.route('/fitness_center/<id>/loyalty_programs', methods=['GET'])
def loyalty_programs(id):
    return f'get loyalty programs for fitness center with id {id}'

if __name__ == '__main__':
    app.run(debug=True)