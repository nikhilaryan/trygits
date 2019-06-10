import boto3
dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key, Attr
table = dynamodb.Table('Gamer')
response = table.query(
    KeyConditionExpression=Key('gid').eq(2)
)
Items= response['Items']
print(Items)
gname = Items[0]['gname']
rating = Items[0]['rating']
print(gname)
print(rating)