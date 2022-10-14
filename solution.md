# SSL Cert Checker

SSL Cert Checker is an AWS Lambda Function invoked by API Gateway used to check expiration of an SSL Certificate

## Installation

Clone the repository into your local filesystem

```bash
git clone https://github.com/chandle-revans/take-home-project1.git
```

## Deploy

Verify that you have your credentials assigned in your CLI

```bash
cd ./infra/scripts
bash deploy.sh
```

## Invoke

Execute the following bash script to invoke the ssl cert checker, you can update the POST body in the curl command to change the domain you wish to test

```bash
cd ./infra/scripts
bash invoke.sh
```

## Cleanup

```bash
cd ./infra/scripts
bash cleanup.sh
```

## Extra Considerations

Some things I would add if I had more time:
- Unit tests for python function
- Add some hardening to the API endpoint
    - Auth if needed
    - Put behind VPC so it's not public
- Hook up an automation platform to this where we can send requests for domains we control and then alert when they are expiring
- Implement CI/CD through github actions
