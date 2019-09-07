REPO="$(dirname $0)/../charts/repo" 
helm package $1 -d $REPO # package the chart into the repo
helm repo index $REPO # reindex the repo with the new chart
