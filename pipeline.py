# WRAPPER FUNCTIONS FOR CREATING PIPELINES
import db

def parse_pipeline(pipeline):
    participant_list = [x.strip('\'\" ') for x in pipeline.split('>')]
    return participant_list #havent validated the users in the list

class Pipeline():

    query_docstatus = "INSERT INTO DOCSTATUS(ACTIVEUSER, COMMENTS, DOCID, OWNER, TAG, USERLIST, WFID) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
    query_docinfo = "INSERT INTO DOCINFO(DOCID, DOCPATH) VALUES (%s, %s)"

    def __init__(self, docid, owner, userlist, wfid, tag, comments = None):
        self._activeuser = userlist[0]
        self._comments = comments
        self._docid = docid
        self._owner = owner
        self._tag = tag
        self._userlist = userlist
        self._wfid = wfid

    def get_value(self):
        return (self._activeuser, self._comments, self._docid, self._owner, self._tag, self._userlist, self._wfid)

    def commit(self, bucket):
        curcnx = db.get_curcnx()
        db.exec_query(curcnx, self.query_docstatus, self.get_value())
        db.exec_query(curcnx, self.query_docinfo, (self._docid, bucket))





