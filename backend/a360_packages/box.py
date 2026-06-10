# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Box"
PACKAGE_ID          = "command-group:box"
PACKAGE_DESCRIPTION = "Manage files and folders in Box cloud storage. 주요 액션: Connect(Establish a secure OAuth2-based connecti...)、Copy file(Copy a file to a destination folder in B...)、Create folder(Create a new folder in Box.)、Create shared link(Creates a shared link for a file or fold...)、Delete file(Deletes a file in Box.) 외 8개."

ACTIONS = [
    {"action": "Connect", "data_item_name": "box#connect", "description": "Establish a secure OAuth2-based connection to Box."},
    {"action": "Copy file", "data_item_name": "box#copyfile", "description": "Copy a file to a destination folder in Box."},
    {"action": "Create folder", "data_item_name": "box#createfolder", "description": "Create a new folder in Box."},
    {"action": "Create shared link", "data_item_name": "box#createsharedlink", "description": "Creates a shared link for a file or folder."},
    {"action": "Delete file", "data_item_name": "box#deletefile", "description": "Deletes a file in Box."},
    {"action": "Delete folder", "data_item_name": "box#deletefolder", "description": "Deletes a folder in Box."},
    {"action": "Disconnect", "data_item_name": "box#disconnect", "description": "Disconnects the Box session and clears credentials."},
    {"action": "Download file", "data_item_name": "box#downloadfile", "description": "Download a file from Box to the local folder."},
    {"action": "Get folder details", "data_item_name": "box#getfolder", "description": "Retrieve details for a Box folder, including name, creation date, and parent folder."},
    {"action": "List folder items", "data_item_name": "box#listfolderitems", "description": "List all files and folders in a Box folder as a table."},
    {"action": "Move file", "data_item_name": "box#movefile", "description": "Move a file to a destination folder in Box."},
    {"action": "Search file/folder", "data_item_name": "box#search", "description": "Searches a specific file or folder."},
    {"action": "Upload file", "data_item_name": "box#uploadfile", "description": "Upload a file from local device to a Box folder."},
]