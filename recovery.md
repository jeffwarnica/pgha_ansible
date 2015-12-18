#Two node cluster - NO STONITH

## Master/Slave lose connectivity

* Master continues to run. VIP remains with master.
* **SPLIT BRAIN** VERY BAD.
* Master continues as master; slave promotes self to master, takes IP address
** Two nodes have VIP, both think and claim they are master
* Connectivity recovers.
* **IMPOSSIBLE TO KNOW WHO HAS BEST DATA** ---> *BONED*

## Slave dies (e.g VM hard off)

* Master continues to run. VIP remains with master.
* *REBOOT* Slave
* Slave restarts, connects to cluster, PG starts, resyncs
* **COOL**

## Master dies (e.g VM hard off)

* Active connections to DB fail
* Cluster detects failure; DB status slave->alone->master; VIP starts
* New connections to VIP on new master OK
* Ex-master reboots; PG refuses to start `My data may be inconsistent. You have to remove /var/opt/rh/rh-postgresql94/lib/pgsql/data/tmp/PGSQL.
lock file to force start.`
** DO SO: `# rm /var/opt/rh/rh-postgresql94/lib/pgsql/data/tmp/PGSQL.lock`
** KICK PCS:`# pcs resource cleanup pgsql`
* PG restarts as slave, resyncs
* **COOL**

