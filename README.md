# clown-src-6k-skill — 黑盒 SRC 漏洞挖掘 + 白盒 0day 审计 AI Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![SRC & 0day Audit](https://img.shields.io/badge/Focus-SRC%20%2F%20Whitebox%200day-EF4444.svg)](#)
[![MCP Ready](https://img.shields.io/badge/MCP-FOFA%20%2B%20Playwright-10B981.svg)](#)

> **clown-src-6k-skill** 是一套面向 **授权黑盒 SRC 漏洞挖掘** 与 **白盒 0day 源码审计** 的 AI Agent 技能与规则套件。集成了完整的全局 Agent 规则（`AGENTS.md` + `rules/`）、按需加载的漏洞测试知识库（`skills/skill/知识库/`）、多账号轮换的 **FOFA MCP Server** 以及 **Playwright 双槽浏览器 MCP 启动脚本**。

---

## ⚠️ 免责声明（Legal Disclaimer）

本项目及其中包含的所有规则、知识库与 MCP 工具**仅限用于已获得明确授权的安全研究、SRC 漏洞众测、企业安全自查及开源项目白盒代码审计**。严禁用于任何未经授权的探测或攻击行为，使用者需自行承担一切法律责任。

---

## ✨ 核心特性

- **双栖安全能力**：同时覆盖「黑盒 SRC 实战挖洞（锁面 / 自由跳一种子闭环 / 深挖优先）」与「白盒 0day 源码审计（Phase 0–6）」。
- **11 项精细化强制规则（`rules/`）**：内置价值优先策略、范围控制与防空转工作流、统一漏洞报告规范、短表迭代机制、Playwright 浏览器协同规则等。
- **模块化漏洞测试知识库（`skills/skill/知识库/`）**：覆盖越权/IDOR、认证绕过、注入、SSRF、XSS、文件上传、业务逻辑、竞态、GraphQL、OAuth/JWT、请求走私、缓存投毒、API 网关、WebSocket、JS 逆向、WAF 绕过、反序列化/JNDI、Agent Tool 执行等 40+ 专题。
- **内置 MCP 工具链**：
  - `mcp-servers/fofa_MCP/`：支持三账号（主号 → backup → backup2）限流自动切换的 FOFA MCP 服务；
  - `bin/playwright-dual-slot.mjs`：Playwright 双槽浏览器启动脚本，支持多会话/登录态并发协同测试。

---

## 📁 目录结构

```text
clown-src-6k-skill/
├── README.md                          # 项目说明文档
├── AGENTS.md                          # 全局 Agent 永久规则入口
├── config.toml                        # CLI 与 MCP Server 配置模板
├── 给朋友的提示词.txt                   # 快速上手与配置提示词
├── bin/
│   └── playwright-dual-slot.mjs       # Playwright 双槽 MCP 启动脚本
├── rules/                             # 11 项核心规则（范围/价值/报告/迭代等）
├── mcp-servers/
│   └── fofa_MCP/                      # 支持三账号自动切换的 FOFA MCP Server
├── skills/skill/
│   ├── SKILL.md                       # SRC 挖洞 + 白盒 0day 主技能入口
│   └── 知识库/                         # 40+ 细分漏洞测试方法论与打穿短表
└── docs/user-guide/                   # CLI 与 Agent 使用手册文档
```

---

## 🚀 快速配置

1. **克隆仓库**：

```bash
git clone https://github.com/shuhuNB515/clown-src-6k-skill.git
cd clown-src-6k-skill
```

2. **配置路径与 FOFA Key**：
   - 编辑 `config.toml`，将其中的占位路径 `C:\Users\USER\.grok` 替换为你的实际目录路径；
   - 复制 `mcp-servers/fofa_MCP/.env.example` 为 `.env`（或直接在 `config.toml` 的 `[mcp_servers.fofa.env]` 中填写你自己的 FOFA Email / Key）。

3. **部署到 AI Agent 目录**：
   - 将 `AGENTS.md`、`config.toml`、`rules/`、`skills/`、`bin/`、`mcp-servers/` 放置到对应 Agent 的配置根目录（如 `~/.grok/` 或兼容的 Claude Code / Codex 目录）即可生效。

---

## 📄 License

本项目基于 [MIT License](LICENSE) 开源。
