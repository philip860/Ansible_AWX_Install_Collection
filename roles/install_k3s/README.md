# Install K3s Configuration Role

## Overview

This Ansible role automates the setup and configuration of k3s, and associated services to support AWX deployment within a Kubernetes environment. 

## Key Functions


- **Configure k3s**: Installs k3s software in order to provide a light-weight kubernetes env.


## Usage

This role should be executed as part of an AWX installation process where K3s is required as the Kubernetes environment and Nginx is used as the ingress controller.

## Documentation

For more details on AWX installation and Kubernetes configuration, refer to:
- [AWX Documentation](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster)


## License

This project is licensed under the MIT License.

## Author

This role was created and maintained by the Ansible community.

