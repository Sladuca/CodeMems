REPO="$(dirname $0)/../charts/repo" 
CHARTS="$(dirname $0)/../charts/"
for d in $CHARTS*; do
  # only grab dirs
  if [ -d "$d" ] && ! echo "$d" | grep "repo"; then
    helm package $d -d $REPO # package the chart into the repo
    helm repo index $REPO # reindex the repo with the new chart
  else
    echo "skipping helm chart repo"
  fi
done
