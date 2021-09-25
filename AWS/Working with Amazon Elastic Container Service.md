## Overview

Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster of Amazon EC2 instances.


 - Create a Task Definition, a description of an application that contains one or more Docker containers.
 - Create a Cluster, a logical grouping of Amazon EC2 instances on which you can place tasks.
 - Create a Service, that allows you to run and maintain a specified number of instances of a task definition simultaneously.
 - Scale up

## ECS
 - Container Instance: An Amazon EC2 instance that is running the Amazon ECS agent and has been registered into a cluster.
 - Cluster: A logical grouping of container instances on which you can place tasks.
 - Task Definition: A description of an application that contains one or more container definitions. For more information, see Amazon ECS Task Definitions.
 - Task: A single instantiation of a Task Definition.
 - Scheduler: The method used for placing tasks on container instances. For more information about the different scheduling options available in Amazon ECS, see Scheduling Amazon ECS Tasks.
 - Amazon ECS service: Allows you to run and maintain a specified number of instances of a task definition simultaneously. For more information, see Services.


The service scheduler ensures that the specified number of tasks are constantly running and reschedules tasks when a task fails (for example, if the underlying container instance fails for some reason). The service scheduler optionally ensures that tasks are registered against a load balancer. You can update your services that are maintained by the service scheduler, such as deploying a new task definition, or changing the running number of desired tasks.

```
 {
  "family": "myContainer",
  "containerDefinitions": [
    {
      "volumesFrom": [],
      "portMappings": [
        {
          "hostPort": 80,
          "containerPort": 80
        }
      ],
      "command": null,
      "environment": [],
      "essential": true,
      "entryPoint": null,
      "links": [],
      "mountPoints": [
        {
          "containerPath": "/usr/local/apache2/htdocs",
          "sourceVolume": "my-vol",
          "readOnly": null
        }
      ],
      "memory": 300,
      "name": "simple-app",
      "cpu": 10,
      "image": "httpd:2.4"
    },
    {
      "volumesFrom": [
        {
          "readOnly": null,
          "sourceContainer": "simple-app"
        }
      ],
      "portMappings": [],
      "command": [
        "/bin/sh -c \"while true; do echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p>' > top; /bin/date > date ; echo '</div></body></html>' > bottom; cat top date bottom > /usr/local/apache2/htdocs/index.html ; sleep 1; done\""
      ],
      "environment": [],
      "essential": false,
      "entryPoint": [
        "sh",
        "-c"
      ],
      "links": [],
      "mountPoints": [],
      "memory": 200,
      "name": "busybox",
      "cpu": 10,
      "image": "busybox"
    }
  ],
  "volumes": [
    {
      "host": {
        "sourcePath": null
      },
      "name": "my-vol"
    }
  ]
}
```

An Amazon ECS service allows you to run and maintain a specified number of instances of a task definition simultaneously.

Your Amazon ECS service can optionally be configured to use Elastic Load Balancing to manage traffic.

## Task 3: Deploy a New Application Version to the Service

If you update the Docker image of your application, you can create a new task definition with that image and deploy it to your service, one task at a time. The service scheduler creates a task with the new task definition (provided there is an available container instance to place it on). After it reaches the Running state, a task that is using the old task definition is drained and stopped. This process continues until all of the desired tasks in your service are using the new task definition.

