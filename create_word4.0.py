import tkinter as tk
from tkinter import ttk
import re
from datetime import datetime
from ttkbootstrap import Style
from tkinter import filedialog
from tkinter import font
import webbrowser





# 创建窗口
window = tk.Tk()
window.title("文书宝")
window.geometry("600x600")

# 创建一个Frame并将它放置在主窗口中
input_frame = ttk.Frame(window, padding="10")
input_frame.grid(column=0, row=0, sticky=(tk.W, tk.N, tk.E, tk.S), padx=4)
custom_font = font.Font(size=10)
# 选择UI主题
style = Style(theme='minty')
# 可供选择的主题有：
# light
# cosmo - flatly - journal - literal - lumen - minty - pulse - sandstone - united - yeti
# dark
# cyborg - darkly - solar - superhero

# 输入变量
委托人性质 = tk.StringVar()
委托人名称 = tk.StringVar()
身份证号码 = tk.StringVar()
性别 = tk.StringVar()
出生日期 = tk.StringVar()
住所 = tk.StringVar()
社会信用代码 = tk.StringVar()
法定代表人姓名 = tk.StringVar()
法定代表人职务 = tk.StringVar()
案件名称 = tk.StringVar()
案件阶段 = tk.StringVar()
代理律师人数 = tk.IntVar()
代理律师1姓名 = tk.StringVar()
代理律师1电话 = tk.StringVar()
代理律师1权限 = tk.StringVar()
代理律师2姓名 = tk.StringVar()
代理律师2电话 = tk.StringVar()
代理律师2权限 = tk.StringVar()
# 创建输入框组件
委托人性质_label = tk.Label(input_frame, text="委托人性质", font=custom_font)
委托人性质_label.grid(row=0, column=0, padx=4, pady=4, sticky=tk.E)

# 创建Radiobutton，并设置value属性，用于表示选项的值
单位_radiobutton = tk.Radiobutton(input_frame, text="单位", variable=委托人性质, value="单位", width=4, anchor=tk.W,
                                  command=lambda: update_widgets())
单位_radiobutton.grid(row=0, column=1, padx=3, pady=1, sticky=tk.W)

自然人_radiobutton = tk.Radiobutton(input_frame, text="自然人", variable=委托人性质, value="自然人", width=6,
                                    anchor=tk.W, command=lambda: update_widgets())
自然人_radiobutton.grid(row=0, column=1, padx=3, pady=1)

# 默认未选中
委托人性质.set(None)

委托人名称_label = tk.Label(input_frame, text="委托人名称")
委托人名称_label.grid(row=1, column=0, padx=4, pady=4, sticky=tk.E)
委托人名称_entry = tk.Entry(input_frame, width=40, textvariable=委托人名称)
委托人名称_entry.grid(row=1, column=1, padx=4, pady=4, sticky=tk.W)
#配置企业名称查询网址
def query():
    url = "https://www.qcc.com/web/search?key=" +委托人名称.get() # 将此处替换为你要打开的网址
    webbrowser.open(url)
#创建查询按钮
查询按钮= ttk.Button(input_frame, text="查询", command=query)
查询按钮.grid(row=1, column=2, padx=4, pady=4, sticky=tk.W)

身份证号码_label = tk.Label(input_frame, text="身份证号码")
身份证号码_label.grid(row=2, column=0, padx=4, pady=4, sticky=tk.E)
身份证号码_entry = tk.Entry(input_frame, width=40, textvariable=身份证号码)
身份证号码_entry.grid(row=2, column=1, padx=4, pady=4, sticky=tk.W)

性别_label = tk.Label(input_frame, text="性别")
性别_label.grid(row=3, column=0, padx=4, pady=4, sticky=tk.E)
性别_entry = tk.Entry(input_frame, width=40, textvariable=性别)
性别_entry.grid(row=3, column=1, padx=4, pady=4, sticky=tk.W)

出生日期_label = tk.Label(input_frame, text="出生日期")
出生日期_label.grid(row=4, column=0, padx=4, pady=4, sticky=tk.E)
出生日期_entry = tk.Entry(input_frame, width=40, textvariable=出生日期)
出生日期_entry.grid(row=4, column=1, padx=4, pady=4, sticky=tk.W)

社会信用代码_label = tk.Label(input_frame, text="社会信用代码")
社会信用代码_label.grid(row=5, column=0, padx=4, pady=4, sticky=tk.E)
社会信用代码_entry = tk.Entry(input_frame, width=40, textvariable=社会信用代码)
社会信用代码_entry.grid(row=5, column=1, padx=4, pady=4, sticky=tk.W)

