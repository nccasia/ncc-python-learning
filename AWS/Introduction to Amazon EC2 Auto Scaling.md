## Overview
Amazon EC2 Auto Scaling:
- Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle your application's workload. You create collections of EC2 instances, called Auto Scaling groups.
  - You can specify the minimum number of instances in each Auto Scaling group, and Auto Scaling ensures that your group never goes below this size.
  - You can specify the maximum number of instances in each Auto Scaling group, and Auto Scaling ensures that your group never goes above this size.
- If you specify a desired capacity, Auto Scaling ensures that your group always has a fixed number of instances.
- If you specify scaling policies, then Auto Scaling will launch new instances or terminate existing instances when the demand on your application increases or decreases.
### Auto Scaling only launches new instances or terminates existing instances. It does not Stop or Start instances.
## Conclusion
I know how to:
- Create a Launch Template
- Create an Auto Scaling group
- Test the Auto Scaling Infrastructure
- View the results of the Auto Scaling launch
