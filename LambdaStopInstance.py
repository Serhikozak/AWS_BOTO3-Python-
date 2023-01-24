import boto3

ec2 = boto3.resource('ec2', region_name='eu-central-1')
def lambda_handler(event, context):
    
    instances = ec2.instances.filter(Filters=[{'Name':'instance-state-name', 'Values': ['running']}, {'Name': 'tag:Name', 'Values': ['SKozakov Server']}])
    for instance in instances:
        #try:
            #instance.stop()
        id = instance.id
        ec2.instances.filter(InstanceIds=[id]).stop()
        print("Instance ID is stopped"+instance.id)
            #print(f'{instance} stopped')
        #except:
            #print(f'Error stopping {instance}')
        
    # TODO implement
    return "success"