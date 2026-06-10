# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Databricks"
PACKAGE_ID          = "command-group:databricks"
PACKAGE_DESCRIPTION = "Manage Databricks clusters, notebooks, jobs, and DBFS files. 주요 액션: Cancel job run(Cancels an active job run.)、Cancel SQL statement(Cancels a running SQL query.)、Connect(Connects to Databricks workspace and cre...)、Delete file(Delete a file from the Databricks Unity...)、Disconnect(Disconnects from Databricks and ends the...) 외 8개."

ACTIONS = [
    {"action": "Cancel job run", "data_item_name": "databricks#canceljobrun", "description": "Cancels an active job run."},
    {"action": "Cancel SQL statement", "data_item_name": "databricks#cancelsqlstatement", "description": "Cancels a running SQL query."},
    {"action": "Connect", "data_item_name": "databricks#connect", "description": "Connects to Databricks workspace and creates a session."},
    {"action": "Delete file", "data_item_name": "databricks#deletefile", "description": "Delete a file from the Databricks Unity Catalog."},
    {"action": "Disconnect", "data_item_name": "databricks#disconnect", "description": "Disconnects from Databricks and ends the active session."},
    {"action": "Download file", "data_item_name": "databricks#downloadfile", "description": "Downloads a file from the Databricks Unity Catalog."},
    {"action": "Execute SQL statement", "data_item_name": "databricks#executesqlstatement", "description": "Executes a SQL query on a Databricks warehouse."},
    {"action": "Get job run output", "data_item_name": "databricks#getjobrunoutput", "description": "Retrieves the output of a Databricks job run."},
    {"action": "Get job run status", "data_item_name": "databricks#getjobrunstatus", "description": "Retrieves the status of an active job run."},
    {"action": "Get SQL statement result", "data_item_name": "databricks#getsqlstatementresult", "description": "Retrieves the result of an executed SQL query."},
    {"action": "List jobs", "data_item_name": "databricks#listjobs", "description": "Lists Databricks jobs in a datatable."},
    {"action": "Run job", "data_item_name": "databricks#runjob", "description": "Runs a Databricks job."},
    {"action": "Upload file", "data_item_name": "databricks#uploadfile", "description": "Uploads a file to the Databricks Unity Catalog."},
]