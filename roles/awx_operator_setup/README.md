# AWX Operator

## Overview

The AWX Operator is an Ansible-based Kubernetes Operator designed to manage the lifecycle of [AWX](https://github.com/ansible/awx) instances within a Kubernetes cluster. Built with the Operator SDK and Ansible, it streamlines the deployment, management, and maintenance of AWX, providing a consistent and automated approach to handling AWX installations.

## Prerequisites

Before deploying the AWX Operator, ensure you have the following:

- **Kubernetes Cluster**: A functioning Kubernetes cluster (e.g., OpenShift, Kubernetes, Minikube).
- **kubectl**: The Kubernetes command-line tool should be installed and configured to interact with your cluster.
- **Helm (optional)**: Used for managing Kubernetes applications.
- **Ansible**: Required for contributing to the AWX Operator.

## Installation

### 1. Clone the AWX Operator Repository

Begin by cloning the AWX Operator repository:

```bash
git clone https://github.com/ansible/awx-operator.git
cd awx-operator
```

### 2. Checkout the Desired Release

List available tags and checkout the desired version:

```bash
git tag
git checkout tags/<tag>
```

Replace `<tag>` with the specific version you intend to deploy, such as `2.19.1`.

### 3. Deploy the Operator Using Kustomize

With a running Kubernetes cluster, deploy the AWX Operator using Kustomize:

```bash
kubectl apply -k .
```

This command applies the necessary manifests to your cluster.

### 4. Verify Operator Deployment

Confirm that the AWX Operator is running:

```bash
kubectl get pods -n awx
```

You should see the `awx-operator-controller-manager` pod in a running state.

## Deploying an AWX Instance

### 1. Create an AWX Custom Resource

Define the AWX instance by creating a YAML file, such as `awx-demo.yml`, with the following content:

```yaml
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-demo
spec:
  service_type: nodeport
```

### 2. Apply the Custom Resource

Apply the AWX custom resource to deploy the instance:

```bash
kubectl apply -f awx-demo.yml
```

Monitor the deployment:

```bash
kubectl get pods -l "app.kubernetes.io/managed-by=awx-operator"
```

Once the pods are running, your AWX instance is ready.

## Configuration Options

The AWX Operator offers various customization options:

- **Admin User Configuration**: Set the admin username, email, and password via Kubernetes secrets.
- **Database Configuration**: Configure external PostgreSQL databases or allow the operator to manage an internal PostgreSQL service.
- **Extra Settings**: Pass additional settings to AWX using the `extra_settings` parameter.

## Documentation

Comprehensive documentation for the AWX Operator is available at [AWX Operator Documentation](https://ansible.readthedocs.io/projects/awx-operator/).

## Contributing

Contributions are welcome. Please refer to the [contributing guidelines](https://github.com/ansible/awx-operator/blob/devel/CONTRIBUTING.md) for more information.

## License

This project is licensed under the Apache-2.0 License.

## Author

The AWX Operator was originally built by the Ansible Team. For real-time interactions, join the community on Matrix:

- **AWX Discussions**: [#awx:ansible.com](https://matrix.to/#/#awx:ansible.com)

For more communication channels, visit the [Ansible communication guide](https://docs.ansible.com/ansible/latest/community/communication.html).

