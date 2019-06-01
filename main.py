import random
import string

import flask
import googleapiclient.discovery

import config

DEVELOPER_KEY = config.CONFIG['secret_key']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')


def getvideo():

    client = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)

    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(1))
    output = search_list_by_keyword(client,
                                  part='snippet',
                                  maxResults=25,
                                  q=random_string,
                                  channelId='UCFKE7WVJfvaHW5q283SxchA',
                                  type='video',
                                  videoEmbeddable ='true')
    return output


def search_list_by_keyword(client, **kwargs):

  response = client.search().list(
    **kwargs
  ).execute()

  return response.get('items')


@app.route('/results')
def results():

    output = getvideo()

    while len(output) is 0:
        output = getvideo()

    random_int = random.randint(0, len(output)-1)
    random_id = output[random_int]['id']['videoId']

    print('size', len(output), 'id', random_int, 'videoid', random_id)
    return flask.render_template('results.html', video_id=random_id)


if __name__ == '__main__':
    app.run('localhost', 5000)