---
title: CLI
---

The Command Line Interface (CLI) lets you interact with devo. directly from your terminal. It allows you do everything that you can do through the Web UI: triggering tasks, monitoring the status of a server or listing your repositories.

## Installation

You will need `python 2.7+` as well as `pip` installed on your system.

### MacOS

We recommend MacOS users to use [Homebrew](http://brew.sh/) for installing pip.

    brew install python-pip
    sudo pip install https://app.devo.ps/cli/devops-cli-latest.tar.gz

### Ubuntu / Debian

    sudo apt-get install python-pip
    sudo pip install https://app.devo.ps/cli/devops-cli-latest.tar.gz

### CentOS / Fedora / RH

You will first need to install EPEL (you can find plenty of tutorials for [Fedora](http://fedoraproject.org/wiki/EPEL/FAQ#howtouse) or [CentOS & RH](http://www.rackspace.com/knowledge_center/article/installing-rhel-epel-repo-on-centos-5x-or-6x))

    sudo pip install https://app.devo.ps/cli/devops-cli-latest.tar.gz

*The CLI isn't currently tested or optimized on the Windows platform.*

## Usage

### Login / Logout

All CLI commands require you to be authenticated. The API keys are available on the [user settings page](https://app.devo.ps/#/user/settings).

```
shell> devops login
shell> devops logout
```

### Help

The help will give you the full list of commands supported by the CLI.

```
shell> devops --help 
```

### List

- **List repositories**: will return the list of all the repositories of your logged-in user

```
shell> devops list repos
```

- **List nodes**: will return the list of the nodes defined in the current repository (if you are in a devo.ps' managed git repository), or in the repository specified in the option

```
# Get the list of nodes in the current repository
shell> devops list nodes

# Get the list of nodes in another repository
shell> devops list --repo=other_repo nodes
```

- **List tasks**: will return the list of the tasks (either in the current repository or in the repo defined in the option - same as for nodes)

```
shell> devops list [--repo=other_repo] tasks
```

- **List webhooks**: will return the list of webhooks registered within the current repository and the linked task

```
shell> devops list [--repo=other_repo] webhooks
```

### Info

- **Nodes info**: will return the essential info about your nodes including:
  - IP address
  - sync status (success / error)
  - short list of services
  - `devops` SSH public key

```
shell> devops info [--repo=other_repo] --node {node_id}
```

### Run and Sync actions

- **Run**: will effectively triggers the execution of the requested task. Eventually will execute each step of the task on the nodes defined in the task definition

```
shell> devops run [--repo=other_repo] {task_id}
```

- **Sync**: will request a node to be synced. Usually sync operation are automatically triggered upon git commit/push of a node YAML file. But the sync operation may sometime fail due (e.g. error in the configuration, network error). The `Sync` action triggered via the CLI will perform a full sync of the node and ensure the remote server effectively is synced with its definition.

```
shell> devops sync [--repo=other_repo] {node_id}
```

### Logs

Getting to know more in detail what is going on during the execution of task may prove invaluable. Logs are there for that.

Not to get confused, the logs available are the logs of the operations performed by the devops platform, not any other log defined on the remote platform (e.g. `/var/log/messages`, nginx logs)

- **Node sync logs**: will show each individual step performed during the sync operation

```
shell> devops logs [--repo=other_repo] --node {node_id}
```

- **Task's run logs**: will show the log of a specific run (by id); the id of a specific run is obtained via the `details` command for a task

```
shell> devops logs [--repo=other_repo] --task {task_id} {run_id}
```

### SSH

Simple yet useful way to access your nodes over ssh without having to bother with the IP address

```
shell> devops ssh [--repo=other_repo] [{node_id}]
```

**Notes**:
- {node_id} is optional and only required if you have more than one node defined in your repository