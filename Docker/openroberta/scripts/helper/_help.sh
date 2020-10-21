#!/bin/bash

echo "run.sh [-q] [-yes] [-D]                                              be quiet, answer all questions with 'y', debug mode"
echo "       help                                                          this text"
echo "       gen <server> | start <server> | stop <server>                 gen builds image; start first tries to stop, then (re-)starts the server; stop stops the server"
echo "       from-hub <server> <repo-name>                                 loads an image from a hub. A repo-name is 'openroberta/server_<x64-or-arm32v7>:<version-as-3.9.0>"
echo "       deploy <server>                                               deploy first calls gen, then calls start"
echo "       admin <server> <admin-cmd>                                    execute admin command on server, e.g. 'cleanup-temp-user-dirs'"
echo "       auto-deploy |                                                 check for git changes for servers found in variable AUTODEPLOY"
echo "       start-all | stop-all                                          start/stop db server and server found in variable SERVERS"
echo "       gen-dbc | start-dbc | stop-dbc                                generate db server, start and stop db server using variable DATABASES"
echo "       backup <database>                                             backup <database>. Note, that "server-<database>" is a container, which TRIGGERS the backup and must be running"
echo "       backup-save <dbBackup@<remote-host>:<from-path> <to-path>     save a db backup from a remote machine to this machine. <to-path> is relative to BASE-DIR"
echo "       alive <url> [mail={always|error}] [msg=<msg>]                 is the server alive? When to send mail (default: always). Set an additional mail header"
echo "       docker-info | network | logs | test-info                      container state, network and some log from running containers; info about deployed servers"
echo ""
echo "       monthly-stat <server> [month]                                 run the monthly stats for a server. Optionally supply the month (e.g. '05' or '12')"
echo "       show-server                                                   some data about processes with many open file descriptors (FD)"
echo "       show-resources <server> [<file> [<lower> [<upper> [ <url> [<hours> [<pid>]]]]] show resource usage. Parameter description is in file helper/_showResources.sh"
echo "       show-activity-once <server> [<file> [ <url>]]                 show accumulated user activity. Parameter description is in file helper/_showActivityOnce.shs"
echo ""
echo "dangerous commands:"
echo "       prune                                                         rm as much unused data from docker as possible"
echo "       auto-restart <server> <url> [<secBetween>] [<secRetry>]       restart a container if <url>/rest/alive doesn't respond. Check every <secBetween> sec (default: 60)"
echo "                                                                     to avoid false positives, check again after <secRetry> sec (default 30). Url is like https://dns:port"
echo "       gen-net                                                       generate the docker network ${DOCKER_NETWORK_NAME}"
echo "       start-export <server>                                         start a server from the export dir outside of docker"
