# hapi-server-setup

This is an early effort to simplify the instantiation of a HAPI server and loading it with an initial set of resources.

Specifically, it allows you to:
- Build a HAPI Spring Boot executable War from a repository and branch/sha of your choice.
  - Currently defaults to building v6.4.0 of https://github.com/hapifhir/hapi-fhir-jpaserver-starter.git
- Run the War.
- Use Postgresql as the HAPI database.
- Use ElasticSearch as the indexing backend
- Use Kibana to explore the ElasticSearch index
- Load individual FHIR resource files
- Load sets of FHIR resources from plain zip files
  - Loading FHIR packages is coming soon
- Docker Compose based
- A built-in simple Python CLI that drives the Docker Compose execution, with a few Bash wrapper scripts for the basic use cases.
  - Windows not supported yet

Further documentation coming soon.