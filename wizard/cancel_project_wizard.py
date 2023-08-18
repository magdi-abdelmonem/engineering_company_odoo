from odoo import models,fields,api


class CancelProjectWizard(models.TransientModel):

    _name='cancel.project.wizard'
    _description = 'Cancel Project Wizard'

    project_id=fields.Many2one('projects' ,string='project cancel')


    def cancel(self):

        get_ids=int(self.project_id)
        return self.env['projects'].browse(get_ids).write({'state':'canceled'})
