# -*- coding: utf-8 -*-
PACKAGE_NAME        = "AWS EC2"
PACKAGE_ID          = "command-group:aws ec2"
PACKAGE_DESCRIPTION = "Automate AWS EC2 instance management using the AWS SDK for Java v2. 주요 액션: Connect(Connects to AWS EC2 and initiates a new...)、Describe instances(Retrieves details for one or more EC2 in...)、Disconnect(Ends the session and releases stored AWS...)、Get instance status(Retrieves status for one or more EC2 ins...)、Disable monitoring(Disables detailed CloudWatch monitoring...) 외 4개."

ACTIONS = [
    {"action": "Connect", "data_item_name": "aws ec2#connect", "description": "Connects to AWS EC2 and initiates a new session for instance operations."},
    {"action": "Describe instances", "data_item_name": "aws ec2#describeinstances", "description": "Retrieves details for one or more EC2 instances."},
    {"action": "Disconnect", "data_item_name": "aws ec2#disconnect", "description": "Ends the session and releases stored AWS credentials."},
    {"action": "Get instance status", "data_item_name": "aws ec2#getinstancestatus", "description": "Retrieves status for one or more EC2 instances."},
    {"action": "Disable monitoring", "data_item_name": "aws ec2#monitorinstancesdisable", "description": "Disables detailed CloudWatch monitoring for one or more EC2 instances."},
    {"action": "Enable monitoring", "data_item_name": "aws ec2#monitorinstancesenable", "description": "Enables detailed CloudWatch monitoring for one or more EC2 instances."},
    {"action": "Start instances", "data_item_name": "aws ec2#startinstance", "description": "Starts one or more EC2 instances."},
    {"action": "Stop instances", "data_item_name": "aws ec2#stopinstance", "description": "Stops one or more running EC2 instances without deleting them."},
    {"action": "Terminate instances", "data_item_name": "aws ec2#terminateinstance", "description": "Permanently deletes one or more EC2 instances."},
]