from datetime import datetime, timedelta
from odoo import api, fields, models,exceptions

   
class Session(models.Model):
    _name="openacademy.session"
    _description = "OpenAcademy Session"
    
    name=fields.Char(required=True,string="name of session")
    strart_date=fields.Date(default=fields.date.today())
    duration=fields.Float(digits=(6,2),help="Duration in days")
    seats=fields.Integer(string="Number of seats")
    instructor_id= fields.Many2one('res.partner',string='Instructor')
    course_id = fields.Many2one('course',string='course',ondelete='cascade',required=True)
    attendee_ids = fields.Many2many('res.partner',string='Attendee')
    taken_seats=fields.Float(string='taken seats',compute='_take_seats')
    end_date=fields.Date(string='End Date',compute='_get_end_date',inverse='_set_end_date' ,store=True)
    attends_count=fields.Integer(string='acount of attends', store=True,compute='_set_attendss_acount')
   
    @api.depends('attendee_ids')
    def _set_attendss_acount(self):
        self.attends_count=len(self.attendee_ids)
   
    @api.depends('strart_date','duration')
    def _get_end_date(self):
        for r in self:
            if not (r.strart_date and r.duration):
                r.end_date = r.strart_date
                continue
           
            duration=timedelta(days=r.duration,seconds=-1)
            r.end_date = r.strart_date + duration
    def _set_end_date(self):
        for r in self:
            if not (r.strart_date and r.end_date):
                continue
            r.duration = (r.end_date - r.strart_date).days+1
            # r.duration =(r.strart_date and r.end_date)
    @api.depends('seats','attendee_ids')
    def _take_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats=0.0
            else:
                    r.taken_seats=100.0 * len(r.attendee_ids)/r.seats
   
   
    @api.constrains('attendee_ids','instructor_id')
    def _chack_value(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError('A instructor dont include in attendess ! ')


