import wx
import sys

class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)

    def OnInit(self):
        frame = wx.Frame(None, -1, "Test")
        #, pos=(50,50), size=(100,40))
        box = wx.BoxSizer(wx.VERTICAL)
        files=sys.argv
        for f in files:
            box.Add(wx.Button(frame, -1, "%s"%f, ))
        frame.SetAutoLayout(True)
        frame.SetSizer(box)
        frame.Layout()
        frame.Show()
        return True

app = MyApp()
app.MainLoop()
