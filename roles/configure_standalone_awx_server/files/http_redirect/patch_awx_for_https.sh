#!/bin/bash

#We will patch the AWX Instance To Force HTTP Redirection to HTTPS



/usr/local/bin/kubectl -n awx patch awx awx --type=merge -p '{"spec": {"ingress_annotations": "traefik.ingress.kubernetes.io/router.middlewares: default-redirect@kubernetescrd"}}'




