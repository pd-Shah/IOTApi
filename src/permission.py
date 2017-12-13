class Permission():
    def __init__(self, connection):
        self.headers=connection.headers

    def get_permission_list(self, page_number, page_size, endpoint="permission/list"):
        params={"pageNumber": page_number, "pageSize":page_size}
        self._get_permission_list=api._api_request(endpoint, headers=self.headers, params=params)
        return self._get_permission_list

    # def grant_permission(self, project_id, user_id, permission_id, endpoint="permission/grant", verb="post"):
    #     data={"projectId": project_id, "userId":user_id, "permissionId":permission_id}
    #     self._grant_permission=api._api_request(endpoint, verb=verb, data=data, headers=self.headers)
    #     return self._grant_permission

    # def deny_permission(self, project_id, user_id, permission_id, endpoint="permission/deny", verb="post"):
    #     data={"projectId": project_id, "userId":user_id, "permissionId":permission_id}
    #     self._deny_permission=api._api_request(endpoint, verb=verb, data=data, headers=self.headers)
    #     return self._deny_permission

    # def get_permission(self, project_id, user_id, endpoint="query/{0}/{1}"):
    #     endpoint=endpoint.format(project_id, user_id)
    #     data={"projectId":project_id, "userId":user_id}
    #     self._get_permission=api._api_request(endpoint, data=data, headers=self.headers)
    #     return self._get_permission
