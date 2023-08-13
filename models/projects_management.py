# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime,timedelta

class ProjectsManagement(models.Model):
    _name = 'projects'
    _description = 'Projects Management'
    _inherit = 'mail.thread'
    _inherit = 'engineers'

    name = fields.Char(string="Building", required=True,tracking=True)
    governorate=fields.Char(string="Government", required=True,tracking=True)
    engineers_res=fields.Many2many('engineers',string="Engineers Responsible For The Project",tracking=True)
    start_date = fields.Date(string="Start Time", default=fields.datetime.today())
    deadline = fields.Date(string="The Deadline", default=fields.datetime.today())
    project_lifetime = fields.Char(string="Project Lifetime",compute="_compute_lifetime",tracking=True)

    _sql_constraints = [

        ('name_description_check',
         'CHECK(start_date!= deadline)',
         "the start_date of project should not be the same of deadline"),

        ('name_uniq', 'unique (name)', "Tag name already exists !")
    ]

    @api.depends("start_date","deadline")
    def _compute_lifetime(self):
        for rec in self:
            rec.project_lifetime= (str((rec.deadline.year - rec.start_date.year))) +' year '+'and ' + (str(abs(rec.deadline.month - rec.start_date.month))) +' month '


    # @api.onchange("engineers_res")
    # def _compute_engineers(self):
    #     bb = self.engineers_res.search([])
    #     self.eng_names = bb.mapped("gender")




