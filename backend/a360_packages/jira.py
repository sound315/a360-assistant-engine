# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Jira"
PACKAGE_ID          = "command-group:jira"
PACKAGE_DESCRIPTION = "Jira 웹훅 이벤트가 수신되면 자동화를 시작하는 트리거. 주요 액션: Add comment(Adds comment to the specified issue.)、Connect(Establish a secure session with Jira.)、Create issue(Create a new Jira issue.)、Create project(Create a new Jira project.)、Delete comment(Delete specified comment of issue.) 외 9개."

ACTIONS = [
    {"action": "Add comment", "data_item_name": "jira#addcomment", "description": "Adds comment to the specified issue."},
    {"action": "Connect", "data_item_name": "jira#connect", "description": "Establish a secure session with Jira."},
    {"action": "Create issue", "data_item_name": "jira#createissue", "description": "Create a new Jira issue."},
    {"action": "Create project", "data_item_name": "jira#createproject", "description": "Create a new Jira project."},
    {"action": "Delete comment", "data_item_name": "jira#deletecomment", "description": "Delete specified comment of issue."},
    {"action": "Delete issue", "data_item_name": "jira#deleteissue", "description": "Delete a Jira issue."},
    {"action": "Delete project", "data_item_name": "jira#deleteproject", "description": "Deletes a Jira project and returns the deletion status."},
    {"action": "Disconnect", "data_item_name": "jira#disconnect", "description": "Terminates the Jira session."},
    {"action": "Get comments", "data_item_name": "jira#getcomments", "description": "Retrieves details of the specified comment."},
    {"action": "Get issue", "data_item_name": "jira#getissue", "description": "Retrieves details of the issue."},
    {"action": "Get projects", "data_item_name": "jira#getprojects", "description": "Get Jira projects and return a normalized project list."},
    {"action": "Update comment", "data_item_name": "jira#updatecomment", "description": "Updates details of the specified comment."},
    {"action": "Update issue", "data_item_name": "jira#updateissue", "description": "Update specified issues fields."},
    {"action": "Update project", "data_item_name": "jira#updateproject", "description": "Update specified project fields."},
]