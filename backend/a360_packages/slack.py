# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Slack"
PACKAGE_ID          = "command-group:slack"
PACKAGE_DESCRIPTION = "Connect to Slack and manage workspaces, channels, and messages. 주요 액션: Connect(Connects to Slack using OAuth2 authentic...)、Disconnect(Disconnects from Slack and ends the acti...)、Get channel ID by name(Retrieves a channel ID for the specified...)、Get channel details(Retrieves detailed information about a S...)、Get conversation details(Retrieves detailed information about a S...) 외 5개."

ACTIONS = [
    {"action": "Connect", "data_item_name": "slack#connect", "description": "Connects to Slack using OAuth2 authentication and initiates a new session."},
    {"action": "Disconnect", "data_item_name": "slack#disconnect", "description": "Disconnects from Slack and ends the active session."},
    {"action": "Get channel ID by name", "data_item_name": "slack#getchannelbyname", "description": "Retrieves a channel ID for the specified channel name."},
    {"action": "Get channel details", "data_item_name": "slack#getchanneldetails", "description": "Retrieves detailed information about a Slack channel."},
    {"action": "Get conversation details", "data_item_name": "slack#getconversationdetails", "description": "Retrieves detailed information about a Slack conversation."},
    {"action": "Get user details", "data_item_name": "slack#getuserdetails", "description": "Retrieves detailed information about a Slack user."},
    {"action": "Get workspace ID by name", "data_item_name": "slack#getworkspacebyname", "description": "Retrieves a workspace ID for the specified workspace name."},
    {"action": "Get workspace details", "data_item_name": "slack#getworkspacedetails", "description": "Retrieves detailed information about a Slack workspace."},
    {"action": "Send channel message", "data_item_name": "slack#sendchannelmessage", "description": "Sends a message to a Slack channel."},
    {"action": "Send direct message", "data_item_name": "slack#senddirectmessage", "description": "Sends a direct message to a Slack user."},
]