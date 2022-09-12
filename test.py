import os
import nbwaf
import subprocess

proc = subprocess.Popen("php NBERR0.php", shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout.read()
script_response = script_response.decode("utf-8")
print(script_response)