#!usr/bin/env python
import subprocess
import os
subprocess.call(['/home/ec2-kali/jenkins_slave/workspace/zap/zap.sh','-daemon'],stdout=open(os.devnull,'w'))

