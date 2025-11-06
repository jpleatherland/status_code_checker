from typing import Mapping, TypedDict

class CodeInfo(TypedDict):
    title: str
    description: str

status_codes: Mapping[int, CodeInfo] = {
  100: {
    "title": "Continue",
    "description": "The server has received the request headers, and the client should proceed to send the request body."
  },
  101: {
    "title": "Switching Protocols",
    "description": "The requester has asked the server to switch protocols."
  },
  200: {
    "title": "OK",
    "description": "The request was successful."
  },
  201: {
    "title": "Created",
    "description": "The request was successful and a resource was created."
  },
  202: {
    "title": "Accepted",
    "description": "The request has been accepted for processing, but the processing has not been completed."
  },
  204: {
    "title": "No Content",
    "description": "The server successfully processed the request, but is not returning any content."
  },
  301: {
    "title": "Moved Permanently",
    "description": "The requested resource has been assigned a new permanent URI."
  },
  302: {
    "title": "Found",
    "description": "The requested resource resides temporarily under a different URI."
  },
  304: {
    "title": "Not Modified",
    "description": "The resource has not been modified since the last request."
  },
  400: {
    "title": "Bad Request",
    "description": "The server could not understand the request due to invalid syntax."
  },
  401: {
    "title": "Unauthorized",
    "description": "The client must authenticate itself to get the requested response."
  },
  403: {
    "title": "Forbidden",
    "description": "The client does not have access rights to the content."
  },
  404: {
    "title": "Not Found",
    "description": "The server can not find the requested resource."
  },
  405: {
    "title": "Method Not Allowed",
    "description": "The request method is known by the server but is not supported by the target resource."
  },
  500: {
    "title": "Internal Server Error",
    "description": "The server has encountered a situation it doesn't know how to handle."
  },
  501: {
    "title": "Not Implemented",
    "description": "The request method is not supported by the server and cannot be handled."
  },
  502: {
    "title": "Bad Gateway",
    "description": "The server was acting as a gateway or proxy and received an invalid response from the upstream server."
  },
  503: {
    "title": "Service Unavailable",
    "description": "The server is not ready to handle the request."
  },
  504: {
    "title": "Gateway Timeout",
    "description": "The server is acting as a gateway and cannot get a response in time."
  }
}
