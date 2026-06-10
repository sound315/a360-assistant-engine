# -*- coding: utf-8 -*-
PACKAGE_NAME        = "IQ Bot"
PACKAGE_ID          = "command-group:iq bot"
PACKAGE_DESCRIPTION = "IQ Bot 서버에 문서를 업로드하고 다운로드합니다 주요 액션: Download all documents(Downloads extracted results from an IQ B...)、Upload Document(Uploads a document for processing with I...) (총 2개)."

ACTIONS = [
    {"action": "Download all documents", "data_item_name": "iq bot#iqbotdownload", "description": "Downloads extracted results from an IQ Bot server that were created by running a bot using the Upload Document action."},
    {"action": "Upload Document", "data_item_name": "iq bot#iqbotupload", "description": "Uploads a document for processing with IQ Bot. Fields are extracted from the document and exported to CSV files."},
]