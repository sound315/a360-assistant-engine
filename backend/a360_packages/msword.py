# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Word"
PACKAGE_ID          = "command-group:msword"
PACKAGE_DESCRIPTION = "This adapter enables Java-based automation of Microsoft Word documents on Windows using the jacob library, which provides a bridge between Java and Microsoft COM automation. The package supports document creation, opening, saving, and closing operations, including password-protected documents. 주요 액션: Close(Closes the active Word document and ends...)、Create document(Creates a new Word document and initiate...)、Find and replace picture(Finds specified picture in a document or...)、Find and replace text(Finds specified text in a document or fi...)、Format text(Formats the specified text within a docu...) 외 8개."

ACTIONS = [
    {"action": "Close", "data_item_name": "msword#closedocument", "description": "Closes the active Word document and ends the session."},
    {"action": "Create document", "data_item_name": "msword#createdocument", "description": "Creates a new Word document and initiates a new session."},
    {"action": "Find and replace picture", "data_item_name": "msword#findandreplacepicture", "description": "Finds specified picture in a document or finds and replaces it with new picture within the document."},
    {"action": "Find and replace text", "data_item_name": "msword#findandreplacetext", "description": "Finds specified text in a document or find and replaces it with new text within the document."},
    {"action": "Format text", "data_item_name": "msword#formattext", "description": "Formats the specified text within a document."},
    {"action": "Insert picture", "data_item_name": "msword#insertpicture", "description": "Inserts a picture at a specified position within a document."},
    {"action": "Insert table", "data_item_name": "msword#inserttable", "description": "Inserts a table at a specified position within a document"},
    {"action": "Insert text", "data_item_name": "msword#inserttext", "description": "Inserts a text at a specified position within a document."},
    {"action": "Open", "data_item_name": "msword#opendocument", "description": "Opens an existing Word document."},
    {"action": "Read table", "data_item_name": "msword#readtable", "description": "Reads a table from a document and stores it in a data table variable."},
    {"action": "Read text", "data_item_name": "msword#readtext", "description": "Reads the whole text at a specified range."},
    {"action": "Save", "data_item_name": "msword#savedocument", "description": "Saves the active Word document."},
    {"action": "Save as", "data_item_name": "msword#savedocumentas", "description": "Saves the current document as a new file with a different name, file format, or location."},
]