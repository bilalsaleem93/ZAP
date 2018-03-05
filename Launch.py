#!usr/bin/env python
import subprocess
import os
api = '-config api.key='+sys.argv[1]
subprocess.call(['/home/ec2-kali/jenkins_slave/workspace/zap/zap.sh',api,'-daemon'])

