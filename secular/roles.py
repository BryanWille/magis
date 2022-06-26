import imp
from rolepermissions.roles import AbstractUserRole

class Diretoria(AbstractUserRole):
    available_permissions = {
            'cadastrar_questoes' : True,
            'alterar_questoes' : True,
            'deletar_questoes' : True,
            'cadastrar_professores' : True,
            'cadastrar_materias' : True,
            'alterar_materias' : True,
            'deletar_materias' : True,
    }

class Professor(AbstractUserRole):
    available_permissions = {
            'cadastrar_questoes' : True,
            'alterar_questoes' : True,
            'deletar_questoes' : True,
            'cadastrar_materias' : True,
            'alterar_materias' : True,
            'deletar_materias' : True,
    }

class Aluno(AbstractUserRole):
    available_permissions = {
            'cadastrar_questoes' : True,
    }