---
configuration:
  event:
    maxclients:
      default: 150
      description: Maximum number of simultaneous client connections
      minimum: 0
      required: false
      type: integer
    maxrequestsperchild:
      default: 0
      description: Maximum number of requests a server process serves.
      minimum: 0
      required: false
      type: integer
    maxsparethreads:
      default: 75
      description: Maximum number of worker threads which are kept spare.
      minimum: 0
      required: false
      type: integer
    minsparethreads:
      default: 25
      description: Minimum number of worker threads which are kept spare,
      minimum: 0
      required: false
      type: integer
    startservers:
      default: 5
      description: Initial number of server processes to start.
      minimum: 0
      required: false
      type: integer
    threadlimit:
      default: 64
      description: ThreadsPerChild can be changed to this maximum value during a graceful
        restart. ThreadLimit can only be changed by stopping and starting Apache.
      minimum: 0
      required: false
      type: integer
    threadsperchild:
      default: 25
      description: Constant number of worker threads in each server process.
      minimum: 0
      required: false
      type: integer
  group:
    default: www-data
    description: Apache running group.
    required: false
    type: string
  keepalive:
    default: true
    description: Whether or not to allow persistent connections.
    enum:
    - true
    - false
    - true
    - false
    required: false
    type: string
  keepalivetimout:
    default: 5
    description: Number of seconds to wait for the next request from the same client
      on the same connection.
    minimum: 0
    required: false
    type: integer
  maxkeepaliverequests:
    default: 100
    description: The maximum number of requests to allow during a persistent connection.
    minimum: 0
    required: false
    type: integer
  prefork:
    maxclients:
      default: 150
      description: Maximum number of server processes allowed to start.
      minimum: 0
      required: false
      type: integer
    maxrequestsperchild:
      default: 4000
      description: Maximum number of requests a server process serves.
      minimum: 0
      required: false
      type: integer
    maxspareservers:
      default: 10
      description: Maximum number of server processes which are kept spare.
      minimum: 0
      required: false
      type: integer
    minspareservers:
      default: 2
      description: Minimum number of server processes which are kept spare.
      minimum: 0
      required: false
      type: integer
    startservers:
      default: 5
      description: Number of server processes to start.
      minimum: 1
      required: false
      type: integer
  timeout:
    default: 300
    description: The number of seconds before receives and sends time out.
    minimum: 0
    required: false
    type: integer
  user:
    default: www-data
    description: Apache running user.
    required: false
    type: string
  worker:
    maxclients:
      default: 150
      description: Maximum number of simultaneous client connections
      minimum: 0
      required: false
      type: integer
    maxrequestsperchild:
      default: 0
      description: Maximum number of requests a server process serves.
      minimum: 0
      required: false
      type: integer
    maxsparethreads:
      default: 75
      description: Maximum number of worker threads which are kept spare.
      minimum: 0
      required: false
      type: integer
    minsparethreads:
      default: 25
      description: Minimum number of worker threads which are kept spare,
      minimum: 0
      required: false
      type: integer
    startservers:
      default: 5
      description: Initial number of server processes to start.
      minimum: 1
      required: false
      type: integer
    threadlimit:
      default: 64
      description: ThreadsPerChild can be changed to this maximum value during a graceful
        restart. ThreadLimit can only be changed by stopping and starting Apache.
      minimum: 0
      required: false
      type: integer
    threadsperchild:
      default: 25
      description: Constant number of worker threads in each server process.
      minimum: 0
      required: false
      type: integer
documentation: http://httpd.apache.org/docs/
experimental: true
tags:
- web
tasks:
- description: Start Apache if stopped
  name: start
- description: Stop Apache if started
  name: stop
- description: Reload Apache, reload the configuration and perform a graceful restart
  name: reload
- description: Restart Apache, reload the configuration (but kills existing connection)
  name: restart
title: Apache

---


### Notes

For better user experience you may prefer the use of the `reload` task instead of `restart`.

