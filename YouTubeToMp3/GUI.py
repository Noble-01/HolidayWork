import wx # First things, first. Import the wxPython package.
app = wx.App() # Next, create an application object. 
frm = wx.Frame(None, wx.ID_ANY, title="Youtube to MP3") # Then a frame. 
frm.Show() # Show it. 
app.MainLoop() # Start the event loop. 
