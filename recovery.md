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
  * DO SO: `# rm /var/opt/rh/rh-postgresql94/lib/pgsql/data/tmp/PGSQL.lock`    
  * KICK PCS:`# pcs resource cleanup pgsql`
* PG restarts as slave, resyncs
* **COOL**

# Adding node to cluster
* Left as excersize of the reader.
  * pcs cluster node add ...
  * pcs .... no-quorum-policy=stop
  * pcs cluster update pgsql ....
  * pcs cluster update msPostgresql ...
  * copy data
  * ...
  * proft?

# Three node cluster

## Single slave loses connectivity
* Disconnected node shuts down pgsql
* Remaining systems continue as-is
* **RECONNECT**
* Node rejoins cluster
* postgres restarted
* postgres resyncs

## *Master* loses connectivity, but slaves keep connectivity to each other
* Disconnected node shuts down postgres, drops VIP 
* Other nodes quicky decide on new master, 
* promote/restart postgres on new master
* starts VIP
* **RECONNECT**
*  Node joins cluster, reconfigures postgres as slave
  * **fails to restart postgres**
  * pg_log/xxx.log > `FATAL:  could not receive data from WAL stream: ERROR:  requested starting point 0/6000000 is ahead of the WAL flush position of this server 0/50006E0`
  * on 'master': `# chown postgres.postgres ./tmp/PGSQL.lock`
  * on recovering node, in `/var/opt/rh/rh-postgresql94/lib/pgsql`:  `# rm -rf data/*; scl enable rh-postgresql94 '/opt/rh/rh-postgresql94/root/usr/bin/pg_basebackup -D data/ -h MASTER_HOST_NAME -U replicator -X stream -P'
  * on recovering node: `# rm /var/opt/rh/rh-postgresql94/lib/pgsql/data/tmp/PGSQL.lock`

## 3 nodes all lose connectivity to everything at the same time

## Master hard off
* vip stops; one slave disconnects; other restarts as master; slave reconnects
* 

## Single slave hard off
