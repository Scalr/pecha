__author__ = 'shaitanich'

from scalrtools import commands


name = "role"
enabled = True


def callback(*args, **kwargs):
    """
    print('in image module')
    print(args)
    print(kwargs)
    """
    pass


class Role(commands.SubCommand):
    pass


class ChangeRoleAttrs(Role):
    name = "change-attributes"
    route = "/{envId}/roles/{roleId}/"
    method = "patch"
    enabled = True


class CreateRole(Role):
    name = "create"
    route = "/{envId}/roles/"
    method = "post"
    enabled = True


class DeleteRole(Role):
    name = "delete"
    route = "/{envId}/roles/{roleId}/"
    method = "delete"
    enabled = True


class ListRoles(Role):
    name = "list"
    route = "/{envId}/roles/"
    method = "get"
    enabled = True


class RetrieveRole(Role):
    name = "retrieve"
    route = "/{envId}/roles/{roleId}/"
    method = "get"
    enabled = True


