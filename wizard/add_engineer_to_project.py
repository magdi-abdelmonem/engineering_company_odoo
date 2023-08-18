from odoo import models, fields


class AddEngineerWizard(models.TransientModel):
    _name = 'projects.wizard'
    _description = 'Wizard: Quick Registration of '

    # def _default_projects(self):
    #     return self.env['projects'].browse(self.env.context.get('active_id'))

    project_id = fields.Many2one("projects", string="The Project", required=True)
    engineers_res = fields.Many2many("engineers", string=" Add Engineers For Projects")



    def confirm(self):
        # get_id=int(self.project_id)
        # update = self.env['projects'].browse(get_id).write(
        #                                             {'engineers_res':self.engineer_attendees})
        # print(update)
        # return update

        self.project_id.engineers_res |= self.engineers_res  # to not repeat attendee
        return {}
