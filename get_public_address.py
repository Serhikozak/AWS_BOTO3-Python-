import boto3
import os
from dotenv import load_dotenv

load_dotenv()

client = boto3.client('ec2')
#response = client.start_instances(InstanceIds=[id])
response = client.start_instances(InstanceIds=[os.environ.get('id_ec2')])
waiter = client.get_waiter('instance_status_ok')
waiter.wait(InstanceIds=[os.environ.get('id_ec2')]) 
    # WaiterConfig={
    #     'Delay': 123,
    #     'MaxAttempts': 123
    #})

Public_Ip = client.describe_instances(InstanceIds=[os.environ.get('id_ec2')])
for r in Public_Ip['Reservations']:
  for i in r['Instances']:
    #public_ip=i['PublicIpAdrress'] #might useless
    #print(public_ip)
    print (i['PublicIpAddress'])
    