住所_label = tk.Label(input_frame, text="住址")
住所_label.grid(row=6, column=0, padx=4, pady=4, sticky=tk.E)
住所_text = tk.Text(input_frame, width=39, height=2, wrap=tk.WORD)
住所_text.grid(row=6, column=1, padx=4, pady=4, sticky=tk.W)

法定代表人姓名_label = tk.Label(input_frame, text="法定代表人姓名")
法定代表人姓名_label.grid(row=7, column=0, padx=4, pady=4, sticky=tk.E)
法定代表人姓名_entry = tk.Entry(input_frame, width=40, textvariable=法定代表人姓名)
法定代表人姓名_entry.grid(row=7, column=1, padx=4, pady=4, sticky=tk.W)

法定代表人职务_label = tk.Label(input_frame, text="法定代表人职务")
法定代表人职务_label.grid(row=8, column=0, padx=4, pady=4, sticky=tk.E)
法定代表人职务_entry = tk.Entry(input_frame, width=40, textvariable=法定代表人职务)
法定代表人职务_entry.grid(row=8, column=1, padx=4, pady=4, sticky=tk.W)

separator_horizontal = ttk.Separator(input_frame, orient='horizontal')
separator_horizontal.grid(row=9, column=0, columnspan=2, padx=4, pady=4, sticky='ew')

案件名称_label = tk.Label(input_frame, text="案件名称")
案件名称_label.grid(row=10, column=0, padx=4, pady=4, sticky=tk.E)
案件名称_entry = tk.Entry(input_frame, width=40, textvariable=案件名称)
案件名称_entry.grid(row=10, column=1, padx=4, pady=4, sticky=tk.W)

案件阶段_label = tk.Label(input_frame, text="案件阶段")
案件阶段_label.grid(row=11, column=0, padx=4, pady=4, sticky=tk.E)
案件阶段_entry = ttk.Combobox(input_frame, values=("劳动仲裁", "商事仲裁", "一审", "二审", "再审", "执行", "其他"),
                              textvariable=案件阶段)
案件阶段_entry.grid(row=11, column=1, padx=4, pady=4, sticky=tk.W)

# 创建Radiobutton，并设置value属性，用于表示选项的值
代理律师人数_label = tk.Label(input_frame, text="代理律师人数")
代理律师人数_label.grid(row=12, column=0, padx=4, pady=4, sticky=tk.E)
rb1 = tk.Radiobutton(input_frame, text="1人", variable=代理律师人数, value=1, width=4, anchor=tk.W,
                     command=lambda: update_widgets())
rb1.grid(row=12, column=1, padx=3, pady=1, sticky=tk.W)

rb2 = tk.Radiobutton(input_frame, text="2人", variable=代理律师人数, value=2, width=6, anchor=tk.W,
                     command=lambda: update_widgets())
rb2.grid(row=12, column=1, padx=3, pady=1)



attorney_row_offset = 12

代理律师1姓名_label = tk.Label(input_frame, text="（代理律师1）姓名")
代理律师1姓名_label.grid(row=13, column=0, padx=4, pady=4, sticky=tk.E)
代理律师1姓名_entry = tk.Entry(input_frame, width=40, textvariable=代理律师1姓名)
代理律师1姓名_entry.grid(row=13, column=1, padx=4, pady=4, sticky=tk.W)

代理律师1电话_label = tk.Label(input_frame, text="（代理律师1）联系电话")
代理律师1电话_label.grid(row=14, column=0, padx=4, pady=4, sticky=tk.E)
代理律师1电话_entry = tk.Entry(input_frame, width=40, textvariable=代理律师1电话)
代理律师1电话_entry.grid(row=14, column=1, padx=4, pady=4, sticky=tk.W)

代理律师1权限_label = tk.Label(input_frame, text="（代理律师1）代理权限")
代理律师1权限_label.grid(row=15, column=0, padx=4, pady=4, sticky=tk.E)
代理律师1特别授权单选按钮= tk.Radiobutton(input_frame, text="特别授权", variable=代理律师1权限, value="特别授权", width=6, anchor=tk.W)
代理律师1一般代理单选按钮= tk.Radiobutton(input_frame, text="一般代理", variable=代理律师1权限, value="一般代理", width=6, anchor=tk.W)
代理律师1特别授权单选按钮.grid(row=15, column=1, padx=3, pady=1, sticky=tk.W)
代理律师1一般代理单选按钮.grid(row=15, column=1, padx=3, pady=1)
# 默认未选中
代理律师1权限.set(None)

