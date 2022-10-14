#!/bin/bash
set -eo pipefail

S3_BUCKET=lambda-packages-2385729835723985723985732

# create the bucket if we haven't already
if aws s3api head-bucket --bucket "$S3_BUCKET" 2>/dev/null; 
then
    echo "S3 Bucket: $S3_BUCKET exists" 
else
    aws s3 mb s3://$S3_BUCKET
fi

# package & deploy
aws cloudformation package --template-file ../cloudformation/main.yml --s3-bucket $S3_BUCKET --output-template-file ../cloudformation/package.yml
aws cloudformation deploy --template-file ../cloudformation/package.yml --stack-name dev-ssl-checker --capabilities CAPABILITY_NAMED_IAM