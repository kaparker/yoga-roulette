import random
import flask

from serve import getvideo

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/results')
def results():

    output = getvideo()

    while len(output) is 0:
        output = getvideo()

    random_int = random.randint(0, len(output)-1)
    random_id = output[random_int]['id']['videoId']

    #print('size', len(output), 'id', random_int, 'videoid', random_id)
    return flask.render_template('results.html', video_id=random_id)


if __name__ == '__main__':
    app.run('localhost', 5000)