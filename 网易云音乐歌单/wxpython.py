#!/bin/python
import wx # 导入wx这个module

class HelloFrame(wx.Frame):
	def __init__(self,*args,**kw):
		#确保父函数被调用
		super(HelloFrame,self).__init__(*args,**kw)
		#在框架中创建一个面板
		pnl = wx.Panel(self)
		#在这个面板中输入字体加粗加大的文字
		st.wx.StaticText(pnl,label='人生苦短，我用Python',pos=(25,25))
		font = st.GetFont()
		font.PointSize += 10
		font = font.Bold()
		st.SetFont(font)

		#创建一个菜单栏
		self.makeMenuBar()
		#创建一个状态栏
		self.CreateStatusBar()
		self.SetStatusText('Welcome to wxPython')
		
