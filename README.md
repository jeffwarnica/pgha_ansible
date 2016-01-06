# Postgresql High Availibility with Ansible

Use ansible to configure a collection of servers as a postgresql async cluster.

# What you get

For >=3 nodes, a highly available cluster for postgresql server.

# What you need

* Two or more RHEL 7.x systems, suitably registered to RHN, in the same subnet. Untested against non-clean installs, but might work if you don't mind other things being broken. Ansible 1.9 somewhere, which could be one of the target nodes.

* An NFS server which is exporting a mount point big enough for a few days worth of the binary logs. Put the configuration in `/configurable_vars.yml` at `nfs_path:`

* A spare IP address in the same subnet as the target systems, to use as the floating master IP.

* DNS, target hosts hostnames, and/or target host /etc/hosts,  and `/inventory` with a shared understanding of hostnames.

* Better imagination as to passwords than `password` as is the default configuration.

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
