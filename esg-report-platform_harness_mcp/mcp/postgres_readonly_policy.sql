-- Example: create a read-only role for MCP access
-- Adjust usernames/passwords in real environment.

-- CREATE ROLE mcp_readonly LOGIN PASSWORD 'change-me';
-- GRANT CONNECT ON DATABASE esg_platform TO mcp_readonly;
-- GRANT USAGE ON SCHEMA public TO mcp_readonly;
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO mcp_readonly;
-- ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO mcp_readonly;
