from odoo import http


class Projects(http.Controller):
    # function that get information from api

    @http.route("/engineering_company/get_projects", type="json", auth="user")
    def get_projects(self):
        projects_rec = http.request.env['projects'].sudo().search([])
        projects = []
        for rec in projects_rec:
            vals = {
                "id": rec.id,
                "name": rec.name,
                "Government": rec.governorate,
                "Engineers Responsible For this Project": rec.engineers_res.mapped('name'),
                "The Manager Of Project": rec.project_manager.name,
                "Start Time": rec.start_date,
                "The Deadline": rec.deadline,
                "Project state": rec.state,
            }
            projects.append(vals)
        data = {"status": 200, "response": projects, "message": "SUCCESS"}
        return data

#create new record using rest api

    @http.route("/engineering_company/create_project", type="json", auth="user")
    def create_projects(self,**params):
        if params["name"] and params["governorate"] and params["state"]:
            vals={
                "name": params["name"],
                "governorate": params["governorate"],
                "state": params["state"],
            }
            project_new = http.request.env['projects'].create([vals])
            data = {"success":True,"message": "project added","id":project_new.id}
        return data



#Update record using rest api

    @http.route("/engineering_company/update_project", type="json", auth="user")
    def update_projects(self,**params):
        if params["id"]:
            project_update = http.request.env['projects'].search([("id","=",params["id"])])
            if project_update:
                project_update.write(params)
            data = {"success":True,"message": "project updated"}
        return data




#Delete record using rest api

    @http.route("/engineering_company/delete_project", type="json", auth="user")
    def delete_projects(self,**params):
        if params["id"]:
            project_delete = http.request.env['projects'].search([("id","=",params["id"])])
            if project_delete:
                project_delete.unlink()
            data = {"success":True,"message": "project deleted", "id": project_delete.id}
        return data