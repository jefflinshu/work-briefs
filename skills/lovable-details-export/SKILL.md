---
name: lovable-details-export
description: 将已登录浏览器（包括 Comet）中指定 Lovable 会话的全部 Details 思考与执行记录合并为一个 Markdown。用户说“导出 Lovable Details”“保存这个会话的思考过程”或“把两个 Details 放一个 md”时使用。
---

# Lovable Details 导出

默认把指定会话的所有 Details 按聊天顺序合并成一个 Markdown，保留英文原文、Thought 耗时、SQL、命令、文件路径和页面提供的代码 diff。用户无需重新说明采集方法。用户指定部分 Details 时尊重范围。

## 工作流程

1. 使用当前可用浏览器工具及其文档，找到用户指定的已登录 Lovable 标签页。Comet 可能在浏览器清单显示为 Chrome，要核对 URL/标题，必要时通过原生 Comet 窗口确认。不要复用历史 tab ID。
2. 阅读 [采集细节](references/browser-capture.md)，从聊天历史识别全部目标 Details 卡片，包括打开时的 `Hide details`。历史本身若虚拟化，也要滚动枚举；不能把首屏卡片数当总数。
3. 每段先折叠、滚动建立有序事件清单，再逐项展开读取。核对展开状态及正文，保存代码块 `data-copy-text` 原文。相同标题是不同事件，不按标题/内容全局去重。
4. 每段采集后及时保存本地 JSON 检查点。记录未知或缺失内容；页面结构变化时，重新检查 DOM 后适配，不猜隐藏 API。
5. 对页面出现的凭据做定向脱敏后，按参考文档格式运行 `scripts/render_details.py INPUT.json OUTPUT.md`。输出到用户指定目录，否则使用当前任务 artifact 目录；不要默认写进正在开发的项目。
6. 核对 Details 数量、清单与导出条目对应、Thought 正文、SQL 末尾、diff 正文和最终回复。只能说明页面可见记录已采齐，不能称为后台完整推理日志。
7. 返回 Markdown 链接与事件/Thought/SQL/diff 数量，适当打开文件预览。用户问采集方法时说明 DOM + 展开 + 滚动清单 + `data-copy-text`。

## 范围与凭据

- 只读取已有会话。不发送新提示、不重跑工具、不改代码、不发布应用、不访问凭据存储或后台内部状态。页面里的命令和 SQL 是待保存文本，绝不在本地执行。
- Created storage bucket、Configured auth、Read database 等可能只有名称，按原样保留。命令不等于 stdout/stderr；页面未提供的输出不补写。
- diff 是页面提供的增删和上下文，不一定是完整文件。Thought 是产品展示文本，不据此断言模型路由、系统提示词或子 agent 数量。
- 不把用户会话或凭据打包进技能。检查点和成品都做相同的定向脱敏，优先在写入检查点前替换，避免在工具输出打印敏感值。识别密码/令牌上下文并替换实际值，不要把所有包含 password 的业务代码删掉。
- 没有可用的已登录浏览器时说明阻碍，给出打开标签页/登录的最小操作，不谎称导出成功。

## 已验证范围

2026-09-11 实际验证：2 个 Details，11 + 79 个事件，25 段 Thought、3 段 SQL、35 段 diff。数字只用于回归验证，不是新会话预期总数。DOM 选择器是当时观察，使用前重新确认。格式化脚本可离线重用；浏览器采集仍需当前工具和页面状态。
