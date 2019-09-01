#SRS for Devs

## Getting Started

### Setting up local dev env

1. Set up [minikube](https://minikube.sigs.k8s.io/docs/start/), [docker](https://docs.docker.com/), and [helm](htttps://helm.sh/docs/using_helm/#quickstart-guide)
  * By default minikube only gets 1GB of RAM. Allocate more using `minikube config set memory N` where `N` is in MB. A short and clean explanation of `minikube config` can be found [here](https://darkowlzz.github.io/post/minikube-config/)
3. setup local helm repo with `setup_helm_local` in `utils`
4. do `helm install 
