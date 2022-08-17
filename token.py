import time

EXPIRED_TIME = 7200 #2 hour expired

def GenerateToken():
    token_id = [100]
    def TokenChange():
        token_id[0] += 1
        return str(token_id[0])
    return TokenChange

TokenMgr = GenerateToken()

class Token(object):
    def __init__(self):
        self.m_token = TokenMgr()
        self.m_start = int(time.time()) #time.time() return now time by second, and is a float result
        self.m_invalid = False

    def Info(self):
        return self.m_token

    def IsValid(self):
        return (not self.m_invalid) and int(time.time()) < self.m_start + EXPIRED_TIME

    def SetInvalidate(self):
        self.m_invalid = True
    
