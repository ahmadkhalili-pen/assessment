1. installing K3s
   '''
   sudo apt install curl wget git
   curl -sfL https://get.k3s.io | sh -
   sudo k3s kubectl get nodes
   sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
   pwd
   mkdir ./.kube
   sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
   sudo chown $(id -u):$(id -g) ~/.kube/config
   export KUBECONFIG=~/.kube/config
   echo 'export KUBECONFIG=~/.kube/config' >> ~/.bashrc
   source ~/.bashrc
   '''

2.Creating the DB
   kubectl create namespace db
   helm repo add bitnami https://charts.bitnami.com/bitnami
   helm repo update
   snap install helm
   sudo snap install helm --classic
   helm repo add bitnami https://charts.bitnami.com/bitnami
   helm repo update
   helm install mysqlcluster bitnami/mysql -f values.yaml --namespace db
   kubectl apply -f mysql-primary-nodeport.yaml


3. IP log
   mkdir ip-api
   cd ip-api/
   vi app.py
   vi requirements.txt
   vi Dockerfile
   sudo docker build -t ip-api:latest .
   sudo apt-get install ca-certificates curl
   sudo install -m 0755 -d /etc/apt/keyrings
   sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
   sudo chmod a+r /etc/apt/keyrings/docker.asc
   echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   sudo docker build -t ip-api:latest .
   kubectl create namespace web
   cat ../values.yaml
   kubectl create secret generic api-db-secret   --from-literal=db-user='root'   --from-literal=db-password='ahmad@123'   --from-literal=db-name='appdb'   -n web
   vi ip-api-deployment.yaml
   kubectl apply -f ip-api-deployment.yaml
   kubectl apply -f ip-api-nodeport.yaml
   sudo docker save ip-api:latest -o ip-api.tar
   sudo ctr -n k8s.io images import ip-api.tar
   sudo ctr -n k8s.io images list | grep ip-api
