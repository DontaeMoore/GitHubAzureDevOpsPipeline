# GitHub to Azure DevOps Pipeline Demo

This project demonstrates how to connect a GitHub repository to an Azure DevOps YAML pipeline and use that pipeline to run practical CI checks against a Python application.

The goal of this repository is to show hands-on experience with pipeline configuration, dependency management, automated validation, and security-focused checks in a source-controlled workflow.

## What This Project Demonstrates

- Connecting a GitHub repository to Azure DevOps using a YAML pipeline
- Triggering pipeline runs for all branches and pull requests
- Installing Python dependencies on a hosted build agent
- Running a lightweight application as part of CI validation
- Adding a dependency security scan as part of the pipeline
- Structuring a pipeline in a way that can be extended into CD later

## Pipeline Overview

The pipeline definition lives in [azure-pipelines.yml](azure-pipelines.yml) and currently includes:

1. `UsePythonVersion@0` to select the Python runtime on the hosted agent
2. A dependency installation step using [dependencies.txt](dependencies.txt)
3. A security scan step using `pip-audit`
4. A Bash task for basic agent and branch diagnostics
5. An application run step for [app.py](app.py)

Current triggers:

- CI triggers for all branches
- PR validation for all branches

## Local Run

Install dependencies:

```bash
py -3 -m pip install -r dependencies.txt
```

Run the application:

```bash
py -3 app.py
```

## Azure DevOps Setup

To connect this repository to Azure DevOps:

1. Create a new pipeline in Azure DevOps.
2. Choose GitHub as the source provider.
3. Select this repository.
4. Choose the existing YAML option.
5. Point the pipeline to [azure-pipelines.yml](azure-pipelines.yml).

Once connected, pushes and pull requests can automatically trigger validation runs based on the YAML configuration in the active branch.

## CI and CD Positioning

This repository currently demonstrates CI directly:

- source integration
- automated validation
- dependency installation
- security scanning
- branch and PR-based pipeline execution

It also provides a clean foundation for CD by making it straightforward to add later stages such as:

- packaging
- artifact publishing
- deployment to a target environment
- post-deployment validation

## Why This Matters

This project shows practical familiarity with the kind of workflow many teams use in production:

- GitHub for source control and pull requests
- Azure DevOps for pipeline orchestration
- YAML for versioned pipeline configuration
- automated checks that improve build reliability and visibility
