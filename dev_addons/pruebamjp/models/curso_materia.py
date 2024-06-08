
from odoo import models, fields, api


class curso_materia(models.Model):
    _name = 'pruebamjp.curso_materia'
    _description = 'Modelo o tabla curso materia'

    # Campo Many2one para relacionar con curso
    curso_id = fields.Many2one('pruebamjp.curso', string="Curso", ondelete='cascade', required=True)
    curso_nombre = fields.Char(related='curso_id.nombre', string='Curso') 
    curso_paralelo = fields.Char(related='curso_id.paralelo', string='Paralelo') 


    materia_id = fields.Many2one('pruebamjp.materia', string="Materia", ondelete='cascade', required=True)
    materia_nombre = fields.Char(related='materia_id.nombre', string='Materia') 
    
    profesor_id = fields.Many2one('pruebamjp.profesor', string="Profesor", ondelete='cascade', required=True)
    profesor_nombre = fields.Char(related='profesor_id.nombre', string='Profesor') 
    


    ciclo_id = fields.Many2one('pruebamjp.ciclo', string="Ciclo", ondelete='cascade', required=True)
    ciclo_nombre = fields.Char(related='ciclo_id.nombre', string='Ciclo') 
    
    
    horario_id = fields.Many2one('pruebamjp.horario', string="Horario", ondelete='cascade', required=True)
    hora_inicio = fields.Integer(related='horario_id.hora_inicio', string='Hora_inicio') 
       
    nota_ids = fields.One2many('pruebamjp.nota', 'curso_materia_id', string="Cursos_Materias_nota")
    
    
    subnota_ids = fields.One2many('pruebamjp.subnota', 'curso_materia_id', string="Cursos_Materias_subnota")
    gestion_id = fields.Many2one('pruebamjp.gestion', string="Gestion", ondelete='cascade', required=True) 
    year = fields.Integer(related='gestion_id.year', string='Año') 
    


    
    @api.depends('curso_nombre','curso_paralelo','materia_nombre','year') 
    def _compute_display_name(self): 
         for rec in self: 
             rec.display_name = f"{rec.curso_nombre} {rec.curso_paralelo}- {rec.materia_nombre} -{rec.year}" 


    @api.constrains('curso_id', 'materia_id')
    def _check_unique_curso_materia(self):
        for rec in self:
            existing_records = self.search([
                ('curso_id', '=', rec.curso_id.id),
                ('materia_id', '=', rec.materia_id.id),
                
                ('id', '!=', rec.id)
            ])
            if existing_records:
                raise ValidationError('La combinación de Curso, Materia ya existe.')    

    @api.constrains('curso_id', 'materia_id', 'horario_id')
    def _check_unique_curso_materia_horario(self):
        for rec in self:
            existing_records = self.search([
                ('curso_id', '=', rec.curso_id.id),
                ('materia_id', '=', rec.materia_id.id),
                ('horario_id', '=', rec.horario_id.id),
                ('id', '!=', rec.id)
            ])
            if existing_records:
                raise ValidationError('La combinación de Curso, Materia y Horario ya existe.')         