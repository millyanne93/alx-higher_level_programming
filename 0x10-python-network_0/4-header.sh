#!/bin/bash
# Send a GET request with a custom header to the URL and display the body of the response
curl "$1" -sX GET -H "X-School-User-Id: 98"

