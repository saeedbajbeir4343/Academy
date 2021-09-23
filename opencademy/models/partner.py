from odoo import fields,models

class Partner(models.Model):
    _inherit = 'res.partner'
    instructor=fields.Boolean("Instructor",default=True)
    session_ids = fields.Many2many('openacademy.session',string="Attended sessions",readonly=True)