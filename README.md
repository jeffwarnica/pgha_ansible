# Postgresql High Availibility with Ansible

Use ansible to configure a collection of servers as a postgresql async cluster.

# What you get

For >=3 nodes, a highly available cluster for postgresql server.

# What you need

Two or more RHEL 7.x systems, suitably registered to RHN. Untested against non-clean installs, but might work if you don't mind other things being broken. Ansible 1.9 somewhere, which could be one of the target nodes.

Highly discourage a 2 node cluster.

**USE AT YOUR OWN RISK. PROHIBITED WHERE VOID. VOID WHERE PROHIBITED.** 

# Quick start:

Configure *inventory* with a list of hosts and *configurable_vars.yml* in this directory.

Runit: `ansible-playbook  hadb.yml`

# Useful runtime commands

* `crm_mon -Afr` for continious cluster monitoring, `crm_mon -Afr -1` for a one time run
* `pcs resource cleanup pgsql` as a generic cluster, er, cleanup ad sanity check.
* Detailed failure and recovery scenarios in: [recovery.md](recovery.md)

Relevant references:
* https://access.redhat.com/sites/default/files/attachments/cloudforms_ha_master_v4.pdf
* http://clusterlabs.org/wiki/PgSQL_Replicated_Cluster


# TODO

* test more failure/recovery scenarios
* include archive/cleanup scripts
