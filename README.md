

using fig for [Docker] orchestration
------------------------------------

* Hardcoding the hostname seems a bit fishy

  ```
  root@offshore:~/test# fig ps
      Name                  Command               State       Ports      
  ----------------------------------------------------------------------
  test_redis_1   redis-server                     Up      6379/tcp       
  test_web_1     uwsgi --http 0.0.0.0:8080  ...   Up      9900->8080/tcp 
  
  root@offshore:~/test# docker inspect test_web_1 | grep -i hosts
    "HostsPath": "/var/lib/docker/containers/a00b...30/hosts",

  root@offshore:~/test# cat /var/lib/docker/containers/a00b...30/hosts
  172.17.0.56   a00b183fb8c2
  # ...
  172.17.0.54   test_redis_1
  172.17.0.54   redis_1
  ```

* Persistence is magical, a little too implicit for my tastes
  ```
  root@offshore:~/test# docker inspect test_redis_1 | grep -C 2 /data
          "User": "redis",
          "Volumes": {
              "/data": {}
          },
          "WorkingDir": "/data"
      },
      "Created": "2014-08-23T02:14:41.412924439Z",
  --
      },
      "Volumes": {
          "/data": "/var/lib/docker/vfs/dir/677a...ad"
      },
      "VolumesRW": {
          "/data": true
      }
  }
  ```
* Using the directory name as 'project name' (and as container name prefix) is clever, but again, frail: redis loses its magical persistence :(

That said, it's not aiming to be a full-blown Shipyard, Orchard or other Docker-based-PaaS systems.
