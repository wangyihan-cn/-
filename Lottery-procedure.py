import tkinter as tk
from tkinter import messagebox, Menu
import threading
import random
import time

# 定义抽号程序类
class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("抽号软件")  # 设置窗口标题
        self.root.geometry("350x450")  # 设置窗口尺寸
        self.root.config(bg="#f0f0f0")  # 设置背景色
        self.root.resizable(False, False)  # 禁止最大化和拉伸窗口

        # 当前抽取的数字
        self.current_number = tk.StringVar()
        self.current_number.set("0")

        # 是否运行标志
        self.running = False

        # 创建菜单栏
        menubar = Menu(self.root)
        
        # 创建选项菜单
        option_menu = Menu(menubar, tearoff=0)
        option_menu.add_command(label="关于", command=self.show_about)  # 关于信息
        option_menu.add_command(label="退出", command=self.root.quit)  # 退出程序
        
        # 设置菜单字体大小
        menubar.add_cascade(label="选项", menu=option_menu, font=("Arial", 16))
        self.root.config(menu=menubar)

        # 创建显示数字的标签
        self.label = tk.Label(self.root, textvariable=self.current_number, font=("Arial", 48), fg="#FF5733", relief="ridge", width=10, height=2, bg="#fff")
        self.label.pack(pady=20)

        # 最小值输入框
        self.min_label = tk.Label(self.root, text="请输入最小值:", font=("Arial", 14), bg="#f0f0f0")
        self.min_label.pack(pady=5)
        self.min_entry = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.min_entry.insert(0, "1")  # 设置默认最小值
        self.min_entry.pack(pady=5)

        # 最大值输入框
        self.max_label = tk.Label(self.root, text="请输入最大值:", font=("Arial", 14), bg="#f0f0f0")
        self.max_label.pack(pady=5)
        self.max_entry = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.max_entry.insert(0, "100")  # 设置默认最大值
        self.max_entry.pack(pady=5)

        # 按钮框架
        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        # 开始抽号按钮
        self.start_button = tk.Button(self.button_frame, text="开始抽号", command=self.start_lottery, width=10, height=1, font=("Arial", 14), relief="solid", bd=2)
        self.start_button.grid(row=0, column=0, padx=10)

        # 暂停抽号按钮
        self.stop_button = tk.Button(self.button_frame, text="暂停抽号", command=self.stop_lottery, width=10, height=1, font=("Arial", 14), relief="solid", bd=2)
        self.stop_button.grid(row=0, column=1, padx=10)

        # 设置按钮悬浮效果
        self.start_button.bind("<Enter>", lambda e: self.on_hover(self.start_button))
        self.start_button.bind("<Leave>", lambda e: self.on_leave(self.start_button))
        self.stop_button.bind("<Enter>", lambda e: self.on_hover(self.stop_button))
        self.stop_button.bind("<Leave>", lambda e: self.on_leave(self.stop_button))

    # 按钮悬浮效果
    def on_hover(self, button):
        button.config(bg="#FF5733", fg="#fff")

    def on_leave(self, button):
        button.config(bg="#f0f0f0", fg="#000")

    # 开始抽号
    def start_lottery(self):
        try:
            min_value = int(self.min_entry.get())  # 获取最小值
            max_value = int(self.max_entry.get())  # 获取最大值
            if min_value >= max_value:
                raise ValueError("最小值必须小于最大值！")
        except ValueError as e:
            messagebox.showerror("输入错误", f"请输入正确的数字范围！\n{e}")
            return

        # 禁用输入框以防止修改
        self.min_entry.config(state="disabled")
        self.max_entry.config(state="disabled")

        # 如果没有正在运行的抽号程序，启动新的线程
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run_lottery, args=(min_value, max_value))
            self.thread.start()

    # 抽号逻辑（动画效果）
    def run_lottery(self, min_value, max_value):
        while self.running:
            num = random.randint(min_value, max_value)  # 生成随机数字
            self.current_number.set(str(num))  # 更新显示的数字
            time.sleep(0.05)  # 控制数字显示的速度

    # 暂停抽号
    def stop_lottery(self):
        # 停止抽号并显示最终结果
        if self.running:
            self.running = False
            min_value = int(self.min_entry.get())  # 获取最小值
            max_value = int(self.max_entry.get())  # 获取最大值
            final_number = random.randint(min_value, max_value)  # 生成最终数字
            self.current_number.set(str(final_number))  # 显示最终数字

        # 启用输入框，允许用户修改最小值和最大值
        self.min_entry.config(state="normal")
        self.max_entry.config(state="normal")

    # 关于窗口
    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("关于")
        about_window.geometry("400x250")
        about_window.config(bg="#f0f0f0")

        title_label = tk.Label(about_window, text="抽号软件", font=("Arial", 24), fg="#FF5733", bg="#f0f0f0")
        title_label.pack(pady=10)

        version_label = tk.Label(about_window, text="版本: 1.0", font=("Arial", 16), bg="#f0f0f0")
        version_label.pack(pady=5)

        author_label = tk.Label(about_window, text="作者: byte", font=("Arial", 16), bg="#f0f0f0")
        author_label.pack(pady=5)

        github_label = tk.Label(about_window, text="已开源: github.com/wangyihan-cn/Lottery-procedure", font=("Arial", 14), bg="#f0f0f0", wraplength=380)
        github_label.pack(pady=5)

        # 关闭按钮
        close_button = tk.Button(about_window, text="关闭", command=about_window.destroy, font=("Arial", 16), width=15, height=2, relief="solid", bd=2)
        close_button.pack(pady=10)

# 启动程序
if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()
