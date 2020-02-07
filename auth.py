# WRAPPER FOR AUTH FUNCTIONS
import db

def get_user(user):
    curcnx = db.get_curcnx()
    query = "SELECT * FROM USERINFO WHERE USERID = %s"
    res = db.exec_query(curcnx, query, user)
    if res is None:
        return None
    else:
        return res[0] 
    



