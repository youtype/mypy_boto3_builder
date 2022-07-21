1.22.5
======

* api-change:``autoscaling``: This release adds support for attribute-based instance type selection, a new EC2 Auto Scaling feature that lets customers express their instance requirements as a set of attributes, such as vCPU, memory, and storage.
* api-change:``ec2``: This release adds: attribute-based instance type selection for EC2 Fleet, Spot Fleet, a feature that lets customers express instance requirements as attributes like vCPU, memory, and storage; and Spot placement score, a feature that helps customers identify an optimal location to run Spot workloads.
* api-change:``eks``: EKS managed node groups now support BOTTLEROCKET_x86_64 and BOTTLEROCKET_ARM_64 AMI types.
* api-change:``sagemaker``: This release allows customers to describe one or more versioned model packages through BatchDescribeModelPackage, update project via UpdateProject, modify and read customer metadata properties using Create, Update and Describe ModelPackage and enables cross account registration of model packages.
* enhancement:Session: Added `get_partition_for_region` allowing partition lookup by region name.
* api-change:``textract``: This release adds support for asynchronously analyzing invoice and receipt documents through two new APIs: StartExpenseAnalysis and GetExpenseAnalysis


1.22.4
======

* api-change:``emr-containers``: This feature enables auto-generation of certificate  to secure the managed-endpoint and removes the need for customer provided certificate-arn during managed-endpoint setup.
* api-change:``chime-sdk-messaging``: The Amazon Chime SDK now supports push notifications through Amazon Pinpoint
* api-change:``chime-sdk-identity``: The Amazon Chime SDK now supports push notifications through Amazon Pinpoint
