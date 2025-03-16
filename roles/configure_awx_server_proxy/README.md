# Nginx Configuration Role

## Overview

This Ansible role automates the setup and configuration of Nginx, to support AWX deployment within a Kubernetes environment. It ensures that K3s is installed, properly configured, and that Nginx is set up with the necessary SSL certificates and routing configurations.

## Key Functions

- **Install and Re-Configure K3s**: Ensures that K3s is installed and properly configured, including permission adjustments and service restarts.
- **Manage Required Directories**: Creates essential directories for Helm, SSL certificates, and Nginx configuration.
- **Install Necessary Packages**: Installs system dependencies such as Nginx, wget, tar, and jq.
- **Deploy Helm for Kubernetes Management**: Downloads and installs Helm to assist with managing Kubernetes resources.
- **Remove Traefik and Apply Custom Routing**: Uninstalls the default Traefik ingress controller from K3s and replaces it with a custom Nginx-based setup.
- **Configure SSL Certificates**: Copies self-generated SSL certificates to the appropriate Nginx directories to enable secure HTTPS communication.
- **Retrieve AWX Service Port**: Extracts the NodePort assigned to the AWX service to enable external access.
- **Apply Custom Nginx Configurations**: Copies predefined Nginx configuration files to enforce security and routing policies.
- **Set SELinux Rules**: Adjusts security policies to allow Nginx to make network connections.
- **Restart Services**: Ensures that K3s and Nginx services are restarted to apply new configurations.

## Usage

This role should be executed as part of an AWX installation process where K3s is required as the Kubernetes environment and Nginx is used as the ingress controller.

## Documentation

For more details on AWX installation and Kubernetes configuration, refer to:
- [AWX Documentation](https://ansible.readthedocs.io/projects/awx/)
- [K3s Documentation](https://rancher.com/docs/k3s/latest/en/)
- [Helm Documentation](https://helm.sh/docs/)

## License

This project is licensed under the MIT License.

## Author

This role was created and maintained by the Ansible community.

