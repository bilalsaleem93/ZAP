#!usr/bin/env python
import subprocess
import os
#import sys
#api = '-config api.key='+sys.argv[1]
subprocess.call(['/home/ec2-kali/jenkins_slave/workspace/zap/zap.sh','-daemon'])

