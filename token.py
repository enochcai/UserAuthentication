import time

EXPIRED_TIME = 7200 #2 hour expired

class Token(object):
    def __init__(self):
        self.m_token = "1"
        self.m_start = int(time.time()) #time.time() return now time by second, and is a float result
        self.m_invalid = False

    def Info(self):
        return self.m_token

    def IsValid(self):
        return (not self.m_invalid) or int(time.time()) < self.m_start + EXPIRED_TIME

    def SetInvalidate(self):
        self.m_invalid = True
    
