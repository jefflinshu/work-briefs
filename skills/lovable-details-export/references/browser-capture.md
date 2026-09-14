# 浏览器采集细节

## 定位与边界

使用当前提供的浏览器/Computer Use 工具和文档，不绑定某个工具名或历史 tab ID。先观察 AX/DOM，再点击 Details；点击后确认对应卡片变为 Hide details 且时间线切换。曾出现一次语义点击未生效：观察截图后定位同一按钮重试，不能直接当作切换成功。

2026-09-11 实际观察：

- 聊天区：`#sidebar-panel` / region `Chat`。
- 时间线区：`#preview-panel` / region `Preview`，也包含隐藏的预览 iframe，避免把 iframe 文本当作 Details。
- 滚动容器：`#preview-panel .overflow-y-auto.px-4`。
- 条目：滚动容器的 `> div > div`，每条有绝对定位 `style.top`。
- 展开按钮：`button[aria-expanded]`。
- diff：`[data-copy-text]` 的 attribute 是可复制原文。`innerText` 可能仅有标题和路径，因为 diff 在自定义元素渲染。

选择器需在新页面核对后使用。不要查询 React fiber、store、cookie、token 或隐藏应用状态，不猜测服务端接口。

## 清单与采集

全折叠后，从顶部向下以重叠视口滚动，持续读取条目。每次 UI 操作后获取新 AX/DOM 状态。保存 `(折叠布局 top, label)`；保持同一段、同一窗口宽度和折叠布局时，top 可作本次采集的临时键。不得跨 Details/刷新复用。

连续两次确认已在底部、滚动位置/总高度稳定且无新增条目后结束枚举。设置合理的扫描次数上限，达到上限仍未到底则标记 incomplete。总高度不是事件数量，空占位条目不计数。

按清单顺序逐条展开再折叠，维持后续 top 基准：

1. 重新读取挂载条目，定位目标 top + label；未挂载则滚动使其出现。
2. 检查 aria-expanded，点击后确认 true；第一次点击可能被布局更新吞掉，基于新状态最多重试三次。
3. 读取展开条目的 innerText、data-copy-text 数组；SQL 没有该属性时读 code 或正文。再次核对展开状态，防止只拿标题。
4. Thought 必须有超过标题的正文；Edited 必须有非空 diff。等待用工具的状态/元素等待能力，不用固定长 sleep。
5. 折叠并确认 false，再处理下一条。失败则保留检查点并说明缺口，不无限重试。

相同耗时的 Thought、同一文件多次 Edited、连续 Created storage bucket 均须保留，不做全局文本去重。

## 只读提取片段

仅在确认上述 DOM 后，通过当前浏览器工具的只读 evaluate 使用；宿主负责点击和滚动。

```javascript
const rows = await tab.playwright.locator(rowsSelector).evaluateAll(elements =>
  elements.map(e => ({
    top: e.style.top,
    label: e.querySelector('button[aria-expanded]')?.innerText.trim()
      || e.innerText.trim().split('\n')[0],
    text: e.innerText.trim(),
    code_blocks: Array.from(e.querySelectorAll('[data-copy-text]'))
      .map(code => code.getAttribute('data-copy-text')),
  })).filter(row => row.text)
);
```

只读 evaluate 沙箱曾不提供全局 parseFloat；top 保留字符串，排序放在宿主 JavaScript。直接读 data-copy-text，避免从高亮 span 和行号拼代码。文件写入使用当前工具允许的 artifact 文件接口或本地文件工具，不以其他技术绕过浏览器操作约束。

## 检查点与渲染

一个会话一个 JSON：

```json
{
  "title": "Project title",
  "source_url": "https://lovable.dev/projects/actual-project-id",
  "captured_at": "2026-09-14T10:00:00+08:00",
  "redaction_note": "页面中的管理员密码已替换为 [REDACTED]。",
  "details": [{
    "title": "Actual card title",
    "complete": true,
    "inventory": [{"label": "Thought for 8s"}],
    "rows": [{
      "label": "Thought for 8s",
      "text": "Thought for 8s\n\nActual displayed text.",
      "code_blocks": []
    }]
  }]
}
```

complete 只能在实际遍历并核对后为 true。未采齐设 false，具体缺口写入 gaps 字符串数组。inventory 包含重复事件。正文和代码原样保存，不做总结。

```sh
python3 <skill-dir>/scripts/render_details.py <capture.json> <output.md>
```

脚本校验清单、正文和 diff，失败时不创建成品。确实无法补齐时用 `--allow-incomplete` 输出明确标注缺口的文档，不静默降低完整性要求。脚本不自动推断全部敏感信息；采集者须在写入 JSON 前定向脱敏。兼容旧检查点 detail1/detail2/inventory2 和已保存的 HTML，只离线解析 data-copy-text，不执行 HTML。旧格式需添加顶层 complete=true，且必须先人工核对清单及边界。
