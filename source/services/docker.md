---
configuration: {}
documentation: https://docs.docker.com/
tags:
- infrastructure
title: Docker

---
Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.

## Example

    services:
      docker: '*'

Add support for Docker containers on the node.

Note that the server will be restarted in order to apply the proper option to the kernel.
## Tasks
### restart
# Task Restart

Restart Docker

### reload
# Task Reload

### start
# Task Start

Start Docker

### stop
# Task Stop

Stop Docker
