from odoo import api, fields, models



class Course(models.Model):
    _name = 'course'
    # _inherit = 'res.users'
    _description = "OpenAcademy Courses"
    name = fields.Char(required=True,string="Tital")
    description=fields.Text()
    responsible_id = fields.Many2one(
        'res.users',ondelete='set null',
        string='Responsabile', index=True,)
    
    session_ids = fields.One2many('openacademy.session', 'course_id',string='Sessions')
    _sql_constraints =[
       ( 'chac_tital',
         'UNIQUE(name)',
         "tital should be unique ")
        ]