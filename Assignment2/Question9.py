import boto3
dynamodb = boto3.resource('dynamodb')
##table = dynamodb.create_table(
##  TableName='Gamer',
##  KeySchema=[
##      {
##          'AttributeName': 'gid',
##         'KeyType': 'HASH'
##        }
##  ],
  ##  AttributeDefinitions=[
    ##    {
    ##      'AttributeName': 'gid',
    ##        'AttributeType': 'N'
    ##  }
    ##],
    ##ProvisionedThroughput={
    ##    'ReadCapacityUnits': 5,
    ##  'WriteCapacityUnits': 5
    ##}
##)
##
# Wait until the table exists.
##table.meta.client.get_waiter('table_exists').wait(TableName='Gamer')

# Print out some data about the table.
##print(table.item_count)
table = dynamodb.Table('Gamer')
table.put_item(
    Item={
        'gid': 2,
        'gname': 'Volley',
        'publisher': 'ubisoft',
        'rating': 25,
        'release_date': '2014',
        'genres':'Action'
    }
)