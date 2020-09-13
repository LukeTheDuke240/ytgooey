import wx
import subprocess

def downloadvideo(url):
    subprocess.Popen(str(r'youtube-dl -f "bestvideo[ext=mp4 height<=480]+bestaudio[ext=m4a]/best[ext=mp4 height<=480]/best" --no-mtime --all-subs --embed-subs -o "C:/Users/Luke/Videos/4K Video Downloader/%(title)s by %(uploader)s.%(ext)s" ' + str(url)))

class urltextdroptarget(wx.TextDropTarget):
    def __init__(self,object):
        wx.TextDropTarget.__init__(self)
        self.object = object        

    def OnDropText(self,x,y,data):
        if "youtube" in data:
            downloadvideo(data)
            return True
        else:
            return False


class ddframe(wx.Frame):
    def __init__(self, *args, **kw):
        super(ddframe,self).__init__(*args,**kw)
        self.initui()

    def initui(self):
        dt = urltextdroptarget(self)
        self.SetDropTarget(dt)

        self.SetTitle("YTGooey")
        self.Centre()

    def OnDragInit(self,event):
        text = self.GetItemText(event.GetIndex())
        tdo = wx.TextDataObject(text)
        tds = wx.DropSource(self)

        tds.SetData(tdo)
        tds.DoDragDrop(True)

def main():
    app = wx.App()
    ex = ddframe(None)
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
