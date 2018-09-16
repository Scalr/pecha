__author__ = 'Dmitriy Korsakov'
__doc__ = 'Manage FarmRoles'

import copy

from scalrctl import commands
from scalrctl import click


class LaunchServer(commands.SimplifiedAction):

    post_template = {}

    def pre(self, *args, **kwargs):
        """
        before request is made
        """
        kv = {"import-data": {}}
        kv.update(kwargs)
        arguments, kw = super(LaunchServer, self).pre(*args, **kv)
        return arguments, kw


class FarmRoleClone(commands.SimplifiedAction):

    epilog = "Example: scalr-ctl farm-roles clone --farmRoleId <ID> --alias <ALIAS> [--farmId <FarmID>]"

    post_template = {
        "cloneFarmRoleRequest": {"name": ""}
    }

    def get_options(self):
        alias_hlp = "New alias name for the FarmRole being cloned."
        alias = click.Option(('--alias', 'alias'), required=True, help=alias_hlp)

        farm_hlp = "Identifier of the Farm to clone into. If omitted, current Farm is a target to clone the FarmRole."
        farm_id = click.Option(('--farmId', 'farm_id'), required=False, help=farm_hlp)

        options = [alias, farm_id]
        options.extend(super(FarmRoleClone, self).get_options())
        return options

    def pre(self, *args, **kwargs):
        """
        before request is made
        """
        name = kwargs.pop("alias", None)
        farm_id = kwargs.pop("farm_id", None)
        post_data = copy.deepcopy(self.post_template)
        post_data["cloneFarmRoleRequest"]["name"] = name
        if farm_id:
            post_data["cloneFarmRoleRequest"]["farm"]["id"] = farm_id
        kv = {"import-data": post_data}
        kv.update(kwargs)
        arguments, kw = super(FarmRoleClone, self).pre(*args, **kv)
        return arguments, kw
