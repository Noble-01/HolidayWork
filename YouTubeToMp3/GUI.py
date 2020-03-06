import wx
  
class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (350,250))
		
      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 

		#label
      hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
      l3 = wx.StaticText(panel, -1, "Enter URL") 
		#create multiline textfield
      hbox3.Add(l3,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      self.t3 = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE) 
		
      hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      vbox.Add(hbox3) 
      #button click me
      self.btn = wx.Button(panel,-1,"click Me") 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClicked)

      panel.SetSizer(vbox) 
        
      self.Centre() 
      self.Show() 
      self.Fit()  
		
   def OnKeyTyped(self, event): 
       print(event.GetString())
   def OnClicked(self, event): 
      btn = self.t3.GetValue()

app = wx.App() 
Mywin(None,  'Youtube To Mp3')
app.MainLoop()