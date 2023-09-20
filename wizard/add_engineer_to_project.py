from odoo import models, fields


class AddEngineerWizard(models.TransientModel):
    _name = 'projects.wizard'
    _description = 'Wizard: Quick Registration of '


    project_id = fields.Many2one("projects", string="The Project", required=True)
    engineers_res = fields.Many2many("engineers", string=" Add Engineers For Projects")



    def confirm(self):
        self.project_id.engineers_res |= self.engineers_res  # to not repeat attendee
        return {}
