# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ASTRAL Command Line Generator - v0.1 (beta)", pos = wx.DefaultPosition, size = wx.Size( 864,627 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TAB_TRAVERSAL|wx.VSCROLL )
		self.main_panel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.main_panel.SetBackgroundColour( wx.Colour( 255, 255, 193 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer68.AddSpacer( ( 5, 0), 0, 0, 0 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.main_panel, wx.ID_ANY, u"Input/Output" ), wx.VERTICAL )
		
		sizer_input = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Input File [-i]", wx.DefaultPosition, wx.Size( 105,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.m_staticText11.SetToolTipString( u"a file containing input gene trees in newick format. (required)" )
		
		sizer_input.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_file_input = wx.FilePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN )
		self.m_file_input.SetBackgroundColour( wx.Colour( 255, 255, 193 ) )
		
		sizer_input.Add( self.m_file_input, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer2.Add( sizer_input, 0, wx.EXPAND, 5 )
		
		sizer_output = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText111 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Output File (-o)", wx.DefaultPosition, wx.Size( 105,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText111.Wrap( -1 )
		self.m_staticText111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.m_staticText111.SetToolTipString( u"a filename for storing the output species tree. Defaults to outputting to stdout." )
		
		sizer_output.Add( self.m_staticText111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_file_output = wx.FilePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_file_output.SetBackgroundColour( wx.Colour( 255, 255, 193 ) )
		
		sizer_output.Add( self.m_file_output, 1, wx.ALL, 5 )
		
		
		sbSizer2.Add( sizer_output, 0, wx.EXPAND, 5 )
		
		sizer_namemap = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText37 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Name Mapping [-a]", wx.DefaultPosition, wx.Size( 105,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText37.Wrap( -1 )
		self.m_staticText37.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText37.SetToolTipString( u"a file containing the mapping between names in gene tree and names in the species tree. The mapping file has one line per species, with one of two formats:\n1.) species: gene1,gene2,gene3,gene4\n2.) species 4 gene1 gene2 gene3 gene4" )
		
		sizer_namemap.Add( self.m_staticText37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_file_namemap = wx.FilePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_file_namemap.SetBackgroundColour( wx.Colour( 255, 255, 193 ) )
		
		sizer_namemap.Add( self.m_file_namemap, 1, wx.ALL, 5 )
		
		
		sbSizer2.Add( sizer_namemap, 0, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.main_panel, wx.ID_ANY, u"Search Arguments" ), wx.VERTICAL )
		
		bSizer5111 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer5111.AddSpacer( ( 10, 0), 0, 0, 5 )
		
		self.m_cb_exact = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Find Exact Solution? [-x]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_exact.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_cb_exact.SetToolTipString( u"find the exact solution by looking at all clusters - recommended only for small (<18) numer of taxa." )
		
		bSizer5111.Add( self.m_cb_exact, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5111.AddSpacer( ( 10, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer5111, 0, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_st_extralevel = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Level of extra bipartitions added [-p]", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_st_extralevel.Wrap( -1 )
		self.m_st_extralevel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_st_extralevel.SetToolTipString( u"How much extra bipartitions should be added: 0, 1, or 2. (default: 1)\n0: adds nothing extra. \n1: adds to X but not excessively (greedy resolutions).\n2: addes a potentially large number and therefore can be slow (quadratic distance-based).\n" )
		
		bSizer17.Add( self.m_st_extralevel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_extralevelChoices = [ u"0 - Nothing", u"1 - Some", u"2 - Many" ]
		self.m_choice_extralevel = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_extralevelChoices, 0 )
		self.m_choice_extralevel.SetSelection( 1 )
		self.m_choice_extralevel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_choice_extralevel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer17.Add( self.m_choice_extralevel, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer17, 0, wx.EXPAND, 5 )
		
		sizer_extragenes = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_st_extragenes = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Extra gene trees [-e]", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT )
		self.m_st_extragenes.Wrap( -1 )
		self.m_st_extragenes.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_st_extragenes.SetToolTipString( u"provide extra trees (with gene labels) used to enrich the set of clusters searched" )
		
		sizer_extragenes.Add( self.m_st_extragenes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_file_extragenes = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_file_extragenes.SetBackgroundColour( wx.Colour( 255, 255, 193 ) )
		self.m_file_extragenes.SetToolTipString( u"provide extra trees (with species lables) used to enrich the set of clusters searched" )
		
		sizer_extragenes.Add( self.m_file_extragenes, 1, wx.ALL, 5 )
		
		
		sbSizer1.Add( sizer_extragenes, 0, wx.EXPAND, 5 )
		
		sizer_extraspecies = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_st_extraspecies = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Extra species trees [-f]", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT )
		self.m_st_extraspecies.Wrap( -1 )
		self.m_st_extraspecies.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_st_extraspecies.SetToolTipString( u"provide extra trees (with species lables) used to enrich the set of clusters searched" )
		
		sizer_extraspecies.Add( self.m_st_extraspecies, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_file_extraspecies = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_file_extraspecies.SetBackgroundColour( wx.Colour( 255, 255, 193 ) )
		self.m_file_extraspecies.SetToolTipString( u"provide extra trees (with species lables) used to enrich the set of clusters searched" )
		
		sizer_extraspecies.Add( self.m_file_extraspecies, 1, wx.ALL, 5 )
		
		
		sbSizer1.Add( sizer_extraspecies, 0, wx.EXPAND, 5 )
		
		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer58.AddSpacer( ( 10, 0), 0, 0, 0 )
		
		self.m_cb_min_leaves = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Minimum # of Leaves [-m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_min_leaves.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_cb_min_leaves.SetToolTipString( u"Remove genes with less than specificed number of leaves" )
		
		bSizer58.Add( self.m_cb_min_leaves, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_txt_min_leaves = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_RIGHT )
		self.m_txt_min_leaves.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.m_txt_min_leaves.Enable( False )
		self.m_txt_min_leaves.SetToolTipString( u"Remove genes with less than specificed number of leaves" )
		
		bSizer58.Add( self.m_txt_min_leaves, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer58, 0, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer1, 0, wx.EXPAND, 5 )
		
		
		bSizer68.Add( bSizer3, 1, 0, 5 )
		
		
		bSizer68.AddSpacer( ( 10, 0), 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.main_panel, wx.ID_ANY, u"Algorithm" ), wx.VERTICAL )
		
		sizer_score_and_exit = wx.BoxSizer( wx.HORIZONTAL )
		
		
		sizer_score_and_exit.AddSpacer( ( 10, 0), 0, 0, 0 )
		
		self.m_cb_score_and_exit = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Score species tree and exit [-q]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_score_and_exit.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_cb_score_and_exit.SetToolTipString( u"score the provided species tree and exit" )
		
		sizer_score_and_exit.Add( self.m_cb_score_and_exit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_file_score_and_exit = wx.FilePickerCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_file_score_and_exit.SetBackgroundColour( wx.Colour( 255, 255, 193 ) )
		self.m_file_score_and_exit.Enable( False )
		self.m_file_score_and_exit.SetToolTipString( u"score the provided species tree and exit" )
		
		sizer_score_and_exit.Add( self.m_file_score_and_exit, 1, wx.ALL, 5 )
		
		
		sbSizer4.Add( sizer_score_and_exit, 0, wx.EXPAND, 5 )
		
		bSizer59 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer59.AddSpacer( ( 10, 0), 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_cb_dyna_min_dup = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Use DynaDup to minimize duplications [-d]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_dyna_min_dup.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_cb_dyna_min_dup.SetToolTipString( u"Solves MGD problem. Minimizes the number duplications required to explain gene trees using DynaDup algorithm (Bayzid, 2011). Note that with this option, DynaDyp would be used *instead of* ASTRAL." )
		
		bSizer59.Add( self.m_cb_dyna_min_dup, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer4.Add( bSizer59, 0, wx.EXPAND, 5 )
		
		bSizer591 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer591.AddSpacer( ( 10, 0), 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_cb_dyna_min_duploss = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Use DynaDup to minimize duplications and losses [-l]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_dyna_min_duploss.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_cb_dyna_min_duploss.SetToolTipString( u"Solves MGDL problem. Minimizes the number duplication and losses required to explain gene trees using DynaDup algorithm. Note that with this option, DynaDyp would be used *instead of* ASTRAL. Use -l 0 for standard (homomorphic) definition, and -l 1 for our new bd definition. Any value in between weights the impact of missing taxa somewhere between these two extremes. -l auto will automaticaly pick this weight." )
		
		bSizer591.Add( self.m_cb_dyna_min_duploss, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer4.Add( bSizer591, 0, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer27.AddSpacer( ( 50, 0), 0, 0, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Dup/Loss Weight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer27.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_txt_duploss_weight = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_txt_duploss_weight.Enable( False )
		
		bSizer27.Add( self.m_txt_duploss_weight, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_cb_duploss_auto = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"(auto)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_duploss_auto.SetValue(True) 
		self.m_cb_duploss_auto.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer27.Add( self.m_cb_duploss_auto, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer4.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer4, 0, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.main_panel, wx.ID_ANY, u"Bootstrap Arguments" ), wx.VERTICAL )
		
		sizer_bootstraps = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_cb_bootstraps = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Bootstraps [-b]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_bootstraps.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_cb_bootstraps.SetToolTipString( u"perform multi-locus bootstrapping using input bootstrap replicate files (use --rep to change the number of replications). The file given with this option should have a list of the gene tree bootstrap files, one per line, and each line corresponding to one gene. By default performs site-only resampling, but gene/site resampling can also be used." )
		
		sizer_bootstraps.Add( self.m_cb_bootstraps, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_file_bootstrap_reps = wx.FilePickerCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_file_bootstrap_reps.SetBackgroundColour( wx.Colour( 255, 255, 193 ) )
		self.m_file_bootstrap_reps.Enable( False )
		
		sizer_bootstraps.Add( self.m_file_bootstrap_reps, 1, wx.ALL, 5 )
		
		
		sbSizer3.Add( sizer_bootstraps, 0, wx.EXPAND, 5 )
		
		bSizer17121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText14121 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"# of Replicates [-r]", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText14121.Wrap( -1 )
		self.m_staticText14121.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText14121.SetToolTipString( u"Set the number of bootstrap replicates done in multi-locus bootstrapping.  (default: 100)" )
		
		bSizer17121.Add( self.m_staticText14121, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_txt_bootreps = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"100", wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_RIGHT )
		self.m_txt_bootreps.Enable( False )
		self.m_txt_bootreps.SetToolTipString( u"Set the number of bootstrap replicates done in multi-locus bootstrapping.  (default: 100)" )
		
		bSizer17121.Add( self.m_txt_bootreps, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer17121, 0, wx.EXPAND, 5 )
		
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer38.AddSpacer( ( 20, 0), 0, 0, 5 )
		
		self.m_staticText28 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Keep [-k]:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		self.m_staticText28.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_staticText28.SetToolTipString( u"When -k option is used, -o option needs to be given. The file name specified using -o is used as the prefix for the name of the extra output files." )
		
		bSizer38.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 2, 3, 0, 0 )
		
		self.m_cb_k_completed = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Completed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_k_completed.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_cb_k_completed.SetToolTipString( u"-k completed: outputs completed gene trees (i.e. after adding missing taxa) to a file called [output file name].completed_gene_trees." )
		
		gSizer1.Add( self.m_cb_k_completed, 0, wx.ALL, 5 )
		
		self.m_cb_k_boots = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Bootstraps", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_k_boots.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_cb_k_boots.SetToolTipString( u"-k bootstraps: outputs individual bootstrap replciates to a file called [output file name].[i].bs" )
		
		gSizer1.Add( self.m_cb_k_boots, 0, wx.ALL, 5 )
		
		self.m_cb_k_searchspace = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Search space", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_k_searchspace.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_cb_k_searchspace.SetToolTipString( u"-k searchspace: outputs the search space and then continues the run." )
		
		gSizer1.Add( self.m_cb_k_searchspace, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_cb_k_boots_norun = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Bootstraps (NR)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_k_boots_norun.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_cb_k_boots_norun.SetToolTipString( u"-k bootstraps_norun: just like -k bootstraps, but exits after outputting bootstraps." )
		
		gSizer1.Add( self.m_cb_k_boots_norun, 0, wx.ALL, 5 )
		
		self.m_cb_k_search_norun = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Search space (NR)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_k_search_norun.SetToolTipString( u"-k searchspace_norun: outputs the search space and exits; use searchspace to continue the run after outputting the search space." )
		
		gSizer1.Add( self.m_cb_k_search_norun, 0, wx.ALL, 5 )
		
		
		bSizer38.Add( gSizer1, 1, 0, 5 )
		
		
		sbSizer3.Add( bSizer38, 0, 0, 5 )
		
		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText32 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Seed [-s]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText32.SetToolTipString( u"Set the seed number used in multi-locus bootstrapping.  (default: 692)" )
		
		bSizer54.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_txt_seed = wx.SpinCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"692", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000000, 692 )
		self.m_txt_seed.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_txt_seed.Enable( False )
		
		bSizer54.Add( self.m_txt_seed, 0, wx.ALL, 5 )
		
		
		bSizer54.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_cb_gene_resampling = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Gene tree resampling? [-g]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cb_gene_resampling.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_cb_gene_resampling.SetToolTipString( u"perform gene tree resampling in addition to site resampling. Useful only with the -b option." )
		
		bSizer54.Add( self.m_cb_gene_resampling, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer3.Add( bSizer54, 0, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer3, 0, wx.EXPAND, 5 )
		
		
		bSizer68.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer68.AddSpacer( ( 5, 0), 0, 0, 0 )
		
		
		bSizer2.Add( bSizer68, 0, wx.EXPAND, 5 )
		
		self.m_staticline8 = wx.StaticLine( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self.main_panel, wx.ID_ANY, u"ASTRAL Command:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_staticText44.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer2.Add( self.m_staticText44, 0, wx.ALL, 2 )
		
		self.m_txt_output_command = wx.TextCtrl( self.main_panel, wx.ID_ANY, u"ASTRAL Command Line Generator", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_txt_output_command.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer2.Add( self.m_txt_output_command, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.main_panel.SetSizer( bSizer2 )
		self.main_panel.Layout()
		bSizer2.Fit( self.main_panel )
		bSizer1.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 2 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menubar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_menubar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		self.m_menu_file = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem6 )
		
		self.m_menuItem1 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Open"+ u"\t" + u"CTRL+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Save"+ u"\t" + u"CTRL+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Save As"+ u"\t" + u"CTRL+A", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem3 )
		
		self.m_menu_file.AppendSeparator()
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem5 )
		
		self.m_menubar1.Append( self.m_menu_file, u"File" ) 
		
		self.m_menu_help = wx.Menu()
		self.m_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.AppendItem( self.m_about )
		
		self.m_menubar1.Append( self.m_menu_help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_file_input.Bind( wx.EVT_FILEPICKER_CHANGED, self.change_input_file )
		self.m_file_output.Bind( wx.EVT_FILEPICKER_CHANGED, self.change_output_file )
		self.m_file_namemap.Bind( wx.EVT_FILEPICKER_CHANGED, self.change_name_mapping )
		self.m_cb_exact.Bind( wx.EVT_CHECKBOX, self.toggle_find_exact )
		self.m_choice_extralevel.Bind( wx.EVT_CHOICE, self.change_extra_level )
		self.m_file_extragenes.Bind( wx.EVT_FILEPICKER_CHANGED, self.change_file_extragenes )
		self.m_file_extraspecies.Bind( wx.EVT_FILEPICKER_CHANGED, self.change_file_extraspecies )
		self.m_cb_min_leaves.Bind( wx.EVT_CHECKBOX, self.toggle_min_leaves_required )
		self.m_txt_min_leaves.Bind( wx.EVT_TEXT, self.change_min_leaves )
		self.m_cb_score_and_exit.Bind( wx.EVT_CHECKBOX, self.toggle_cb_score_and_exit )
		self.m_file_score_and_exit.Bind( wx.EVT_FILEPICKER_CHANGED, self.change_file_score_and_exit )
		self.m_cb_dyna_min_dup.Bind( wx.EVT_CHECKBOX, self.toggle_dyn_dup )
		self.m_cb_dyna_min_duploss.Bind( wx.EVT_CHECKBOX, self.toggle_dyn_duploss )
		self.m_txt_duploss_weight.Bind( wx.EVT_TEXT_ENTER, self.enter_text_duploss_weight )
		self.m_cb_duploss_auto.Bind( wx.EVT_CHECKBOX, self.tog_dynduploss_auto )
		self.m_cb_bootstraps.Bind( wx.EVT_CHECKBOX, self.toggle_bootstrap )
		self.m_file_bootstrap_reps.Bind( wx.EVT_FILEPICKER_CHANGED, self.change_file_bootstrap )
		self.m_cb_k_completed.Bind( wx.EVT_CHECKBOX, self.toggle_k_completed )
		self.m_cb_k_boots.Bind( wx.EVT_CHECKBOX, self.toggle_k_boots )
		self.m_cb_k_searchspace.Bind( wx.EVT_CHECKBOX, self.toggle_k_search )
		self.m_cb_k_boots_norun.Bind( wx.EVT_CHECKBOX, self.toggle_k_boots_norun )
		self.m_cb_k_search_norun.Bind( wx.EVT_CHECKBOX, self.toggle_k_search_norun )
		self.m_txt_seed.Bind( wx.EVT_SPINCTRL, self.change_seed )
		self.m_cb_gene_resampling.Bind( wx.EVT_CHECKBOX, self.toggle_gene_resampling )
		self.Bind( wx.EVT_MENU, self.new_settings, id = self.m_menuItem6.GetId() )
		self.Bind( wx.EVT_MENU, self.open_settings, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.save_settings, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.save_as_settings, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.config_astral, id = self.m_menuItem5.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def change_input_file( self, event ):
		event.Skip()
	
	def change_output_file( self, event ):
		event.Skip()
	
	def change_name_mapping( self, event ):
		event.Skip()
	
	def toggle_find_exact( self, event ):
		event.Skip()
	
	def change_extra_level( self, event ):
		event.Skip()
	
	def change_file_extragenes( self, event ):
		event.Skip()
	
	def change_file_extraspecies( self, event ):
		event.Skip()
	
	def toggle_min_leaves_required( self, event ):
		event.Skip()
	
	def change_min_leaves( self, event ):
		event.Skip()
	
	def toggle_cb_score_and_exit( self, event ):
		event.Skip()
	
	def change_file_score_and_exit( self, event ):
		event.Skip()
	
	def toggle_dyn_dup( self, event ):
		event.Skip()
	
	def toggle_dyn_duploss( self, event ):
		event.Skip()
	
	def enter_text_duploss_weight( self, event ):
		event.Skip()
	
	def tog_dynduploss_auto( self, event ):
		event.Skip()
	
	def toggle_bootstrap( self, event ):
		event.Skip()
	
	def change_file_bootstrap( self, event ):
		event.Skip()
	
	def toggle_k_completed( self, event ):
		event.Skip()
	
	def toggle_k_boots( self, event ):
		event.Skip()
	
	def toggle_k_search( self, event ):
		event.Skip()
	
	def toggle_k_boots_norun( self, event ):
		event.Skip()
	
	def toggle_k_search_norun( self, event ):
		event.Skip()
	
	def change_seed( self, event ):
		event.Skip()
	
	def toggle_gene_resampling( self, event ):
		event.Skip()
	
	def new_settings( self, event ):
		event.Skip()
	
	def open_settings( self, event ):
		event.Skip()
	
	def save_settings( self, event ):
		event.Skip()
	
	def save_as_settings( self, event ):
		event.Skip()
	
	def config_astral( self, event ):
		event.Skip()
	

###########################################################################
## Class astral_settings_dialog
###########################################################################

class astral_settings_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ASTRAL Settings", pos = wx.DefaultPosition, size = wx.Size( 331,320 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer69 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox15 = wx.CheckBox( self, wx.ID_ANY, u"Running Locally", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox15.SetValue(True) 
		bSizer28.Add( self.m_checkBox15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_checkBox16 = wx.CheckBox( self, wx.ID_ANY, u"Running on Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_checkBox16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		
		bSizer69.Add( bSizer28, 0, wx.EXPAND, 2 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer29.AddSpacer( ( 13, 0), 0, 0, 2 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Common Prefix on Server:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText15.Wrap( 90 )
		self.m_staticText15.SetToolTipString( u"If all the files to be referenced in the ASTRAL job lie in subfolders of some common path on the server, enter that path here to avoid typing it out several times later." )
		
		bSizer29.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl7.Enable( False )
		
		bSizer29.Add( self.m_textCtrl7, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer69.Add( bSizer29, 0, wx.EXPAND, 22 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer69.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 2 )
		
		bSizer70 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Java Memory (MB)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		self.m_staticText45.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer70.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, u"1024", wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_RIGHT )
		bSizer70.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		
		bSizer69.Add( bSizer70, 0, wx.EXPAND, 2 )
		
		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer69.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 2 )
		
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"ASTRAL Call:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		self.m_staticText46.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer71.Add( self.m_staticText46, 0, wx.ALL, 2 )
		
		bSizer72 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox29 = wx.CheckBox( self, wx.ID_ANY, u"Select JAR on disk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer72.Add( self.m_checkBox29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_filePicker20 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker20.SetFont( wx.Font( 10, 75, 90, 90, False, "Consolas" ) )
		self.m_filePicker20.Enable( False )
		
		bSizer72.Add( self.m_filePicker20, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		bSizer71.Add( bSizer72, 0, wx.EXPAND, 2 )
		
		self.m_checkBox28 = wx.CheckBox( self, wx.ID_ANY, u"Enter custom path to JAR file:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox28.SetValue(True) 
		bSizer71.Add( self.m_checkBox28, 0, wx.ALL, 2 )
		
		bSizer73 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer73.AddSpacer( ( 15, 0), 0, wx.EXPAND, 2 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, u"astral.4.7.8.jar", wx.DefaultPosition, wx.DefaultSize, wx.TE_CHARWRAP )
		self.m_textCtrl6.SetFont( wx.Font( 10, 75, 90, 90, False, "Consolas" ) )
		
		bSizer73.Add( self.m_textCtrl6, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		bSizer71.Add( bSizer73, 1, wx.EXPAND, 2 )
		
		
		bSizer69.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer69.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 2 )
		
		bSizer75 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer75.AddSpacer( ( 0, 0), 1, wx.EXPAND, 2 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		
		bSizer69.Add( bSizer75, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer69 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.load_astral_settings )
		self.m_checkBox15.Bind( wx.EVT_CHECKBOX, self.tog_running_locally )
		self.m_checkBox16.Bind( wx.EVT_CHECKBOX, self.tog_running_on_server )
		self.m_checkBox29.Bind( wx.EVT_CHECKBOX, self.tog_settings_select_on_disk )
		self.m_checkBox28.Bind( wx.EVT_CHECKBOX, self.tog_settings_enter_custom )
		self.m_button2.Bind( wx.EVT_BUTTON, self.save_settings )
		self.m_button3.Bind( wx.EVT_BUTTON, self.cancel_settings )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def load_astral_settings( self, event ):
		event.Skip()
	
	def tog_running_locally( self, event ):
		event.Skip()
	
	def tog_running_on_server( self, event ):
		event.Skip()
	
	def tog_settings_select_on_disk( self, event ):
		event.Skip()
	
	def tog_settings_enter_custom( self, event ):
		event.Skip()
	
	def save_settings( self, event ):
		event.Skip()
	
	def cancel_settings( self, event ):
		event.Skip()
	

