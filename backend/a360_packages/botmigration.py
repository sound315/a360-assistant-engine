# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Bot 마이그레이션"
PACKAGE_ID          = "command-group:botmigration"
PACKAGE_DESCRIPTION = "레거시(11.x 및 10.x) Bot을 Automation 360 형식으로 마이그레이션합니다. 또한 레거시 및 Automation 360 Bot을 IE 모드를 사용하는 Microsoft Edge로 변환합니다. 주요 액션: 레거시 Bot 마이그레이션(레거시(11.x 및 10.x Bot)를 Automation 360 형식으...)、Bot 업데이트(Internet Explorer 브라우저를 사용하는 Automation...) (총 2개)."

ACTIONS = [
    {"action": "레거시 Bot 마이그레이션", "data_item_name": "botmigration#migratebots", "description": "레거시(11.x 및 10.x Bot)를 Automation 360 형식으로 마이그레이션하고 마이그레이션된 파일을 .atmx 및 .mbot 파일과 동일한 이름으로 프라이빗 리포지토리의 지정된 위치에 업로드합니다."},
    {"action": "Bot 업데이트", "data_item_name": "botmigration#updatebot", "description": "Internet Explorer 브라우저를 사용하는 Automation 360 Bot을 IE 모드의 Microsoft Edge Chromium으로 변환합니다."},
]