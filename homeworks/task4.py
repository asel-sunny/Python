# Task 4

# In AWS there is something that is called ARN Format that follows this format:

# arn:partition:service:region:account-id:resource-id

partition = input("Give a partition: ")
service = input("Give a service: ")
region = input("Give a region: ")
account_id = int(input("Give the account ID: "))
resource_id = int(input("Give the resource ID: "))

print("arn",partition,service,region,account_id,resource_id, sep=":")