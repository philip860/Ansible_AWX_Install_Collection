# Configuration AWX Server Role

## Overview

This Ansible role automates the setup and configuration of the AWX server. It ensures that the awx-operator is deployed properly configured, and that all the necessary kubernetes configuration have been made.

## Key Functions

- **Install awx-operator**: Ensures that the awx is deployed using the awx-operator.
- **Manage Required Directories**: Creates essential directories for Helm, SSL certificates, and Nginx configuration.
- **Restart Services**: Ensures that K3s and Nginx services are restarted to apply new configurations.

## Usage

This role should be executed as part of an AWX installation process where K3s is required as the Kubernetes environment and Nginx is used as the ingress controller.

## Documentation

For more details on AWX installation and Kubernetes configuration, refer to:
- [AWX Documentation](https://ansible.readthedocs.io/projects/awx/)

## License

This project is licensed under the MIT License.

## Author

This role was created and maintained by the Ansible community.

