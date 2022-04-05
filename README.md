# ultraworking

The challenge was to deploy a simple endpoint that responds with the IP address of the requester.

Deliverable: Link us to your API endpoint AND a public Github Gist or repo with the source code.

It should provide a JSON response body:
{
  "ip": "11.11.11.11"
}
Includes a x-hello-world custom header with a value of your initials.
If a query string parameter of name is present, greeting key is addded to the response and use the name as part of the value.
