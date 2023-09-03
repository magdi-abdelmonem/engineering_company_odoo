# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime,timedelta

class EngineersManagement(models.Model):
    _name = 'engineers'
    _inherit = 'mail.thread'
    _description = 'Engineers Management'


    name = fields.Char(string="Name", required=True,tracking=True,trim=True)
    reference = reference = fields.Char(string='Subject Reference', required=True, copy=False, readonly=True
                                        , default=lambda self: _("New"))
    age = fields.Integer(string="Age", required=True,tracking=True)
    personal_img=fields.Image(string="Personal image",tracking=True)
    gender = fields.Selection([("male", "Male"),("female", "Female")],string="Gender",tracking=True)
    date=fields.Date(string="Date Time", default=fields.datetime.today() ,readonly=True)
    spec = fields.Selection([("software  engineering", "Software engineering"),
                             ("civil engineering", "Civil engineering"),
                             ("architecture engineering", "Architecture engineering"),
                             ("communications engineering", "Communications engineering"),
                             ("electrical engineering", "Electrical engineering"),
                             ("mechanical engineering", "Mechanical engineering"),
                             ("information technology", "Information technology"),
                             ], string="Specialization", required=True,tracking=True)

    exp_years = fields.Integer(string="Experiance Years", required=True,tracking=True)

    phone=fields.Char(string="Phone")
    email=fields.Char(string="Email")



    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('sequence.engineer') or _('New')
            return super(EngineersManagement, self).create(vals)
'''
    # example for creation
    def creation(self):
        self.env['engineers'].create([{
            'name':"foad ",
            'age':48,
            'spec':"communications engineering",
            'exp_years':26,
        }, {
                   'name': "smsm daly",
                   'age': 33,
                   'spec': "civil engineering",
                   'exp_years': 9,
               }])
  '''

'''
    #example for search 
    def print_record(self):
        filter= self.env['engineers'].search([('gender','=','female')])
        for rec in filter:
            rec.spec="architecture engineering"
'''


