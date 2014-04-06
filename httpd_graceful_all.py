#! /usr/bin/env python
import sys
from fabfile import *
from fabric.tasks import execute

def httpdGracefulAll():
    # get host name from hosts file
    hosts=[]
    f = open('/etc/hosts', 'r')
    for line in f:
        if line.find('sv') >= 0:
            hosts.append(line.split()[1])
    f.close()
    
    if len(hosts) == 0:
        sys.exit('Host Not Found.')
    
    # show target hosts, and make extra sure
    print 'Target host is ...'
    for host in hosts:
        print host
    
    confirm = raw_input('OK [yes/No]:')
    if confirm == 'yes' or confirm == 'Yes' or confirm == 'YES':
        pass
    else:
        sys.exit('execute stop')
    
    # execute httpd graceful serially
    for host in hosts :
        #execute(checkAccesslogUpdateContinue, hosts=host, accesslog='/var/log/httpd/8080_access_log', egrep='OPTIONS|304', invert_match=True)
        execute(httpdConfigtest, hosts=host)
        #execute(httpdMaintenanceStart, hosts=host, maintenance_start_command='/root/http-maintenance-for-webserver.sh web01')
        #execute(checkAccesslogUpdateStop, hosts=host, accesslog='/var/log/httpd/8080_access_log', egrep='OPTIONS|304', invert_match=True)
        execute(httpdGraceful, hosts=host)
        #execute(httpdStatus, hosts=host)
        #execute(httpdMaintenanceStop, hosts=host, maintenance_stop_command='/root/http-maintenance-for-webserver.sh up-all')
        #execute(checkAccesslogUpdateContinue, hosts=host, accesslog='/var/log/httpd/8080_access_log', egrep='OPTIONS|304', invert_match=True)

if __name__ == '__main__':
    httpdGracefulAll()

# vim: set ts=4 sw=4 et:
