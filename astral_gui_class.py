__author__ = 'Michael'

import wx
import configparser
import astral_gui_wxfb
import os.path

class MyApp(wx.App):
    def OnInit(self):
        self.mainframe = astral_gui_frame(None)
        self.SetTopWindow(self.mainframe)
        self.mainframe.Show()

        return True

class astral_gui_frame(astral_gui_wxfb.main_frame):
    def __init__(self,parent):
        self.parent=parent
        astral_gui_wxfb.main_frame.__init__(self,parent)
        self.job_config=create_fresh_job_config()
        self.astral_config=get_astral_settings()
        self.update_command()

    def populate_form_from_job_config(self):
        pass

    def update_command(self):
        cmd=get_commandline_from_jobcfg(self.job_config,self.astral_config)
        self.m_txt_output_command.SetValue(cmd)

    def update_job_config_from_GUI_state(self):
        # little function here...
        def cjc(mjc,val,show=1):
            if show==0:
                s='false'
            elif show==1:
                s='true'
            elif show==True:
                s='true'
            elif show==False:
                s='false'

            self.job_config.set(mjc,'value',val)
            self.job_config.set(mjc,'show',s)

        # input
        jc = 'input'
        fi=self.m_file_input.GetTextCtrlValue()
        cjc(jc,fi,1)

        #output
        jc='output'
        fi=self.m_file_output.GetTextCtrlValue()
        if fi<>'':
            cjc(jc,fi,1)
        else:
            cjc(jc,fi,0)

        #name_map
        jc='name_map'
        fi=self.m_file_namemap.GetTextCtrlValue()
        if fi<>'':
            cjc(jc,fi,1)
        else:
            cjc(jc,fi,0)

        # exact
        jc='exact'
        ex=self.m_cb_exact.IsChecked()
        if ex==False:
            cjc(jc,str(ex).lower(),0)
        else:
            cjc(jc,str(ex).lower(),1)

        jc='extra_bip'
        eb=str(self.m_choice_extralevel.GetSelection()[0])
        if self.m_choice_extralevel.IsEnabled()==True and eb<>'1':
            cjc(jc,eb,1)
        else:
            cjc(jc,eb,0)

        jc='extra_genes'
        eg=self.m_file_extragenes.GetTextCtrlValue()
        if self.m_file_extragenes.IsEnabled()==True and eg<>'':
            cjc(jc,eg,1)
        else:
            cjc(jc,eg,0)

        jc='extra_species'
        es=self.m_file_extraspecies.GetTextCtrlValue()
        if self.m_file_extragenes.IsEnabled()==True and es<>'':
            cjc(jc,es,1)
        else:
            cjc(jc,es,0)

        jc='min_leaves'
        ml=int(self.m_txt_min_leaves.GetValue())
        if self.m_cb_min_leaves.IsChecked()==True:
            cjc(jc,ml,1)
        else:
            cjc(jc,ml,0)

        jc= 'score_and_exit'
        se=self.m_file_score_and_exit.GetTextCtrlValue()
        if self.m_cb_score_and_exit.IsChecked()==True:
            cjc(jc,se,1)
        else:
            cjc(jc,se,0)

        jc='dynadup_min_dup'
        dmd=self.m_cb_dyna_min_dup.IsChecked()
        if dmd==True:
            cjc(jc,'',1)
        else:
            cjc(jc,'',0)

        jc='dynadup_min_duploss'
        ddl=self.m_cb_dyna_min_duploss.IsChecked() and self.m_cb_dyna_min_duploss.IsEnabled()
        ddl_val=float(self.m_txt_duploss_weight.GetValue())
        ddl_auto=self.m_cb_duploss_auto.IsChecked()
        if ddl==True:
            if ddl_auto==True:
                cjc(jc,'(auto)',1)
            else:
                cjc(jc,ddl_val,1)
        else:
            if ddl_auto==True:
                cjc(jc,'(auto)',0)
            else:
                cjc(jc,ddl_val,0)

        jc='boots'
        bsval=self.m_file_bootstrap_reps.GetTextCtrlValue()
        bs=self.m_cb_bootstraps.IsChecked() and self.m_cb_bootstraps.IsEnabled() and bsval<>''
        if bs==True:
            cjc(jc,bsval,1)
        else:
            cjc(jc,bsval,0)

        jc='boot_reps'
        brval=self.m_txt_bootreps.GetValue()
        br = self.m_txt_bootreps.IsEnabled() and brval<>''
        if br==True:
            cjc(jc,brval,1)
        else:
            cjc(jc,brval,0)

        jc='keep'
        k_com=str(self.m_cb_k_completed.IsEnabled() and self.m_cb_k_completed.IsChecked()).lower()
        k_boot=str(self.m_cb_k_boots.IsEnabled() and self.m_cb_k_boots.IsChecked()).lower()
        k_boot_nr=str(self.m_cb_k_boots_norun.IsEnabled() and self.m_cb_k_boots_norun.IsChecked()).lower()
        # k_search=str(self.m_cb_k_search.)
        self.job_config.set(jc,'completed',k_com)
        self.job_config.set(jc,'bootstraps',k_boot)



        jc='seed'
        #TODO: and this part

        jc='gene_tree_resampling'
        #TODO: and this part


    def update_GUI_state_from_job_config(self):
        #TODO: implement
        pass



    #
    #   Event Handlers
    #
    def change_input_file( self, event ):
        self.job_config.set('input','value',self.m_file_input.GetTextCtrlValue())
        self.update_command()

    def change_output_file( self, event ):
        newfile=self.m_file_output.GetTextCtrlValue()
        if newfile != '':
            self.job_config.set('output','show','true')
            self.job_config.set('output','value',newfile)
        self.update_command()

    def change_name_mapping( self, event ):
        newfile=self.m_file_namemap.GetTextCtrlValue()
        if newfile != '':
            self.job_config.set('name_map','show','true')
            self.job_config.set('name_map','value',newfile)
        self.update_command()

    def toggle_find_exact( self, event ):

        if self.m_cb_exact.IsChecked()==True:
            self.job_config.set('exact','show','true')
            self.m_choice_extralevel.Enable(False)
            self.m_file_extragenes.Enable(False)
            self.m_file_extraspecies.Enable(False)
            self.m_st_extralevel.Enable(False)
            self.m_st_extragenes.Enable(False)
            self.m_st_extraspecies.Enable(False)
            self.m_cb_min_leaves.Enable(False)
            self.m_txt_min_leaves.Enable(False)
            for i in ['extra_bip','extra_genes','extra_species','min_leaves']:
                self.job_config.set(i,'show','false')
        else:
            self.job_config.set('exact','show','false')
            self.m_choice_extralevel.Enable(True)
            self.m_file_extragenes.Enable(True)
            self.m_file_extraspecies.Enable(True)
            self.m_st_extralevel.Enable(True)
            self.m_st_extragenes.Enable(True)
            self.m_st_extraspecies.Enable(True)
            self.m_cb_min_leaves.Enable(True)

            #handle min leaves
            self.toggle_min_leaves_required()

            #handle extralevel
            if self.m_choice_extralevel.GetSelection()[0]==1:
                self.job_config.set('extra_bip','show','false')
            else:
                self.job_config.set('extra_bip','show','true')

            for i in ['extra_genes','extra_species']:
                if self.job_config.get(i,'value')!='':
                    self.job_config.set(i,'show','false')
                else:
                    self.job_config.set(i,'show','false')
        self.update_command()



    def change_extra_level( self, event ):
        lev=self.m_choice_extralevel.GetSelection()
        mylev=lev[0]
        self.job_config.set('extra_bip','value',mylev)
        if mylev<>'1':
            self.job_config.set('extra_bip','show','true')
        else:
            self.job_config.set('extra_bip','show','false')
        self.update_command()

    def change_file_extragenes( self, event ):
        newfile=self.m_file_extragenes.GetTextCtrlValue()
        jcat='extra_genes'
        self.job_config.set(jcat,'value',newfile)
        if newfile=='':
            self.job_config.set(jcat,'show','false')
        else:
            self.job_config.set(jcat,'show','true')
        self.update_command()

    def change_file_extraspecies( self, event ):
        newfile=self.m_file_extraspecies.GetTextCtrlValue()
        jcat='extra_species'
        self.job_config.set(jcat,'value',newfile)
        if newfile=='':
            self.job_config.set(jcat,'show','false')
        else:
            self.job_config.set(jcat,'show','true')
        self.update_command()

    def toggle_min_leaves_required( self, event=None ):
        jcat='min_leaves'
        if self.m_cb_min_leaves.IsChecked()==True:
            self.m_txt_min_leaves.Enable(True)
            self.job_config.set(jcat,'show','true')
        else:
            self.m_txt_min_leaves.Enable(False)
            self.job_config.set(jcat,'show','false')

    def toggle_cb_score_and_exit( self, event ):
        jcat = 'score_and_exit'
        if self.m_cb_score_and_exit.IsChecked()==True:
            self.m_file_score_and_exit.Enable(True)
            if self.job_config.get(jcat,'value')<>'':
                self.job_config.set(jcat,'show','true')
            else:
                self.job_config.set(jcat,'show','false')
        else:
            self.m_file_score_and_exit.Enable(False)
            self.job_config.set(jcat,'show','false')
        self.update_command()

    def change_file_score_and_exit( self, event ):
        jcat = 'score_and_exit'


    def toggle_dyn_dup( self, event ):
        pass




