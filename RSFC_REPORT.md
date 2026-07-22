# Quality Assessment for RSFC 0.1.8

An automated assessment of the RSFC tool based on the EVERSE software quality indicators, run on 2026-07-22.

## General Information

- **Software:** RSFC
- **Repository:** ./
- **Assessment date:** 2026-07-22T11:42:09Z
- **Total checks:** 26

## Summary

- **Passed (`true`)**: 20
- **Failed (`false`)**: 6
- **Errors (`error`)**: 0

## Results Table

| TEST ID | Short Description | Output |
| --- | --- | --- |
| [RSFC-01-1](https://w3id.org/rsfc/test/RSFC-01-1) | There is an identifier and it resolves | true |
| [RSFC-01-2](https://w3id.org/rsfc/test/RSFC-01-2) | There is an identifier in the metadata files | true |
| [RSFC-01-3](https://w3id.org/rsfc/test/RSFC-01-3) | There is an identifier and it follows a common schema | true |
| [RSFC-03-6](https://w3id.org/rsfc/test/RSFC-03-6) | There is a version number stated in metadata files | true |
| [RSFC-04-2](https://w3id.org/rsfc/test/RSFC-04-2) | There is a README file | true |
| [RSFC-04-3](https://w3id.org/rsfc/test/RSFC-04-3) | Title and description are declared | true |
| [RSFC-04-4](https://w3id.org/rsfc/test/RSFC-04-4) | There is descriptive metadata | true |
| [RSFC-05-1](https://w3id.org/rsfc/test/RSFC-05-1) | There is a repostatus badge in the README file | true |
| [RSFC-05-2](https://w3id.org/rsfc/test/RSFC-05-2) | Contact and support metadata exists | true |
| [RSFC-05-3](https://w3id.org/rsfc/test/RSFC-05-3) | Software documentation exists | true |
| [RSFC-06-1](https://w3id.org/rsfc/test/RSFC-06-1) | Authors are declared | true |
| [RSFC-06-2](https://w3id.org/rsfc/test/RSFC-06-2) | Contributors are declared | false |
| [RSFC-06-3](https://w3id.org/rsfc/test/RSFC-06-3) | Authors have an ORCID assigned | false |
| [RSFC-07-1](https://w3id.org/rsfc/test/RSFC-07-1) | There is an identifier in README or CITATION | true |
| [RSFC-08-1](https://w3id.org/rsfc/test/RSFC-08-1) | Metadata record is found in SWHeritage or Zenodo | true |
| [RSFC-12-1](https://w3id.org/rsfc/test/RSFC-12-1) | There is an article citation or reference publication | false |
| [RSFC-13-1](https://w3id.org/rsfc/test/RSFC-13-1) | Dependencies are declared | true |
| [RSFC-13-2](https://w3id.org/rsfc/test/RSFC-13-2) | There are installation instructions | true |
| [RSFC-13-3](https://w3id.org/rsfc/test/RSFC-13-3) | Dependencies have version numbers | false |
| [RSFC-13-4](https://w3id.org/rsfc/test/RSFC-13-4) | Dependencies are in a machine-readable format | true |
| [RSFC-14-2](https://w3id.org/rsfc/test/RSFC-14-2) | There are actions to automate tests | false |
| [RSFC-15-1](https://w3id.org/rsfc/test/RSFC-15-1) | There is a license | true |
| [RSFC-15-2](https://w3id.org/rsfc/test/RSFC-15-2) | License is in SPDX format | true |
| [RSFC-19-1](https://w3id.org/rsfc/test/RSFC-19-1) | Repository has continuous integration workflows | true |
| [RSFC-21-1](https://w3id.org/rsfc/test/RSFC-21-1) | Repository has contribution guidelines | false |
| [RSFC-22-1](https://w3id.org/rsfc/test/RSFC-22-1) | Software offers a container file to run it | true |

## Detailed Results by Indicator

### archived_in_software_heritage

<a id="archived_in_software_heritage-https---w3id-org-rsfc-test-rsfc-08-1"></a>
#### Metadata record in Software Heritage or Zenodo

- **Test ID:** https://w3id.org/rsfc/test/RSFC-08-1
- **Result:** true
- **Process:** Searches for Zenodo and Software Heritage badges in the README file of the repository
- **Evidence:** A Zenodo DOI identifier was found in:
	- https://doi.org/10.5281/zenodo.1653148
	- https://doi.org/10.5281/zenodo.16531481
- **Suggestions:** N/A

### descriptive_metadata

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-03-6"></a>
#### Version number in metadata

- **Test ID:** https://w3id.org/rsfc/test/RSFC-03-6
- **Result:** true
- **Process:** Checks if a version number for the software is indicated in the CITATION.cff, codemeta.json or package files(i.e. pyproject.toml, pom.xml, etc.)
- **Evidence:** Found the software version in:
	- https://raw.githubusercontent.com////CITATION.cff
	- https://raw.githubusercontent.com////codemeta.json
	- https://raw.githubusercontent.com////pyproject.toml
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-04-3"></a>
#### There are title and description

- **Test ID:** https://w3id.org/rsfc/test/RSFC-04-3
- **Result:** true
- **Process:** Checks if there is a title and a description for the software in the metadata
- **Evidence:** A title was found in [https://raw.githubusercontent.com////README.md] and a description was found in [https://raw.githubusercontent.com////codemeta.json]
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-04-4"></a>
#### Software has descriptive metadata

- **Test ID:** https://w3id.org/rsfc/test/RSFC-04-4
- **Result:** true
- **Process:** Searches for description, programming languages, date of creation and keywords in the repository
- **Evidence:** Descriptive metadata found in: Description [https://raw.githubusercontent.com////codemeta.json, https://raw.githubusercontent.com////pyproject.toml], Languages [https://raw.githubusercontent.com////codemeta.json], Date Created [https://raw.githubusercontent.com////codemeta.json], Keywords [https://raw.githubusercontent.com////codemeta.json]
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-06-1"></a>
#### Authors are declared

- **Test ID:** https://w3id.org/rsfc/test/RSFC-06-1
- **Result:** true
- **Process:** Searches for authors in various files of the repository (i.e. CITATION.cff, AUTHORS.md, codemeta.json)
- **Evidence:** Authors were found in:
	- https://raw.githubusercontent.com////CITATION.cff
	- https://raw.githubusercontent.com////codemeta.json
	- https://raw.githubusercontent.com////pyproject.toml
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-06-2"></a>
#### Contributors are declared

- **Test ID:** https://w3id.org/rsfc/test/RSFC-06-2
- **Result:** false
- **Process:** Searches for contributors in various files of the repository (i.e. codemeta.json, pyproject.toml, pom.xml)'
- **Evidence:** Could not find any contributors in the repository
- **Suggestions:** Your software should also document its contributors if there are any. More information at https://everse.software/RSQKit/documenting_software_project

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-06-3"></a>
#### Authors have an ORCID

- **Test ID:** https://w3id.org/rsfc/test/RSFC-06-3
- **Result:** false
- **Process:** Checks if all authors stated in the CITATION.cff file have an ORCID assigned
- **Evidence:** Authors that do not have an orcid were found in:
	- https://raw.githubusercontent.com////CITATION.cff
	- https://raw.githubusercontent.com////codemeta.json
- **Suggestions:** When documenting your software's authors, you should include their ORCIDs if possible.

### has_contribution_guidelines

<a id="has_contribution_guidelines-https---w3id-org-rsfc-test-rsfc-21-1"></a>
#### Repository has contribution guidelines

- **Test ID:** https://w3id.org/rsfc/test/RSFC-21-1
- **Result:** false
- **Process:** Checks if there are contribution guidelines either in the README file or if there is a CONTRIBUTING.md file
- **Evidence:** Could not find contribution guidelines in the repository
- **Suggestions:** If you want to properly keep track of the colaborations your project receives to ensure its quality and fiability, you should add some contribution guidelines so the colaborators know how you want contributions to be made

### persistent_and_unique_identifier

<a id="persistent_and_unique_identifier-https---w3id-org-rsfc-test-rsfc-01-1"></a>
#### There is an identifier and resolves

- **Test ID:** https://w3id.org/rsfc/test/RSFC-01-1
- **Result:** true
- **Process:** Searches for an identifier (i.e. DOI or SWHID) in the README file of the repository
- **Evidence:** Found the identifier https://doi.org/10.5281/zenodo.16531481 in the README and it resolves
- **Suggestions:** N/A

<a id="persistent_and_unique_identifier-https---w3id-org-rsfc-test-rsfc-01-2"></a>
#### There is an identifier associated with the software

- **Test ID:** https://w3id.org/rsfc/test/RSFC-01-2
- **Result:** true
- **Process:** Searches for an identifier in the CITATION.cff, codemeta.json and README files
- **Evidence:** An identifier was found in CITATION.cff, README.md, codemeta.json.
- **Suggestions:** N/A

<a id="persistent_and_unique_identifier-https---w3id-org-rsfc-test-rsfc-01-3"></a>
#### Software identifier follows a proper schema

- **Test ID:** https://w3id.org/rsfc/test/RSFC-01-3
- **Result:** true
- **Process:** Checks if the identifiers associated with the software follow any of these schemas: DOI, URN, GITHUB and SWHID
- **Evidence:** All of the identifiers detected follow a common schema
- **Suggestions:** N/A

<a id="persistent_and_unique_identifier-https---w3id-org-rsfc-test-rsfc-07-1"></a>
#### There is an identifier in README or CITATION.cff

- **Test ID:** https://w3id.org/rsfc/test/RSFC-07-1
- **Result:** true
- **Process:** Searches for an identifier in the README or CITATION.cff files of the repository
- **Evidence:** An identifier was found in both the README and CITATION.cff files of the repository
	- https://doi.org/10.5281/zenodo.16531481
	- 10.5281/zenodo.16531481
- **Suggestions:** N/A

### repository_workflows

<a id="repository_workflows-https---w3id-org-rsfc-test-rsfc-14-2"></a>
#### There are actions to automate tests

- **Test ID:** https://w3id.org/rsfc/test/RSFC-14-2
- **Result:** false
- **Process:** Searches for workflows that contain test or tests in their names
- **Evidence:** Could not find any workflows or actions that mention test in their names
- **Suggestions:** You should include github actions that run tests to ensure quality. More information at https://everse.software/RSQKit/task_automation_github_actions

<a id="repository_workflows-https---w3id-org-rsfc-test-rsfc-19-1"></a>
#### Repository has workflows

- **Test ID:** https://w3id.org/rsfc/test/RSFC-19-1
- **Result:** true
- **Process:** Searches for workflows in the repository
- **Evidence:** Workflows were found in:
	- https://raw.githubusercontent.com////.github/workflows/pypi-publish.yml
	- https://raw.githubusercontent.com////.github/workflows/run-rsfc.yml
	- https://raw.githubusercontent.com////.github/workflows/use-rsfc.yml
- **Suggestions:** N/A

### requirements_specified

<a id="requirements_specified-https---w3id-org-rsfc-test-rsfc-13-1"></a>
#### Dependencies are declared

- **Test ID:** https://w3id.org/rsfc/test/RSFC-13-1
- **Result:** true
- **Process:** Searches for dependencies in project configuration files, README and dependencies files such as requirements.txt
- **Evidence:** Requirements were found in:
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////requirements.txt, https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////README.md
- **Suggestions:** N/A

<a id="requirements_specified-https---w3id-org-rsfc-test-rsfc-13-3"></a>
#### Dependencies have version numbers

- **Test ID:** https://w3id.org/rsfc/test/RSFC-13-3
- **Result:** false
- **Process:** Checks if all of the dependencies stated in the machine-readable file (e.g. requirements.txt, pyproject.toml, etc.) of the repository have a version indicated
- **Evidence:** The following dependencies do not have a version stated:
	- poetry-core
- **Suggestions:** All of your dependencies should have their versions stated to ensure its reproducibility. More information at https://everse.software/RSQKit/reproducible_software_environments

<a id="requirements_specified-https---w3id-org-rsfc-test-rsfc-13-4"></a>
#### There is a dependencies machine-readable file

- **Test ID:** https://w3id.org/rsfc/test/RSFC-13-4
- **Result:** true
- **Process:** Checks if dependencies are indicated in a machine-readable file
- **Evidence:** There is a machine-readable file for dependencies at:
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
	- https://raw.githubusercontent.com////requirements.txt
- **Suggestions:** N/A

### software_has_citation

<a id="software_has_citation-https---w3id-org-rsfc-test-rsfc-12-1"></a>
#### There is an article citation or reference publication

- **Test ID:** https://w3id.org/rsfc/test/RSFC-12-1
- **Result:** false
- **Process:** Searches for an article citation or a reference publication in the codemeta and citation files
- **Evidence:** Could not find neither a reference publication or citation to an article in the repository
- **Suggestions:** You should include other forms of citation like article citations and reference publications in your software's metadata. More information at https://everse.software/RSQKit/creating_good_readme

### software_has_documentation

<a id="software_has_documentation-https---w3id-org-rsfc-test-rsfc-04-2"></a>
#### There is a README

- **Test ID:** https://w3id.org/rsfc/test/RSFC-04-2
- **Result:** true
- **Process:** Searches for a README file in the repository
- **Evidence:** There is a README file in the repository
- **Suggestions:** N/A

<a id="software_has_documentation-https---w3id-org-rsfc-test-rsfc-05-2"></a>
#### There is contact and/or support metadata

- **Test ID:** https://w3id.org/rsfc/test/RSFC-05-2
- **Result:** true
- **Process:** Searches for contact and support information in the repository
- **Evidence:** Contact and support information was found in:
	- https://raw.githubusercontent.com////README.md
- **Suggestions:** N/A

<a id="software_has_documentation-https---w3id-org-rsfc-test-rsfc-05-3"></a>
#### Software documentation

- **Test ID:** https://w3id.org/rsfc/test/RSFC-05-3
- **Result:** true
- **Process:** Searches for a README file in the root repository and other forms of documentation such as a Read The Docs badge or url
- **Evidence:** Documentation was found in:
	- https://raw.githubusercontent.com////README.md
- **Suggestions:** N/A

<a id="software_has_documentation-https---w3id-org-rsfc-test-rsfc-13-2"></a>
#### There are installation instructions

- **Test ID:** https://w3id.org/rsfc/test/RSFC-13-2
- **Result:** true
- **Process:** Searches for installation instructions in the README file of the repository
- **Evidence:** Installation instructions were found in:
	- https://raw.githubusercontent.com////README.md
- **Suggestions:** N/A

### software_has_license

<a id="software_has_license-https---w3id-org-rsfc-test-rsfc-15-1"></a>
#### Software has license

- **Test ID:** https://w3id.org/rsfc/test/RSFC-15-1
- **Result:** true
- **Process:** Searches for a file named 'LICENSE' or 'LICENSE.md' in the root of the repository.
- **Evidence:** A license was found in:
	- https://raw.githubusercontent.com////CITATION.cff
	- https://raw.githubusercontent.com////pyproject.toml
	- https://raw.githubusercontent.com////LICENSE
	- https://raw.githubusercontent.com////codemeta.json
- **Suggestions:** N/A

<a id="software_has_license-https---w3id-org-rsfc-test-rsfc-15-2"></a>
#### License is SPDX compliant

- **Test ID:** https://w3id.org/rsfc/test/RSFC-15-2
- **Result:** true
- **Process:** Checks if the licenses detected are SPDX compliant
- **Evidence:** All licenses are SPDX compliant
- **Suggestions:** N/A

### software_is_containerized

<a id="software_is_containerized-https---w3id-org-rsfc-test-rsfc-22-1"></a>
#### Software is containerized

- **Test ID:** https://w3id.org/rsfc/test/RSFC-22-1
- **Result:** true
- **Process:** Searches in the root of the repository for container files such as dockerfile, apptainer, podman, etc.
- **Evidence:** Found container files at:
	- https://raw.githubusercontent.com////Dockerfile
- **Suggestions:** N/A

### version_control_use

<a id="version_control_use-https---w3id-org-rsfc-test-rsfc-05-1"></a>
#### There is a repostatus badge

- **Test ID:** https://w3id.org/rsfc/test/RSFC-05-1
- **Result:** true
- **Process:** Searches for a repo status badge in the README file of the repository
- **Evidence:** A repo status badge was found in:
	- https://raw.githubusercontent.com////README.md
- **Suggestions:** N/A
