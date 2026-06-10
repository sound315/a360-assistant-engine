# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Gmail"
PACKAGE_ID          = "command-group:gmail"
PACKAGE_DESCRIPTION = "Connects to Gmail and manages emails, attachments, and labels. 주요 액션: Change status(Changes the current status of the curren...)、Connect(Connects to Gmail using OAuth2 and initi...)、Delete email(Moves the current email in a Gmail loop...)、Delete all(Moves emails matching the specified filt...)、Disconnect(Terminates the Gmail session.) 외 9개."

ACTIONS = [
    {"action": "Change status", "data_item_name": "gmail#changestatus", "description": "Changes the current status of the current email to read or unread. Use this action within a loop."},
    {"action": "Connect", "data_item_name": "gmail#connect", "description": "Connects to Gmail using OAuth2 and initiates a session."},
    {"action": "Delete email", "data_item_name": "gmail#delete", "description": "Moves the current email in a Gmail loop to Trash."},
    {"action": "Delete all", "data_item_name": "gmail#deleteall", "description": "Moves emails matching the specified filter criteria to Trash."},
    {"action": "Disconnect", "data_item_name": "gmail#disconnect", "description": "Terminates the Gmail session."},
    {"action": "Forward", "data_item_name": "gmail#forward", "description": "Forwards the current email in a Gmail loop to one or more recipients."},
    {"action": "Move email", "data_item_name": "gmail#move", "description": "Moves the current email in a Gmail loop by removing source labels and applying destination labels."},
    {"action": "Move all", "data_item_name": "gmail#moveall", "description": "Moves all emails matching the specified filter criteria from source to destination labels."},
    {"action": "Reply", "data_item_name": "gmail#reply", "description": "Replies to the current email in a Gmail loop."},
    {"action": "Reply all", "data_item_name": "gmail#replyall", "description": "Replies to all recipients of the current email in a Gmail loop."},
    {"action": "Save attachment", "data_item_name": "gmail#saveattachment", "description": "Saves attachments from the current email in a Gmail loop to a folder."},
    {"action": "Save all attachments", "data_item_name": "gmail#saveattachmentall", "description": "Saves attachments from emails matching the specified filter criteria to a folder."},
    {"action": "Save email", "data_item_name": "gmail#saveemail", "description": "Saves the current email in a Gmail loop to a file. Use this action within a loop."},
    {"action": "Send", "data_item_name": "gmail#send", "description": "Sends an email to one or more recipients via Gmail."},
]