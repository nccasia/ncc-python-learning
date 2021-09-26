- [Introduction to Docker](#introduction-to-docker)
  - [Overview](#overview)
  - [How to build, run, and debug Docker containers.](#how-to-build-run-and-debug-docker-containers)
  - [How to pull Docker images from Docker Hub and Google Container Registry.](#how-to-pull-docker-images-from-docker-hub-and-google-container-registry)
  - [How to push Docker images to Google Container Registry.](#how-to-push-docker-images-to-google-container-registry)
- [Hello Node Kubernetes](#hello-node-kubernetes)
  - [Prepare a container](#prepare-a-container)
  - [Create your cluster](#create-your-cluster)
  - [Create your pod](#create-your-pod)
  - [Allow external traffic](#allow-external-traffic)
  - [Scale up your service](#scale-up-your-service)
- [Kubernetes Engine: Qwik Start](#kubernetes-engine-qwik-start)
  - [Overview](#overview-1)
  - [GKE cluster](#gke-cluster)
  - [Deploy an application to the cluster](#deploy-an-application-to-the-cluster)
- [Orchestrating the Cloud with Kubernetes](#orchestrating-the-cloud-with-kubernetes)
  - [Overview](#overview-2)
  - [Sample code](#sample-code)
  - [Deployments and pods and services](#deployments-and-pods-and-services)
  - [Pods](#pods)
  - [Services](#services)
  - [Adding Labels to Pods](#adding-labels-to-pods)
  - [Deploying Applications with Kubernetes](#deploying-applications-with-kubernetes)
- [Managing Deployments Using Kubernetes Engine](#managing-deployments-using-kubernetes-engine)
  - [Prepare cluster, deployment, pod, service](#prepare-cluster-deployment-pod-service)
  - [Scale a Deployment](#scale-a-deployment)
  - [Rolling update](#rolling-update)
  - [Pause and resume and rollback a rolling update](#pause-and-resume-and-rollback-a-rolling-update)
  - [Canary deployments](#canary-deployments)
  - [Blue-green deployments](#blue-green-deployments)
- [Setting up Jenkins on Kubernetes Engine](#setting-up-jenkins-on-kubernetes-engine)
  - [Create a cluster](#create-a-cluster)
  - [Configure and install Jenkin via Helm.](#configure-and-install-jenkin-via-helm)
- [Continuous Delivery with Jenkins in Kubernetes Engine](#continuous-delivery-with-jenkins-in-kubernetes-engine)
  - [What is Continuous Delivery / Continuous Deployment?](#what-is-continuous-delivery--continuous-deployment)
  - [Provisioning Jenkins](#provisioning-jenkins)
  - [Deploying the Application](#deploying-the-application)
  - [Scale up the production environment](#scale-up-the-production-environment)
  - [Creating the Jenkins Pipeline](#creating-the-jenkins-pipeline)
  - [Adding your service account credentials](#adding-your-service-account-credentials)
  - [Creating the Development Environment](#creating-the-development-environment)
- [Troubleshooting Workloads on GKE for Site Reliability Engineers](#troubleshooting-workloads-on-gke-for-site-reliability-engineers)

# Introduction to Docker

## Overview

Docker is an open platform for developing, shipping, and running applications. With Docker, you can separate your applications from your infrastructure and treat your infrastructure like a managed application. 

Docker does this by combining kernel containerization features with workflows and tooling that helps you manage and deploy your applications.



## How to build, run, and debug Docker containers.

run a hello world container to get started:

```
docker run hello-world
```

Run the following command to take a look at the container image it pulled from Docker Hub:

```
docker images
```

List containers 
```
docker ps -a
```

Build from Dockerfile
```
docker build -t node-app:0.1 .
```

Run
```
docker run -p 4000:80 --name my-app node-app:0.1
```

## How to pull Docker images from Docker Hub and Google Container Registry.

```
docker logs -f [container_id]
```

Sometimes you will want to start an interactive Bash session inside the running container.
```
docker exec -it [container_id] bash
```

You can examine a container's metadata in Docker by using Docker inspect:
```
docker inspect [container_id]
```

## How to push Docker images to Google Container Registry.
Tag node-app:0.2. Replace [project-id] with your configuration..
```
docker tag node-app:0.2 gcr.io/[project-id]/node-app:0.2
```

Push to grc
```
docker push gcr.io/[project-id]/node-app:0.2
```

# Hello Node Kubernetes

## Prepare a container

Create a simple nodeJs web application

Create a docker image from a file 
```
FROM node:6.9.2
EXPOSE 8080
COPY server.js .
CMD node server.js
```

Build a docker image with a target to GCR (google container registry)
```
docker build -t gcr.io/qwiklabs-gcp-02-63f0493fd933/hello-node:v1 .
```

Run the container from the image
```
docker run -d -p 8080:8080 gcr.io/qwiklabs-gcp-02-63f0493fd933/hello-node:v1
```

Stop the container
```
docker stop container_id
```

Config to push image to GCT
```
gcloud auth configure-docker
```

Push image
```
docker push gcr.io/qwiklabs-gcp-02-63f0493fd933/hello-node:v1
```

Check in your GCR

## Create your cluster
A cluster consists of a Kubernetes master API server hosted by Google and a set of worker nodes. The worker nodes are Compute Engine virtual machines.

Config gcloud
```
gcloud config set project PROJECT_ID
```

Create a cluster
```
gcloud container clusters create hello-world \
                --num-nodes 2 \
                --machine-type n1-standard-1 \
                --zone us-central1-a
```

## Create your pod
A Kubernetes pod is a group of containers tied together for administration and networking purposes. It can contain single or multiple containers. 

Create a pod with the kubectl run command
```
kubectl create deployment hello-node \
    --image=gcr.io/qwiklabs-gcp-02-63f0493fd933/hello-node:v1
```

As you can see, you've created a deployment object. Deployments are the recommended way to create and scale pods. Here, a new deployment manages a single pod replica running the hello-node:v1 image. => Workloads - type Deployment

Type Workloads 
 - Deployment
 - Deamon Set
 - Pod


Get info
```
kubectl get deployments
kubectl get pods
kubectl cluster-info
kubectl config view
kubectl get events
kubectl logs <pod-name>
```

## Allow external traffic

By default, the pod is only accessible by its internal IP within the cluster. In order to make the hello-node container accessible from outside the Kubernetes virtual network, you have to expose the pod as a Kubernetes **service**.

```
kubectl expose deployment hello-node --type="LoadBalancer" --port=8080
```

To find the publicly-accessible IP address of the service, request kubectl to list all the cluster services:
```
kubectl get services
```

## Scale up your service

One of the powerful features offered by Kubernetes is how easy it is to scale your application (change the number of pods inside the deployment). Suppose you suddenly need more capacity. You can tell the replication controller to manage a new number of replicas for your pod:
```
kubectl scale deployment hello-node --replicas=4
```



# Kubernetes Engine: Qwik Start

## Overview

The Kubernetes Engine environment consists of multiple machines grouped to form a container cluster. 

Kubernetes provides the mechanisms through which you interact with your container cluster. You use Kubernetes commands and resources to deploy and manage your applications, perform administrative tasks, set policies, and monitor the health of your deployed workloads.

 - Load balancing for Compute Engine instances
 - Node pools to designate subsets of nodes within a cluster for additional flexibility
 - Automatic scaling of your cluster's node instance count
 - Automatic upgrades for your cluster's node software
 - Node auto-repair to maintain node health and availability
 - Logging and Monitoring with Cloud Monitoring for visibility into your cluster

## GKE cluster

A cluster consists of at least one cluster master machine and multiple worker machines called nodes. Nodes are Compute Engine virtual machine (VM) instances that run the Kubernetes processes necessary to make them part of the cluster.

## Deploy an application to the cluster

You can now deploy a containerized application to the cluster. For this lab, you'll run hello-app (the previous lab container on the grc) in your cluster.

create a new **Deployment**
```
kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
```

create a Kubernetes **Service**, which is a Kubernetes resource that lets you expose your application to external traffic
```
kubectl expose deployment hello-server --type=LoadBalancer --port 8080
```

inspect the hello-server, now the **service** can be accessed via public IP
```
kubectl get service
```

open Kubernet Engine to inspect the cluster details

delete the cluster
```
gcloud container clusters delete [CLUSTER-NAME]
```

# Orchestrating the Cloud with Kubernetes

## Overview 

start up a cluster

```
gcloud container clusters create io
```

## Sample code
```
deployments/  /* Deployment manifests */
  ...
nginx/        /* nginx config files */
  ...
pods/         /* Pod manifests */
  ...
services/     /* Services manifests */
  ...
tls/          /* TLS certificates */
  ...
cleanup.sh    /* Cleanup script */
```

## Deployments and pods and services

use the `kubectl create` command to launch a single instance of the nginx container -> you can see it in the Workloads tab in Kubernes Engine
```
kubectl create deployment nginx --image=nginx:1.10.0
```

Kubernetes has created a **deployment**, deployments keep the pods up and running even when the nodes they run on fail.

In Kubernetes, all containers run in a **pod**. Use the kubectl get pods command to view the running nginx container: -> see details in each node
```
kubectl get pods
```

Once the nginx container has a Running status you can expose it outside of Kubernetes using the kubectl expose command: -> see in **Services**
```
kubectl expose deployment nginx --port 80 --type LoadBalancer
```

So what just happened? Behind the scenes Kubernetes created an external Load Balancer with a public IP address attached to it. Any client who hits that public IP address will be routed to the pods behind the service.

List our services
```
kubectl get services
```

## Pods

Pods represent and hold a collection of one or more containers. Generally, if you have multiple containers with a hard dependency on each other, you package the containers inside a single pod.

Single pod or multiple pods run inside a Node.

Pods also have Volumes. Volumes are data disks that live as long as the pods live, and can be used by the containers in that pod. Pods provide a shared namespace for their contents which means that the two containers inside of our example pod can communicate with each other, and they also share the attached volumes.

Pods also share a network namespace. This means that there is one IP Address per pod.

pod configuration files `monolith.yaml`
```
apiVersion: v1
kind: Pod
metadata:
  name: monolith
  labels:
    app: monolith
spec:
  containers:
    - name: monolith
      image: kelseyhightower/monolith:1.0.0
      args:
        - "-http=0.0.0.0:80"
        - "-health=0.0.0.0:81"
        - "-secret=secret"
      ports:
        - name: http
          containerPort: 80
        - name: health
          containerPort: 81
      resources:
        limits:
          cpu: 0.2
          memory: "10Mi"
```

Create the monolith pod using kubectl: -> see Workloads
```
kubectl create -f pods/monolith.yaml
```

By default, pods are allocated a private IP address and cannot be reached outside of the cluster. Use the kubectl port-forward command to map a local port to a port inside the monolith pod.

Use the kubectl exec command to run an interactive shell inside the Monolith Pod. This can come in handy when you want to troubleshoot from within a container:
```
kubectl exec monolith --stdin --tty -c monolith /bin/sh
```

## Services

Pods aren't meant to be persistent. They can be stopped or started for many reasons - like failed liveness or readiness checks - and this leads to a problem:

What happens if you want to communicate with a set of Pods? When they get restarted they might have a different IP address.

That's where Services come in. Services provide stable endpoints for Pods.

Services use labels to determine what Pods they operate on. If Pods have the correct labels, they are automatically picked up and exposed by our services.

Pod configuration files `secure-monolith.yaml`
```
apiVersion: v1
kind: Pod
metadata:
  name: "secure-monolith"
  labels:
    app: monolith
spec:
  containers:
    - name: nginx
      image: "nginx:1.9.14"
      lifecycle:
        preStop:
          exec:
            command: ["/usr/sbin/nginx","-s","quit"]
      volumeMounts:
        - name: "nginx-proxy-conf"
          mountPath: "/etc/nginx/conf.d"
        - name: "tls-certs"
          mountPath: "/etc/tls"
    - name: monolith
      image: "kelseyhightower/monolith:1.0.0"
      ports:
        - name: http
          containerPort: 80
        - name: health
          containerPort: 81
      resources:
        limits:
          cpu: 0.2
          memory: "10Mi"
      livenessProbe:
        httpGet:
          path: /healthz
          port: 81
          scheme: HTTP
        initialDelaySeconds: 5
        periodSeconds: 15
        timeoutSeconds: 5
      readinessProbe:
        httpGet:
          path: /readiness
          port: 81
          scheme: HTTP
        initialDelaySeconds: 5
        timeoutSeconds: 1
  volumes:
    - name: "tls-certs"
      secret:
        secretName: "tls-certs"
    - name: "nginx-proxy-conf"
      configMap:
        name: "nginx-proxy-conf"
        items:
          - key: "proxy.conf"
            path: "proxy.conf"
```

Create the `secure-monolith` **pods** and their configuration data:
```
kubectl create secret generic tls-certs --from-file tls/
kubectl create configmap nginx-proxy-conf --from-file nginx/proxy.conf
kubectl create -f pods/secure-monolith.yaml
```

`services/monolith.yaml`
```
kind: Service
apiVersion: v1
metadata:
  name: "monolith"
spec:
  selector:
    app: "monolith"
    secure: "enabled"
  ports:
    - protocol: "TCP"
      port: 443
      targetPort: 443
      nodePort: 31000
  type: NodePort
```

Use the kubectl create command to create the `monolith` **service** from the monolith service configuration file:
```
kubectl create -f services/monolith.yaml
```

Things to note:

- There's a selector which is used to automatically find and expose any pods with the labels app: monolith and secure: enabled.
- Now you have to expose the nodeport here because this is how you'll forward external traffic from port 31000 to nginx (on port 443).

## Adding Labels to Pods

```
kubectl label pods secure-monolith 'secure=enabled'
kubectl get pods secure-monolith --show-labels
```

## Deploying Applications with Kubernetes

Deployments are a declarative way to ensure that the number of Pods running is equal to the desired number of Pods, specified by the user.

 Behind the scenes Deployments use Replica Sets to manage starting and stopping the Pods. If Pods need to be updated or scaled, the Deployment will handle that. Deployment also handles restarting Pods if they happen to go down for some reason.

`auth.yaml`
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: auth
spec:
  selector:
    matchlabels:
      app: auth
  replicas: 1
  template:
    metadata:
      labels:
        app: auth
        track: stable
    spec:
      containers:
        - name: auth
          image: "kelseyhightower/auth:2.0.0"
          ports:
            - name: http
              containerPort: 80
            - name: health
              containerPort: 81
...
```

When you run the kubectl create command to create the auth deployment it will make one pod that conforms to the data in the Deployment manifest. This means you can scale the number of Pods by changing the number specified in the Replicas field.
```
kubectl create -f deployments/auth.yaml
```
-> see in Workloads

# Managing Deployments Using Kubernetes Engine

## Prepare cluster, deployment, pod, service

Create a **cluster** with five n1-standard-1 nodes (this will take a few minutes to complete):
```
gcloud container clusters create bootcamp --num-nodes 5 --scopes "https://www.googleapis.com/auth/projecthosting,storage-rw"
```

Deployment
```
kubectl explain deployment --recursive
```

When you run the kubectl create command to create the auth deployment, it will make one pod that conforms to the data in the Deployment manifest. This means we can scale the number of Pods by changing the number specified in the replicas field.
```
kubectl create -f deployments/auth.yaml
```

Once the deployment is created, Kubernetes will create a ReplicaSet for the Deployment. We can verify that a ReplicaSet was created for our Deployment:
```
kubectl get replicasets
```

Create service
```
kubectl create -f services/auth.yaml
```

## Scale a Deployment

```
kubectl scale deployment hello --replicas=5
```

## Rolling update

Deployments support updating images to a new version through a rolling update mechanism. When a Deployment is updated with a new version, it creates a new ReplicaSet and slowly increases the number of replicas in the new ReplicaSet as it decreases the replicas in the old ReplicaSet.

To update your Deployment, run the following command:
```
kubectl edit deployment hello
```

Then you can change the image definition => save

You can also see a new entry in the rollout history:
```
kubectl rollout history deployment/hello
```

## Pause and resume and rollback a rolling update
```
kubectl rollout pause deployment/hello
kubectl rollout status deployment/hello
kubectl rollout resume deployment/hello
kubectl rollout status deployment/hello
kubectl rollout undo deployment/hello
kubectl rollout history deployment/hello
```

## Canary deployments

A canary deployment is a deployment strategy that releases an application or service incrementally to a subset of users.

```
kubectl create -f deployments/hello-canary.yaml
```

To make sure the same user will always be served from the same version by creating a service with **session affinity**. 

 In the example below the service is the same as before, but a new sessionAffinity field has been added, and set to ClientIP. All clients with the same IP address will have their requests sent to the same version of the hello application.

```
kind: Service
apiVersion: v1
metadata:
  name: "hello"
spec:
  sessionAffinity: ClientIP
  selector:
    app: "hello"
  ports:
    - protocol: "TCP"
      port: 80
      targetPort: 80
```

## Blue-green deployments

The blue-green deployment approach does this by ensuring you have two production environments, as identical as possible.

Kubernetes achieves this by creating two separate deployments; one for the old "blue" version and one for the new "green" version.

# Setting up Jenkins on Kubernetes Engine

## Create a cluster
```
gcloud container clusters create jenkins-cd \
--num-nodes 2 \
--machine-type n1-standard-2 \
--scopes "https://www.googleapis.com/auth/projecthosting,cloud-platform"
```

Get the credentials for your cluster. Kubernetes Engine uses these credentials to access your newly provisioned cluster.
```
gcloud container clusters get-credentials jenkins-cd
```

Confirm that you can connect to your cluster.
```
kubectl cluster-info
```

## Configure and install Jenkin via Helm. 

Helm is a package manager that makes it easy to configure and deploy Kubernetes applications.

Jenkins is an open-source automation server that lets you flexibly orchestrate your build, test, and deployment pipelines. Jenkins allows developers to iterate quickly on projects without worrying about overhead issues that can stem from continuous delivery.

```
helm install cd stable/jenkins -f jenkins/values.yaml --version 1.2.2 --wait
```

Jenkin yml file
```
controller:
  installPlugins:
    - kubernetes:latest
    - workflow-job:latest
    - workflow-aggregator:latest
    - credentials-binding:latest
    - git:latest
    - google-oauth-plugin:latest
    - google-source-plugin:latest
    - google-kubernetes-engine:latest
    - google-storage-plugin:latest
  resources:
    requests:
      cpu: "50m"
      memory: "1024Mi"
    limits:
      cpu: "1"
      memory: "3500Mi"
  javaOpts: "-Xms3500m -Xmx3500m"
  serviceType: ClusterIP
agent:
  resources:
    requests:
      cpu: "500m"
      memory: "256Mi"
    limits:
      cpu: "1"
      memory: "512Mi"
persistence:
  size: 100Gi
serviceAccount:
  name: cd-jenkins
```

Run the following command to setup port forwarding to the Jenkins UI from the Cloud Shell
```
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/component=jenkins-master" -l "app.kubernetes.io/instance=cd" -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward $POD_NAME 8080:8080 >> /dev/null &
```

check that the Jenkins Service was created properly:
```
kubectl get svc
```

We are using the Kubernetes Plugin so that our builder nodes will be automatically launched as necessary when the Jenkins master requests them. Upon completion of their work, they will automatically be turned down and their resources added back to the clusters resource pool.

Notice that this service exposes ports 8080 and 50000 for any pods that match the selector. This will expose the Jenkins web UI and builder/agent registration ports within the Kubernetes cluster. Additionally, the jenkins-ui service is exposed using a ClusterIP so that it is not accessible from outside the cluster.


# Continuous Delivery with Jenkins in Kubernetes Engine

you will learn how to set up a continuous delivery pipeline with Jenkins on Kubernetes engine.

## What is Continuous Delivery / Continuous Deployment?

When you need to set up a continuous delivery (CD) pipeline, deploying Jenkins on Kubernetes Engine provides important benefits over a standard VM-based deployment.

When your build process uses containers, one virtual host can run jobs on multiple operating systems. Kubernetes Engine provides ephemeral build executors—these are only utilized when builds are actively running, which leaves resources for other cluster tasks such as batch processing jobs. Another benefit of ephemeral build executors is speed—they launch in a matter of seconds.

Kubernetes Engine also comes pre-equipped with Google's global load balancer, which you can use to automate web traffic routing to your instance(s). The load balancer handles SSL termination and utilizes a global IP address that's configured with Google's backbone network—coupled with your web front, this load balancer will always set your users on the fastest possible path to an application instance.

Now that you've learned a little bit about Kubernetes, Jenkins, and how the two interact in a CD pipeline, it's time to go build one.

## Provisioning Jenkins

Creating a Kubernetes cluster
```
gcloud container clusters create jenkins-cd \
--num-nodes 2 \
--machine-type n1-standard-2 \
--scopes "https://www.googleapis.com/auth/source.read_write,cloud-platform"
```

Now, get the credentials for your cluster:
```
gcloud container clusters get-credentials jenkins-cd
```

Install Jekin via Helm, check details in values.yaml file
```
helm install cd jenkins/jenkins -f jenkins/values.yaml --wait
```

Get list services
```
NAME               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)     AGE
cd-jenkins         ClusterIP   10.3.255.134   <none>        8080/TCP    8m53s
cd-jenkins-agent   ClusterIP   10.3.251.14    <none>        50000/TCP   8m53s  //where comes from???
kubernetes         ClusterIP   10.3.240.1     <none>        443/TCP     12m
```

Configure the Jenkins service account to be able to deploy to the cluster
```
kubectl create clusterrolebinding jenkins-deploy --clusterrole=cluster-admin --serviceaccount=default:cd-jenkins
```

Run the following command to setup port forwarding to the Jenkins UI from the Cloud Shell
```
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/component=jenkins-master" -l "app.kubernetes.io/instance=cd" -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward $POD_NAME 8080:8080 >> /dev/null &
```

## Deploying the Application

Create the Kubernetes namespace to logically isolate the deployment:
```
kubectl create ns production
```

Create the production and canary deployments, and the services using the `kubectl apply` commands:
```
kubectl apply -f k8s/production -n production
kubectl apply -f k8s/canary -n production
kubectl apply -f k8s/services -n production
```

## Scale up the production environment

```
kubectl scale deployment gceme-frontend-production -n production --replicas 4
kubectl get pods -n production -l app=gceme -l role=frontend
kubectl get pods -n production -l app=gceme -l role=backend
kubectl get service gceme-frontend -n production
```

## Creating the Jenkins Pipeline
Create a copy of the gceme sample app and push it to a Cloud Source Repository:
```
gcloud source repos create default
git init
git config credential.helper gcloud.sh
git remote add origin https://source.developers.google.com/p/$DEVSHELL_PROJECT_ID/r/default
...
```

## Adding your service account credentials

In the Jenkins user interface, click Manage Jenkins in the left navigation then click Manage Credentials.
-> add Credential Google

Navigate to your Jenkins user interface and create Pipeline

Config git credential

## Creating the Development Environment

The Jenkinsfile that defines that pipeline is written using the Jenkins Pipeline Groovy syntax. Using a Jenkinsfile allows an entire build pipeline to be expressed in a single file that lives alongside your source code. Pipelines support powerful features like parallelization and require manual user approval.

In order for the pipeline to work as expected, you need to modify the Jenkinsfile to set your project ID.

 

# Troubleshooting Workloads on GKE for Site Reliability Engineers

Google Kubernetes Engine (GKE) is a managed, production-ready environment for running containerized applications.

Your organization has deployed a multi-tier microservices application. It is a web-based e-commerce application called "Hipster Shop", where users can browse for vintage items, add them to their cart and purchase them. Hipster Shop is composed of many microservices, written in different languages, that communicate via gRPC and REST APIs. 

The architecture of the deployment is optimized for learning purposes and includes modern technologies as part of the stack: 
- Kubernetes, 
- Istio: extends Kubernetes to establish a programmable, application-aware network using the powerful Envoy service proxy. Working with both Kubernetes and traditional workloads, Istio brings standard, universal traffic management, telemetry, and security to complex deployments.
- Cloud Operations 
- App Engine
- gRPC
- OpenTelemetry: OpenTelemetry is a collection of tools, APIs, and SDKs. You can use it to instrument, generate, collect, and export telemetry data (metrics, logs, and traces) for analysis in order to understand your software's performance and behavior., and similar cloud-native technologies.

As a member of the Site Reliability Engineering (SRE) team, you are contacted when end users report issues viewing products and adding them to their cart. You will explore the various services deployed to determine the root cause of the issue and set up a Service Level Objective (SLO) to prevent similar incidents from occuring in the future.

