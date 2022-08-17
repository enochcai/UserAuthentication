
class CRole(object):
    def __init__(self, roleName):
        self.m_roleName= roleName
        self.m_user = None
    
    def GetName(self):
        return self.m_roleName

    def AddAssociated(self, user):
        self.m_user = user.GetName()

    def IsAssociated(self):
        if self.m_user is None:
            return False
        return True
    
    def GetUser(self):
        return self.m_user

