# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Calculator
###########################################################################

class Calculator ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calculator", pos = wx.DefaultPosition, size = wx.Size( 260,388 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )

		timelineSizer = wx.BoxSizer( wx.VERTICAL )

		self.Textarea = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 340,50 ), 0 )
		self.Textarea.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		timelineSizer.Add( self.Textarea, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 4, 0, 0 )

		self.buttonKuadrat = wx.Button( self, wx.ID_ANY, u"x²", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonKuadrat, 0, wx.ALL, 5 )

		self.buttonX = wx.Button( self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonX, 0, wx.ALL, 5 )

		self.buttonClear = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonClear, 0, wx.ALL, 5 )

		self.buttonBack = wx.Button( self, wx.ID_ANY, u"⌫", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonBack, 0, wx.ALL, 5 )

		self.buttonSeven = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonSeven, 0, wx.ALL, 5 )

		self.buttonEight = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonEight, 0, wx.ALL, 5 )

		self.buttonNine = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonNine, 0, wx.ALL, 5 )

		self.buttonDivide = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonDivide, 0, wx.ALL, 5 )

		self.buttonFour = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonFour, 0, wx.ALL, 5 )

		self.buttonFive = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonFive, 0, wx.ALL, 5 )

		self.buttonSix = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonSix, 0, wx.ALL, 5 )

		self.buttonMinus = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonMinus, 0, wx.ALL, 5 )

		self.buttonOne = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonOne, 0, wx.ALL, 5 )

		self.buttonTwo = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonTwo, 0, wx.ALL, 5 )

		self.buttonTree = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonTree, 0, wx.ALL, 5 )

		self.buttonPlus = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonPlus, 0, wx.ALL, 5 )

		self.buttonDot = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonDot, 0, wx.ALL, 5 )

		self.buttonZero = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonZero, 0, wx.ALL, 5 )

		self.buttonPM = wx.Button( self, wx.ID_ANY, u"+/-", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonPM, 0, wx.ALL, 5 )

		self.buttonResult = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		gSizer1.Add( self.buttonResult, 0, wx.ALL, 5 )


		bSizer2.Add( gSizer1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		timelineSizer.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( timelineSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonKuadrat.Bind( wx.EVT_BUTTON, self.buttonKuadratOnButtonClick )
		self.buttonX.Bind( wx.EVT_BUTTON, self.buttonXOnButtonClick )
		self.buttonClear.Bind( wx.EVT_BUTTON, self.buttonClearOnButtonClick )
		self.buttonBack.Bind( wx.EVT_BUTTON, self.buttonBackOnButtonClick )
		self.buttonSeven.Bind( wx.EVT_BUTTON, self.buttonSevenOnButtonClick )
		self.buttonEight.Bind( wx.EVT_BUTTON, self.buttonEightOnButtonClick )
		self.buttonNine.Bind( wx.EVT_BUTTON, self.buttonNineOnButtonClick )
		self.buttonDivide.Bind( wx.EVT_BUTTON, self.buttonDivideOnButtonClick )
		self.buttonFour.Bind( wx.EVT_BUTTON, self.buttonFourOnButtonClick )
		self.buttonFive.Bind( wx.EVT_BUTTON, self.buttonFiveOnButtonClick )
		self.buttonSix.Bind( wx.EVT_BUTTON, self.buttonSixOnButtonClick )
		self.buttonMinus.Bind( wx.EVT_BUTTON, self.buttonMinusOnButtonClick )
		self.buttonOne.Bind( wx.EVT_BUTTON, self.buttonOneOnButtonClick )
		self.buttonTwo.Bind( wx.EVT_BUTTON, self.buttonTwoOnButtonClick )
		self.buttonTree.Bind( wx.EVT_BUTTON, self.buttonTreeOnButtonClick )
		self.buttonPlus.Bind( wx.EVT_BUTTON, self.buttonPlusOnButtonClick )
		self.buttonDot.Bind( wx.EVT_BUTTON, self.buttonDotOnButtonClick )
		self.buttonZero.Bind( wx.EVT_BUTTON, self.buttonZeroOnButtonClick )
		self.buttonPM.Bind( wx.EVT_BUTTON, self.buttonPMOnButtonClick )
		self.buttonResult.Bind( wx.EVT_BUTTON, self.buttonResultOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def buttonKuadratOnButtonClick( self, event ):
		event.Skip()

	def buttonXOnButtonClick( self, event ):
		event.Skip()

	def buttonClearOnButtonClick( self, event ):
		event.Skip()

	def buttonBackOnButtonClick( self, event ):
		event.Skip()

	def buttonSevenOnButtonClick( self, event ):
		event.Skip()

	def buttonEightOnButtonClick( self, event ):
		event.Skip()

	def buttonNineOnButtonClick( self, event ):
		event.Skip()

	def buttonDivideOnButtonClick( self, event ):
		event.Skip()

	def buttonFourOnButtonClick( self, event ):
		event.Skip()

	def buttonFiveOnButtonClick( self, event ):
		event.Skip()

	def buttonSixOnButtonClick( self, event ):
		event.Skip()

	def buttonMinusOnButtonClick( self, event ):
		event.Skip()

	def buttonOneOnButtonClick( self, event ):
		event.Skip()

	def buttonTwoOnButtonClick( self, event ):
		event.Skip()

	def buttonTreeOnButtonClick( self, event ):
		event.Skip()

	def buttonPlusOnButtonClick( self, event ):
		event.Skip()

	def buttonDotOnButtonClick( self, event ):
		event.Skip()

	def buttonZeroOnButtonClick( self, event ):
		event.Skip()

	def buttonPMOnButtonClick( self, event ):
		event.Skip()

	def buttonResultOnButtonClick( self, event ):
		event.Skip()


