# Start-and-Stop-EC2---Python-script
Code of Python that is used in my Dreametive youtube channel

Below is the code shared:
===========================

import boto3

region = "us-east-1"
target_instance_id = ""  # Place your target instance ID here

# Create an EC2 client
ec2_client = boto3.client('ec2', region_name=region)

def get_instance_state(instance_id):
    try:
        # Describe the instance to get its current state
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        state = response['Reservations'][0]['Instances'][0]['State']['Name']
        return state
    except Exception as e:
        print(f"Error getting instance state: {e}")
        return None

def stop_instance(instance_id):
    try:
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance {instance_id}: {response}")
        ec2_client.get_waiter('instance_stopped').wait(InstanceIds=[instance_id])
        print(f"Instance {instance_id} is now stopped.")
    except Exception as e:
        print(f"Error stopping instance {instance_id}: {e}")

def start_instance(instance_id):
    try:
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Starting instance {instance_id}: {response}")
        ec2_client.get_waiter('instance_running').wait(InstanceIds=[instance_id])
        print(f"Instance {instance_id} is now running.")
    except Exception as e:
        print(f"Error starting instance {instance_id}: {e}")

def manage_instance(instance_id):
    state = get_instance_state(instance_id)
    if state == 'running':
        print(f"Instance {instance_id} is currently running. Stopping it.")
        stop_instance(instance_id)
    elif state == 'stopped':
        print(f"Instance {instance_id} is currently stopped. Starting it.")
        start_instance(instance_id)
    else:
        print(f"Instance {instance_id} is in an unexpected state: {state}")

# Example usage
manage_instance(target_instance_id)


Execution command to run the above script:
===========================================
Python3 <filename>


=> You go Dreamers, Subscribe to My Dreametive Channel Now -> https://www.youtube.com/channel/UCrvCGX4Wop0-Ll_1CMhfJwA
