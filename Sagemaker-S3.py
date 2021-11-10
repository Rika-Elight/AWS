import boto3
import pandas as pd
s3=boto3.resource('s3')
bucket=s3.Bucket('chrishelawsbucket')
for bucket in s3.buckets.all():
    print(bucket.name)
obj=s3.Bucket('chrishelawsbucket').Object('weather.csv').get()
whether=pd.read_csv(obj['Body'], index_col=0)
s3.Bucket('chrishelawsbucket').download_file(Key='weather.csv', Filename='foo.csv')
pd.read_csv('foo.csv', index_col=0)