def create_fresh_job_config():
    jobcfg=configparser.ConfigParser()
    # first my own property: location
    jobcfg.add_section('self')
    jobcfg.set('self','path','')

    jobcfg.add_section('input')
    jobcfg.add_section('output')
    jobcfg.add_section('name_map')
    jobcfg.add_section('exact')
    jobcfg.add_section('extra_bip')
    jobcfg.add_section('extra_genes')
    jobcfg.add_section('extra_species')
    jobcfg.add_section('min_leaves')
    jobcfg.add_section('score_and_exit')
    jobcfg.add_section('dynadup_min_dup')
    jobcfg.add_section('dynadup_min_duploss')
    jobcfg.add_section('boots')
    jobcfg.add_section('boot_reps')
    jobcfg.add_section('keep')
    jobcfg.add_section('seed')
    jobcfg.add_section('gene_tree_resampling')
    jobcfg.set('input','arg','i')
    jobcfg.set('output','arg','o')
    jobcfg.set('name_map','arg','a')
    jobcfg.set('exact','arg','x')
    jobcfg.set('extra_bip','arg','p')
    jobcfg.set('extra_genes','arg','e')
    jobcfg.set('extra_species','arg','f')
    jobcfg.set('min_leaves','arg','m')
    jobcfg.set('score_and_exit','arg','q')
    jobcfg.set('dynadup_min_dup','arg','d')
    jobcfg.set('dynadup_min_duploss','arg','l')
    jobcfg.set('boots','arg','b')
    jobcfg.set('boot_reps','arg','r')
    jobcfg.set('keep','arg','k')
    jobcfg.set('seed','arg','s')
    jobcfg.set('gene_tree_resampling','arg','g')
    jobcfg.set('input','show','true')
    jobcfg.set('output','show','false')
    jobcfg.set('name_map','show','false')
    jobcfg.set('exact','show','false')
    jobcfg.set('extra_bip','show','false')
    jobcfg.set('extra_genes','show','false')
    jobcfg.set('extra_species','show','false')
    jobcfg.set('min_leaves','show','false')
    jobcfg.set('score_and_exit','show','false')
    jobcfg.set('dynadup_min_dup','show','false')
    jobcfg.set('dynadup_min_duploss','show','false')
    jobcfg.set('boots','show','false')
    jobcfg.set('boot_reps','show','false')
    # jobcfg.set('keep','show','false')
    jobcfg.set('seed','show','false')
    jobcfg.set('gene_tree_resampling','show','false')
    jobcfg.set('input','value','')
    jobcfg.set('output','value','')
    jobcfg.set('name_map','value','')
    jobcfg.set('extra_bip','value','1')
    jobcfg.set('extra_genes','value','')
    jobcfg.set('extra_species','value','')
    jobcfg.set('min_leaves','value','')
    jobcfg.set('score_and_exit','value','')
    jobcfg.set('dynadup_min_dup','value','')
    jobcfg.set('dynadup_min_duploss','value','(auto)')
    jobcfg.set('boots','value','')
    jobcfg.set('boot_reps','value','')
    # jobcfg.set('keep','value','')
    jobcfg.set('seed','value','692')
    jobcfg.set('gene_tree_resampling','value','')

    # keep category is different:
    jobcfg.set('keep','completed','false')
    jobcfg.set('keep','bootstraps','false')
    jobcfg.set('keep','bootstraps_norun','false')
    jobcfg.set('keep','searchspace','false')
    jobcfg.set('keep','searchspace_norun','false')
    return jobcfg

