from flask import Flask, render_template
from flask_socketio import SocketIO, join_room

app = Flask(__name__,
            template_folder='template')
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app,cors_allowed_origins="*")

calculations = []

@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('Message was received.')
    

@socketio.on('my event')
def handle_my_event(json, methods=['GET', 'POST']):
    global calculations
    print("Received my event: " + str(json))
    calculations.append(json)
    if len(calculations) > 10:
        calculations = calculations[1:]
        
    resp = {}
    resp['calculation'] = calculations
    socketio.emit('my response', resp, callback=messageReceived)
    
    
@socketio.on('join room')
def handle_join_room(json, methods=['GET', 'POST']):
    print("Received join room event: " + str(json))
    username = json['username']
    join_room('default')
    socketio.emit('joined', json['username'] + ' joined room default', callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
