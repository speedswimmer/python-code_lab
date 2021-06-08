# Script to check connection status and host status on local FritzBox!
import time, sys
from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import ActionError, FritzConnectionException, FritzServiceError
from fritzconnection.lib.fritzhosts import FritzHosts
from fritzconnection.lib.fritzstatus import FritzStatus

try:
    fc = FritzConnection(address='Your_FritzBox_IP4_Address', password='Your_Password', use_tls=True)
except FritzConnectionException:
    print("Can't connect to FritzBox!")
    sys.exit(0)
    
def getFritzStatus():
    fs = FritzStatus(fc)
    print("*************** Status FritzBox! ********************\n")
    print("FritzBox Model: %s" % (fs.modelname))
    print("FritzBox is linked: ",fs.is_linked)
    print("FritzBox is connected:", fs.is_connected)
    print("FritzBox uptime:", fs.str_uptime)
    print("FritzBox external IP4: %s\n" %(fs.external_ip))

def getWLANstatus():
    action = 'GetInfo'
    status = []
    print("******************* WLAN Status FritzBOX! **************")
    for i in range (1,10):
        try:
            wlan_status = fc.call_action(f'WLANConfiguration{i}', action)
        except FritzServiceError:
            break
        print(wlan_status["NewSSID"] + ": " + wlan_status["NewStatus"])
    print("\n")
    
def getHostStatus():
    fh = FritzHosts(fc)
    hosts = fh.get_hosts_info()
    activehosts = fh.get_active_hosts()
    print("**********************************\n")
    print("Übersicht der bekannten Hosts:")
    print("Es sind %s Hosts bekannt!\n" %(len(hosts)))
    print("Folgende %s Hosts sind aktive im Netzwerk:" %(len(activehosts)))
    print("IP-Address         Name                      Status")
    print("---------------------------------------------------")

    for i in range(0, len(hosts)-1):
        if hosts[i]["status"] == True:
            ipaddress = hosts[i]["ip"]
            hostname = hosts[i]["name"]
            hoststatus = hosts[i]["status"]
            print(f"{ipaddress:18} {hostname:25} - {hoststatus}")

getWLANstatus()
getHostStatus()
