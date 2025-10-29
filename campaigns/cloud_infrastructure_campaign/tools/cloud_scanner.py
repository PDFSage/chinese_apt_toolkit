import boto3
import sys

def scan_cloud(profile):
    session = boto3.Session(profile_name=profile)
    s3 = session.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        try:
            s3.get_bucket_acl(Bucket=bucket['Name'])
        except Exception as e:
            if "AccessDenied" in str(e):
                print(f"Bucket {bucket['Name']} is private")
            else:
                print(f"Bucket {bucket['Name']} is public")

def main():
    profile = input("Enter AWS profile: ")
    scan_cloud(profile)

if __name__ == "__main__":
    main()
