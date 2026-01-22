# Serverless Event Management System

## Project Description
This project is a serverless cloud-based application developed using AWS services to manage events.

## Technologies Used
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Python

## Features
- Create events using REST API
- Store event data in DynamoDB
- Fully serverless backend architecture

## Architecture
Client → API Gateway → AWS Lambda → DynamoDB

## API Endpoint
POST /create-event

### Sample Request
```json
{
  "event_name": "Cloud Internship Workshop"
}
