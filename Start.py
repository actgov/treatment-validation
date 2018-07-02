from __future__ import division

import datetime
import os
import sys

import dicom as dcm
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtWidgets
from pylab import rcParams

import QAResultsScript as QAResults
# FluDo script imports
import RTPlanParse
from MainWindow import Ui_MainWindow

rcParams['figure.figsize'] = 17, 12

class StartQT(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.DoseDiffs=[]
        self.CurDir=os.getcwd()
        self.PlanDCMPath=''
        #Remove old report image everytime
        try:
            os.remove('Report.tiff')
            os.remove('Report.pdf')
        except:
            pass

        self.TxInfo={}
        self.TxInfo['PatientID']=''
        self.TxInfo['PatientName'] = ''
        self.TxInfo['LinacID'] = ''
        self.TxInfo['MeasuredBy'] = ''
        self.TxInfo['MeasuredOn'] = ''
        self.TxInfo['Technique']=''
        self.TxInfo['Site']=''


        #True by default, i.e.,runs batch files to parse and transfer new files each time "Analyse" is clicked
        self.RestartSesssion=True
        self.ui.statusbar.showMessage("Click Analyse to start.")
        self.ui.textEditInfo.append("--------------------------------------FluDoPy------------------------------------------------------------------------")
        self.ui.pushButtonAnalyse.clicked.connect(self.Analyse)
        self.ui.pushButtonDB.clicked.connect(self.pushResultsToDB)
        self.PowerShellPath = os.getcwd() + '\\' + 'CopyDynasFluDoPy.ps'




    def display_histo(self,diffs, bins=20):
        # hist, edges = np.histogram(diffs, bins=bins)
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        ax.hist(diffs.flatten(), bins, color='green', alpha=0.8)
        plt.show(block=False)


    def collectTxInfo(self):
        FileData=dcm.read_file(self.PlanDCMPath)
        self.TxInfo['PatientName']=str(FileData.PatientName).replace('^',' ')
        self.TxInfo['PatientID']=FileData.PatientID
        self.TxInfo['LinacID'] = self.ui.comboBoxLA.currentText()
        self.TxInfo['Technique'] = self.ui.comboBoxTechnique.currentText()
        self.TxInfo['Site'] = self.ui.comboBoxSite.currentText()
        self.TxInfo['MeasuredOn'] =datetime.datetime.today().date()

    def pushResultsToDB(self):
        pass

    def Analyse(self):
        self.ui.textEditInfo.clear()
        SelectedLinac = self.ui.comboBoxLA.currentIndex()
        # ************************************End Find_IMRT_DCM*********************************************************


        if self.ui.radioButtonRestart.isChecked():
            # Run RTPlanParser class to scan for new RTPlans
            PP = RTPlanParse.RTPlanParser()
            PP.filterIMRT(PP.src_dcm_files)
            print("Done.")
            self.ui.statusbar.showMessage("No. of patients found: "+str(len(PP.imrt_candidates)))

            for f, n, pln, pld, plt in PP.imrt_candidates:
                self.ui.textEditInfo.append("patient: %s with plan name %s, on this date %s, at this time %s" % (n, pln, pld, plt))
            self.ui.textEditInfo.append("*********************************************************************************")

            #************************************End Find_IMRT_DCM**********************************************************




        # ************************LaunchFluDO   CELL 01*****************************************************************
        # dynalog_dir_path = r'/home/mpre/tmp_dynalogs_la4/Moss'
        # pinnacle_dcm_path = r'/home/mpre/tmp2/RTPLAN9869.1.dcm'
        init_pin_path = r'D:\RTPlanFromPin'
        init_dynalog_path = r'D:\Temp'

        pinnacle_dcm_path = QtWidgets.QFileDialog.getOpenFileNames(self,"Select RT Plan",init_pin_path)[0]
        self.PlanDCMPath=pinnacle_dcm_path[0]

        ResultsDlg = QAResults.QAResultsDlg(self)
        ResultsDlg.setModal(True)
        ResultsDlg.CurLinac=np.int(SelectedLinac)
        ResultsDlg.CurDir=self.CurDir
        ResultsDlg.DCMFile=pinnacle_dcm_path[0]
        ResultsDlg.DynsPath=init_dynalog_path
        ResultsDlg.PowerShellPath=self.PowerShellPath
        ResultsDlg.Restart=self.ui.radioButtonRestart.isChecked()
        ResultsDlg.updateForm()

        ResultsDlg.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = StartQT()
    myapp.show()
    myapp.setWindowTitle('FluDoPy')
    myapp.setStyle(QtWidgets.QStyleFactory.create('Plastique'))
    sys.exit(app.exec_())