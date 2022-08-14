Lambda

{
  "dbUrl": "ec2-34-234-164-250.compute-1.amazonaws.com",
  "dbName": "mom_pop_db",
  "dbUser": "root",
  "dbPassword": "re:St@rt!9"
}

arn:aws:iam::888030915647:role/salesAnalysisReportRole

aws lambda create-function \
--function-name salesAnalysisReport \
--runtime python3.7 \
--zip-file fileb://salesAnalysisReport.zip \
--handler salesAnalysisReport.lambda_handler \
--region eu-west-2 \
--role arn:aws:iam::888030915647:role/salesAnalysisReportRole

