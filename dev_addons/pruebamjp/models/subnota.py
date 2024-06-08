
from odoo import models, fields, api


class subnota(models.Model):
    _name = 'pruebamjp.subnota'
    _description = 'Modelo o tabla subnota'

    nota = fields.Float(required=True)
    # modalidad = fields.Char()
    numero = fields.Integer(required=True)
  
    curso_materia_id = fields.Many2one('pruebamjp.curso_materia', string="Curso_Materia", ondelete='cascade', required=True)
    curso_nombre = fields.Char(related='curso_materia_id.curso_nombre', string='Curso') 
    curso_paralelo = fields.Char(related='curso_materia_id.curso_paralelo', string='Paralelo')
    materia_nombre=fields.Char(related='curso_materia_id.materia_nombre', string='Materia')
    year=fields.Integer(related='curso_materia_id.year', string='Año')
    modalidad_gestion_id = fields.Many2one('pruebamjp.modalidad_gestion', string="Modalidad_Gestion", ondelete='cascade')
    #modalidad_id=fields.Char(related='curso_materia_id.gestion_id.modalidad_gestion_id', string='Modalidad')
    modalidad_nombre=fields.Char(related='curso_materia_id.gestion_id.modalidad_gestion_id.nombre', string='Modalidad')
     
    estudiante_id = fields.Many2one('pruebamjp.estudiante', string="Estudiante", ondelete='cascade', required=True)
    estudiante_nombre=fields.Char(related='estudiante_id.nombre', string='Estudiante')
