# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime,timedelta

class EngineersManagement(models.Model):
    _name = 'engineers'
    _inherit = 'mail.thread'
    _description = 'Engineers Management'


    name = fields.Char(string="Name", required=True,tracking=True,trim=True)
    reference =fields.Char(string='Subject Reference', required=True, copy=False, readonly=True
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
    color=fields.Integer(string="Color")



    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('sequence.engineer') or _('New')
            return super(EngineersManagement, self).create(vals)





