# AWX Standalone Server Installation

## Overview
This Ansible playbook automates the installation and configuration of an AWX standalone server. AWX is an open-source web-based automation platform that provides a user-friendly interface for Ansible.

This is not a development AWX-server but a fully functionality install of a Ansible AWX Server.

## Prerequisites

- A Linux-based server (Ubuntu, CentOS, RHEL)
- Ansible installed on your local system
- SSH access to the target server
- Sufficient resources (minimum: 4 CPU cores, 8GB RAM, 80GB disk space - please make sure to have sufficent storage, or install may fail)
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

## Operating Systems Install Tested On

The following operating systems were tested with this AWX standalone server installation:

Alternatively,
  - Version: `8/9`

- **Centos**: Community ENTerprise Operating System.
  - Version: `8/9`

- **Ubuntu**: Canonical Ubuntu.
  - Version: `22.04.5 LTS`



## Essential Software Components

The following software components are used to complete the AWX standalone server installation:

- **AWX Operator**: Automates the deployment and management of AWX in Kubernetes.
  - Version: `2.19.1`
- **K3s**: A lightweight Kubernetes distribution used to run AWX.
  - Version: `v1.31.6+k3s1`
- **Helm**: A package manager for Kubernetes, used to manage AWX deployment.
  - Version: `v3.15.3`
- **PostgreSQL**: The database backend for AWX.
  - Version: `15`

## Keynote: K3s and Ingress Configuration

By default, K3s installs the Traefik Ingress Controller, which uses strict DNS resolution. While this may be suitable for some environments, it can cause issues with AWX resolving to the backend correctly, unless you use the EXACT hostname use specified at the star of the install. To ensure broader compatibility and improved functionality across various use cases, we have removed the Traefik Ingress Controller and instead set up an NGINX proxy directly on the server. This provides greater flexibility in managing ingress traffic and enhances overall system performance.

## Installation Steps

### 1. Clone the Repository (Option 1)

```sh
git clone https://github.com/philip860/Ansible_AWX_Install_Collection
cd ansible-awx-install
```

### 1. Install via Ansible Galaxy (Option 2)

Alternatively, you can install the collection from Ansible Galaxy:

```sh
ansible-galaxy collection install philip860.awx_install
```

### 2. Update Inventory and Variables

Modify the `inventory.yml` file to include your target server details.

Alternatively, you can define variables in `vars/main.yml` instead of using prompts.

### 4. Generate a Secure Password

When the playbook runs you will be prompted to specify passwords for the following:

- `awx_postgres_db_password`: Password for AWX PostgreSQL database
- `secret_key`: Secret key for encrypting PostgreSQL database
- `awx_admin_username_password`: AWX admin user password
- `awx_user_password_var`: Password for the local AWX user

You can generate random passwords using this command below:

```sh
date +%s | sha256sum | base64 | head -c 32 ; echo
```

### 5. Run the Playbook

For repository installation, execute the playbook using:

```sh
ansible-playbook configure_awx_standalone.yml -vvv
```

If using the Ansible Galaxy collection, execute the playbook using:

```sh
ansible-playbook "$HOME/.ansible/collections/ansible_collections/philip860/awx_install/Configure_AWX_Standalone_Server.yml" -vvv
```

If using prompts, remove `vars_prompt` comments before running.

### 6. Verify the Installation

Once the playbook completes, verify the AWX setup:

- Access AWX via the web UI: `https://<server-ip>`
- Log in with the admin credentials specified earlier. (Ansible playbook will show users the admin password at the end.)

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



## SSL Cert Update

- A default SSL cert (tls.crt) & key (tls.key), is created to enable HTTPS for the AWX server.
- The default cert is located here:
```sh
  ls /admin_tools/awx-operator/awx-deploy/
```
- To add your own custom SSL certs you will need to replace the default (tls.crt) & key (tls.key)
```sh
  cd /admin_tools/awx-operator/awx-deploy/
  mv tls.crt tls-old.crt
  mv tls.key tls-old.key 
  cp -r /full_path/server.crt tls.crt
  cp -r /full_path/server.key tls.key
  kubectl apply -k awx-deploy
  kubectl create secret tls awx-secret-tls -n awx  --cert=/admin_tools/awx-operator/awx-deploy/tls.crt --key=/admin_tools/awx-operator/awx-deploy/tls.key  --dry-run=client -o yaml | kubectl apply -f - 
  kubectl rollout restart deployment -n awx
  cp -r /admin_tools/awx-operator/awx-deploy/tls.crt /etc/nginx/certs/server.crt
  cp -r /admin_tools/awx-operator/awx-deploy/tls.key /etc/nginx/certs/server.key
  systemctl restart nginx
```


## Installation Workflow

### 1. Start of Installation and Variable Prompts
![Initial variable prompts](https://raw.githubusercontent.com/philip860/Ansible_AWX_Install_Collection/main/screenshots/AWX-Server-Install.png)

Image shows: user prompts for the required information needed at the beginning of the installation process.

### 2. Pods Starting to Initialize
![Pods starting to initialize](https://raw.githubusercontent.com/philip860/Ansible_AWX_Install_Collection/main/screenshots/AWX-Server-Migration-Pod.png)

Image shows: what a user might see if they ran a 'kubectl get pods -n awx' while the ansible-playbook is running the installation.

### 3. AWX Web Browser Show Migration In Progress
![Web browser waiting for pods to initialize](https://raw.githubusercontent.com/philip860/Ansible_AWX_Install_Collection/main/screenshots/AWX-Server-Upgrade-Message.png)

Image shows: what a user will see if they tried to access AWX-Server with a web browser before the pods finished initializing.


### 4. Pods Finshed Initializing - Login Ready!
![Default login screen](https://raw.githubusercontent.com/philip860/Ansible_AWX_Install_Collection/main/screenshots/Default-Login-Screen.png)

Image shows: Default AWX login screen accessible after the pods finised initializing.

### 5. Successfully logged in - AWX GUI
![AWX GUI](https://raw.githubusercontent.com/philip860/Ansible_AWX_Install_Collection/main/screenshots/AWX-GUI.png)

Image shows: User logged into AWX server, via the admin user.


## Final Notes
Depending on your system's resources this installation can take anywhere from about 25mins to 45min to fully complete.

If any issues occur during the build, first check to make sure your system has enough free storage available.

The following commands can help to shed some light on possible installation issues with AWX & Kubernetes Use the command "kubectl get pods -n awx" to get the full names of the pods because they are subject to change.

- Show all awx related pods running for kubernetes:
```sh
  kubectl get pods -n awx
```
- Show all related events for awx deployment in kubernetes:

```sh
  kubectl get events -n awx
```

- Show all related information for the awx-operator-controller-manager pod:

```sh
  kubectl logs awx-operator-controller-manager-subject_to_change -f -n awx
```

## License
This project is licensed under the MIT License.

## Addional questions/inquiries
Email: philipduncan860@gmail.com

## Author
[Philip Duncan](https://github.com/philip860/)

