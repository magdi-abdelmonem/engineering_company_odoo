from odoo import models,fields,api
from odoo.exceptions import ValidationError

class PROJECTMANAGER(models.Model):
    _name = "project.manager"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", required=True, tracking=True, trim=True)
    age = fields.Integer(string="Age", required=True, tracking=True)
    personal_img = fields.Image(string="Personal image", tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender", tracking=True)
    spec = fields.Selection([("civil engineering", "Civil engineering"),
                             ("mechanical engineering", "Mechanical engineering"),
                             ], string="Specialization", required=True, tracking=True)
    certification=fields.Boolean(string="Have PMP certification")
    exp_years = fields.Integer(string="Experiance Years", required=True, tracking=True)

    address=fields.Char(string="Address")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")


    @api.constrains('certification', 'exp_years')
    def check(self):
        for rec in self:
            if rec.certification == False :
                raise ValidationError(" you should have PMP")
            elif rec.exp_years <=10 :
                raise ValidationError(" you should have more than 10 years of experiance" )

