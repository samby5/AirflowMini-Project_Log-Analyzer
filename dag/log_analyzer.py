from pathlib import Path
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
#from airflow.operators.bash_operator import BashOperator
from datetime import date, datetime, timedelta

def logger():
	log_dir = '/opt/airflow/logs/marketvol1'
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






default_args = {
            "owner": "airflow",
            "start_date": datetime(2021, 11, 24),
            "depends_on_past": False,
            "email_on_failure": False,
            "retries": 1, # retry twice
            "retry_delay": timedelta(minutes=5) # five minutes interval
        }
		
dag = DAG(dag_id='marketvol1_err_logger',
			#schedule_interval="6 0 * * 1-5", # running at 6pm for weekdays
			schedule_interval='*/10 5 * * *', # run every 5 hours 
			
			default_args=default_args,
			description='Log errors for marketvol1 log'
			)
		


t0 = PythonOperator(
    task_id='Logger_task',
    python_callable=logger,
	dag=dag)

t0

        