#!usr/bin/env python
import subprocess
import os
subprocess.Popen(['/usr/share/zaproxy/zap.sh','-daemon'],stdout=open(os.devnull,'w'))
