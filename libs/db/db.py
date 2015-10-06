#-*-coding=utf-8-*-
from libs.facility import initializer

class BaseDB(object):
    
    def __init__(self):
        pass
    
    def _connection(self):
        try:
            self._conn = initializer.create_local_mysql()
            self.cursor = self._conn.cursor()
        except Exception, e:
            print str(e)
        return None
        
    def conn(self):
        return self._connection()
    
    def _commit(self):
        if self._conn != None:
            self._conn.commit()
        return None
    
    def commit(self):
        return self._commit()
    
    def _close(self):
        try:
            self.commit()
            self.cursor.close()
        except Exception, e:
            print str(e)
        finally:
            self._conn.close()
        return None
    
    def close(self):
        return self._close()
    
    def _single(self):
        return [(e.encode('utf8') if isinstance(e, unicode) else e) for e in self._tmp]
    
    def fetchone(self):
        self._tmp = self.cursor.fetchone()
        if not self._tmp:
            return None
        return self._single()
    
    def fetchall(self):
        result_list = []
        while True:
            self._tmp = self.cursor.fetchone()
            if not self._tmp: 
                return result_list
            result_list.append(self._single())
        
    
