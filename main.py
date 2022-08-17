#--coding:utf-8---
import user
import role
import token

def INFO(*args):
    print(args)

ALL_USERS = {}
ALL_ROLES = {}
ALL_TOKEN_TO_USER = {}

def CreateUser():
    name = raw_input("Input user name:")
    if not name:
        INFO("name can't none")
        return False
    if name in ALL_USERS:
        INFO("User already exist! Please change other name")
        return False

    password = input("Input password:")
    if not password:
        INFO("password can't none'")
        return False
    
    newUser = user.User(name, password)
    ALL_USERS[name] = newUser
    INFO("Create User success!")
    return True

def DeleteUser():
    name = raw_input("Input user name to delete:")
    if name not in ALL_USERS:
        INFO("User not exist!")
        return False
    INFO("Delete user success!")
    ALL_USERS.pop(name)
    return True

def CreateRole():
    roleName = raw_input("Input role name:")
    if not roleName:
        INFO("Role name can't none")
        return
    if roleName in ALL_ROLES:
        INFO("Role already exist!")
        return False
	newRole = role.Role(roleName)
    #INFO("create Role:", role.Role(roleName))
    ALL_ROLES[roleName] = newRole
    INFO("Create Role Success!")
    return True

def DeleteRole():#Should fail if the user doesn't exist
    roleName = raw_input("Input role name to delete:")
    if not roleName:
        INFO("Role name can't none")
        return
    if roleName not in ALL_ROLES:
        INFO("Role not exist!")
        return False, "Role not exist!"
    ALL_ROLES.pop(roleName)
    INFO("Delete role success!")
    return True
			
def AddRoleToUser():
    userName = raw_input("Input user name:")
    if not userName:
        INFO("user name can't none")
        return
    if not userName in ALL_USERS:
        INFO("User not exist!")
        return
    user = ALL_USERS[userName]
    
    roleName = raw_input("Input role name:")
    if not roleName:
        INFO("Role name can't none")
        return
    if not roleName in ALL_ROLES:
        INFO("Role not exist!")
        return
    role = ALL_ROLES[roleName]
    if role.IsAssociated():
        INFO("Role is already associated!")
        return
    user.AddRole(role)
    INFO("Role associate to role success!")
		
def Authenticate():
    userName = raw_input("Input user name:")
    if not userName:
        INFO("User name can't none")
        return False
    if userName not in ALL_USERS:
        INFO("User not exist!")
        return False

    password = raw_input("Input password:")
    if not password:
        INFO("password can't none'")
        return False 

    user = ALL_USERS[username]
    if not user.CheckPassword(password):
        INFO("Password error!Please retry!")
        return False
    newToken = token.Token()
    user.AddToken(newToken)
    ALL_TOKEN_TO_USER[newToken.Info()] = user
    INFO("Authenticate success!token is:%s", newToken.Info())
    return True

def	Invalidate():
    authToken = raw_input("Please input token:")
    if authToken not in ALL_TOKEN_TO_USER:
        INFO("Token error!")
        return
    user = ALL_TOKEN_TO_USER[authToken]
    myToken = user.GetToken()
    if not myToken.IsValid():
        return
    myToken.SetInvalidate()
    INFO("Set token invalidate success!")

def CheckRole():
    authToken = raw_input("Please input token:")
    if authToken not in ALL_TOKEN_TO_USER:
        INFO("Token error!")
        return False
    roleName = raw_input("Please input role name:")
    if roleName not in ALL_ROLES:
        INFO("Role not exist!")
        return False
    user = ALL_TOKEN_TO_USER[authToken]
    if not user.HasRole(role):
        INFO("role and token not associated!")
        return False
    token = user.GetToken()
    if token.IsValid():
        INFO("Token and role is right! ")
        return True
    INFO("Token is invalidate!")
    return False

def AllRoles():
    authToken = raw_input("Please input token:")
    if authToken not in ALL_TOKEN_TO_USER:
        INFO("Token not exist!")
        return False
    user = ALL_TOKEN_TO_USER[authToken]
    token = user.GetToken()
    if not token.IsValid():
        INFO("Token is invalidate!")
        return False
    lstRoleNames = user.GetAllRoleName()
    INFO("all roles are: %s", lstRoleNames.join(","))
    return True

def generatenum(n):
    num = [n]
    def addnum():
        num[0] += 1
        return num[0]
    return addnum

GetNum = generatenum(0)

CREATE_USER = GetNum()
DELETE_USER = GetNum()
CREATE_ROLE = GetNum()
DELETE_ROLE = GetNum()
ADD_ROLE_TO_USER = GetNum()
AUTHENTICATE = GetNum()
INVALIDATE = GetNum()
CHECK_ROLE = GetNum()
PRINT_ALL_ROLES = GetNum()

MENU_FUNC = {
    CREATE_USER:CreateUser,
    DELETE_USER:DeleteUser,
    CREATE_ROLE:CreateRole,
    DELETE_ROLE:DeleteRole,
    ADD_ROLE_TO_USER:AddRoleToUser,
    AUTHENTICATE:Authenticate,
    INVALIDATE:Invalidate,
    CHECK_ROLE:CheckRole,
    PRINT_ALL_ROLES:AllRoles,
}

if __name__ == "__main__":
    print "###########################################"
    print "#          program_start! Hello!          #"
    print "###########################################"

    while True:
        print "###########################################"
        print "#          menu:1.create user             #"
        print "#               2.delete user             #"
        print "#               3.create role             #"
        print "#               4.delete role             #"
        print "#               5.add role to user        #"
        print "#               6.authenticate            #"
        print "#               7.invalidate              #"
        print "#               8.check role              #"
        print "#               9.print all roles         #"
        print "###########################################"
        try:
            iSelect = input("input menu select:")
        except:
            INFO("select must be num")
            continue
        if iSelect not in MENU_FUNC:
            INFO("menu select must between 1 and 9")
            continue
        func = MENU_FUNC[iSelect]
        func()
        print 

        
