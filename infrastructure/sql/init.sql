-- =============================================================
-- Social Fund Platform – Database Initialization
-- =============================================================

-- Regions table
CREATE TABLE IF NOT EXISTS regions (
    id          SERIAL PRIMARY KEY,
    region_code VARCHAR(20)  NOT NULL UNIQUE,
    province    VARCHAR(50)  NOT NULL,
    city        VARCHAR(50)  NOT NULL,
    status      VARCHAR(20)  NOT NULL DEFAULT 'active',
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

-- Source documents table
CREATE TABLE IF NOT EXISTS source_documents (
    id               SERIAL PRIMARY KEY,
    region_id        INTEGER      REFERENCES regions(id),
    title            VARCHAR(512) NOT NULL,
    source_url       TEXT         NOT NULL,
    source_org       VARCHAR(255),
    content_type     VARCHAR(50)  NOT NULL DEFAULT 'text/html',
    content_hash     VARCHAR(64),
    raw_text         TEXT,
    object_path      TEXT,
    snapshot_path    TEXT,
    parse_status     VARCHAR(20)  NOT NULL DEFAULT 'pending',
    fetched_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    created_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

-- Policy versions table
CREATE TABLE IF NOT EXISTS policy_versions (
    id                   SERIAL PRIMARY KEY,
    region_id            INTEGER      NOT NULL REFERENCES regions(id),
    policy_type          VARCHAR(50)  NOT NULL,  -- housing_fund | social_insurance
    version_no           VARCHAR(50)  NOT NULL,
    effective_from       DATE         NOT NULL,
    effective_to         DATE,
    publish_status       VARCHAR(20)  NOT NULL DEFAULT 'draft',
    current_flag         BOOLEAN      NOT NULL DEFAULT FALSE,
    source_document_id   INTEGER      REFERENCES source_documents(id),
    approved_by          VARCHAR(100),
    approved_at          TIMESTAMPTZ,
    created_at           TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    updated_at           TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

-- =============================================================
-- Seed data – three example regions
-- =============================================================
INSERT INTO regions (region_code, province, city, status) VALUES
    ('CN-BJ',    '北京市', '北京市', 'active'),
    ('CN-SH',    '上海市', '上海市', 'active'),
    ('CN-GD-SZ', '广东省', '深圳市', 'active')
ON CONFLICT (region_code) DO NOTHING;
