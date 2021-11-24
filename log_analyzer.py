log_dir = '/opt/airflow/logs/marketvol1'
from pathlib import Path
file_list = Path(log_dir).rglob('*.log')

def analyse_file(file):
    log=''
    c=0
    for line in file:
        if line.startswith("["):
            errorMessage=[]
            if line.split(" ")[3]=="ERROR":
                log+=str(line)
                c=c+1
    return ((c,log))
err=''
tc=0
for file in file_list:
    with open(file) as f:
        c,log = analyse_file(f)
        tc+=c
        err+=str(log)

#print(err)

print(f'Total number of errors:{tc}\nHere are all the errors:\n{err}')
        