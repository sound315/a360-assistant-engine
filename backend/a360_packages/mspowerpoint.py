# -*- coding: utf-8 -*-
PACKAGE_NAME        = "PowerPoint"
PACKAGE_ID          = "command-group:mspowerpoint"
PACKAGE_DESCRIPTION = "Automates Microsoft PowerPoint desktop presentations on Windows using the PowerPoint COM object model. Supports creating, opening, saving, and exporting presentations, and slide operations such as adding, deleting, copying, inserting text, pictures, and tables. 주요 액션: Add slide(Adds a slide to the active presentation.)、Close(Closes the active presentation.)、Copy paste slide(Copies a slide and pastes the slide at t...)、Create presentation(Creates a new presentation.)、Delete slide(Deletes the slide at the specified index...) 외 9개."

ACTIONS = [
    {"action": "Add slide", "data_item_name": "mspowerpoint#addslide", "description": "Adds a slide to the active presentation."},
    {"action": "Close", "data_item_name": "mspowerpoint#close", "description": "Closes the active presentation."},
    {"action": "Copy paste slide", "data_item_name": "mspowerpoint#copypasteslide", "description": "Copies a slide and pastes the slide at the specified position."},
    {"action": "Create presentation", "data_item_name": "mspowerpoint#createpresentation", "description": "Creates a new presentation."},
    {"action": "Delete slide", "data_item_name": "mspowerpoint#deleteslide", "description": "Deletes the slide at the specified index from the active presentation."},
    {"action": "Find and replace picture", "data_item_name": "mspowerpoint#findandreplacepicture", "description": "Finds specified picture in a presentation or finds and replaces it with new picture within the presentation."},
    {"action": "Find and replace text", "data_item_name": "mspowerpoint#findandreplacetext", "description": "Finds specified text in a presentation or finds and replaces it with new text within the presentation."},
    {"action": "Format text", "data_item_name": "mspowerpoint#formattext", "description": "Format text by applying styling and alignment properties to enhance text appearance."},
    {"action": "Insert picture", "data_item_name": "mspowerpoint#insertpicture", "description": "Inserts a picture at a specified position within a presentation."},
    {"action": "Insert table", "data_item_name": "mspowerpoint#inserttable", "description": "Inserts a table at a specified slide within presentation."},
    {"action": "Insert text", "data_item_name": "mspowerpoint#inserttext", "description": "Inserts text into a new text box on the selected slide."},
    {"action": "Open", "data_item_name": "mspowerpoint#open", "description": "Opens an existing presentation."},
    {"action": "Save", "data_item_name": "mspowerpoint#save", "description": "Saves changes to the active presentation."},
    {"action": "Save as", "data_item_name": "mspowerpoint#saveas", "description": "Saves the active presentation to a new file path."},
]