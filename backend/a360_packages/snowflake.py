# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Snowflake"
PACKAGE_ID          = "command-group:snowflake"
PACKAGE_DESCRIPTION = "Connect to Snowflake and perform CRUD operations on tables, execute SQL statements, and run stored procedures. 주요 액션: Connect(Connects to Snowflake and initiates a ne...)、Insert Row(Inserts one or more rows into a Snowflak...)、Delete rows(Deletes rows from a Snowflake table.)、Disconnect(Disconnect from Snowflake and close the...)、Execute DDL(Runs a DDL statement on Snowflake.) 외 3개."

ACTIONS = [
    {"action": "Connect", "data_item_name": "snowflake#connect", "description": "Connects to Snowflake and initiates a new session for database operations"},
    {"action": "Insert Row", "data_item_name": "snowflake#createrow", "description": "Inserts one or more rows into a Snowflake table using an insert statement."},
    {"action": "Delete rows", "data_item_name": "snowflake#deleterows", "description": "Deletes rows from a Snowflake table."},
    {"action": "Disconnect", "data_item_name": "snowflake#disconnect", "description": "Disconnect from Snowflake and close the session."},
    {"action": "Execute DDL", "data_item_name": "snowflake#executeddl", "description": "Runs a DDL statement on Snowflake."},
    {"action": "Execute stored procedure", "data_item_name": "snowflake#executestoredprocedure", "description": "Runs a Snowflake stored procedure with optional input parameters."},
    {"action": "Select rows", "data_item_name": "snowflake#selectrow", "description": "Executes a select statement and returns matching rows as a data table."},
    {"action": "Update rows", "data_item_name": "snowflake#updaterows", "description": "Updates rows in a Snowflake table"},
]