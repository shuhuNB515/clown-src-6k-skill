# Contributing to clown-src-6k-skill

欢迎为 **clown-src-6k-skill** 贡献新的漏洞测试知识库专题（`skills/skill/知识库/`）、Agent 规则（`rules/`）或 MCP 工具增强！

## 提交前检查

1. 运行本地完整性与语法校验：
   ```bash
   python3 scripts/setup.py --check
   ```
2. 确认未将 `.env` 或任何真实 FOFA Key、目标未脱敏敏感信息纳入提交。
3. 使用清晰的分支名（如 `feat/kb-xxx`、`fix/fofa-mcp`）与 Conventional Commits 提交信息。
