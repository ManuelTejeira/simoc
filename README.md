# SIMOC
`SIMOC` - A Scalable, Interactive Model of an Off-world Community

## Getting Started

Depending on your use case, infrastructure and environment,
you can choose out of multiple deployment scenarios supported by `SIMOC`.

Please use the corresponding guide based on your set up:
- [Start SIMOC locally on Linux/macOS](https://github.com/kstaats/simoc/blob/master/local_instructions.md)
- [Deploy SIMOC via Docker on Linux/macOS](https://github.com/kstaats/simoc/blob/master/docker_instructions.md)
- [Deploy SIMOC to Google Kubernetes Engine](https://github.com/kstaats/simoc/blob/master/k8s_instructions.md)

## Jupyter Workflow

A Jupyter Notebook is included, `Custom_Agent_Template.ipynb`, which
demonstrates the command-line usage of the SIMOC Agent Model.

To setup the Jupyter environment:
```
pip install -r requirements-jupyter.txt
jupyter notebook
```
