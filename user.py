
class User(object):
    def __init__(self, name, password):
        self.m_name = name
        self.m_password = password #TODO:need encrypt
        self.m_token = None
        self.m_roles = {}
       
    def GetName(self):
        return self.m_name
    
    def CheckPassword(self, password):
        print "checkpass:", self.m_password, password, self.m_password == password
        print type(self.m_password), len(self.m_password)
        print type(password), len(password)
        return self.m_password == password

    def AddRole(self, role):
        self.m_roles[role.GetName()] = role
        role.AddAssociated(self)
    
    def DeleteRole(self, roleName):
        self.m_roles.pop(roleName, None)

    def HasRole(self, role):
        roleName = role.GetName()
        if roleName in self.m_roles:
            return True
        return False
        
    def GetAllRoleName(self):
        return self.m_roles.keys()

    def AddToken(self, token):
        self.m_token = token
    
    def GetToken(self):
        return self.m_token

