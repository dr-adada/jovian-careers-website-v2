from sqlalchemy import create_engine, text
import os

connect_db_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(connect_db_string,connect_args={
  'ssl':{
    "ssl_ca": "/etc/ssl/cert.pem" 
  }
})

def load_jobs_from_db():
  with engine.connect() as con:
    result = con.execute(text('select * from jobs'))
  
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
      
    return jobs

  
    
