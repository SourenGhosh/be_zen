import boto3
import os
import traceback

from configparser import RawConfigParser

config = RawConfigParser()
config.read(os.path.join(settings.BASE_DIR, f'{os.environ.get("ENV")}.ini'))


dynamodb = boto3.client(
    'dynamodb',
    aws_access_key_id=config.get('dynamo_db_local_aws_config', 'access_key_id'),
    aws_secret_access_key=('dynamo_db_local_aws_config', 'secret_access_key'),
    endpoint_url='http://localhost:8000',
    )

def create_table():
    dynamodb.create_table(
        TableName='SubtitleCollection',
        KeySchema=[
            {
                'AttributeName': 'video_id',
                'KeyType': 'HASH' 
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'subtitle',
                'AttributeType': 'RANGE'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        },
        )

def put_subs(video_name, subtitles):
    try:
        dynamodb.put_item(
                TableName='SubtitleCollection',
                Item={"video_id":{"S": video_name}, "subtitle":{"S": subtitles}}
                )
    except:
        traceback.print_exc()


