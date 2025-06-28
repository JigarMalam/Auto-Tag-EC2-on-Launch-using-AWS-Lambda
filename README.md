# Auto-Tag-EC2-on-Launch-using-AWS-Lambda
This project automatically tags newly launched EC2 instances with the **current date** and a **custom tag** using AWS Lambda and EventBridge.

##  Objective

Automatically add the following tags to every newly launched EC2 instance:

- `LaunchDate`: Current UTC date (e.g., 2025-06-25)
- `Project`: AutoTagged (custom tag example)

---

##  Setup Instructions

### 1. Prerequisites

- AWS account with permission to:
  - Launch EC2 instances
  - Create IAM roles
  - Deploy Lambda functions
  - Use EventBridge (CloudWatch Events)

---

### 2. Create IAM Role for Lambda

1. Go to **IAM > Roles > Create Role**
2. Select **Trusted Entity**: AWS Service > Lambda
3. Attach the policy: `AmazonEC2FullAccess`
4. Name the role: `LambdaEC2TaggingRole`

---

### 3. Create Lambda Function

1. Go to **AWS Lambda > Create Function**
2. Set:
   - Name: `AutoTagNewEC2`
   - Runtime: Python 3.13
   - Execution role: Use existing role `LambdaEC2TaggingRole`

3. Code:
   - Please refere the "lambda_function.py" file.

4. Create EventBridge Rule (EC2 Launch Trigger)
   - Go to Amazon EventBridge > Rules > Create Rule

      Enter:

          Name: EC2LaunchTriggerRule

          Event bus: default

          Rule type: Rule with an event pattern

     Set event pattern:

          Event source: AWS events

          Service Name: EC2
          
          Event Type: AWS API Call via CloudTrail
          
          Operation: RunInstances

     Add Target:

          Target type: AWS Service
          
          Service: Lambda
          
          Function: AutoTagNewEC2

     Click Create
   ---
## 📸 Screenshots

| Description                  | Screenshot |
|-----------------------------|------------|
| Amazon EventBridge Rules     | ![](Screenshots/Amazon%20EventBridge%20rules.png) |
| EC2 Tags                     | ![](Screenshots/EC2%20Tags.png)                   |
| IAM Role Permissions         | ![](Screenshots/IAM%20Role%20permissions.png)     |
| Lambda Code                  | ![](Screenshots/Lambda%20Code.png)               |
   ---
   

### 5. Testing
  Launch a new EC2 instance.
  After ~1 minute, check the Tags section of the instance.



