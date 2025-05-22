from flask import Flask, jsonify
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-west-2',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN')
)

table = dynamodb.Table('ListTeman')

app = Flask(__name__)

@app.route('/app2')
def index():
    response = table.scan()
    return jsonify(response['Items'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001)
