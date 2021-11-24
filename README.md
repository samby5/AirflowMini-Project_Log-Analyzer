# AirflowMini-Project_LogAnalyzer
Python script is copied to docker container(from local) using the below command -
```cp "C:\Users\samy8\Desktop\Work Lab\SpringBoard\github\AirflowMini-Project_Log-Analyzer\log_analyzer.py" 0faa5da98d7e:/opt/airflow```
To run the python script in the docker container -
``` python log_analyzer.py ```
error logs for the dag marketvol1

## Added the dag(log_analyzer.py) to run the python script
Details in the \dag folder 
Airflow localhost UI path -
http://localhost:8080/log?dag_id=marketvol1_err_logger&task_id=Logger_task&execution_date=2021-11-24T12%3A16%3A06.682152%2B00%3A00


