"""Event constants shared across all services."""


class CollectorEvents:
    DISCOVERY_STARTED = "collector.discovery.started"
    DISCOVERY_COMPLETED = "collector.discovery.completed"
    DOCUMENT_FETCHED = "collector.document.fetched"
    DOCUMENT_FETCH_FAILED = "collector.document.fetch_failed"


class ParserEvents:
    PARSE_STARTED = "parser.parse.started"
    PARSE_COMPLETED = "parser.parse.completed"
    PARSE_FAILED = "parser.parse.failed"


class ExtractEvents:
    EXTRACT_STARTED = "extract.fields.started"
    EXTRACT_COMPLETED = "extract.fields.completed"
    EXTRACT_FAILED = "extract.fields.failed"


class PolicyEvents:
    POLICY_CREATED = "policy.version.created"
    POLICY_UPDATED = "policy.version.updated"
    POLICY_PUBLISHED = "policy.version.published"
