import wx
import os
import youtube_dl
from sys import argv
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
      #button add URL
      self.btn = wx.Button(panel,-1,"add URL") 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClicked)
      #demonstration
      #button Convert Button
      self.btn1 = wx.Button(panel,-1,"convert") 
      vbox.Add(self.btn1,0,wx.ALIGN_CENTER) 
      self.btn1.Bind(wx.EVT_BUTTON,self.OnClickedConvert)

      panel.SetSizer(vbox) 
        
      self.Centre() 
      self.Show() 
      self.Fit()  

   def OnClicked(self, event): 
      btn = self.t3.GetValue()
      # Open the file in append & read mode ('a+')
      with open("songs.txt", "a+") as file_object:
         # Move read cursor to the start of file.
         file_object.seek(0)
         # If file is not empty then append '\n'
         data = file_object.read(100)
         if len(data) > 0 :
            file_object.write("\n")
         # Append text at the end of file
         file_object.write(btn)
      btn = self.t3.SetValue(" ")

   def OnClickedConvert(self, event):
      os.system("python YoutubeToMp3.py songs.txt")
app = wx.App() 
Mywin(None,  'Youtube To Mp3')
app.MainLoop()