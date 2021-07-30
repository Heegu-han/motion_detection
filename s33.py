import boto3
import datetime

s3=boto3.resource('s3')
nowDatetime=datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')
data=open('1.txt','rb')
s3.Bucket('han-cctv').put_object(Key=nowDatetime+'/''1.txt',Body=data,ACL='public-read')
