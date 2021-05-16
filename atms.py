# Use this to run the website locally
from source import create_app

app = create_app(debug=True)

if __name__ == '__main__':
    app.run()
