from odoo import http


class Projects(http.Controller):
    @http.route("/engineering_company/projects" ,auth="user",website=True)

    def Project(self,**params):
        projects=http.request.env["projects"].search([])

        return http.request.render("engineering_company.company_projects",
                                   {'projects':projects})
