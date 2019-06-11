import boto3
s3=boto3.client('s3')
response = s3.list_object_versions(Bucket='aryabucketformeonly',Prefix='cat.jpeg')
obj= response["Versions"]
print(obj)
print(obj[0])
sorted(obj,key=lambda student: student['LastModified'],reverse=True)
print(obj[1])
Versionid=obj[1]['VersionId']
s3.download_file('aryabucketformeonly', 'cat.jpeg', 'cat.jpeg',ExtraArgs={'VersionId':Versionid})