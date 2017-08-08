import wx

class windowClass(wx.Frame):
	def __init__( parent, title):
		super(windowClass, self).__init__(parent, title=title, size =(500,300))

		self.Center()
		self.Show()

app = wx.App()
windowClass(None, title='epic window!!')
app.MainLoop()
