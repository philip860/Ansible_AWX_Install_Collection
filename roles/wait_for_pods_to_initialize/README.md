# Waiting for Pods to come online

## Overview

This Ansible role watches the AWX-pods to make sure they are fully initialized. 

## Key Functions


- **Wait for pods to initialize**: Watches kubernetes AWX-Pods.


## Usage

This role should be executed as part of an AWX installation process where K3s is required as the Kubernetes environment and Nginx is used as the ingress controller.

## Documentation

For more details on AWX installation and Kubernetes configuration, refer to:
- [Kuberentes Documentation](https://kubernetes.io/docs/home/)


## License

This project is licensed under the MIT License.

## Author

This role was created and maintained by the Ansible community.

