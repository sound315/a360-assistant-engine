# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Azure DevOps"
PACKAGE_ID          = "command-group:azuredevops"
PACKAGE_DESCRIPTION = "Automates pipeline operations in Azure DevOps, including creating, editing, running, and managing pipelines and pipeline runs. 주요 액션: Connect(Connects to Azure DevOps using OAuth2 an...)、Create pipeline(Creates a new pipeline in the connected...)、Delete pipeline(Deletes a pipeline from the connected pr...)、Disconnect(Disconnects from Azure DevOps and ends t...)、Edit pipeline(Updates an existing pipeline in the acti...) 외 5개."

ACTIONS = [
    {"action": "Connect", "data_item_name": "azuredevops#connect", "description": "Connects to Azure DevOps using OAuth2 and initiates a new session."},
    {"action": "Create pipeline", "data_item_name": "azuredevops#createpipeline", "description": "Creates a new pipeline in the connected Azure DevOps project"},
    {"action": "Delete pipeline", "data_item_name": "azuredevops#deletepipeline", "description": "Deletes a pipeline from the connected project"},
    {"action": "Disconnect", "data_item_name": "azuredevops#disconnect", "description": "Disconnects from Azure DevOps and ends the current session"},
    {"action": "Edit pipeline", "data_item_name": "azuredevops#editpipeline", "description": "Updates an existing pipeline in the active session"},
    {"action": "Get pipeline details", "data_item_name": "azuredevops#getpipelinedetails", "description": "Retrieves the details of a pipeline in the connected project."},
    {"action": "Get pipeline run details", "data_item_name": "azuredevops#getpipelinerundetails", "description": "Retrieves the details of a specific pipeline run."},
    {"action": "List pipeline runs", "data_item_name": "azuredevops#listpipelineruns", "description": "Retrieves a list of runs for a specific pipeline in the connected project."},
    {"action": "List pipelines", "data_item_name": "azuredevops#listpipelines", "description": "Retrieves a list of pipelines in the connected project."},
    {"action": "Run pipeline", "data_item_name": "azuredevops#runpipeline", "description": "Triggers a run of an existing pipeline in the connected project"},
]