import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World",size=(400,300))

# 点击按钮次数
clickNum = 0
# 定义一个函数处理点击按钮的事件
def clickButton(event):
    global clickNum
    clickNum  += 1
    # 输出信息到标准输出上
    print(f"点击{clickNum}次")

# 通常 Frame里面不直接放控件，
# 定义一个 面板 Panel，里面放其它控件
panel = wx.Panel(frame, wx.ID_ANY)

# 定义按钮， pos参数指定按钮在panel里面的坐标
# size参数指定按钮控件的宽度和高度，单位为像素
button = wx.Button(panel, wx.ID_ANY, "点击试试",
        pos=(0, 0), size=(100,40))

# 指定该按钮的点击事件的处理函数是 clickButton
button.Bind( wx.EVT_BUTTON, clickButton)

frame.Show(True)
app.MainLoop()