from ansible import errors, runner
import json

def get_fqdn_host_list(host_vars, groups, target = 'all'):
    if type(host_vars) != runner.HostVars:
        raise errors.AnsibleFilterError("|failed expects a HostVars")

    if type(groups) != dict:
        raise errors.AnsibleFilterError("|failed expects a Dictionary")

    data = []
    for host in host_vars:
        data.append(host_vars[host][ansible_fqdn])
    return data

class FilterModule (object):
    def filters(self):
        return {"get_fqdn_host_list": get_fqdn_host_list}