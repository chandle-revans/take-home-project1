#!/bin/bash

echo $(curl --header "Content-Type: application/json" --request POST --data '{"host": "google.com", "days": 30}' https://y3q97ow5ii.execute-api.us-east-1.amazonaws.com/ssl-check)