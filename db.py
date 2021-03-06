# WRAPPER CODE FOR THE POSTGRESQL DB CONNECTORS
import psycopg2

DB_URI= "postgres://qgnvbmsplbvqce:8cb4b33626fed4f446c45ad0956379133e6c946f70643b2a866b867a3969d94f@ec2-184-72-236-3.compute-1.amazonaws.com:5432/dbd7uveailk0vg"

def get_curcnx():
    db = psycopg2.connect(DB_URI)
    return  (db, db.cursor())

def exec_query(curcnx, query, values=None):
    if type(values) is not tuple:
        values = tuple([values])
    curcnx[1].execute(query, values)
    
    try:
        resp = curcnx[1].fetchall()
        return resp
    
    except psycopg2.ProgrammingError as e:
        curcnx[0].commit()
        return None



