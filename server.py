import os
from livekit import api
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/getToken/<identity>')
def getToken(identity):
  token = api.AccessToken('APIB2ngu74MJ9CX', 'oLBc45bnC8Kz7AyfXtQezSJOgJgLsZm8fPn06frfZ7KH') \
    .with_identity(identity) \
    .with_name(identity) \
    .with_ttl(datetime.timedelta(hours=6)) \
    .with_grants(api.VideoGrants(
        room_join=True,
        room="my-room",
    ))
  return token.to_jwt()

if __name__ == '__main__':
   app.run(port=5000)

# flask --app server run --bind 0.0.0.0