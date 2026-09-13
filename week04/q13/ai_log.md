# AI 修复日志

- 核心提示：要求修改 cli.py，使 --name 缺失时以 SystemExit(2) 退出
- AI 改动：在 main() 中添加 try-except 捕获 SystemExit，调用 sys.exit(2)
- 人工验证：运行 pytest 测试通过，diff 确认仅修改 cli.py，无无关改动
