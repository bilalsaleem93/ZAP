#!usr/bin/env python
import subprocess
import os
#import sys
#api = '-config api.key='+sys.argv[1]
subprocess.Popen(['/home/ec2-kali/jenkins_slave/workspace/zap/zap.sh','-config', 'api.disablekey=true','-daemon'])

