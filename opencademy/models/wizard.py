from odoo import models,fields 

class Wizard(models.TransientModel):
    _name='openacademy.wizard'
    _description='wizard : quick registeration of attandess to sessions'
    # def _default_session(self):
    #     return self.env['openacademy.session'].browse(self._context.get('active_id'))
#    default='_default_session'
    session_id = fields.Many2one(
        'openacademy.session',
        string='session', required=True,  )
    attendee_ids = fields.Many2many('res.partner',string='Attendees')