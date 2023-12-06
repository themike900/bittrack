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
import wx.richtext

###########################################################################
## Class BaseFrame
###########################################################################

class BaseFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bittrack", pos = wx.DefaultPosition, size = wx.Size( 850,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,500 ), wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		mainSizer_vert = wx.BoxSizer( wx.VERTICAL )

		mainSizer_hor = wx.BoxSizer( wx.HORIZONTAL )

		mainSizer_hor.SetMinSize( wx.Size( 100,-1 ) )
		listSizer = wx.BoxSizer( wx.VERTICAL )

		self.transactionList = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		self.transactionList.SetMinSize( wx.Size( 540,-1 ) )

		self.colTid = self.transactionList.AppendTextColumn( u"tID", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.colDate = self.transactionList.AppendTextColumn( u"Date", wx.dataview.DATAVIEW_CELL_INERT, 130, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.colType = self.transactionList.AppendTextColumn( u"Type", wx.dataview.DATAVIEW_CELL_INERT, 100, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.colInput = self.transactionList.AppendTextColumn( u"FromTo", wx.dataview.DATAVIEW_CELL_INERT, 170, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.colValue = self.transactionList.AppendTextColumn( u"Value", wx.dataview.DATAVIEW_CELL_INERT, 80, wx.ALIGN_RIGHT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.colCur = self.transactionList.AppendTextColumn( u"Cur", wx.dataview.DATAVIEW_CELL_INERT, 30, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		listSizer.Add( self.transactionList, 2, wx.ALL, 5 )

		self.m_button61 = wx.Button( self, wx.ID_ANY, u"New Transaction", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		listSizer.Add( self.m_button61, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		mainSizer_hor.Add( listSizer, 0, wx.EXPAND, 5 )

		detailSizer_vert = wx.BoxSizer( wx.VERTICAL )

		sizerTransaction = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Transaction" ), wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText6 = wx.StaticText( sizerTransaction.GetStaticBox(), wx.ID_ANY, u"Datetime", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer2.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.fd_datetime = wx.TextCtrl( sizerTransaction.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fd_datetime.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.fd_datetime.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer2.Add( self.fd_datetime, 0, wx.ALL, 5 )

		self.ld_type = wx.StaticText( sizerTransaction.GetStaticBox(), wx.ID_ANY, u"Type", wx.Point( -1,-1 ), wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.ld_type.Wrap( -1 )

		self.ld_type.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer2.Add( self.ld_type, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.fd_type = wx.TextCtrl( sizerTransaction.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fd_type.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.fd_type.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer2.Add( self.fd_type, 0, wx.ALL, 5 )


		sizerTransaction.Add( fgSizer2, 0, wx.EXPAND, 5 )


		detailSizer_vert.Add( sizerTransaction, 0, wx.EXPAND, 5 )

		SizerInput = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Transaction Input" ), wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.ld_input = wx.StaticText( SizerInput.GetStaticBox(), wx.ID_ANY, u"Input", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
		self.ld_input.Wrap( -1 )

		self.ld_input.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer1.Add( self.ld_input, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.fd_input = wx.TextCtrl( SizerInput.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fd_input.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.fd_input.SetMinSize( wx.Size( 100,-1 ) )

		fgSizer1.Add( self.fd_input, 0, wx.ALL, 5 )

		self.ld_inputval = wx.StaticText( SizerInput.GetStaticBox(), wx.ID_ANY, u"Value", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.ld_inputval.Wrap( -1 )

		self.ld_inputval.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer1.Add( self.ld_inputval, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.fd_inputval = wx.TextCtrl( SizerInput.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.fd_inputval.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.fd_inputval.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.fd_inputval.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.fd_inputval.SetMinSize( wx.Size( 100,-1 ) )

		fgSizer1.Add( self.fd_inputval, 0, wx.ALL, 5 )


		SizerInput.Add( fgSizer1, 0, wx.EXPAND, 5 )


		detailSizer_vert.Add( SizerInput, 0, wx.EXPAND, 5 )

		sizerOutput = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Transaction Output" ), wx.VERTICAL )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( sizerOutput.GetStaticBox(), wx.ID_ANY, u"Output", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer3.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.fd_output = wx.TextCtrl( sizerOutput.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fd_output.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.fd_output.SetMinSize( wx.Size( 100,-1 ) )

		fgSizer3.Add( self.fd_output, 0, wx.ALL, 5 )

		self.ld_outputval = wx.StaticText( sizerOutput.GetStaticBox(), wx.ID_ANY, u"Value", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.ld_outputval.Wrap( -1 )

		self.ld_outputval.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer3.Add( self.ld_outputval, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.fd_outputval = wx.TextCtrl( sizerOutput.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.fd_outputval.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.fd_outputval.SetMinSize( wx.Size( 100,-1 ) )

		fgSizer3.Add( self.fd_outputval, 0, wx.ALL, 5 )


		sizerOutput.Add( fgSizer3, 0, wx.EXPAND, 5 )


		detailSizer_vert.Add( sizerOutput, 0, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Transaction Fee" ), wx.VERTICAL )

		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.ld_fee = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Fee", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
		self.ld_fee.Wrap( -1 )

		self.ld_fee.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer4.Add( self.ld_fee, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.fd_fee = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.fd_fee.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.fd_fee.SetMinSize( wx.Size( 100,-1 ) )

		fgSizer4.Add( self.fd_fee, 0, wx.ALL, 5 )

		self.ld_fraction = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"0,0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ld_fraction.Wrap( -1 )

		self.ld_fraction.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer4.Add( self.ld_fraction, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		sbSizer4.Add( fgSizer4, 0, wx.EXPAND, 5 )


		detailSizer_vert.Add( sbSizer4, 0, wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Save Changes", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		detailSizer_vert.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		detailSizer_vert.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		mainSizer_hor.Add( detailSizer_vert, 1, wx.EXPAND, 5 )


		mainSizer_vert.Add( mainSizer_hor, 1, wx.EXPAND, 5 )


		self.SetSizer( mainSizer_vert )
		self.Layout()

		self.menubar1 = wx.MenuBar( 0 )
		self.menu = wx.Menu()
		self.m_about = wx.MenuItem( self.menu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu.Append( self.m_about )

		self.m_close = wx.MenuItem( self.menu, wx.ID_ANY, u"close", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu.Append( self.m_close )

		self.menubar1.Append( self.menu, u"Menu" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Wallet values", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )

		self.menubar1.Append( self.m_menu2, u"Statistics" )

		self.SetMenuBar( self.menubar1 )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.transactionList.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.onSelectionChanged, id = wx.ID_ANY )
		self.Bind( wx.EVT_MENU, self.aboutaction, id = self.m_about.GetId() )
		self.Bind( wx.EVT_MENU, self.closeaction, id = self.m_close.GetId() )
		self.Bind( wx.EVT_MENU, self.onOpenWalletSums, id = self.m_menuItem3.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def onSelectionChanged( self, event ):
		event.Skip()

	def aboutaction( self, event ):
		event.Skip()

	def closeaction( self, event ):
		event.Skip()

	def onOpenWalletSums( self, event ):
		event.Skip()


###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 280,230 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Bittracker", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer5.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, u"Bittracker version 0.0.0\nA tool to track your bitcoin transactions,\nusing a SQLLite 3 database,\nrunning on Python 3.11 \nand wxPython 4.2.1", wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.m_richText1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_richText1.SetMinSize( wx.Size( 300,250 ) )

		bSizer5.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )

		self.b_ok = wx.Button( self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.b_ok, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.b_ok.Bind( wx.EVT_BUTTON, self.onOK )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def onOK( self, event ):
		event.Skip()


###########################################################################
## Class sumDialog
###########################################################################

class sumDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,800 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.Size( 350,500 ), wx.DefaultSize )

		sumDialogSizer = wx.BoxSizer( wx.VERTICAL )

		sizerNcWallets = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Noncustodial Wallets" ), wx.VERTICAL )

		sizerNcWallets.SetMinSize( wx.Size( -1,100 ) )
		self.ncWalletList = wx.dataview.DataViewListCtrl( sizerNcWallets.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 280,-1 ), wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		self.ncwalletname = self.ncWalletList.AppendTextColumn( u"Wallet", wx.dataview.DATAVIEW_CELL_INERT, 90, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.ncwalletvalue = self.ncWalletList.AppendTextColumn( u"Value Sum", wx.dataview.DATAVIEW_CELL_INERT, 100, wx.ALIGN_RIGHT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.ncwalletfiat = self.ncWalletList.AppendTextColumn( u"Fiat", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_RIGHT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		sizerNcWallets.Add( self.ncWalletList, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		sumDialogSizer.Add( sizerNcWallets, 11, wx.EXPAND, 5 )

		sizerCWallets = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Custodial Wallets" ), wx.VERTICAL )

		sizerCWallets.SetMinSize( wx.Size( -1,100 ) )
		self.cWalletList = wx.dataview.DataViewListCtrl( sizerCWallets.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 280,-1 ), wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		self.cwalletname = self.cWalletList.AppendTextColumn( u"Wallet", wx.dataview.DATAVIEW_CELL_INERT, 90, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.cwalletvalue2 = self.cWalletList.AppendTextColumn( u"Value Sum", wx.dataview.DATAVIEW_CELL_INERT, 100, wx.ALIGN_RIGHT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.cwalletfiat = self.cWalletList.AppendTextColumn( u"Fiat", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_RIGHT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		sizerCWallets.Add( self.cWalletList, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		sumDialogSizer.Add( sizerCWallets, 4, wx.EXPAND, 5 )

		sizerLNWallets = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Lightning Wallets" ), wx.VERTICAL )

		sizerLNWallets.SetMinSize( wx.Size( -1,100 ) )
		self.lnWalletList = wx.dataview.DataViewListCtrl( sizerLNWallets.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 280,-1 ), wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		self.lnwalletname = self.lnWalletList.AppendTextColumn( u"Wallet", wx.dataview.DATAVIEW_CELL_INERT, 90, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.lnwalletvalue = self.lnWalletList.AppendTextColumn( u"Value Sum", wx.dataview.DATAVIEW_CELL_INERT, 100, wx.ALIGN_RIGHT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.lnwalletfiat = self.lnWalletList.AppendTextColumn( u"Fiat", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_RIGHT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		sizerLNWallets.Add( self.lnWalletList, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		sumDialogSizer.Add( sizerLNWallets, 9, wx.EXPAND, 5 )

		sizerSum = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"wallet sum" ), wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.sumLabel = wx.StaticText( sizerSum.GetStaticBox(), wx.ID_ANY, u"all sum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sumLabel.Wrap( -1 )

		bSizer7.Add( self.sumLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.fd_allsum = wx.TextCtrl( sizerSum.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.TE_RIGHT )
		bSizer7.Add( self.fd_allsum, 0, wx.ALL, 5 )

		self.fd_allsumfiat = wx.TextCtrl( sizerSum.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,-1 ), wx.TE_RIGHT )
		bSizer7.Add( self.fd_allsumfiat, 0, wx.ALL, 5 )


		sizerSum.Add( bSizer7, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sumDialogSizer.Add( sizerSum, 0, wx.EXPAND, 5 )

		self.ok_button = wx.Button( self, wx.ID_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		sumDialogSizer.Add( self.ok_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( sumDialogSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


