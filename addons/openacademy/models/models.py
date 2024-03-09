# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'
#     _description = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import fields, models
# el nombre de nuestra clase será como el nbombre d ela tabla
class users(models.Model):
    _name= "users"
    _description="Tabla de usuarios"

    name = fields.Char(String="Nombre")
    description = fields.Text(String="Descripcion")


class courses(models.Model):
    _name= "courses"
    _description="Que cursos impartimos"

    name = fields.Char(String="Nombre")#nombre columna
    description = fields.Text(String="Descripcion")
    # a continuacion añadimos dos funciones que se ejecutaran al llamar al boton de agregar usuario o al boton de crear nuevo curso

class puntuacion(models.Model):
    _name= "puntuacion"
    _description="puntos de los usuarios"

    name = fields.Char(String="hola")#nombre columna
    description = fields.Text(String="queTal")
    # a continuacion añadimos dos funciones que se ejecutaran al llamar al boton de agregar usuario o al boton de crear nuevo curso



