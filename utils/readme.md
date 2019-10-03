# Utils
This directory contains several utility scripts useful for development. Their functionality and usage is roughly documented here

## clean_minikube.sh
When helm fails to install a chart, oftentimes it has leftover state in the cluster that needs to be cleared. While you could go and prune it using kubectl, it's kind of annoying. Instead, this script simply tears down the cluster, deletes it, rebuilds a new cluster, and inits helm inside it. It takes no arguments

## docker_build_all.sh
Rebuilds all of the microservices. This will probably be made to take args to specify a specific one or all of them, but I haven't gotten around to that yet

## package_chart.sh
Takes one argument, the path to a chart directory, and packages it into the chart repo laziy being hosted within this github repo

## setup_helm_local
Sets up all of the helm shit in minikube. Requires that minikube be already running.
