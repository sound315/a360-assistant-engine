"""
09_generate_package_descriptions.py
공식 hover 설명 + 액션 요약 합산 → 패키지 설명 완성

실행 순서:
  1. node 08_extract_package_desc.js  (output/package_hover_desc.json 생성)
  2. python 09_generate_package_descriptions.py

출력:
  - output/actions.json  : 각 패키지에 packageDescription 필드 추가
  - backend/a360_tasks.py        : PACKAGES description 포함
  - backend/a360_packages/*.py   : PACKAGE_DESCRIPTION 상수 추가
"""

import json, sys, os, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR    = Path(__file__).parent.parent.parent  # a360-assistant-engine_sdd
OUTPUT_DIR  = Path(__file__).parent.parent / 'output'
ACTIONS_PATH = OUTPUT_DIR / 'actions.json'
HOVER_PATH   = OUTPUT_DIR / 'package_hover_desc.json'
PACKAGES_DIR = BASE_DIR / 'backend' / 'a360_packages'
TASKS_PATH   = BASE_DIR / 'backend' / 'a360_tasks.py'

# ─── 로드 ────────────────────────────────────────────────────────────────────
with open(ACTIONS_PATH, encoding='utf-8') as f:
    data = json.load(f)

hover_desc = {}
if HOVER_PATH.exists():
    with open(HOVER_PATH, encoding='utf-8') as f:
        raw = json.load(f)
    # 빈 문자열 제거
    hover_desc = {k: v for k, v in raw.items() if v and v.strip()}
    print(f'hover 공식 설명 로드: {len(hover_desc)}개 확보')
else:
    print('package_hover_desc.json 없음 → 액션 요약만 사용')

# ─── 패키지 설명 생성 ─────────────────────────────────────────────────────────
def build_description(pkg: dict, official: str) -> str:
    actions = pkg['actions']
    total   = len(actions)

    # 설명이 있는 액션 우선 선택, 최대 5개
    with_desc = [a for a in actions if a.get('description', '').strip()]
    selected  = with_desc[:5] if with_desc else actions[:5]

    reps = []
    for act in selected:
        desc = act.get('description', '').replace('\n', ' ').replace('\r', '').strip()
        if desc:
            short = desc[:40].rstrip() + ('...' if len(desc) > 40 else '')
            reps.append(f"{act['name']}({short})")
        else:
            reps.append(act['name'])

    action_summary = '、'.join(reps)
    suffix = f' 외 {total - len(reps)}개' if total > len(reps) else f' (총 {total}개)'

    if official:
        return f"{official} 주요 액션: {action_summary}{suffix}."
    else:
        return f"주요 액션: {action_summary}{suffix}."

# ─── 파일명 변환 (08 재생성 스크립트와 동일 로직) ────────────────────────────
def to_filename(pkg_id: str) -> str:
    name = pkg_id.split(':')[-1] if ':' in pkg_id else pkg_id
    name = re.sub(r'[^a-zA-Z0-9]', '_', name).lower().strip('_')
    return name or 'package'

used: dict[str, int] = {}
for pkg in data:
    base = to_filename(pkg['packageId'])
    cnt  = used.get(base, 0)
    used[base] = cnt + 1
    pkg['_fname'] = base if cnt == 0 else f'{base}_{cnt}'

# ─── 패키지별 처리 ──────────────────────────────────────────────────────────
updated_actions = 0
for pkg in data:
    official = hover_desc.get(pkg['packageId'], '').strip()
    desc     = build_description(pkg, official)
    pkg['packageDescription'] = desc
    updated_actions += 1

# ─── actions.json 업데이트 ─────────────────────────────────────────────────
# _fname 임시 키 제거 후 저장
clean_data = [{k: v for k, v in p.items() if k != '_fname'} for p in data]
with open(ACTIONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(clean_data, f, ensure_ascii=False, indent=2)
print(f'actions.json 업데이트: {updated_actions}개 패키지에 packageDescription 추가')

# ─── a360_packages/*.py 재생성 ────────────────────────────────────────────
file_count = 0
for pkg in data:
    fname    = pkg['_fname']
    pkg_name = pkg['packageName'].replace('"', '\\"')
    pkg_id   = pkg['packageId']
    pkg_desc = pkg['packageDescription'].replace('\n', ' ').replace('\r', '').replace('"', '\\"')

    lines = [
        '# -*- coding: utf-8 -*-',
        f'PACKAGE_NAME        = "{pkg_name}"',
        f'PACKAGE_ID          = "{pkg_id}"',
        f'PACKAGE_DESCRIPTION = "{pkg_desc}"',
        '',
        'ACTIONS = [',
    ]
    for act in pkg['actions']:
        act_name  = act['name'].replace('"', '\\"')
        item_name = act['attrs'].get('data-item-name', '')
        act_desc  = act.get('description', '').replace('"', '\\"').replace('\n', ' ').strip()
        lines.append(f'    {{"action": "{act_name}", "data_item_name": "{item_name}", "description": "{act_desc}"}},')
    lines.append(']')

    path = PACKAGES_DIR / f'{fname}.py'
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    file_count += 1

print(f'a360_packages/*.py 재생성: {file_count}개')

# ─── a360_tasks.py 재생성 ─────────────────────────────────────────────────
pkg_lines = ['# -*- coding: utf-8 -*-', '# A360 패키지 메타데이터', 'from a360_packages import load_all_tasks', '', 'PACKAGES = [']
for pkg in data:
    n    = pkg['packageName'].replace('"', '\\"')
    pid  = pkg['packageId']
    cnt  = pkg['actionCount']
    fn   = pkg['_fname']
    desc = pkg['packageDescription'].replace('\n', ' ').replace('\r', '').replace('"', '\\"')
    pkg_lines.append(
        f'    {{"name": "{n}", "id": "{pid}", "action_count": {cnt}, "file": "{fn}", "description": "{desc}"}},'
    )
pkg_lines += [']', '', 'A360_TASKS    = load_all_tasks()', 'ALLOWED_PAIRS = {(t["package"], t["action"]) for t in A360_TASKS}', '']

with open(TASKS_PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(pkg_lines))
print(f'a360_tasks.py 재생성: {len(data)}개 패키지 (description 포함)')

# ─── 요약 출력 ──────────────────────────────────────────────────────────────
official_count = sum(1 for p in data if p['packageDescription'] and not p['packageDescription'].startswith('주요'))
print(f'\n공식 설명 포함 패키지: {official_count}개')
print(f'액션 요약만 포함 패키지: {len(data) - official_count}개')
print('\n샘플 (처음 3개):')
for pkg in data[:3]:
    print(f'  [{pkg["packageName"]}] {pkg["packageDescription"][:80]}')
