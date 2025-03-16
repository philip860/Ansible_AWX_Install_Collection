# AWX Standalone Server Installation

## Overview
This Ansible playbook automates the installation and configuration of an AWX standalone server. AWX is an open-source web-based automation platform that provides a user-friendly interface for Ansible.

## Prerequisites

- A Linux-based server (Ubuntu, CentOS, RHEL)
- Ansible installed on your local system
- SSH access to the target server
- Sufficient resources (minimum: 4 CPU cores, 8GB RAM, 20GB disk space)
- Internet access for package installations

## Playbook Details

### Playbook Name

**configure_awx_standalone.yml**

### Variables (Prompted or Predefined)

This playbook includes optional interactive prompts for user inputs. Uncomment the `vars_prompt` section in the playbook to enable them, or define the variables manually.

#### Required Variables:
- `awx_single_node`: Target server for AWX installation
- `awx_postgres_db_password`: Password for AWX PostgreSQL database
- `secret_key`: Secret key for encrypting PostgreSQL database
- `awx_admin_username`: AWX admin username
- `awx_admin_username_password`: AWX admin user password
- `awx_user_password_var`: Password for the local AWX user

### Roles Used in the Playbook

The playbook uses the following roles:

1. **install_required_packages** - Installs dependencies required for AWX.
2. **install_k3s** - Sets up a lightweight Kubernetes distribution (K3s) for AWX.
3. **generate_self_signed_tls_certs_for_awx_server** - Creates self-signed TLS certificates for secure communication.
4. **awx_operator_setup** - Deploys the AWX Operator to manage AWX in Kubernetes.
5. **configure_standalone_awx_server** - Configures and finalizes the standalone AWX server setup.

## Essential Software Components

The following software components are required for completing the AWX standalone server installation:

- **AWX Operator**: Automates the deployment and management of AWX in Kubernetes.
  - Version: `2.19.1`
- **K3s**: A lightweight Kubernetes distribution used to run AWX.
  - Version: `v1.24.0+k3s1`
- **Helm**: A package manager for Kubernetes, used to manage AWX deployment.
  - Version: `v3.10.3`
- **PostgreSQL**: The database backend for AWX.
  - Version: `15`

## Keynote: K3s and Ingress Configuration

By default, K3s installs the Traefik Ingress Controller, which uses strict DNS resolution. While this may be suitable for some environments, it can cause issues with AWX resolving to the backend correctly, unless you use the EXACT hostname use specified at the star of the install. To ensure broader compatibility and improved functionality across various use cases, we have removed the Traefik Ingress Controller and instead set up an NGINX proxy directly on the server. This provides greater flexibility in managing ingress traffic and enhances overall system performance.

## Installation Steps

### 1. Clone the Repository

```sh
git clone https://github.com/philip860/Ansible_AWX_Install_Collection
cd ansible-awx-install
```

### 2. Update Inventory and Variables

Modify the `inventory.yml` file to include your target server details.

Alternatively, you can define variables in `vars/main.yml` instead of using prompts.

### 3. Run the Playbook

Execute the playbook using:

```sh
ansible-playbook -i inventory.yml configure_awx_standalone.yml --ask-become-pass
```

If using prompts, remove `vars_prompt` comments before running.

### 4. Verify the Installation

Once the playbook completes, verify the AWX setup:

- Access AWX via the web UI: `https://<server-ip>:<port>`
- Log in with the admin credentials specified earlier.

## Troubleshooting

- Ensure the target server meets resource requirements.
- Check logs for errors:
  ```sh
  journalctl -u k3s -f
  kubectl logs -n awx awx-operator-xxxx
  ```
- Validate Kubernetes pods:
  ```sh
  kubectl get pods -n awx
  ```

## License
This project is licensed under the MIT License.

## Author
[Philip Duncan](https://github.com/philip860/)

