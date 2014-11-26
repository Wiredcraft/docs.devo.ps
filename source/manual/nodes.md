---
title: Nodes
---

A node is usually a server, either physical or virtual. However, it may also refer to another component of your infrastructure: a firewall, a load balancer or storage (e.g. S3).

*Currently, we only support servers but are actively working on adding support for load balancers, firewalls and clusters.*

## Node file

Each node is defined in a YAML (`.yml`) file.

*We currently require that you name the file as the node id (see example) and save it in the `nodes/` folder. We are working on adding support for arbitrary file names and folders, allowing you to save multiple nodes in a single file.*

For example, we could add a `web.yml` file with the following content:

    id: nodejs_server
    name: Node.js server
    type: server

    provider:
      name: digitalocean
      size: 66
      location: 3
      image: 5141286

    services:
      nodejs: '*'
      nginx: '*'

    configuration:
      nodejs:
        packages:
          - gulp
          - forever
          - bower      

Once pushed to `master`, this will provision a 512MB Ubuntu server on Digital Ocean (using the [provider credentials defined in your profile](/manual/profile#providers)) in their `San Francisco 1` datacenter (location and size values are [documented in the provider section](/providers/digitalocean/)). It will also install [Nginx](/services/nginx) and [Node.js](/services/nodejs) and additionally add the the `gulp`, `forever` and `bower` packages to Node.js.

### Format

<dl>
  <dt><code><span class='type'>string</span> id</code></dt>
  <dd>The id of the node, currently has to match the file name.</dd>

  <dt><code><span class='type'>string</span> name</code></dt>
  <dd>The name of the server as displayed in the Web UI and CLI.</dd>

  <dt><code><span class='type'>string</span> type</code></dt.>
  <dd>Type of the node, currently only `server` is supported.</dd>

  <dt><code><span class='type'>object</span> provider</code></dt>
  <dd>
    The provider information for the node, used for provisioning.
    <dl>
      <dt><code><span class='type'>string</span> name</code></dt>
      <dd>The id of the provider you want to use. We currently support Digital Ocean ([digitalocean](/providers/digitalocean)), EC2 ([ec2](/providers/ec2)), Linode ([linode](/providers/linode)) and Rackspace ([rackspace](/providers/rackspace)).</dd>
      
      <dt><code><span class='type'>integer</span> size</code></dt>
      <dd>id of the server size to use, as defined in the provider's documentation.</dd>
      
      <dt><code><span class='type'>integer</span> location</code></dt>
      <dd>id of the location (datacenter) to use, as defined in the provider's documentation.</dd>
      
      <dt><code><span class='type string'>string</span> image</code></dt>
      <dd>id of the image (OS) you want to use.</dd>
    </dl>
  </dd>

  <dt>
    <code><span class='type'>array</span> services</code>
    <span class='optional'>Optional</span>
  </dt>
  <dd>The list of services to be installed on the node; available services are documented in the **Services** section.</dd>

  <dt>
    <code><span class='type'>object</span> configuration</code>
    <span class='optional'>Optional</span>
  </dt>
  <dd>A list of configuration settings to apply to the installed services, as defined in each service's documentation page. Use the service id as the key (see the [services](#services) section below for an example).</dd>
</dl>

### Services

A service refers to a technology you want to add support for on your node; it may be a database (MySQL, CouchBase, MongoDB), a language (PHP, Python, Ruby, Node.js), a Web server (NGINX, Apache), a reverse-proxy or a load-balancer (Varnish), HAproxy, Squid)...

When adding a service to a node, you can specify a version or use the `*` as a wildcard for the latest avaiable version:

    services:
      nginx: '*'

*We are currently only support the wildcard option but will soon enable users to pick a specific version of a service and handle service ugprades.*

Services usually come with configuration and commands, both of which are detailed on the documentation page of the service.

For example, you can configure NGINX's gzip compression by modifying `http.gzip` variable, or change the default keepalive timeout (see [NGINX configuration](/services/nginx/#configuration)):

    services:
      nginx: '*'

    configuration:
      nginx:
        http:
          gzip: off
          keepalive_timeout: 120

Similarly, services may have commnads that you can use in [tasks](/manual/tasks). For an example, you could use the `devops nginx start` command (see [NGINX commands](/services/nginx/#commands)).

## Status

Whenever a change to a node is pushed to your repository, devo.ps will try to apply that change to your infrastructure (more information on this process in the [git section](/manual/git-repositories)).

Status | Description | Icon
--- | --- | ---
<span class='icon synced'></span> | **Synced** | The node is matching the state described in your repository. Traditional configuration management systems call this a "converged" state.
<span class='icon syncing'></span> | **Syncing** | The node is currently being updated to try and reach the state described in your repository. Traditional configuration management systems call "converging".
 <span class='icon error'></span> | **Out of sync** | The latest snycing failed or the service lost contact with the node. The current state isn't the same as what is in your repo. Check the console logs for more information.

*If a syncing fails, the system will try a certain amount of times before giving up. You trigger another series of attempts by using the sync action either through the Web UI or CLI.*

## SSH keys & Users

A `devops` user is created on all servers provisioned by devo.ps. This user is used by our service to maintain your servers (add services, update configuration...) and orchestrate [tasks](/manual/tasks).

Additionally, we add the [SSH keys defined in the profile](/manual/profile#ssh) of all collaborators to the server's `authorized_keys` file for the `devops` user. This means you can log in as the `devops` user by simply running the following command:

<code class='terminal pre'>ssh devops@{IP ADDRESS}</code>

*The IP address can be retrieved both from the Web UI (in the node's details) or using the CLI.*

If you have installed the [CLI](/manual/CLI.html), you can also use one of the following commands:

- From anywhere on your workstation:

    <code class='terminal pre'>devops ssh --repo={REPOSITORY} {NODE_ID}</code>

    Where `{REPOSITORY}` is the name of the repository and `{NODE_ID}` the id of the node you want to log into.

- From within the local repository clone:

    <code class='terminal pre'>devops ssh {NODE_ID}</code>

    *If you only have 1 node in the repository, `devops ssh` would suffice.*
    
## Adding and Removing nodes

Adding a node is as simple as creating a new `.yml` file in the `nodes/` folder that respects the conventions established above.

Removing a node will effectively remove the server (shutdown / delete) from the cloud provider it is seating on. To remove a node you can either:

- Edit the node and click on `Remove` next to the save button
- Remove the file directly if you are using `git`, commit and push back to your devo.ps repository.
