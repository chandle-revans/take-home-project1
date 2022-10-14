#!/bin/bash
set -eo pipefail

aws s3 rm s3://lambda-packages-2385729835723985723985732 --recursive
aws s3api delete-bucket --bucket lambda-packages-2385729835723985723985732

aws cloudformation delete-stack --stack-name dev-ssl-checker