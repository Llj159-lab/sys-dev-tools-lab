Issue: Windows 环境下运行 sdt-greet 时，传入仅含空白字符的 --name 仍会被当作有效输入。
复现命令: sdt-greet --name "   "
期望结果: 程序应拒绝空白姓名，并以非 0 状态退出。
实际结果: 仍输出 "Hello, !"，且返回码为 0。
修复建议: 在参数校验中对 name 做 strip，若结果为空则报错并退出。

提交信息: fix: reject whitespace-only name input

评审意见: Blocking: 当前实现会接受空白姓名，导致无效输出。建议在 main 中加入显式校验，并补充对应测试。
