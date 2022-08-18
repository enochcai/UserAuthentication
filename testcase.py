#test case
import main as test_interface
import time

#test create user

#test_interface.CreateUser("zhangsan", "123")

#test_interface.CreateUser("", None)

#test_interface.CreateUser("zhangsan", None)

#test_interface.CreateUser("zhangsan li", "123")

#test_interface.CreateUser("zhangsan","123")
#test_interface.CreateUser("zhangsan","123")



#test delete user
#test_interface.DeleteUser("")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.DeleteUser("zhangsan")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.DeleteUser("li")



#test create role
#test_interface.CreateRole("rzhang")

#test_interface.CreateRole("")

#test_interface.CreateRole("rzhang l")



#test delete role
#test_interface.DeleteRole("")

#test_interface.CreateRole("rzhang")
#test_interface.DeleteRole("rr")

#test_interface.CreateRole("rzhang")
#test_interface.DeleteRole("rzhang")



#test add role to user
#test_interface.AddRoleToUser("", "")

#test_interface.AddRoleToUser("zhang1", "r1")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.AddRoleToUser("zhangsan", "")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.CreateRole("rzhang")
#test_interface.AddRoleToUser("zhangsan", "rzhang")



#test authenticate
#test_interface.Authenticate("", "")

#test_interface.Authenticate("zhangsan", "")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "12345")



#test invalidate
#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#test_interface.Invalidate("101")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#test_interface.Invalidate("102")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#test_interface.Invalidate("101")
#test_interface.AllRoles("101")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#time.sleep(2)#should modify the expiredtime in token.py
#test_interface.AllRoles("101")



#test check role
#test_interface.CheckRole("101", "r")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#test_interface.CheckRole("101", "r")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#test_interface.CreateRole("rzhang")
#test_interface.AddRoleToUser("zhangsan", "rzhang")
#test_interface.CheckRole("101", "rzhang2")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#test_interface.CreateRole("rzhang")
#test_interface.AddRoleToUser("zhangsan", "rzhang")
#test_interface.CheckRole("101", "rzhang")

#test all roles
#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#test_interface.CreateRole("rzhang")
#test_interface.AddRoleToUser("zhangsan", "rzhang")
#test_interface.CreateRole("rzhang2")
#test_interface.AddRoleToUser("zhangsan", "rzhang2")
#test_interface.AllRoles("101")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#test_interface.CreateRole("rzhang")
#test_interface.AddRoleToUser("zhangsan", "rzhang")
#test_interface.CreateRole("rzhang2")
#test_interface.AddRoleToUser("zhangsan", "rzhang2")
#test_interface.AllRoles("")

#test_interface.CreateUser("zhangsan", "123")
#test_interface.Authenticate("zhangsan", "123")
#test_interface.CreateRole("rzhang")
#test_interface.AddRoleToUser("zhangsan", "rzhang")
#test_interface.CreateRole("rzhang2")
#test_interface.AddRoleToUser("zhangsan", "rzhang2")
#test_interface.Invalidate("101")
#test_interface.AllRoles("zhangsan")



