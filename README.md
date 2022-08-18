# UserAuthentication
a simple authentication and authorization service use Python2.7

##run
enter this command and run the program.
python main.py

##file
user.py class user, the entity user.A user to multi-roles. A user has password and m_roles which contains all its role.

token.py class token which manager the token. When a token object is created, a token producted.You can replace the TokenMgr by your token algoritham.The token is limit time in valid and m_invalid is a special valid state to control the token.

role.py class role.

tool.py the encryption algoritham.You can replace as you want.

main.py the main vocational work.

testcase.py is the interface testcase.
