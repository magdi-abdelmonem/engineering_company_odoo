# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime,timedelta

class ProjectsManagement(models.Model):
    _name = 'projects'
    _description = 'Projects Management'
    _inherit = 'mail.thread'

    name = fields.Char(string="Building", required=True,tracking=True)
    governorate=fields.Selection([("cairo", "Cairo"),("alexandria", "Alexandria"),
                                ("giza", "Giza"),("monufia", "Monufia"),("dakahlia", "Dakahlia")
                                 ,("fayoum", "Fayoum"),("aswan", "Aswan"),("damietta", "Damietta"),
                                ("qena", "Qena"),("sharqia", "Sharqia"),("sohag", "Sohag")]
                                ,string="Government", required=True,tracking=True)
    engineers_res=fields.Many2many('engineers',string="Engineers Responsible For this Project",tracking=True)
    start_date = fields.Date(string="Start Time", default=fields.datetime.today())
    deadline = fields.Date(string="The Deadline", default=fields.datetime.today())
    project_lifetime = fields.Char(string="Project Lifetime",compute="_compute_lifetime",tracking=True)

    engineers_responsible_for_the_project = fields.Text(String = 'Engineers Responsible For The Project',)
    state = fields.Selection(
        [
            ('not_started', "Not_started"),
            ('in_progress', "In_progress"),
            ('finished', "Finished"),
            ('canceled', "Canceled"),
        ], string="Project state", readonly=True, copy=False, default='not_started', tracking=True)

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



    @api.model
    def create(self, vals_list):
        rec = super(ProjectsManagement, self).create(vals_list)
        rec.compute_eng_res_appear()
        return rec



    # function for buttons in statusbar

    def start_project_action(self):
        for rec in self:
            rec.state='in_progress'

    def finish_project_action(self):
        for rec in self:
            rec.state='finished'


    def reset_project_action(self):
        for rec in self:
            rec.state='not_started'


    def cancel_project_action(self):
        for rec in self:
            rec.state='canceled'