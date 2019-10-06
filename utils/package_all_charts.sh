REPO="$(dirname $0)/../charts/repo" 
for d in */; do
  helm package $d -d $REPO # package the chart into the repo
  helm repo index $REPO # reindex the repo with the new chart
done
