#!/usr/bin/env python3
"""Render captured Lovable UI events; no network or execution of captured code."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


class CopyTextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'data-copy-text' in attrs:
            self.blocks.append(attrs['data-copy-text'])


def code_blocks(row):
    if row.get('code_blocks'):
        return row['code_blocks']
    parser = CopyTextParser()
    parser.feed(row.get('html', ''))
    return parser.blocks


def normalize(data):
    if 'details' in data:
        return data['details']
    keys = sorted((k for k in data if re.fullmatch(r'detail\d+', k)),
                  key=lambda k: int(k[6:]))
    return [{'title': f'Details {k[6:]}', 'rows': data[k],
             'inventory': data.get('inventory' + k[6:]),
             'complete': data.get('complete', False)} for k in keys]


def fence(text, language='text'):
    width = max([3] + [len(m) + 1 for m in re.findall(r'`+', text)])
    marker = '`' * width
    return f'{marker}{language}\n{text.rstrip()}\n{marker}\n'


def render(data, allow_incomplete=False):
    details = normalize(data)
    if not details:
        raise ValueError('No Details found')
    issues = []
    counts = dict(details=len(details), events=0, thoughts=0, sql=0, diffs=0)
    for n, detail in enumerate(details, 1):
        rows = detail.get('rows', [])
        if not detail.get('complete'):
            issues.append(f'Details {n}: 尚未确认遍历完整。')
        if not rows:
            issues.append(f'Details {n}: 没有事件。')
        inventory = detail.get('inventory')
        if inventory is not None:
            expected = [r['label'] if isinstance(r, dict) else r for r in inventory]
            if expected != [r.get('label') if r else None for r in rows]:
                issues.append(f'Details {n}: 清单与采集事件数量或顺序不一致。')
        issues.extend(f'Details {n}: {gap}' for gap in detail.get('gaps', []))
        for i, row in enumerate(rows, 1):
            if not row:
                issues.append(f'Details {n}.{i}: 条目缺失。')
                continue
            label, text = row.get('label', ''), row.get('text', '')
            counts['events'] += 1
            if not label or not text:
                issues.append(f'Details {n}.{i}: 标签或文本缺失。')
            if label.startswith('Thought'):
                counts['thoughts'] += 1
                if text.strip() == label.strip():
                    issues.append(f'Details {n}.{i}: Thought 正文缺失。')
            if label.startswith('Edited'):
                counts['diffs'] += 1
                if not any(b.strip() for b in code_blocks(row)):
                    issues.append(f'Details {n}.{i}: diff 原文缺失。')
            if label == 'Modified database':
                counts['sql'] += 1
                if text.strip() == label.strip() and not code_blocks(row):
                    issues.append(f'Details {n}.{i}: SQL 原文缺失。')
    if issues and not allow_incomplete:
        raise ValueError('\n'.join(issues))
    lines = [f"# {data.get('title', 'Lovable')} — Details\n"]
    for field, title in [('source_url', '来源'), ('captured_at', '采集时间')]:
        if data.get(field):
            lines.append(f'{title}：{data[field]}\n')
    lines.append(f"共 {counts['details']} 个 Details、{counts['events']} 个事件、"
                 f"{counts['thoughts']} 段 Thought、{counts['sql']} 段 SQL、"
                 f"{counts['diffs']} 段代码 diff。\n")
    lines.append('通过已登录浏览器 DOM、滚动清单、逐项展开和代码块 data-copy-text 采集。'
                 '保留页面原文与顺序，不代表后台全部推理或调度日志。'
                 '命令不等于完整运行输出，diff 不等于完整文件。\n')
    lines.append('脱敏说明：' + data.get('redaction_note', '未提供，需核对采集源。') + '\n')
    if issues:
        lines.append('## 采集缺口\n\n' + '\n'.join('- ' + issue for issue in issues) + '\n')
    for n, detail in enumerate(details, 1):
        title = detail.get('title', f'Details {n}').replace('\n', ' ')
        lines.append(f'## {n}. {title}\n')
        for i, row in enumerate(detail.get('rows', []), 1):
            if not row:
                lines.append(f'### {n}.{i:02d} · 缺失事件\n')
                continue
            label, text = row.get('label', ''), row.get('text', '')
            title = label.replace('\n', ' ')
            body = text[len(label):].lstrip('\n') if text.startswith(label) else text
            if len(title) > 115:
                title, body = '阶段进度 / 结果', text
            lines.append(f'### {n}.{i:02d} · {title}\n')
            blocks = code_blocks(row)
            if blocks:
                if body.strip():
                    lines.append(body.strip() + '\n')
                language = 'diff' if label.startswith('Edited') else 'sql' if label == 'Modified database' else 'text'
                lines.extend(fence(block, language) for block in blocks)
            elif label == 'Modified database':
                lines.append(fence(body, 'sql'))
            elif body.strip():
                prose = label.startswith('Thought') or label in ('Questions answered', 'Read') or len(label) > 115
                lines.append(body.strip() + '\n' if prose else fence(body))
            else:
                lines.append('> 页面仅展示此事件名称。\n')
    return '\n'.join(lines), counts, issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--allow-incomplete', action='store_true')
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output exists; choose a new filename to preserve it')
    try:
        data = json.loads(args.input.read_text(encoding='utf-8'))
        markdown, counts, issues = render(data, args.allow_incomplete)
    except (ValueError, KeyError, TypeError) as exc:
        parser.error(str(exc))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding='utf-8')
    print(json.dumps({'output': str(args.output.resolve()), **counts,
                      'incomplete': bool(issues)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
