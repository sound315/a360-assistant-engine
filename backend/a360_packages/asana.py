# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Asana"
PACKAGE_ID          = "command-group:asana"
PACKAGE_DESCRIPTION = "This package enables robust integration with Asana via the Asana v2 API. It delivers comprehensive CRUD (Create, Read, Update, Delete) operations for Tasks, Projects, and Comments (Stories) on both Tasks and Projects. This package is ideal for automating workflows, project management, and collaboration tasks within Asana from Automation Anywhere bots. 주요 액션: Connect(Connects to Asana using an API token or...)、Create comment on task(Creates a comment on a specified Asana t...)、Create project(Creates a new project in Asana with the...)、Create task(Creates a new task in an Asana workspace...)、Delete comment(Deletes a specific comment from an Asana...) 외 9개."

ACTIONS = [
    {"action": "Connect", "data_item_name": "asana#connect", "description": "Connects to Asana using an API token or OAuth connection and initiates a new session."},
    {"action": "Create comment on task", "data_item_name": "asana#createcommentontask", "description": "Creates a comment on a specified Asana task."},
    {"action": "Create project", "data_item_name": "asana#createproject", "description": "Creates a new project in Asana with the specified details."},
    {"action": "Create task", "data_item_name": "asana#createtask", "description": "Creates a new task in an Asana workspace or project."},
    {"action": "Delete comment", "data_item_name": "asana#deletecomment", "description": "Deletes a specific comment from an Asana task."},
    {"action": "Delete project", "data_item_name": "asana#deleteproject", "description": "Deletes a specified project from Asana."},
    {"action": "Delete task", "data_item_name": "asana#deletetask", "description": "Deletes a specified task from Asana."},
    {"action": "Disconnect", "data_item_name": "asana#disconnect", "description": "Disconnects from Asana and terminates the current session."},
    {"action": "Get comment", "data_item_name": "asana#getcomment", "description": "Retrieves a specific comment in Asana task."},
    {"action": "Get project", "data_item_name": "asana#getproject", "description": "Retrieves information about a specific Asana project."},
    {"action": "Get task", "data_item_name": "asana#gettask", "description": ": Retrieves the details of a specific Asana task."},
    {"action": "Update comment", "data_item_name": "asana#updatecomment", "description": "Updates the text of an existing comment on an Asana task."},
    {"action": "Update project", "data_item_name": "asana#updateproject", "description": "Updates the properties of an existing Asana project."},
    {"action": "Update task", "data_item_name": "asana#updatetask", "description": "Updates the properties of an existing Asana task."},
]