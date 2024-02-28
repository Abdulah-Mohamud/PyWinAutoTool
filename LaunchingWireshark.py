from pywinauto.application import Application
import time

class Wireshark:
    # Launches wireshark
    app = Application(backend='uia').start('C:\Program Files\Wireshark\Wireshark.exe').connect(
        title='The Wireshark Network Analyzer', timeout=10)
    
    def __init__(self,):
        InterfaceName = "Wifi"
        return InterfaceName

    def openSavedTrace(self):
        #Opens Sample Wireshark trace downloaded from Wireshark.wiki.
        savedTrace = self.app.TheWiresharkNetworkAnalyzer.child_window(
            title=r"C:\Users\abdulPycharmProjects\RDCandWiresharkAnaylsis\Traces\TraceToReview.pcap",
            control_type="ListItem").wrapper_object()

        savedTrace.click_input(button='left', double=True)

    def startTrace(self):
        # Using pyWinAuto to select 'Start Trace' Button
        captureMenu = self.app.TheWiresharkNetworkAnalyzer.child_window(title="Capture",
                                                                   control_type="MenuItem").wrapper_object()
        captureMenu.click_input()
        startButton = self.app.TheWiresharkNetworkAnalyzer.child_window(title="Start",
                                                                   auto_id="WiresharkMainWindow.actionCaptureStart",
                                                                   control_type="MenuItem").wrapper_object()
        startButton.click_input()

    def stopTrace(self):
        # Using pyWinAuto to select 'Stop Trace' Button
        stopButton = self.app.child_window(title="Stop", control_type="Button").wrapper_object()
        stopButton.click_input(button='left')
        print("Wireshark capture stopped.")

    def saveTraceFile(self):
        pass


pcap = Wireshark()

pcap.startTrace()
time.sleep(5)
pcap.stopTrace()
