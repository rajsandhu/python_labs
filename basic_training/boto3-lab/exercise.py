
# this basically a googling exercise for specific documentation

# ----- for me maybe since I haven't done the terraform stuff yet ----
# Write a boto3 script that prints out all EC2 instances
# in your lab account.
# Then for each instance found, attach a new AWS tag


# --- for rest of class ---
# Write a boto3 script that prints out all VPCs and Subnets
# in your lab account.
# Then for each resource found (VPC and subnets), attach a new AWS tag
# Project: Talent-Academy" where tag key is "Project" and tag value is
# "Talent-Academy"

# but it does look like I have VPC stuff running in the Frankfurt 

# --------

# https://stackoverflow.com/questions/43694793/how-to-list-the-name-of-all-aws-subnets-using-boto3

import boto3

client = boto3.client("s3")

response = client.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])

# vpc_client = boto3.client("vpc")
# response = client.list_vpcs()


