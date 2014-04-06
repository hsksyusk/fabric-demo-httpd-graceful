#! /usr/bin/env python
from fabric.api import run, put, env
from fabric.tasks import execute

def dev():
    env.hosts = ['sv01','sv02']
    env.user = 'root'
    env.key_filename = '/home/hosokoshi/.ssh/id_rsa'

def putHttpdConf():
    put(
        local_path='httpd.conf',
	remote_path='/etc/httpd/conf/httpd.conf',
    )

def httpdConfigtest():
    run('/etc/init.d/httpd configtest')

def httpdGraceful():
    run('/etc/init.d/httpd graceful')

if __name__ == '__main__':
    env.parallel = True
    execute(dev)
    execute(putHttpdConf)
    execute(httpdConfigtest)
    execute(httpdGraceful)
