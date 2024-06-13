from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

questions = [

    {
        "question": "Under the shared responsibility model which of the following is the customer responsible for?",
        "options": [
            "A. Ensuring that disk drives are wiped after use.",
 	           "B. Ensuring that firmware is updated on hardware devices.",
            "C. Ensuring that data is encrypted at rest.",
            "D. Ensuring that network cables are category six or higher."        ],
        "answer": "C"
    },
    {
        "question": "Which allows companies to track and categorize spending on a detailed level?",
        "options": [
            "A. Cost allocation tags",
            "B. Consolidated billing",
            "C. AWS Budgets",
            "D. AWS Marketplace"
        ],
        "answer": "A"
    },
    {
        "question": "Which of the following are benefits of using AWS Trusted Advisor? (Choose two.)",
        "options": ["A. Providing high-performance container orchestration", "B. Creating and rotating encryption keys", "C. Detecting underutilized resources to save costs", "D. Improving security by proactively monitoring the AWS environment", "E. Implementing enforced tagging across AWS resources"],
        "answer": ["C", "D"]
    },
    {
        "question": "A developer has been hired by a large company and needs AWS credentials. Which are security best practices that should be followed? (Choose two.)",
        "options": ["A. Grant the developer access to only the AWS resources needed to perform the job.", "B. Share the AWS account root user credentials with the developer.", "C. Add the developer to the administrator's group in AWS IAM.", "D. Configure a password policy that ensures the developer's password cannot be changed.", "E. Ensure the account password policy requires a minimum length."],
        "answer": ["A", "E"]
    },
    {
        "question": "A user is planning to migrate an application workload to the AWS Cloud. Which control becomes the responsibility of AWS once the migration is complete?",
        "options": ["A. Patching the guest operating system", "B. Maintaining physical and environmental controls", "C. Protecting communications and maintaining zone security", "D. Patching specific applications"],
        "answer": "B"
    },
    {
        "question": "A company has multiple data sources across the organization and wants to consolidate data into one data warehouse. Which AWS service can be used to meet this requirement?",
        "options": ["A. Amazon DynamoDB", "B. Amazon Redshift", "C. Amazon Athena", "D. Amazon QuickSight"],
        "answer": "B"
    },
    {
        "question": "A user has underutilized on-premises resources. Which AWS Cloud concept can BEST address this issue?",
        "options": ["A. High availability", "B. Elasticity", "C. Security", "D. Loose coupling"],
        "answer": "B"
    },
    {
        "question": "A user has a stateful workload that will run on Amazon EC2 for the next 3 years. What is the MOST cost-effective pricing model for this workload?",
        "options": ["A. On-Demand Instances", "B. Reserved Instances", "C. Dedicated Instances", "D. Spot Instances"],
        "answer": "B"
    },
    {
        "question": "Which allows companies to track and categorize spending on a detailed level?",
        "options": ["A. Cost allocation tags", "B. Consolidated billing", "C. AWS Budgets", "D. AWS Marketplace"],
        "answer": "A"
    },
    {
        "question": "What AWS team assists customers with accelerating cloud adoption through paid engagements in any of several specialty practice areas?",
        "options": ["A. AWS Enterprise Support", "B. AWS Solutions Architects", "C. AWS Professional Services", "D. AWS Account Managers"],
        "answer": "C"
    },
    {
        "question": "A customer would like to design and build a new workload on AWS Cloud but does not have the AWS-related software technical expertise in-house. Which of the following AWS programs can a customer take advantage of to achieve that outcome?",
        "options": ["A. AWS Partner Network Technology Partners", "B. AWS Marketplace", "C. AWS Partner Network Consulting Partners", "D. AWS Service Catalogue"],
        "answer": "C"
    },
    {
        "question": "Which AWS services can host a Microsoft SQL Server database? (choose two)",
        "options": ["A. Amazon EC2", "B. Amazon Relational Database Service (Amazon RDS)", "C. Amazon Aurora", "D. Amazon Redshift", "E. Amazon S3"],
        "answer": ["A", "B"]
    },
    {   
    	"question": "When performing a cost analysis that supports physical isolation of acustomer workload, which compute hosting model should be accounted for in the Total Cost of Ownership (TCO)?",
    	"options": ["A. Dedicated Hosts", "B. Reserved Instances", "C. On-Demand Instances", "D. No Upfront Reserved Instances"],
    	"answer": ["A"]
    },
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    question_id = data['question_id']
    selected_option = data['selected_option']
    correct = questions[question_id]['answer'] == selected_option
    return jsonify({"correct": correct})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
        