代理律师2姓名_label = tk.Label(input_frame, text="（代理律师2）姓名")
代理律师2姓名_label.grid(row=16, column=0, padx=4, pady=4, sticky=tk.E)
代理律师2姓名_entry = tk.Entry(input_frame, width=40, textvariable=代理律师2姓名)
代理律师2姓名_entry.grid(row=16, column=1, padx=4, pady=4, sticky=tk.W)

代理律师2电话_label = tk.Label(input_frame, text="（代理律师2）联系电话")
代理律师2电话_label.grid(row=17, column=0, padx=4, pady=4, sticky=tk.E)
代理律师2电话_entry = tk.Entry(input_frame, width=40, textvariable=代理律师2电话)
代理律师2电话_entry.grid(row=17, column=1, padx=4, pady=4, sticky=tk.W)

代理律师2权限_label = tk.Label(input_frame, text="（代理律师2）代理权限")
代理律师2权限_label.grid(row=18, column=0, padx=4, pady=4, sticky=tk.E)
代理律师2特别授权单选按钮= tk.Radiobutton(input_frame, text="特别授权", variable=代理律师1权限, value="特别授权", width=6, anchor=tk.W)
代理律师2一般代理单选按钮= tk.Radiobutton(input_frame, text="一般代理", variable=代理律师1权限, value="一般代理", width=6, anchor=tk.W)
代理律师2特别授权单选按钮.grid(row=18, column=1, padx=3, pady=1, sticky=tk.W)
代理律师2一般代理单选按钮.grid(row=18, column=1, padx=3, pady=1)
# 默认未选中
代理律师2权限.set(None)

# 创建上传组件
def browse_file():
    file_path = filedialog.askopenfilename(title="选择文件",
                                           filetypes=(("所有文件", "*.*"),
                                                      ("文本文件", "*.txt"),
                                                      ("图片文件", "*.jpg;*.png;*.gif")))
    if file_path:
        selected_file_label.config(text=file_path)


# 添加“选择文件”按钮到 input_frame
browse_button = tk.Button(input_frame, text="点击上传", width=12, command=browse_file)
browse_button.grid(row=25, column=0, padx=4, pady=4)

# 添加文件路径标签到 input_frame
selected_file_label = tk.Label(input_frame, text="未选择文件")
selected_file_label.grid(row=25, column=1, columnspan=3, padx=4, pady=4, sticky=tk.W)


# 检查输入的身份证号码是否有效
def is_valid_身份证号码(身份证号码):
    if not re.match(r"^\d{17}(\d|X|x)$", 身份证号码):
        return False
    return True


# 从身份证号码中提取性别
def extract_性别(身份证号码):
    if is_valid_身份证号码(身份证号码):
        return "男" if int(身份证号码[-2]) % 2 == 1 else "女"
    return ""


# 从身份证号码中提取出生日期
def extract_出生日期(身份证号码):
    if is_valid_身份证号码(身份证号码):
        return datetime.strptime(身份证号码[6:14], "%Y%m%d").strftime("%Y年%m月%d日")
    return ""


# 检查输入的手机号码是否有效
def is_valid_phone_number(phone_number):
    if not re.match(r"^1[3-9]\d{9}$", phone_number):
        return False
    return True


