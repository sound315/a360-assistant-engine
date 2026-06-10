# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Okta"
PACKAGE_ID          = "command-group:okta"
PACKAGE_DESCRIPTION = "Manage Okta users and groups, including provisioning and lifecycle operations. 주요 액션: Activate user(Activates a user in Okta.)、Add user to group(Add a user to a specified group in Okta.)、Connect(Establish a secure session with Okta.)、Create user(Create a new user in Okta.)、Deactivate user(Deactivates a user in Okta.) 외 8개."

ACTIONS = [
    {"action": "Activate user", "data_item_name": "okta#activateuser", "description": "Activates a user in Okta."},
    {"action": "Add user to group", "data_item_name": "okta#addusertogroup", "description": "Add a user to a specified group in Okta."},
    {"action": "Connect", "data_item_name": "okta#connect", "description": "Establish a secure session with Okta."},
    {"action": "Create user", "data_item_name": "okta#createuser", "description": "Create a new user in Okta."},
    {"action": "Deactivate user", "data_item_name": "okta#deactivateuser", "description": "Deactivates a user in Okta."},
    {"action": "Disconnect", "data_item_name": "okta#disconnect", "description": "Terminates the Okta session."},
    {"action": "Get group ID by name", "data_item_name": "okta#getgroupidbyname", "description": "Retrieve details of the group."},
    {"action": "Get user details", "data_item_name": "okta#getuserdetails", "description": "Retrieves detailed information of the user."},
    {"action": "List user groups", "data_item_name": "okta#listusergroups", "description": "Retrieves a list of all group names assigned to a specified user."},
    {"action": "Remove user from group", "data_item_name": "okta#removeuserfromgroup", "description": "Remove a user from a specified group."},
    {"action": "Search groups", "data_item_name": "okta#searchgroups", "description": "Searches for groups matching specified criteria and returns their details."},
    {"action": "Search users", "data_item_name": "okta#searchusers", "description": "Searches for users matching specified criteria and returns their details."},
    {"action": "Update user", "data_item_name": "okta#updateuser", "description": "Updates a user's profile fields in Okta."},
]