def get_astral_settings(return_run_string=False):
    ast_file_path = get_astral_settings_path()

    if os.path.exists(ast_file_path)==True:
        astral_config=configparser.ConfigParser().read(ast_file_path)
    else:
        astral_config=configparser.ConfigParser()
        astral_config.add_section('main')
        astral_config.set('main','running_local','true')
        astral_config.set('main','common_server_path','')
        astral_config.set('main','java_memory','1024')
        astral_config.set('main','astral_path','astral.4.7.8.jar')
        astral_config.set('main','find_on_disk','false')
    if return_run_string==False:
        return astral_config
    else:
        outstr=astral_command_string_from_config(astral_config)
        return outstr


def astral_command_string_from_config(astral_config):
        outstr='java -Xmx'
        outstr=outstr + astral_config.get('main','java_memory')
        outstr=outstr + 'M -jar ' + astral_config.get('main','astral_path')
        return outstr

def get_commandline_from_jobcfg(job,astral_config):
    command_str=astral_command_string_from_config(astral_config)
    for i in job.sections():
        if i!='self' and i !='keep':
            if job.getboolean(i,'show')==True:
                command_str=command_str + ' -' + job.get(i,'arg')
                if job.has_option(i,'value')==True:
                    command_str=command_str + ' ' +  job.get(i,'value')
        while command_str[-1]==' ':
            command_str=command_str[:-1]
    return command_str

def get_astral_settings_path():
    pa, fi = os.path.split(__file__)
    ast_file_path = os.path.join(pa, 'astral_settings.cfg')
    return ast_file_path