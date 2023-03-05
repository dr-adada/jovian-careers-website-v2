from sqlalchemy import create_engine, text

connect_db_string = "mysql+pymysql://fcfmr1h90foalypf9t0p:pscale_pw_kPbH89iDKTmACXa5CDV9k24BjJUNsGLgikf7yeAbZjT@aws-eu-west-2.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(connect_db_string,connect_args={
  'ssl':{
    "ssl_ca": "/etc/ssl/cert.pem" 
  }
})

with engine.connect() as con:
  result = con.execute(text('select * from jobs'))

  result_dicts = []
  for row in result.all():
    result_dicts.append(row._mapping)

  print(result_dicts)
    
