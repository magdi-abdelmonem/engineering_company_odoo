from odoo import models,fields,api


class CancelProjectWizard(models.TransientModel):

    _name='cancel.project.wizard'
    _description = 'Cancel Project Wizard'

    project_id=fields.Many2one('projects' ,string='project cancel')
    canceled_reason=fields.Text(string="Reasons for canceling the project",required=True)


    def cancel(self):
        get_ids=int(self.project_id)
        return self.env['projects'].browse(get_ids).write({'state':'canceled','canceled_reason':self.canceled_reason})
