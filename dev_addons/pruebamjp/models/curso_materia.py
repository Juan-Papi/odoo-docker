
from odoo import models, fields, api


class curso_materia(models.Model):
    _name = 'pruebamjp.curso_materia'
    _description = 'Modelo o tabla curso materia'

    # Campo Many2one para relacionar con curso
    curso_id = fields.Many2one('pruebamjp.curso', string="Curso", ondelete='cascade', required=True)
    materia_id = fields.Many2one('pruebamjp.materia', string="Materia", ondelete='cascade', required=True)
    profesor_id = fields.Many2one('pruebamjp.profesor', string="Profesor", ondelete='cascade', required=True)
    ciclo_id = fields.Many2one('pruebamjp.ciclo', string="Ciclo", ondelete='cascade', required=True)
    horario_id = fields.Many2one('pruebamjp.horario', string="Horario", ondelete='cascade', required=True)
    nota_ids = fields.One2many('pruebamjp.nota', 'curso_materia_id', string="Cursos_Materias_nota")
    subnota_ids = fields.One2many('pruebamjp.subnota', 'curso_materia_id', string="Cursos_Materias_subnota")
    gestion_id = fields.Many2one('pruebamjp.gestion', string="Gestion", ondelete='cascade', required=True) 