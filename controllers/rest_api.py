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


    # function that get one record using id from api

    @http.route("/engineering_company/get_one_project", type="json", auth="user")
    def get_one_project(self, **params):
        if params["id"]:
            get_one_project = http.request.env['projects'].search([("id", "=", params["id"])])
            project_details = []
            vals = {
                "id": get_one_project.id,
                "name": get_one_project.name,
                "Government": get_one_project.governorate,
                "Engineers Responsible For this Project": get_one_project.engineers_res.mapped('name'),
                "The Manager Of Project": get_one_project.project_manager.name,
                "Start Time": get_one_project.start_date,
                "The Deadline": get_one_project.deadline,
                "Project state": get_one_project.state,
            }
            project_details.append(vals)
            data = {"status": 200, "response": project_details, "message": "SUCCESS"}
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