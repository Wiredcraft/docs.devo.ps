---
configuration:
  events:
    worker_connections:
      default: 1024
      description: Number of concurrent http connection handled per nginx process
      minimum: 1
      required: false
      type: integer
  http:
    access_log:
      default: /var/log/nginx/access.log
      description: Global access log file path
      required: false
      type: string
    error_log:
      default: /var/log/nginx/error.log
      description: Global error log file path
      required: false
      type: string
    gzip:
      default: 'on'
      description: Enable gzip compression
      required: false
      type: string
    gzip_disable:
      default: msie6
      description: Space separated list of browser to disable gzip compression for
      required: false
      type: string
    keepalive_timeout:
      default: 65
      description: Keepalive timeout (sec) - 0 to disable
      minimum: 0
      required: false
      type: integer
    sendfile:
      default: 'on'
      description: Enable sendfile
      required: false
      type: string
    tcp_nodelay:
      default: 'on'
      description: Enable tcp_nodelay
      required: false
      type: string
    tcp_nopush:
      default: 'on'
      description: Enable tcp_nopush
      required: false
      type: string
    types_hash_max_size:
      default: 2048
      description: Maximum size of hash tables
      minimum: 0
      required: false
      type: integer
  pid:
    default: /var/run/nginx.pid
    description: Pid file path
    required: false
    type: string
  user:
    default: www-data
    description: Nginx running user.
    required: false
    type: string
  worker_processes:
    default: 4
    description: Number of Nginx processes
    minimum: 1
    required: false
    type: integer
documentation: http://wiki.nginx.org/Modules
tags:
- web
tasks:
- description: Start MongoDB if stopped
  name: start
- description: Stop MongoDB if started
  name: stop
- description: Reload MongoDB, reload the configuration and perform a graceful restart
  name: reload
- description: Restart MongoDB, reload the configuration (but kills existing connection)
  name: restart
- description: Defines a HTTP virtual host in Nginx config
  name: vhost add
  options:
    aliases:
      description: space separated list of domain name aliases
      required: false
      type: string
    domain:
      description: domain name
      required: true
      type: string
    port:
      description: listening port
      required: true
      type: integer
    routes:
      description: list of route objects
      required: true
      type: array
    upstreams:
      description: list of upstream objects
      required: false
      type: array
    webroot:
      description: subfolder to serve data from based on the root /var/www/_domain_
      required: false
      type: string
title: Nginx

---


### Options

#### Route object

Name | Type | Required | Default | Valid Values | Description
----|----|----|----|----|----
uri | string | True | | Any string including regex | Any string / regex that nginx understand as a `location`
type | string | True | | proxy / fastcgi / websocket / uwsgi / static | The type of handler for that route
to | string | True | | | Either an upstream name, or a service / url, or a path
custom | string | False | | | Custom inline nginx config to include within the route (e.g. auth, custom timeout)
static | string | False | root | alias / root | For type static only, define how to consider the source folder - alias or root

#### Upstream object

Name | Type | Required | Default | Valid Values | Description
----|----|----|----|----|----
name | string | True | | unique name on the node | Name of the upstream
backends | array | True | | TCP URL and Unix socket path | List of backends associated with the upstream

Note that the upstream name MUST be unique on the node.