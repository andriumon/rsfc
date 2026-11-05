# Quality Assessment for somef 0.11.5

An automated assessment of the somef tool based on the EVERSE software quality indicators, run on 2026-11-05.

## General Information

- **Software:** somef
- **Repository:** https://github.com/KnowledgeCaptureAndDiscovery/somef
- **Assessment date:** 2026-11-05T08:45:39Z
- **Total checks:** 43

## Summary

- **Passed (`true`)**: 39
- **Failed (`false`)**: 4
- **Errors (`error`)**: 0

## Results Table

| TEST ID | Short Description | Output |
| --- | --- | --- |
| [RSFC-01-1](https://w3id.org/rsfc/test/RSFC-01-1) | There is an identifier and it resolves | true |
| [RSFC-01-2](https://w3id.org/rsfc/test/RSFC-01-2) | There is an identifier in the metadata files | true |
| [RSFC-01-3](https://w3id.org/rsfc/test/RSFC-01-3) | There is an identifier and it follows a common schema | true |
| [RSFC-03-1](https://w3id.org/rsfc/test/RSFC-03-1) | The software has releases | true |
| [RSFC-03-2](https://w3id.org/rsfc/test/RSFC-03-2) | Releases have version and identifier | true |
| [RSFC-03-3](https://w3id.org/rsfc/test/RSFC-03-3) | Release versions follow SemVer or CalVer | true |
| [RSFC-03-4](https://w3id.org/rsfc/test/RSFC-03-4) | Release identifiers follow the same scheme | true |
| [RSFC-03-5](https://w3id.org/rsfc/test/RSFC-03-5) | Last release version corresponds to version in package file | true |
| [RSFC-03-6](https://w3id.org/rsfc/test/RSFC-03-6) | There is a version number stated in metadata files | true |
| [RSFC-04-1](https://w3id.org/rsfc/test/RSFC-04-1) | Metadata files exist | true |
| [RSFC-04-2](https://w3id.org/rsfc/test/RSFC-04-2) | There is a README file | true |
| [RSFC-04-3](https://w3id.org/rsfc/test/RSFC-04-3) | Title and description are declared | true |
| [RSFC-04-4](https://w3id.org/rsfc/test/RSFC-04-4) | There is descriptive metadata | true |
| [RSFC-04-5](https://w3id.org/rsfc/test/RSFC-04-5) | There is a codemeta file | true |
| [RSFC-05-1](https://w3id.org/rsfc/test/RSFC-05-1) | There is a repostatus badge in the README file | true |
| [RSFC-05-2](https://w3id.org/rsfc/test/RSFC-05-2) | Contact and support metadata exists | true |
| [RSFC-05-3](https://w3id.org/rsfc/test/RSFC-05-3) | Software documentation exists | true |
| [RSFC-05-4](https://w3id.org/rsfc/test/RSFC-05-4) | Software has active communication channels | false |
| [RSFC-06-1](https://w3id.org/rsfc/test/RSFC-06-1) | Authors are declared | true |
| [RSFC-06-2](https://w3id.org/rsfc/test/RSFC-06-2) | Contributors are declared | true |
| [RSFC-06-3](https://w3id.org/rsfc/test/RSFC-06-3) | Authors have an ORCID assigned | false |
| [RSFC-07-1](https://w3id.org/rsfc/test/RSFC-07-1) | There is an identifier in README or CITATION | true |
| [RSFC-07-2](https://w3id.org/rsfc/test/RSFC-07-2) | Software identifier resolves and links back to software | false |
| [RSFC-08-1](https://w3id.org/rsfc/test/RSFC-08-1) | Metadata record is found in SWHeritage | true |
| [RSFC-08-2](https://w3id.org/rsfc/test/RSFC-08-2) | Metadata record is found in Zenodo | true |
| [RSFC-09-1](https://w3id.org/rsfc/test/RSFC-09-1) | Repository is from Github or Gitlab | true |
| [RSFC-12-1](https://w3id.org/rsfc/test/RSFC-12-1) | There is an article citation or reference publication | true |
| [RSFC-13-1](https://w3id.org/rsfc/test/RSFC-13-1) | Dependencies are declared | true |
| [RSFC-13-2](https://w3id.org/rsfc/test/RSFC-13-2) | There are installation instructions | true |
| [RSFC-13-3](https://w3id.org/rsfc/test/RSFC-13-3) | Dependencies have version numbers | false |
| [RSFC-13-4](https://w3id.org/rsfc/test/RSFC-13-4) | Dependencies are in a machine-readable format | true |
| [RSFC-14-1](https://w3id.org/rsfc/test/RSFC-14-1) | Tests are provided | true |
| [RSFC-14-2](https://w3id.org/rsfc/test/RSFC-14-2) | There are actions to automate tests | true |
| [RSFC-15-1](https://w3id.org/rsfc/test/RSFC-15-1) | There is a license | true |
| [RSFC-15-2](https://w3id.org/rsfc/test/RSFC-15-2) | License is in SPDX format | true |
| [RSFC-16-1](https://w3id.org/rsfc/test/RSFC-16-1) | License is referenced in metadata files | true |
| [RSFC-17-2](https://w3id.org/rsfc/test/RSFC-17-2) | Repository has a commit history | true |
| [RSFC-17-3](https://w3id.org/rsfc/test/RSFC-17-3) | Commits are linked to issues | true |
| [RSFC-18-1](https://w3id.org/rsfc/test/RSFC-18-1) | There are citations | true |
| [RSFC-19-1](https://w3id.org/rsfc/test/RSFC-19-1) | Repository has continuous integration workflows | true |
| [RSFC-20-1](https://w3id.org/rsfc/test/RSFC-20-1) | Repository has an issue tracker | true |
| [RSFC-21-1](https://w3id.org/rsfc/test/RSFC-21-1) | Repository has contribution guidelines | true |
| [RSFC-22-1](https://w3id.org/rsfc/test/RSFC-22-1) | Software offers a container file to run it | true |

## Detailed Results by Indicator

### archived_in_scholarly_repository

<a id="archived_in_scholarly_repository-https---w3id-org-rsfc-test-rsfc-08-2"></a>
#### Metadata record in scholarly repository

- **Test ID:** https://w3id.org/rsfc/test/RSFC-08-2
- **Result:** true
- **Process:** Searches for a Zenodo badge in the README file of the repository
- **Evidence:** A Zenodo DOI identifier was found in:
	- https://zenodo.org/badge/latestdoi/190487675
- **Suggestions:** N/A

### archived_in_software_heritage

<a id="archived_in_software_heritage-https---w3id-org-rsfc-test-rsfc-08-1"></a>
#### Metadata record in Software Heritage

- **Test ID:** https://w3id.org/rsfc/test/RSFC-08-1
- **Result:** true
- **Process:** Searches for a Software Heritage badge in the README file of the repository
- **Evidence:** A Software Heritage badge was found in:
	- https://archive.softwareheritage.org/swh:1:rev:cefb0f9a53ba1fae671819f943e84c087aed6f7d
- **Suggestions:** N/A

### descriptive_metadata

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-03-6"></a>
#### Version number in metadata

- **Test ID:** https://w3id.org/rsfc/test/RSFC-03-6
- **Result:** true
- **Process:** Checks if a version number for the software is indicated in the CITATION.cff, codemeta.json or package files(i.e. pyproject.toml, pom.xml, etc.)
- **Evidence:** Found the software version in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-04-1"></a>
#### Metadata exists

- **Test ID:** https://w3id.org/rsfc/test/RSFC-04-1
- **Result:** true
- **Process:** Searches for codemeta, citation and package files in the repository
- **Evidence:** Found CITATION.cff, codemeta.json, package_file in the repository
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-04-3"></a>
#### There are title and description

- **Test ID:** https://w3id.org/rsfc/test/RSFC-04-3
- **Result:** true
- **Process:** Checks if there is a title and a description for the software in the metadata
- **Evidence:** Found title in https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md and description (no source found, obtained via GitHub_API).
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-04-4"></a>
#### Software has descriptive metadata

- **Test ID:** https://w3id.org/rsfc/test/RSFC-04-4
- **Result:** true
- **Process:** Searches for description, programming languages, date of creation and keywords in the repository
- **Evidence:** Descriptive metadata found in: Description [https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json, https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml], Languages [https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json], Date Created [https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json], Keywords [https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json]
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-04-5"></a>
#### There is a codemeta file

- **Test ID:** https://w3id.org/rsfc/test/RSFC-04-5
- **Result:** true
- **Process:** Searches for a codemeta.json file in the repository
- **Evidence:** A codemeta.json file was found in the root of the repository
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-06-1"></a>
#### Authors are declared

- **Test ID:** https://w3id.org/rsfc/test/RSFC-06-1
- **Result:** true
- **Process:** Searches for authors in various files of the repository (i.e. CITATION.cff, AUTHORS.md, codemeta.json)
- **Evidence:** Authors were found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/CITATION.cff
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
- **Suggestions:** N/A

<a id="descriptive_metadata-https---w3id-org-rsfc-test-rsfc-06-3"></a>
#### Authors have an ORCID

- **Test ID:** https://w3id.org/rsfc/test/RSFC-06-3
- **Result:** false
- **Process:** Checks if all authors stated in the CITATION.cff file have an ORCID assigned
- **Evidence:** Authors that do not have an orcid were found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/CITATION.cff
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json
- **Suggestions:** When documenting your software's authors, you should include their ORCIDs if possible.

### has_active_communication_channels

<a id="has_active_communication_channels-https---w3id-org-rsfc-test-rsfc-05-4"></a>
#### Software has active commmunication channels

- **Test ID:** https://w3id.org/rsfc/test/RSFC-05-4
- **Result:** false
- **Process:** Searches for support channels in the repository
- **Evidence:** Could not find any support channels in the repository
- **Suggestions:** You should give the users an active support channel in case they want to ask questions or have discussions with your developers

### has_active_contributors

<a id="has_active_contributors-https---w3id-org-rsfc-test-rsfc-06-2"></a>
#### Contributors are declared

- **Test ID:** https://w3id.org/rsfc/test/RSFC-06-2
- **Result:** true
- **Process:** Searches for contributors in various files of the repository (i.e. codemeta.json, pyproject.toml, pom.xml)'
- **Evidence:** Contributors were found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md
- **Suggestions:** N/A

### has_contribution_guidelines

<a id="has_contribution_guidelines-https---w3id-org-rsfc-test-rsfc-21-1"></a>
#### Repository has contribution guidelines

- **Test ID:** https://w3id.org/rsfc/test/RSFC-21-1
- **Result:** true
- **Process:** Checks if there are contribution guidelines either in the README file or if there is a CONTRIBUTING.md file
- **Evidence:** Found contribution guidelines at:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md
- **Suggestions:** N/A

### has_releases

<a id="has_releases-https---w3id-org-rsfc-test-rsfc-03-1"></a>
#### Software has releases

- **Test ID:** https://w3id.org/rsfc/test/RSFC-03-1
- **Result:** true
- **Process:** Searches for release tags in the repository
- **Evidence:** These releases were found:
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.11.5
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.11.4
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.11.3
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.11.2
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.11.1
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.11.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.10.3
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.10.2
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.10.1
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.10.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.13
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.12
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.11
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.10
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.9
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.8
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.7_2
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.7_1
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.7
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.6
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.5
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.4
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.3
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.2
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.1
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.9.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.8.2_2
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.8.2
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.8.1
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.8.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.7.2
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.7.1
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.7.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.6.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.5.1
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.5.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.4.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/v0.3.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.2.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.1.0
	- https://github.com/KnowledgeCaptureAndDiscovery/somef/releases/tag/0.0.1
- **Suggestions:** N/A

<a id="has_releases-https---w3id-org-rsfc-test-rsfc-03-2"></a>
#### Releases have an id and version number

- **Test ID:** https://w3id.org/rsfc/test/RSFC-03-2
- **Result:** true
- **Process:** Checks if all of the releases have an identifier and a version
- **Evidence:** All of the releases have an id and a version
- **Suggestions:** N/A

<a id="has_releases-https---w3id-org-rsfc-test-rsfc-03-4"></a>
#### Release identifiers follow the same scheme

- **Test ID:** https://w3id.org/rsfc/test/RSFC-03-4
- **Result:** true
- **Process:** Checks if all of the version identifiers follow the same scheme
- **Evidence:** All of the releases URLs follow the same scheme
- **Suggestions:** N/A

<a id="has_releases-https---w3id-org-rsfc-test-rsfc-03-5"></a>
#### Last release consistency

- **Test ID:** https://w3id.org/rsfc/test/RSFC-03-5
- **Result:** true
- **Process:** Checks if the latest release tag matches the version stated in the codemeta or package files of the repository
- **Evidence:** Latest release matches the latest version stated in the metadata files
- **Suggestions:** N/A

### persistent_and_unique_identifier

<a id="persistent_and_unique_identifier-https---w3id-org-rsfc-test-rsfc-01-1"></a>
#### There is an identifier and resolves

- **Test ID:** https://w3id.org/rsfc/test/RSFC-01-1
- **Result:** true
- **Process:** Searches for an identifier (i.e. DOI or SWHID) in the README file of the repository
- **Evidence:** Found the identifier https://archive.softwareheritage.org/swh:1:rev:cefb0f9a53ba1fae671819f943e84c087aed6f7d in the README and it resolves
- **Suggestions:** N/A

<a id="persistent_and_unique_identifier-https---w3id-org-rsfc-test-rsfc-01-2"></a>
#### There is an identifier associated with the software

- **Test ID:** https://w3id.org/rsfc/test/RSFC-01-2
- **Result:** true
- **Process:** Searches for an identifier in the CITATION.cff, codemeta.json and README files
- **Evidence:** An identifier was found in README.md, codemeta.json. However, no identifier was found in CITATION.cff.
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
- **Evidence:** An identifier was found in the README file of the repository
	- https://zenodo.org/badge/latestdoi/190487675
	- https://archive.softwareheritage.org/swh:1:rev:cefb0f9a53ba1fae671819f943e84c087aed6f7d
- **Suggestions:** N/A

<a id="persistent_and_unique_identifier-https---w3id-org-rsfc-test-rsfc-07-2"></a>
#### Software identifier resolves to software

- **Test ID:** https://w3id.org/rsfc/test/RSFC-07-2
- **Result:** false
- **Process:** Checks if the identifier found in the README file or metadata files (i.e. codemeta.json, CITATION.cff) resolves to a page that links back to the software repository
- **Evidence:** DOI found but not resolvable
- **Suggestions:** You should make sure that your identifier is resolvable and persistent. More information at https://everse.software/RSQKit/software_identifiers

### repository_workflows

<a id="repository_workflows-https---w3id-org-rsfc-test-rsfc-14-2"></a>
#### There are actions to automate tests

- **Test ID:** https://w3id.org/rsfc/test/RSFC-14-2
- **Result:** true
- **Process:** Searches for workflows that contain test or tests in their names
- **Evidence:** There are workflows or actions that perform automated tests
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/.github/workflows/action-test-before-PR.yml
- **Suggestions:** N/A

<a id="repository_workflows-https---w3id-org-rsfc-test-rsfc-19-1"></a>
#### Repository has workflows

- **Test ID:** https://w3id.org/rsfc/test/RSFC-19-1
- **Result:** true
- **Process:** Searches for workflows in the repository
- **Evidence:** Workflows were found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/.github/workflows/action-test-before-PR.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/.github/workflows/docker-publish.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/.github/workflows/pypi-publish.yml
- **Suggestions:** N/A

### requirements_specified

<a id="requirements_specified-https---w3id-org-rsfc-test-rsfc-13-1"></a>
#### Dependencies are declared

- **Test ID:** https://w3id.org/rsfc/test/RSFC-13-1
- **Result:** true
- **Process:** Searches for dependencies in project configuration files, README and dependencies files such as requirements.txt
- **Evidence:** Requirements were found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/docs/requirements.txt
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md
- **Suggestions:** N/A

<a id="requirements_specified-https---w3id-org-rsfc-test-rsfc-13-3"></a>
#### Dependencies have version numbers

- **Test ID:** https://w3id.org/rsfc/test/RSFC-13-3
- **Result:** false
- **Process:** Checks if all of the dependencies stated in the machine-readable file (e.g. requirements.txt, pyproject.toml, etc.) of the repository have a version indicated
- **Evidence:** The following dependencies do not have a version stated:
	- Unknown dependency
	- mkdocs-material
	- numpy
	- pandas
	- scikit-learn
	- requests
	- nltk
	- markdown
	- jupyter
	- matplotlib
	- beautifulsoup4
- **Suggestions:** All of your dependencies should have their versions stated to ensure its reproducibility. More information at https://everse.software/RSQKit/reproducible_software_environments

<a id="requirements_specified-https---w3id-org-rsfc-test-rsfc-13-4"></a>
#### There is a dependencies machine-readable file

- **Test ID:** https://w3id.org/rsfc/test/RSFC-13-4
- **Result:** true
- **Process:** Checks if dependencies are indicated in a machine-readable file
- **Evidence:** There is a machine-readable file for dependencies at:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/pyproject.toml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/docs/requirements.txt
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/old_experiments/helper_scripts/environment.yml
- **Suggestions:** N/A

### software_has_citation

<a id="software_has_citation-https---w3id-org-rsfc-test-rsfc-12-1"></a>
#### There is an article citation or reference publication

- **Test ID:** https://w3id.org/rsfc/test/RSFC-12-1
- **Result:** true
- **Process:** Searches for an article citation or a reference publication in the codemeta and citation files
- **Evidence:** Both a citation to an article and a reference publication were found in:
	- A Framework for Creating Knowledge Graphs of Scientific Software Metadata
	- A Framework for Creating Knowledge Graphs of Scientific Software Metadata
	- SoMEF: A Framework for Capturing Scientific Software Metadata from its Documentation
- **Suggestions:** N/A

<a id="software_has_citation-https---w3id-org-rsfc-test-rsfc-18-1"></a>
#### Repository has citation

- **Test ID:** https://w3id.org/rsfc/test/RSFC-18-1
- **Result:** true
- **Process:** Searches for a CITATION.cff file and README file in the repository
- **Evidence:** A citation was found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/CITATION.cff
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json
- **Suggestions:** N/A

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
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md
- **Suggestions:** N/A

<a id="software_has_documentation-https---w3id-org-rsfc-test-rsfc-05-3"></a>
#### Software documentation

- **Test ID:** https://w3id.org/rsfc/test/RSFC-05-3
- **Result:** true
- **Process:** Searches for a README file in the root repository and other forms of documentation such as a Read The Docs badge or url
- **Evidence:** Documentation was found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md
- **Suggestions:** N/A

<a id="software_has_documentation-https---w3id-org-rsfc-test-rsfc-13-2"></a>
#### There are installation instructions

- **Test ID:** https://w3id.org/rsfc/test/RSFC-13-2
- **Result:** true
- **Process:** Searches for installation instructions in the README file of the repository
- **Evidence:** Installation instructions were found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/docs/install.md
- **Suggestions:** N/A

### software_has_license

<a id="software_has_license-https---w3id-org-rsfc-test-rsfc-15-1"></a>
#### Software has license

- **Test ID:** https://w3id.org/rsfc/test/RSFC-15-1
- **Result:** true
- **Process:** Searches for a file named 'LICENSE' or 'LICENSE.md' in the root of the repository.
- **Evidence:** A license was found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/LICENSE
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/CITATION.cff
- **Suggestions:** N/A

<a id="software_has_license-https---w3id-org-rsfc-test-rsfc-15-2"></a>
#### License is SPDX compliant

- **Test ID:** https://w3id.org/rsfc/test/RSFC-15-2
- **Result:** true
- **Process:** Checks if the licenses detected are SPDX compliant
- **Evidence:** All licenses are SPDX compliant
- **Suggestions:** N/A

<a id="software_has_license-https---w3id-org-rsfc-test-rsfc-16-1"></a>
#### License referenced in metadata files

- **Test ID:** https://w3id.org/rsfc/test/RSFC-16-1
- **Result:** true
- **Process:** Searches for licensing information in the codemeta, CITATION.cff and package files if they exist
- **Evidence:** Found license information in codemeta (MIT), CITATION.cff (MIT) but could not find any in package
- **Suggestions:** N/A

### software_has_tests

<a id="software_has_tests-https---w3id-org-rsfc-test-rsfc-14-1"></a>
#### Presence of tests in repository

- **Test ID:** https://w3id.org/rsfc/test/RSFC-14-1
- **Result:** true
- **Process:** Searches for files and/or directories that mention test in their names. Also, ignores doc and docs directories
- **Evidence:** Files and/or directories that mention test were found at:
	- .github/workflows/action-test-before-PR.yml
	- experiments/old_experiments/training_allen/testing.py
	- notebook/test.json
	- pytest.ini
	- src/somef/rolf/models_test
	- src/somef/rolf/models_test/astrophysics.sav
	- src/somef/rolf/models_test/rationale.md
	- src/somef/rolf/models_test/sequential.sav
	- src/somef/test
	- src/somef/test/__init__.py
	- src/somef/test/conftest.py
	- src/somef/test/test_JSON_export.py
	- src/somef/test/test_bitbucket.py
	- src/somef/test/test_bower_parser.py
	- src/somef/test/test_cabal_parser.py
	- src/somef/test/test_cli.py
	- src/somef/test/test_codeberg.py
	- src/somef/test/test_codemeta_export.py
	- src/somef/test/test_codemeta_gitlab_export.py
	- src/somef/test/test_codemeta_parser.py
	- src/somef/test/test_composer_parser.py
	- src/somef/test/test_conda_environment_parser.py
	- src/somef/test/test_configuration.py
	- src/somef/test/test_data
	- src/somef/test/test_data/README-EUVpy.md
	- src/somef/test/test_data/README-FTR.md
	- src/somef/test/test_data/README-GENI.md
	- src/somef/test/test_data/README-MEL-TNNT.md
	- src/somef/test/test_data/README-OBA-SPARQL.md
	- src/somef/test/test_data/README-OWL-To-OAS.md
	- src/somef/test/test_data/README-PPool.md
	- src/somef/test/test_data/README-TINTO.md
	- src/somef/test/test_data/README-agora.md
	- src/somef/test/test_data/README-almost-empty.md
	- src/somef/test/test_data/README-base-images.md
	- src/somef/test/test_data/README-ci-sample-project.md
	- src/somef/test/test_data/README-citation-file-format.md
	- src/somef/test/test_data/README-componentinstaller.md
	- src/somef/test/test_data/README-csl-editor.md
	- src/somef/test/test_data/README-devilog.md
	- src/somef/test/test_data/README-easytv-annotator.md
	- src/somef/test/test_data/README-epw2rdf-contents.md
	- src/somef/test/test_data/README-epw2rdf.md
	- src/somef/test/test_data/README-fair-ontologies.md
	- src/somef/test/test_data/README-fastify.md
	- src/somef/test/test_data/README-gammalearn.md
	- src/somef/test/test_data/README-gammapy.rst
	- src/somef/test/test_data/README-kgtk-notebooks.md
	- src/somef/test/test_data/README-laueNN.md
	- src/somef/test/test_data/README-licensius.md
	- src/somef/test/test_data/README-lighttwin.md
	- src/somef/test/test_data/README-loupe-api.md
	- src/somef/test/test_data/README-manim.md
	- src/somef/test/test_data/README-mapeathor.md
	- src/somef/test/test_data/README-mapshaper.md
	- src/somef/test/test_data/README-menty.md
	- src/somef/test/test_data/README-os-platforms.md
	- src/somef/test/test_data/README-panda.md
	- src/somef/test/test_data/README-pylops.md
	- src/somef/test/test_data/README-pytorch.md
	- src/somef/test/test_data/README-raidologist.md
	- src/somef/test/test_data/README-reggae.md
	- src/somef/test/test_data/README-stract.md
	- src/somef/test/test_data/README-sunpy.rst
	- src/somef/test/test_data/README-tada-gam.md
	- src/somef/test/test_data/README-tensorflow-2.6.0.md
	- src/somef/test/test_data/README-tokei.md
	- src/somef/test/test_data/README-tpronk.md
	- src/somef/test/test_data/README-unboundedsystems.md
	- src/somef/test/test_data/README-uncbiag.md
	- src/somef/test/test_data/README-urllib3.md
	- src/somef/test/test_data/README-wothive.md
	- src/somef/test/test_data/README-ya2o.md
	- src/somef/test/test_data/SimulatedReads2Map.wdl
	- src/somef/test/test_data/api_responses
	- src/somef/test/test_data/api_responses/bitbucket
	- src/somef/test/test_data/api_responses/bitbucket/bitbucket_response.json
	- src/somef/test/test_data/api_responses/bitbucket/bitbucket_tags.json
	- src/somef/test/test_data/api_responses/codeberg
	- src/somef/test/test_data/api_responses/codeberg/codeberg_forgejo.json
	- src/somef/test/test_data/api_responses/codeberg/codeberg_forgejo_languages.json
	- src/somef/test/test_data/api_responses/codeberg/codeberg_forgejo_releases.json
	- src/somef/test/test_data/api_responses/somef-demo.json
	- src/somef/test/test_data/api_responses/zenodo
	- src/somef/test/test_data/api_responses/zenodo/zenodo_somef_22943101.json
	- src/somef/test/test_data/authors_files
	- src/somef/test/test_data/authors_files/ireeOrg_AUTHORS.txt
	- src/somef/test/test_data/authors_files/jetBrain_AUTHORS.txt
	- src/somef/test/test_data/authors_files/pluginsGLPI_AUTHORS.txt
	- src/somef/test/test_data/authors_files/tensorFlow_AUTHORS.txt
	- src/somef/test/test_data/expected
	- src/somef/test/test_data/expected/aladin-lite.yaml
	- src/somef/test/test_data/expected/gammapy.yaml
	- src/somef/test/test_data/expected/r3broot2.yaml
	- src/somef/test/test_data/expected/runtime_platform_repo.yaml
	- src/somef/test/test_data/export_test.json
	- src/somef/test/test_data/extract_bash_code.txt
	- src/somef/test/test_data/input-test.txt
	- src/somef/test/test_data/package_neors.json
	- src/somef/test/test_data/package_npm.json
	- src/somef/test/test_data/pyansys-README.rst
	- src/somef/test/test_data/rasterio-README.md
	- src/somef/test/test_data/repositories
	- src/somef/test/test_data/repositories/A-Dynamic-E-Commerce-Website-master
	- src/somef/test/test_data/repositories/A-Dynamic-E-Commerce-Website-master/README.md
	- src/somef/test/test_data/repositories/A-Dynamic-E-Commerce-Website-master/admin.php
	- src/somef/test/test_data/repositories/A-Dynamic-E-Commerce-Website-master/admin_orders.php
	- src/somef/test/test_data/repositories/A-Dynamic-E-Commerce-Website-master/delete_from_cart.php
	- src/somef/test/test_data/repositories/A-Dynamic-E-Commerce-Website-master/mangola.sql
	- src/somef/test/test_data/repositories/Clamp
	- src/somef/test/test_data/repositories/Clamp/README.md
	- src/somef/test/test_data/repositories/Fairwinds
	- src/somef/test/test_data/repositories/Fermi
	- src/somef/test/test_data/repositories/Fermi/README.md
	- src/somef/test/test_data/repositories/Flux.jl
	- src/somef/test/test_data/repositories/Flux.jl/Project.toml
	- src/somef/test/test_data/repositories/JAFFA-master
	- src/somef/test/test_data/repositories/JAFFA-master/README
	- src/somef/test/test_data/repositories/JAFFA-master/README.md
	- src/somef/test/test_data/repositories/JAFFA-master/cwl
	- src/somef/test/test_data/repositories/JAFFA-master/cwl/converter.cwl
	- src/somef/test/test_data/repositories/JAFFA-master/cwl/smcFusion-jaffa-workflow.cwl
	- src/somef/test/test_data/repositories/JAFFA-master/cwl/tar.cwl
	- src/somef/test/test_data/repositories/JAFFA-master/cwl/twoBitToFa.cwl
	- src/somef/test/test_data/repositories/OWL-To-OAS-Specification-master
	- src/somef/test/test_data/repositories/OWL-To-OAS-Specification-master/README.md
	- src/somef/test/test_data/repositories/OWL-To-OAS-Specification-master/requirements.txt
	- src/somef/test/test_data/repositories/Pluto.jl
	- src/somef/test/test_data/repositories/Pluto.jl/Project.toml
	- src/somef/test/test_data/repositories/Prometeus
	- src/somef/test/test_data/repositories/RDFChess
	- src/somef/test/test_data/repositories/RDFChess/.gitignore
	- src/somef/test/test_data/repositories/RDFChess/README.md
	- src/somef/test/test_data/repositories/RDFChess/pom.xml
	- src/somef/test/test_data/repositories/RDFChess/rdfchess.config
	- src/somef/test/test_data/repositories/RDFChess/run.bat
	- src/somef/test/test_data/repositories/ack
	- src/somef/test/test_data/repositories/ack/ACKNOWLEDGMENT.md
	- src/somef/test/test_data/repositories/ack/README.md
	- src/somef/test/test_data/repositories/aladin-lite
	- src/somef/test/test_data/repositories/aladin-lite/codemeta.json
	- src/somef/test/test_data/repositories/auroral-ontology-core
	- src/somef/test/test_data/repositories/auroral-ontology-core/ontology.rdf
	- src/somef/test/test_data/repositories/auroral-ontology-core/ontology.xml
	- src/somef/test/test_data/repositories/auroral-ontology-core/readme.md
	- src/somef/test/test_data/repositories/basis_functions_approach_to_GP-master
	- src/somef/test/test_data/repositories/basis_functions_approach_to_GP-master/BF_1D_notebook.Rmd
	- src/somef/test/test_data/repositories/basis_functions_approach_to_GP-master/Diagnosis_HSGP_v2.Rmd
	- src/somef/test/test_data/repositories/basis_functions_approach_to_GP-master/Rnb_case3D_diagnosis.Rmd
	- src/somef/test/test_data/repositories/bimerr-epw
	- src/somef/test/test_data/repositories/bimerr-epw/LICENSE
	- src/somef/test/test_data/repositories/bimerr-epw/README.md
	- src/somef/test/test_data/repositories/bootstrap-datepicker-rails
	- src/somef/test/test_data/repositories/bootstrap-datepicker-rails/bootstrap-datepicker-rails-2.gemspec
	- src/somef/test/test_data/repositories/bootstrap-datepicker-rails/bootstrap-datepicker-rails.gemspec
	- src/somef/test/test_data/repositories/captum
	- src/somef/test/test_data/repositories/captum/.gitattributes
	- src/somef/test/test_data/repositories/captum/.gitignore
	- src/somef/test/test_data/repositories/captum/AWESOME_LIST.md
	- src/somef/test/test_data/repositories/captum/CITATION
	- src/somef/test/test_data/repositories/captum/CODE_OF_CONDUCT.md
	- src/somef/test/test_data/repositories/captum/CONTRIBUTING.md
	- src/somef/test/test_data/repositories/captum/LICENSE
	- src/somef/test/test_data/repositories/captum/README.md
	- src/somef/test/test_data/repositories/captum/environment.yml
	- src/somef/test/test_data/repositories/captum/pyproject.toml
	- src/somef/test/test_data/repositories/captum/setup.cfg
	- src/somef/test/test_data/repositories/captum/setup.py
	- src/somef/test/test_data/repositories/chosen
	- src/somef/test/test_data/repositories/chosen/bower.json
	- src/somef/test/test_data/repositories/cloud-genomics
	- src/somef/test/test_data/repositories/cloud-genomics/.zenodo.json
	- src/somef/test/test_data/repositories/codecov
	- src/somef/test/test_data/repositories/codecov/composer.json
	- src/somef/test/test_data/repositories/codemeta_repo
	- src/somef/test/test_data/repositories/codemeta_repo/codemeta.json
	- src/somef/test/test_data/repositories/componentInstaller
	- src/somef/test/test_data/repositories/componentInstaller/CITATION.cff
	- src/somef/test/test_data/repositories/componentInstaller/LICENSE
	- src/somef/test/test_data/repositories/componentInstaller/README.md
	- src/somef/test/test_data/repositories/composer
	- src/somef/test/test_data/repositories/composer/composer.json
	- src/somef/test/test_data/repositories/corpuser
	- src/somef/test/test_data/repositories/corpuser/README.md
	- src/somef/test/test_data/repositories/cropwater
	- src/somef/test/test_data/repositories/cropwater/DESCRIPTION
	- src/somef/test/test_data/repositories/cropwater/LICENSE.md
	- src/somef/test/test_data/repositories/cropwater/README.md
	- src/somef/test/test_data/repositories/cropwater/codemeta.json
	- src/somef/test/test_data/repositories/ecfo
	- src/somef/test/test_data/repositories/ecfo/ontology.ttl
	- src/somef/test/test_data/repositories/epic
	- src/somef/test/test_data/repositories/epic/.zenodo.json
	- src/somef/test/test_data/repositories/fair-ontologies
	- src/somef/test/test_data/repositories/fair-ontologies/README.md
	- src/somef/test/test_data/repositories/fair-ontologies/citation.cff
	- src/somef/test/test_data/repositories/fair-ontologies/codemeta.json
	- src/somef/test/test_data/repositories/fair-ontologies/pom.xml
	- src/somef/test/test_data/repositories/fake_zenodo
	- src/somef/test/test_data/repositories/fake_zenodo/.zenodo.json
	- src/somef/test/test_data/repositories/fuji
	- src/somef/test/test_data/repositories/fuji/AUTHORS
	- src/somef/test/test_data/repositories/fuji/CITATION.cff
	- src/somef/test/test_data/repositories/fuji/README.md
	- src/somef/test/test_data/repositories/fuji/pyproject.toml
	- src/somef/test/test_data/repositories/gammalearn
	- src/somef/test/test_data/repositories/gammalearn/pyproject.toml
	- src/somef/test/test_data/repositories/gammapy
	- src/somef/test/test_data/repositories/gammapy/codemeta.json
	- src/somef/test/test_data/repositories/ggplot2
	- src/somef/test/test_data/repositories/ggplot2/DESCRIPTION
	- src/somef/test/test_data/repositories/ggstatsplot
	- src/somef/test/test_data/repositories/ggstatsplot/DESCRIPTION
	- src/somef/test/test_data/repositories/ggstatsplot/codemeta.json
	- src/somef/test/test_data/repositories/haskell
	- src/somef/test/test_data/repositories/haskell/cabal.cabal
	- src/somef/test/test_data/repositories/inspect4py
	- src/somef/test/test_data/repositories/inspect4py/CITATION.cff
	- src/somef/test/test_data/repositories/inspect4py/README.md
	- src/somef/test/test_data/repositories/inspect4py/pyproject.toml
	- src/somef/test/test_data/repositories/inspect4py/requirements.txt
	- src/somef/test/test_data/repositories/inspect4py/setup.py
	- src/somef/test/test_data/repositories/ipynb-master
	- src/somef/test/test_data/repositories/ipynb-master/__init__.py
	- src/somef/test/test_data/repositories/ipynb-master/bogus_ipynb.ipynb
	- src/somef/test/test_data/repositories/ipynb-master/r_notebook.ipynb
	- src/somef/test/test_data/repositories/js-template
	- src/somef/test/test_data/repositories/js-template/bower.json
	- src/somef/test/test_data/repositories/js-template/package.json
	- src/somef/test/test_data/repositories/kgtk-notebooks
	- src/somef/test/test_data/repositories/kgtk-notebooks/LICENSE
	- src/somef/test/test_data/repositories/kgtk-notebooks/README.md
	- src/somef/test/test_data/repositories/kgtk-notebooks/tutorial
	- src/somef/test/test_data/repositories/kgtk-notebooks/tutorial/01-kgtk-introduction.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/tutorial/02-kg-profiling.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/tutorial/03-kg-graph-embeddings.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/tutorial/04-kg-enrichment-with-csv.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/tutorial/05-kg-enrichment-with-lod.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/tutorial/06-kg-network-analysis.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/tutorial/07-kg-constraint-validation.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/tutorial/kgtk-browser.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/use-cases
	- src/somef/test/test_data/repositories/kgtk-notebooks/use-cases/Visualize-force-graph-example.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/use-cases/browser-profiling.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/use-cases/class-visualization.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/use-cases/ontology-examples.ipynb
	- src/somef/test/test_data/repositories/kgtk-notebooks/use-cases/properties-for-this-type.ipynb
	- src/somef/test/test_data/repositories/maven
	- src/somef/test/test_data/repositories/maven/pom.xml
	- src/somef/test/test_data/repositories/maykinMedia
	- src/somef/test/test_data/repositories/maykinMedia/publiccode.yaml
	- src/somef/test/test_data/repositories/mir_eval
	- src/somef/test/test_data/repositories/mir_eval/LICENSE.txt
	- src/somef/test/test_data/repositories/mir_eval/README.rst
	- src/somef/test/test_data/repositories/mir_eval/setup.py
	- src/somef/test/test_data/repositories/mira
	- src/somef/test/test_data/repositories/mira/LICENSE
	- src/somef/test/test_data/repositories/mira/README.md
	- src/somef/test/test_data/repositories/nemo
	- src/somef/test/test_data/repositories/nemo/CITATION.cff
	- src/somef/test/test_data/repositories/nemo/README.md
	- src/somef/test/test_data/repositories/pcake
	- src/somef/test/test_data/repositories/pcake/README.md
	- src/somef/test/test_data/repositories/pcake/setup.py
	- src/somef/test/test_data/repositories/probot-12.1.1
	- src/somef/test/test_data/repositories/probot-12.1.1/.editorconfig
	- src/somef/test/test_data/repositories/probot-12.1.1/.gitignore
	- src/somef/test/test_data/repositories/probot-12.1.1/CODE_OF_CONDUCT.md
	- src/somef/test/test_data/repositories/probot-12.1.1/CONTRIBUTING.md
	- src/somef/test/test_data/repositories/probot-12.1.1/LICENSE
	- src/somef/test/test_data/repositories/probot-12.1.1/README.md
	- src/somef/test/test_data/repositories/probot-12.1.1/README.pt-br.md
	- src/somef/test/test_data/repositories/probot-12.1.1/codecov.yml
	- src/somef/test/test_data/repositories/publicCode-Example
	- src/somef/test/test_data/repositories/publicCode-Example/publiccode.yml
	- src/somef/test/test_data/repositories/r3broot2
	- src/somef/test/test_data/repositories/r3broot2/codemeta.json
	- src/somef/test/test_data/repositories/rdflib-6.0.2
	- src/somef/test/test_data/repositories/rdflib-6.0.2/CHANGELOG.md
	- src/somef/test/test_data/repositories/rdflib-6.0.2/CONTRIBUTORS
	- src/somef/test/test_data/repositories/rdflib-6.0.2/LICENSE
	- src/somef/test/test_data/repositories/rdflib-6.0.2/MANIFEST.in
	- src/somef/test/test_data/repositories/rdflib-6.0.2/Makefile
	- src/somef/test/test_data/repositories/rdflib-6.0.2/README.md
	- src/somef/test/test_data/repositories/rdflib-6.0.2/black.toml
	- src/somef/test/test_data/repositories/rdflib-6.0.2/pull_request_template.md
	- src/somef/test/test_data/repositories/rdflib-6.0.2/requirements.dev.txt
	- src/somef/test/test_data/repositories/rdflib-6.0.2/requirements.txt
	- src/somef/test/test_data/repositories/rdflib-6.0.2/run_tests.py
	- src/somef/test/test_data/repositories/rdflib-6.0.2/run_tests.sh
	- src/somef/test/test_data/repositories/rdflib-6.0.2/run_tests_with_coverage_report.sh
	- src/somef/test/test_data/repositories/rdflib-6.0.2/setup.cfg
	- src/somef/test/test_data/repositories/rdflib-6.0.2/setup.py
	- src/somef/test/test_data/repositories/rdflib-6.0.2/skiptests.list
	- src/somef/test/test_data/repositories/rdflib-6.0.2/tox.ini
	- src/somef/test/test_data/repositories/repos_oeg
	- src/somef/test/test_data/repositories/repos_oeg/bimerr-core
	- src/somef/test/test_data/repositories/repos_oeg/bimerr-core/README.md
	- src/somef/test/test_data/repositories/resolver_deco
	- src/somef/test/test_data/repositories/resolver_deco/LICENSE.txt
	- src/somef/test/test_data/repositories/resolver_deco/README.txt
	- src/somef/test/test_data/repositories/resolver_deco/resolver_deco.py
	- src/somef/test/test_data/repositories/resolver_deco/setup.py
	- src/somef/test/test_data/repositories/runtime_platform_repo
	- src/somef/test/test_data/repositories/runtime_platform_repo/codemeta.json
	- src/somef/test/test_data/repositories/rustdesk
	- src/somef/test/test_data/repositories/rustdesk/Cargo.toml
	- src/somef/test/test_data/repositories/soca
	- src/somef/test/test_data/repositories/soca/README.md
	- src/somef/test/test_data/repositories/soca/codemeta.json
	- src/somef/test/test_data/repositories/soca/pyproject.toml
	- src/somef/test/test_data/repositories/soca/setup.cfg
	- src/somef/test/test_data/repositories/software_catalog
	- src/somef/test/test_data/repositories/software_catalog/LICENSE
	- src/somef/test/test_data/repositories/software_catalog/README.md
	- src/somef/test/test_data/repositories/software_catalog/repo_icons
	- src/somef/test/test_data/repositories/software_catalog/repo_icons/acknowledgement.png
	- src/somef/test/test_data/repositories/software_catalog/repo_icons/citation.png
	- src/somef/test/test_data/repositories/somef_repo
	- src/somef/test/test_data/repositories/somef_repo/CITATION.cff
	- src/somef/test/test_data/repositories/somef_repo/README.md
	- src/somef/test/test_data/repositories/somef_repo/lib
	- src/somef/test/test_data/repositories/somef_repo/lib/python
	- src/somef/test/test_data/repositories/somef_repo/lib/python/pip-24.2.dist-info
	- src/somef/test/test_data/repositories/somef_repo/lib/python/pip-24.2.dist-info/AUTHORS.txt
	- src/somef/test/test_data/repositories/somef_repo/pyproject.toml
	- src/somef/test/test_data/repositories/sprint-main
	- src/somef/test/test_data/repositories/sprint-main/netex_accounting_version.xsd.rdf
	- src/somef/test/test_data/repositories/sprint-main/setup.sh
	- src/somef/test/test_data/repositories/stable-diffusion
	- src/somef/test/test_data/repositories/stable-diffusion/README.md
	- src/somef/test/test_data/repositories/stable-diffusion/environment.yaml
	- src/somef/test/test_data/repositories/sunpy
	- src/somef/test/test_data/repositories/sunpy/CITATION.cff
	- src/somef/test/test_data/repositories/sunpy/pyproject.toml
	- src/somef/test/test_data/repositories/sunpy_short_desc
	- src/somef/test/test_data/repositories/sunpy_short_desc/README.rst
	- src/somef/test/test_data/repositories/sunpy_short_desc/pyproject.toml
	- src/somef/test/test_data/repositories/tensorflow
	- src/somef/test/test_data/repositories/tensorflow/CODEOWNERS
	- src/somef/test/test_data/repositories/tensorflow/README.md
	- src/somef/test/test_data/repositories/termlex-main
	- src/somef/test/test_data/repositories/termlex-main/README.md
	- src/somef/test/test_data/repositories/termlex-main/ontology
	- src/somef/test/test_data/repositories/termlex-main/ontology/termlex.ttl
	- src/somef/test/test_data/repositories/termlex-main/termlex_core.png
	- src/somef/test/test_data/repositories/tidyverse
	- src/somef/test/test_data/repositories/tidyverse/DESCRIPTION
	- src/somef/test/test_data/repositories/unused
	- src/somef/test/test_data/repositories/unused/unused.cabal
	- src/somef/test/test_data/repositories/wav2letter
	- src/somef/test/test_data/repositories/wav2letter/CMakeLists.txt
	- src/somef/test/test_data/repositories/wav2letter/CODE_OF_CONDUCT.md
	- src/somef/test/test_data/repositories/wav2letter/CONTRIBUTING.md
	- src/somef/test/test_data/repositories/wav2letter/Decode.cpp
	- src/somef/test/test_data/repositories/wav2letter/LICENSE
	- src/somef/test/test_data/repositories/wav2letter/README.md
	- src/somef/test/test_data/repositories/wav2letter/Test.cpp
	- src/somef/test/test_data/repositories/wav2letter/Train.cpp
	- src/somef/test/test_data/repositories/wav2letter/scripts
	- src/somef/test/test_data/repositories/wav2letter/scripts/OptimizeSortParams.cpp
	- src/somef/test/test_data/repositories/wav2letter/scripts/Seq2SeqAnalysis.cpp
	- src/somef/test/test_data/repositories/wav2letter/scripts/arrayfire_parser.py
	- src/somef/test/test_data/repositories/wav2letter/scripts/fair_cluster
	- src/somef/test/test_data/repositories/wav2letter/scripts/fair_cluster/w2l_fair_cluster_build.sh
	- src/somef/test/test_data/repositories/wav2letter/scripts/fair_cluster/w2l_fair_cluster_decode.sh
	- src/somef/test/test_data/repositories/wav2letter/scripts/fair_cluster/w2l_fair_cluster_distributed_training_benchmarks.sh
	- src/somef/test/test_data/repositories/wav2letter/scripts/fair_cluster/w2l_fair_cluster_train.sh
	- src/somef/test/test_data/repositories/wav2letter/scripts/imgcat
	- src/somef/test/test_data/repositories/wav2letter/scripts/launch_distributed_chronos.sh
	- src/somef/test/test_data/repositories/wav2letter/scripts/tensorboard.py
	- src/somef/test/test_data/repositories/wav2letter/scripts/wavdiff
	- src/somef/test/test_data/repositories/wav2letter/scripts/wavextract
	- src/somef/test/test_data/repositories/wav2letter/scripts/wavplot
	- src/somef/test/test_data/repositories/wav2letter/scripts/wavstatus
	- src/somef/test/test_data/repositories/website-static-master
	- src/somef/test/test_data/repositories/website-static-master/fonts.css
	- src/somef/test/test_data/repositories/website-static-master/header.js
	- src/somef/test/test_data/repositories/website-static-master/image.js
	- src/somef/test/test_data/repositories/website-static-master/index.html
	- src/somef/test/test_data/repositories/website-static-master/index.js
	- src/somef/test/test_data/repositories/website-static-master/layout.js
	- src/somef/test/test_data/repositories/website-static-master/privacy.js
	- src/somef/test/test_data/repositories/website-static-master/terms.js
	- src/somef/test/test_data/repositories/workloopr
	- src/somef/test/test_data/repositories/workloopr/LICENSE
	- src/somef/test/test_data/repositories/workloopr/README.md
	- src/somef/test/test_data/repositories/workloopr/codemeta.json
	- src/somef/test/test_data/repositories/wot-hive
	- src/somef/test/test_data/repositories/wot-hive/README.md
	- src/somef/test/test_data/repostatus-README-2.md
	- src/somef/test/test_data/repostatus-README.md
	- src/somef/test/test_data/test_465.md
	- src/somef/test/test_data/test_arxiv_links.txt
	- src/somef/test/test_data/test_extract_bibtex.txt
	- src/somef/test/test_data/test_extract_binder_links.txt
	- src/somef/test/test_data/test_extract_dois.txt
	- src/somef/test/test_data/test_extract_gitter_chat.txt
	- src/somef/test/test_data/test_extract_header_content_hash.txt
	- src/somef/test/test_data/test_extract_header_content_hash_complex.txt
	- src/somef/test/test_data/test_extract_header_content_underline.txt
	- src/somef/test/test_data/test_extract_title_hash.txt
	- src/somef/test/test_data/test_extract_title_underline.txt
	- src/somef/test/test_data/test_extract_title_with_md.txt
	- src/somef/test/test_data/test_images.txt
	- src/somef/test/test_data/test_issue_181.txt
	- src/somef/test/test_data/test_issue_181_2.txt
	- src/somef/test/test_data/test_issue_181_3.txt
	- src/somef/test/test_data/test_issue_270.txt
	- src/somef/test/test_data/test_issue_images.txt
	- src/somef/test/test_data/test_logo.txt
	- src/somef/test/test_data/test_logo2.txt
	- src/somef/test/test_data/test_logo_tensorflow.txt
	- src/somef/test/test_data/test_logo_uscisii2.txt
	- src/somef/test/test_data/test_pypi.md
	- src/somef/test/test_data/test_repo_status.txt
	- src/somef/test/test_data/test_wiki.md
	- src/somef/test/test_description_parser.py
	- src/somef/test/test_doi_zenodo.py
	- src/somef/test/test_enrichment.py
	- src/somef/test/test_extract_authors.py
	- src/somef/test/test_extract_ontologies.py
	- src/somef/test/test_extract_workflows.py
	- src/somef/test/test_gemspec_parser.py
	- src/somef/test/test_gitlab_selfhosted.py
	- src/somef/test/test_gitlab_token_handling.py
	- src/somef/test/test_google_compliant_export.py
	- src/somef/test/test_header_analysis.py
	- src/somef/test/test_package_json_parser.py
	- src/somef/test/test_parser_somef.py
	- src/somef/test/test_pom_parser.py
	- src/somef/test/test_process_repository.py
	- src/somef/test/test_process_results.py
	- src/somef/test/test_publiccode_parser.py
	- src/somef/test/test_python_parser.py
	- src/somef/test/test_regular_expressions.py
	- src/somef/test/test_setupcfg_parser.py
	- src/somef/test/test_software_type.py
	- src/somef/test/test_supervised_classification.py
	- src/somef/test/test_toml_parser.py
	- src/somef/test/test_turtle_export.py
	- src/somef/test/test_verify_token.py
	- src/somef/test/test_wiki.py
	- src/somef/test/test_zenodo_parser.py
- **Suggestions:** N/A

### software_is_containerized

<a id="software_is_containerized-https---w3id-org-rsfc-test-rsfc-22-1"></a>
#### Software is containerized

- **Test ID:** https://w3id.org/rsfc/test/RSFC-22-1
- **Result:** true
- **Process:** Searches in the root of the repository for container files such as dockerfile, apptainer, podman, etc.
- **Evidence:** Found container files at:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/Dockerfile
- **Suggestions:** N/A

### support_issue_tracking

<a id="support_issue_tracking-https---w3id-org-rsfc-test-rsfc-20-1"></a>
#### Repository has an issue tracker

- **Test ID:** https://w3id.org/rsfc/test/RSFC-20-1
- **Result:** true
- **Process:** Checks if there is an issue tracker in the repository.
- **Evidence:** Found an issue tracker in the repository at:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/codemeta.json
- **Suggestions:** N/A

### version_control_use

<a id="version_control_use-https---w3id-org-rsfc-test-rsfc-05-1"></a>
#### There is a repostatus badge

- **Test ID:** https://w3id.org/rsfc/test/RSFC-05-1
- **Result:** true
- **Process:** Searches for a repo status badge in the README file of the repository
- **Evidence:** A repo status badge was found in:
	- https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md
- **Suggestions:** N/A

<a id="version_control_use-https---w3id-org-rsfc-test-rsfc-09-1"></a>
#### Repository is from Github/Gitlab

- **Test ID:** https://w3id.org/rsfc/test/RSFC-09-1
- **Result:** true
- **Process:** Checks if the URL provided is indeed a Github or Gitlab repository
- **Evidence:** URL provided is a Github or Gitlab repository
- **Suggestions:** N/A

<a id="version_control_use-https---w3id-org-rsfc-test-rsfc-17-2"></a>
#### Commit history

- **Test ID:** https://w3id.org/rsfc/test/RSFC-17-2
- **Result:** true
- **Process:** Checks if the software repository has a commits history
- **Evidence:** A commit history was found in:
	- https://api.github.com/repos/KnowledgeCaptureAndDiscovery/somef/commits?sha=master&since=2026-08-07T08:44:54.282925+00:00&per_page=100
- **Suggestions:** N/A

<a id="version_control_use-https---w3id-org-rsfc-test-rsfc-17-3"></a>
#### Commits are linked to issues

- **Test ID:** https://w3id.org/rsfc/test/RSFC-17-3
- **Result:** true
- **Process:** Checks if there is at least one of the existing issues (opened or closed) referenced in any of the commits made in the default branch of the repository
- **Evidence:** There is at least one commit linked to an issue
	- Commit '35cfc65' linked to Issue #1135
	- Commit 'f931596' linked to Issue #1136
	- Commit 'aee901e' linked to Issue #1136
	- Commit '2310c68' linked to Issue #1135
	- Commit '4afcd50' linked to Issue #1103
	- Commit '0e7acc3' linked to Issue #1104
	- Commit 'cae75d7' linked to Issue #1103
	- Commit 'c55b18a' linked to Issue #1104
	- Commit '5a14bfb' linked to Issue #1105
	- Commit 'a500955' linked to Issue #1105
	- Commit 'a126976' linked to Issue #1102
	- Commit 'd23a4f2' linked to Issue #1102
	- Commit 'a0ad995' linked to Issue #1096
	- Commit 'bbe7568' linked to Issue #1096
- **Suggestions:** N/A

### versioning_standards_use

<a id="versioning_standards_use-https---w3id-org-rsfc-test-rsfc-03-3"></a>
#### Release versions follow a community established convention

- **Test ID:** https://w3id.org/rsfc/test/RSFC-03-3
- **Result:** true
- **Process:** Checks if all of the releases versions follow the SemVer or CalVer versioning standards
- **Evidence:** All of the releases follow a versioning standard
Note: Some versions did not follow the convention but passed the 80% threshold:
	- 0.9.7_2
	- 0.9.7_1
	- 0.8.2_2
- **Suggestions:** N/A