# 更新窗口中的输入框
def update_widgets():
    if 委托人性质.get() == "自然人":
        社会信用代码_label.grid_remove()
        社会信用代码_entry.grid_remove()
        法定代表人姓名_label.grid_remove()
        法定代表人姓名_entry.grid_remove()
        法定代表人职务_label.grid_remove()
        法定代表人职务_entry.grid_remove()

        身份证号码_label.grid(row=2, column=0, padx=4, pady=4, sticky=tk.E)
        身份证号码_entry.grid(row=2, column=1, padx=4, pady=4, sticky=tk.W)
        身份证号码_entry.bind("<KeyRelease>", update_gender_and_birthdate)
        性别_label.grid(row=3, column=0, padx=4, pady=4, sticky=tk.E)  # Add this line
        性别_entry.grid(row=3, column=1, padx=4, pady=4, sticky=tk.W)  # Add this line
        出生日期_label.grid(row=4, column=0, padx=4, pady=4, sticky=tk.E)  # Update this line
        出生日期_entry.grid(row=4, column=1, padx=4, pady=4, sticky=tk.W)  # Update this line
        住所_label.grid(row=5, column=0, padx=4, pady=4, sticky=tk.E)  # Update this line
        住所_text.grid(row=5, column=1, padx=4, pady=4, sticky=tk.W)  # Update this line
    else:
        社会信用代码_label.grid(row=2, column=0, padx=4, pady=4, sticky=tk.E)
        社会信用代码_entry.grid(row=2, column=1, padx=4, pady=4, sticky=tk.W)
        住所_label.grid(row=3, column=0, padx=4, pady=4, sticky=tk.E)
        住所_text.grid(row=3, column=1, padx=4, pady=4, sticky=tk.W)
        法定代表人姓名_label.grid(row=4, column=0, padx=4, pady=4, sticky=tk.E)
        法定代表人姓名_entry.grid(row=4, column=1, padx=4, pady=4, sticky=tk.W)
        法定代表人职务_label.grid(row=5, column=0, padx=4, pady=4, sticky=tk.E)
        法定代表人职务_entry.grid(row=5, column=1, padx=4, pady=4, sticky=tk.W)

    if 代理律师人数.get() == 1:
        代理律师2姓名_label.grid_remove()
        代理律师2姓名_entry.grid_remove()
        代理律师2电话_label.grid_remove()
        代理律师2电话_entry.grid_remove()
        代理律师2权限_label.grid_remove()
        代理律师2特别授权单选按钮.grid_remove()
        代理律师2一般代理单选按钮.grid_remove()
        代理律师1姓名_label.grid(row=6 + attorney_row_offset, column=0, padx=4, pady=4, sticky=tk.E)
        代理律师1姓名_entry.grid(row=6 + attorney_row_offset, column=1, padx=4, pady=4, sticky=tk.W)
        代理律师1电话_label.grid(row=7 + attorney_row_offset, column=0, padx=4, pady=4, sticky=tk.E)
        代理律师1电话_entry.grid(row=7 + attorney_row_offset, column=1, padx=4, pady=4, sticky=tk.W)
        代理律师1权限_label.grid(row=8 + attorney_row_offset, column=0, padx=4, pady=4, sticky=tk.E)
        代理律师1特别授权单选按钮.grid(row=8 + attorney_row_offset, column=1, padx=3, pady=1, sticky=tk.W)
        代理律师1一般代理单选按钮.grid(row=8 + attorney_row_offset, column=1, padx=3, pady=1)
    else:
        代理律师1姓名_label.grid(row=6 + attorney_row_offset, column=0, padx=4, pady=4, sticky=tk.E)
        代理律师1姓名_entry.grid(row=6 + attorney_row_offset, column=1, padx=4, pady=4, sticky=tk.W)
        代理律师1电话_label.grid(row=7 + attorney_row_offset, column=0, padx=4, pady=4, sticky=tk.E)
        代理律师1电话_entry.grid(row=7 + attorney_row_offset, column=1, padx=4, pady=4, sticky=tk.W)
        代理律师1权限_label.grid(row=8 + attorney_row_offset, column=0, padx=4, pady=4, sticky=tk.E)
        代理律师1特别授权单选按钮.grid(row=8 + attorney_row_offset, column=1, padx=3, pady=1, sticky=tk.W)
        代理律师1一般代理单选按钮.grid(row=8 + attorney_row_offset, column=1, padx=3, pady=1)
        代理律师2姓名_label.grid(row=9 + attorney_row_offset, column=0, padx=4, pady=4, sticky=tk.E)
        代理律师2姓名_entry.grid(row=9 + attorney_row_offset, column=1, padx=4, pady=4, sticky=tk.W)
        代理律师2电话_label.grid(row=10 + attorney_row_offset, column=0, padx=4, pady=4, sticky=tk.E)
        代理律师2电话_entry.grid(row=10 + attorney_row_offset, column=1, padx=4, pady=4, sticky=tk.W)
        代理律师2权限_label.grid(row=11 + attorney_row_offset, column=0, padx=4, pady=4, sticky=tk.E)
        代理律师2特别授权单选按钮.grid(row=11 + attorney_row_offset, column=1, padx=3, pady=1, sticky=tk.W)
        代理律师2一般代理单选按钮.grid(row=11 + attorney_row_offset, column=1, padx=3, pady=1)


# 根据身份证号码填写性别、出生日期
def update_gender_and_birthdate(event):
    身份证号码_value = 身份证号码.get()
    gender_value = extract_性别(身份证号码_value)
    birthdate_value = extract_出生日期(身份证号码_value)
    性别.set(gender_value)
    出生日期.set(birthdate_value)


# 初始化窗口中的输入框
update_widgets()

# 主循环
window.mainloop()
