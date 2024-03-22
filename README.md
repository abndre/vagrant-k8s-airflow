# K8S e Airflow local dev

Este projeto foi feito para auxiliar o deploy do airflow com k8s, em sua maquina local, utilizando vagrant.


# vagrant

Alguns comandos basicos para ajudar

```
vagrant init

vagrant up

vagrant suspend

vagrant resume

vagrant reload

vagrant halt
```

Inicio o projeto vagrant usando o seguinte comando:

```
vagrant up
```


# ############################
## kubernets

Entre na maquina com

```
vagrant ssh
```


```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
```

## helm
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

## kind

```
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-amd64
chmod +x ./kind
```

# airflow

```
kind create cluster --image kindest/node:v1.21.1
```

confirmar que tudo esta ok

```
kubectl cluster-info --context kind-kind
```

```
helm repo add apache-airflow https://airflow.apache.org
```

```
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace -f airflow_var.yaml
```


## deletar
```
helm delete airflow --namespace airflow
```

## updgrade
```
helm upgrade airflow apache-airflow/airflow --namespace airflow -f airflow_var.yaml
```


## enviar imagem docker para o kind

```
docker build --pull --tag my-dags:0.0.2 .

kind load docker-image my-dags:latest
```

## ver o webserver so airflow no localhost

```
kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow --address 0.0.0.0
```