
class Role(object):
    def __init__(self, roleName):
        self.m_rolename = roleName
        self.m_user = None
    
    def GetName(self):
        return self.m_rolename

    def AddAssociated(self, user):
        self.m_user = user.GetName()

    def IsAssociated(self):
        if self.m_User is None:
            return False
        return True


