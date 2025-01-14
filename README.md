# 抽号软件

一个简单的抽号软件，使用 Python 和 Tkinter 开发，用户可以设置最小值和最大值，点击按钮进行抽号，抽号过程带有动画效果。

## 功能

- **设置最小值和最大值**：用户可以在输入框中输入最小值和最大值，限制抽号范围。
- **开始抽号**：点击“开始抽号”按钮，软件会自动显示随机数字，并持续更新直到点击“暂停抽号”。
- **暂停抽号**：点击“暂停抽号”按钮，停止抽号并显示最终的随机数字。
- **禁用输入框**：在抽号过程中，最小值和最大值的输入框会被禁用，直到停止抽号才会重新启用。
- **关于窗口**：可以查看软件版本、作者信息和项目的 GitHub 地址。

## 界面截图

![抽号软件界面](screenshots/lottery_app.png)

## 使用方法

1. **设置范围**：在“最小值”和“最大值”输入框中输入数字，设置抽号的范围。
2. **点击开始抽号**：点击“开始抽号”按钮，软件将随机抽取数字并显示。
3. **点击暂停抽号**：点击“暂停抽号”按钮，抽号过程停止并显示最终数字。

## 安装与运行

### 安装依赖

1. 安装 Python 3：[下载 Python](https://www.python.org/downloads/)。

2. 确保 `tkinter` 已安装，通常 `tkinter` 会随 Python 一起安装。可以通过以下命令确认：

   ```bash
   python -m tkinter
   ```

如果能成功弹出 Tkinter 窗口，说明已经安装。

### 运行程序

1. 下载或克隆本仓库到本地。

2. 在项目目录下打开终端，运行以下命令启动程序：

   ```bash
   python lottery_app.py
   ```

   启动后将会看到抽号软件的窗口界面。

## 项目结构


```bash
lottery_app.py        # 主程序文件
README.md             # 项目的说明文档
LICENSE               # 项目许可证（MIT）
```

## 贡献

欢迎提出问题和贡献代码！如果你有任何建议或问题，可以在 GitHub 上创建 issue 或提交 pull request。


## 联系方式

- 作者：[byte](https://github.com/wangyihan-cn)
- GitHub：[github.com/wangyihan-cn/Lottery-procedure](https://github.com/wangyihan-cn/Lottery-procedure)
