# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 834,452 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer4.SetMinSize( wx.Size( 100,-1 ) )
		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListCtrl1.SetMinSize( wx.Size( 100,-1 ) )

		bSizer4.Add( self.m_dataViewListCtrl1, 0, wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button5, 0, wx.ALL, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button4, 0, wx.ALL, 5 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button7, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu = wx.Menu()
		self.m_close = wx.MenuItem( self.m_menu, wx.ID_ANY, u"close", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu.Append( self.m_close )

		self.m_menubar1.Append( self.m_menu, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.closeaction, id = self.m_close.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def closeaction( self, event ):
		event.Skip()


