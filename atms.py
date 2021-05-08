# from source  socketio
from source import create_app

app = create_app(debug=True)

if __name__ == '__main__':
    # socketio.run(app)
    app.run()
