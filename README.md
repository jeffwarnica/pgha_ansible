# Postgresql High Availibility with Ansible

Use ansible to configure a collection of servers as a postgresql async cluster.

#Current limitations

Currently works with RHEL 7.x OS, and has been tested with 2 nodes. Currently
suitable for testing purposes only; e.g. it compleately wipes out RPM repository 
configuration.  

**USE AT YOUR OWN RISK. PROHIBITED WHERE VOID. VOID WHERE PROHIBITED.** 

# Configure:

*inventory* and *vars.yml* in this directory

Relevant references:
* https://access.redhat.com/sites/default/files/attachments/cloudforms_ha_master_v4.pdf
* http://clusterlabs.org/wiki/PgSQL_Replicated_Cluster
* 


# TODO

* include archive/cleanup scripts
* Deal with selinux being enabled (proper labeling of /var/opt/rh/rh-postgresql94/lib/pgsql/wal-archive )

