# Automated EC2 State Change Monitoring and Notification System using AWS EventBridge, Lambda, and SNS

This project involves setting up an AWS architecture to monitor changes in the state of EC2 instances and send real-time notifications. The solution leverages Amazon EventBridge to detect state change events for EC2 instances. When a state change is identified (e.g., from "running" to "stopped"), an AWS Lambda function is triggered. The Lambda function processes the event and publishes a notification to an Amazon SNS topic, which then delivers the message to subscribed endpoints, such as email or SMS.

This setup ensures efficient and automated monitoring of EC2 instance states, enabling prompt action through real-time notifications.
![Automate EC2 status change (4)](https://github.com/user-attachments/assets/61d57639-db65-49b3-8b10-cfd58abac3d4)
**Step-by-Step Guide:**

**Step 1: Create a Lambda Function (Target)**

This function will receive the event and log it.

1. Go to AWS Lambda in the AWS Console
2. Click Create function → Select Author from scratch.
3. Enter Function name: EC2StateChangeHandler
4. Choose Runtime: Python 3.9 (or another language).
5. Click Create function.
6. In the Code source section, replace the default code with: # with code from eventlog.py file in src folder
7. Click Deploy

**Step 2: Create an EventBridge Rule:**

Now, create a rule to capture EC2 instance state changes.

1. Go to Amazon EventBridge in the AWS Console.
2. Click Rules → Create rule.
3. Enter Rule name: EC2StateChangeRule
4. Choose Event bus: default
5. Under Event source, select AWS events.
6. Under Event pattern, choose Event Source → AWS services.
7. Select Service Name → EC2
8. Select Event Type → EC2 Instance State-change Notification
9. Click Next.

**Step 3: Set the Target (Lambda Function):**

1. Under Select targets, choose AWS Lambda function.
2. In the Function dropdown, select EC2StateChangeHandler.
3. Click Next, then Create rule.

**Step 4: Test the Setup:**
1. Start or stop an EC2 instance.
2. Go to CloudWatch Logs → Logs for Lambda function (EC2StateChangeHandler).
3. Check if the Lambda function logs the event.

**Step-by-Step Guide to Add SNS Notifications**
We will modify the existing EventBridge rule to trigger both SNS and Lambda.

**Step 5:** Create an SNS Topic
1. Go to Amazon SNS in the AWS Console.
2. Click Topics → Create topic.
3. Choose Type: Standard
4. Enter Topic name: EC2StateChangeTopic
5. Click Create topic.
6. Copy the Topic ARN (you’ll need it in the next step).

**Step 6:** Subscribe to the SNS Topic
1. Click on the newly created topic (EC2StateChangeTopic).
2. Click Create subscription.
3. Choose Protocol: Email (or SMS if you want a phone notification).
4. Enter your email address or phone number.
5. Click Create subscription.
6. Check your email inbox and confirm the subscription by clicking the confirmation link.

**Step 7:** Modify the EventBridge Rule to Add SNS as a Target
1. Go to Amazon EventBridge → Rules.
2. Click on EC2StateChangeRule (the rule you created earlier).
3. Click Edit → Go to the Targets section.
4. Click Add another target.
5. Select SNS topic from the dropdown.
6. Choose the SNS topic: EC2StateChangeTopic.
7. Click Update.

**Step 8:** Update the Lambda Function
Update the Lambda function with new code # with code from the sns_topic.py file in src folder


**Step 9:** Steps to Deploy the Updated Lambda Code:
1.  Go to AWS Lambda → Select EC2StateChangeHandler.
2. Click Deploy after replacing the code.
3. Make sure the Lambda function has SNS Publish permissions (Attach AmazonSNSFullAccess policy to its IAM role).

**Step 10:** Test the Setup
1. Start or stop an EC2 instance.
2. You should receive an email notification from SNS.
3. Check CloudWatch Logs for Lambda execution details.

**Summary of Enhancements**

✅ EventBridge listens for EC2 state changes (like "stopped", "terminated")

✅ Lambda function processes the event and logs it

✅ SNS sends notifications (email/SMS) when an instance state changes

✅ Useful for automation, such as sending alerts, triggering workflows, or auto-scaling.
