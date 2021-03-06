---
title: Tasks
---

Tasks are simple sequences of commands performed on designed [nodes](/manual/nodes) of a repository upon certain events (aka "triggers").

## Task file

As with nodes, you define a task using a simple YAML (`.yml`) file.

*We currently require that you name the file as the task id (see example) and save it in the `tasks/` folder. We are working on adding support for arbitrary file names and folders, allowing you to save multiple tasks in a single file.*

For example, we could add a `deploy.yml` file with the following content:

    id: deploy
    type: task
    name: Deployment pipeline

    triggers:
      webhooks:
        - path: deploy/my/app
    
    targets:
      - nodejs_server
    
    vars:
      build: /opt/build_temp
      domain: example.com
    
    steps:
      - run: devops git update
        options:
          repo: https://github.com/Wiredcraft/octokan.com.git
          dest: "{{ build }}"
          version: master
      - run: cd {{ build }}; make build ; cp -a _site/* /var/www/{{ domain }}

## Format

<dl>
  <dt><code><span class='type'>string</span> id</code></dt>
  <dd>The id of the task, currently has to match the file name.</dd>

  <dt><code><span class='type'>string</span> name</code></dt>
  <dd>The name of the task as displayed in the Web UI and CLI.</dd>

  <dt><code><span class='type'>string</span> type</code></dt>
  <dd>Must be set to `task`, defines this file as a task.</dd>
  
  <dt><code><span class='type'>object</span> vars</code> <span class='optional'>Optional</span></dt>
  <dd>Used to define a list of variables local to the task. Useful to define values you want to use in the steps (see belows).</dd>

  <dt><code><span class='type'>object</span> triggers</code> <span class='optional'>Optional</span></dt>
  <dd>A list of events upon which to run the task. Currently only supports manual trigger and webhooks. <a href='#triggers'>Read more about triggers below</a>.</dd>

  <dt><code><span class='type'>object</span> targets</code></dt>
  <dd>A list of nodes id on which to run the task.</dd>

  <dt><code><span class='type'>object</span> steps</code></dt>
  <dd>
    A series of commands and tasks to be run one after the other.
    <dl>
      <dt><code><span class='type'>string</span> run</code></dt>
      <dd>A command to be run; it may be an inline shell command, the path to one of the [scripts](/manual/scripts) available in the repository or a `devops` command. <a href='#steps'>Read more about steps below</a>.</dd>
      
      <dt><code><span class='type'>object</span> options</code> <span class='optional'>Optional</span></dt>
      <dd>An object of options to be passed to the command if it is a devops command.</dd>

      <dt><code><span class='type'>object</span> targets</code></dt>
      <dd>A list of nodes id on which to run the command. **This takes precedence over the targets defined at the root of the task**.</dd>
    </dl>
  </dd>
</dl>

## Runs & Status

Everytime a task is triggered, an instance of that task, called a "run", is instanciated. Changes happening after a run has started won't affect it. Each run is asigned a unique id (the "run id").

A run can be:

Status | Description | Icon
--- | --- | ---
<span class='icon done'></span> | **Done** | The run completed successfully.
<span class='icon running'></span> | **Running** | The run is currently ongoing.
 <span class='icon error'></span> | **Failed** | The run aborted after running into an error (details about the error can be found in the console).

## Steps

The `steps` attribute defines the series of commands that composes the task. These commands can be of 3 kinds:

- **Inline command**: regular shell command. For example:

      steps:
        - run: mkdir folder

- **Script**: you can define shell, python or Ruby scripts in the `scripts/` folder, making it convenient to reuse commands across multiple tasks or simply isolate a complex set of commands. For example:

      steps:
        - run: devops scripts/some_script.sh

    *To use packages (`pip` or `gems`) we recommend you use the configuration of respectively the [Python](/services/python) or [Ruby](/services/ruby) services rather than installing them from within a script.*

- **devops command**: services installed on your nodes usually come with some helper commands. A devops command looks like `devops {SERVICE} {COMMAND}` where `{SERVICE}` is the name of the service and `{COMMAND}` the name of the specific command. Some of these commands require you to define options. For example, cloning or updating a git repository can be done as follow:

      steps:
        - run: devops git update
          options:
            repo: https://github.com/user/repo.git
            dest: /some/local/folder
            version: master

    *As for the scripts, we use the `devops` keyword. Services documentations list the devops commands available for each service. See for example [Git list of commands](/services/git#commands).*

Commands are run as the `devops` user on targeted nodes. You can however switch users by using the `sudo` command in scripts or inline commands.

## Triggers

Tasks are run whenever one of the triggers conditions are met.

### Webhook

Webhooks allow you define HTTP callbacks which you, or a 3rd party, can query with a `POST` payload.

The following definition in a task:

    triggers:
      webhooks:
        - path: some/secret/url
        - path: some/other/url

*While we are considering more security measures, like restricting access to webhooks for user defined IPs, we recommend that you use obfuscted/complex URLs for your webhooks (if you wish to keep it private).*

Will automatically create the following endpoints:

    https://wh.devo.ps/{USER}/{REPO}/some/secret/url
    https://wh.devo.ps/{USER}/{REPO}/some/other/url

Where `{USER}` is the repository owner and `{REPO}` the name of the repository.

When a webhook receives a `POST` payload, it gets converted a JSON object and assigned to the `{{ payload }}` [variable](/manual/variables).

### Cron

Crons allow you define a schedule when the task should be started.

The following definition in a task:

    triggers:
      crons:
        - '0 */2 * * *'

Will automatically create a new execution schedule and will get the task started every 2 hours.

*The syntax of the cron follows the regular unix crontab; you can find more details [here](https://en.wikipedia.org/wiki/Cron)*

You may typically want to use cron triggers for backup, any operation you want to schedule in advance, or periodically restart a buggy application.

### Event

Events are triggered at various time during the life of your infrastructure, for example when a `sync` operation on a node starts, when it completes, or when a task `run` starts and complete. Defining events in your trigger list allow tasks to listen to those events and automatically starts whenever such signal is received.

The following definition in a task:

    triggers:
      events:
        - node.my-node.create.success
        - task.some-task.run.error

Will automatically register this task to be executed when:

- the node `my-node` has been successfully created
- the task `some-task` fails a run

A complete list of the events is available in the [events](/manual/events/) section of the documentation.


