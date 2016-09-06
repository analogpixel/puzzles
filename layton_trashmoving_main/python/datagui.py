import wx
import wx.xrc
import wx.grid
import wx.propgrid as pg

# http://zetcode.com/wxpython/gdi/
# https://github.com/cool-RR/PythonTurtle/tree/master/src
# http://zetcode.com/wxpython/customwidgets/

class turtle(wx.Panel):
  def __init__(self, parent, *args,**kwargs):
    wx.Panel.__init__(self, parent,style=wx.SUNKEN_BORDER,  *args,**kwargs)
    self.BACKGROUND_COLOR = wx.Colour(212,2,200)
    self.Bind(wx.EVT_PAINT, self.onPaint)
    self.Show()

  def onPaint(self,event):
    dc = wx.PaintDC(self)
    pen2 = wx.Pen('#4c4c4c', 1, wx.SOLID)
    dc.SetPen(pen2)
    dc.DrawLine(30, 130, 30, 250)
    dc.DrawLine(150, 130, 150, 250)
    dc.DrawLine(155, 130, 155, 250)


class dataSolver( wx.Frame):

  def __init__(self, parent):
    wx.Frame.__init__( self, parent, id=wx.ID_ANY, title="Data Solver")
    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    #solution variables
    numTries = 25

    bSizer1 = wx.BoxSizer(wx.HORIZONTAL)
    bSizer2 = wx.BoxSizer(wx.VERTICAL) # grid
    bSizer3 = wx.BoxSizer(wx.VERTICAL) # turtles

    b1 = wx.Panel(self);
    b2 = wx.Panel(self);
    t1 = turtle(b1, size=(400,400))
    t2 = turtle(b2, size=(400,400))

    bSizer3.Add(b1)
    bSizer3.Add(b2)

    self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

    # Grid
    self.m_grid1.CreateGrid( numTries, 1 )
    self.m_grid1.EnableEditing( True )
    self.m_grid1.EnableGridLines( True )
    self.m_grid1.EnableDragGridSize( False )
    self.m_grid1.SetMargins( 0, 0 )

    # Columns
    self.m_grid1.EnableDragColMove( False )
    self.m_grid1.EnableDragColSize( True )
    self.m_grid1.SetColLabelSize( 30 )
    self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

    # Rows
    self.m_grid1.EnableDragRowSize( True )
    self.m_grid1.SetRowLabelSize( 80 )
    self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

    # Label Appearance

    # Cell Defaults
    self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )

    bSizer2.Add(self.m_grid1)


    # turtles

    bSizer1.Add( bSizer2 , 1, wx.FIXED_MINSIZE, 5 )
    bSizer1.Add( bSizer3 , 1, wx.FIXED_MINSIZE, 5 )
    self.SetSizerAndFit(bSizer1)
    self.Layout()
    self.Centre(wx.BOTH)

  def __del__(self):
    pass


app=wx.App()
frame = dataSolver(None)
frame.Show()
app.MainLoop()
