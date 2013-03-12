from subprocess import *
import re
p = Popen('gpart create -s gpt /dev/ad1', stdin=PIPE, stdout=PIPE, stderr=PIPE,shell=True)
print p.communicate()
print p.returncode
