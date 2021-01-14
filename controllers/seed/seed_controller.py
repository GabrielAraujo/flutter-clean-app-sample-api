from flask import Blueprint, Response, jsonify, make_response, request
from datetime import datetime, timedelta, timezone
import random
import string
import os
import boto3

seed_controller = Blueprint('seed_controller', __name__)
seed_size = 36
expiration_minutes = int(os.environ['EXPIRATION'])
SEED_TABLE = os.environ['SEED_TABLE']
IS_OFFLINE = os.environ.get('IS_OFFLINE')

if IS_OFFLINE:
  client = boto3.client(
    'dynamodb',
    region_name='localhost',
    endpoint_url='http://localhost:8000'
  )
else:
  client = boto3.client('dynamodb')


@seed_controller.route('', methods=['GET'])
def generate():
  seed = ''.join(random.choice(string.ascii_lowercase + string.digits)
                   for _ in range(seed_size))
  now = datetime.now().replace(tzinfo=timezone.utc)
  expires_at = (now +
                  timedelta(minutes=expiration_minutes)).isoformat()

  try:
    client.put_item(
      TableName=SEED_TABLE,
      Item={
        'seed': {'S': seed},
        'expires_at': {'S': expires_at}
      }
    )

    return make_response(
      jsonify(
        seed=seed,
        expires_at=expires_at
      ),
      200
    )
  except:
    return make_response(
      jsonify(
        message="Something unexpected happened, try again later"
      ),
      500
    )


@seed_controller.route('/validate', methods=['POST'])
def validate():
  seed = request.json['seed']

  try:
    resp = client.get_item(
      TableName=SEED_TABLE,
      Key={'seed': {'S': seed}}
    )

    if 'Item' in resp:
      return make_response(
        jsonify(),
        204
      )

    return make_response(
      jsonify(
        message= "No seed found for this code"
      ),
      404
    )
  except Exception as error:
    print(error)
    return make_response(
      jsonify(
          message="Something unexpected happened, try again later"
      ),
      500
    )
