from odoo import models,fields,api

class Wizard(models.TransientModel):

    _name = 'projects.wizard'
    _description = 'Wizard: Quick Registration of '


    def _default_projects(self):
        return self.env['projects'].browse(self.env.context.get('active_id'))

    project_id = fields.Many2one("projects", string="The Project", required=True, default=_default_projects)
    engineer_attendees = fields.Many2many("engineers", string=" Add Engineers For Projects")

    def confirm(self):
        self.project_id.engineer_attendees |= self.engineer_attendees       #to not repeat attendee
        return {}
