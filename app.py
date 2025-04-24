from flask import Flask
from ProductionCode import most_banned

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/')
def homepage():
    return "Click here to go to parse_csv."

@app.route('/most_banned/<type>/<num>')
def most_banned(type, num):
    if type == "author":
        most_banned = most_banned.most_banned_authors(int(num))
    elif type == "title":
        most_banned = most_banned.most_banned_titles(int(num))
    elif type == "district":
        most_banned = most_banned.most_banned_districts(int(num))
    elif type == "state":
        most_banned = most_banned.most_banned_states(int(num))

    return most_banned
