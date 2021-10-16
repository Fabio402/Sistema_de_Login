import bcrypt as encoder

# Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# gensalt's log_rounds parameter determines the complexity.
# The work factor is 2**log_rounds, and the default is 12
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))

# Check that an unencrypted password matches one that has
# previously been hashed
if bcrypt.hashpw(password, hashed) == hashed:
        print "It matches"
else:
        print "It does not match"
#Sistema de Login
#Cadastro com nome email e senha.
#Para fazer login com email e senha.


# Banco de dados
# ORM SQL ALQUEMY
# Pesquisar modo de criptografia
