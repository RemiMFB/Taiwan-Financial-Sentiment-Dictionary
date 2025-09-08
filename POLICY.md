# Policy for Retiring Terms & Handling Buzzwords

1. **Deprecation window**: Terms flagged as `deprecated=true` remain in the lexicon for one release after deprecation with a `deprecated_in_version` field. They are then removed in the next release; a mapping is kept in `data/deprecated_map.csv`.
2. **Short‑lived buzzwords**: Candidate terms must be observed in at least 3 independent sources over a rolling 6‑month window. Otherwise they are blocked. Blocked candidates are logged in `data/blocked_terms.csv`.
3. **Audit trail**: Every addition, removal, or label change must reference a GitHub Issue/PR and the supporting sources.
4. **Consistency rules**: One term → one canonical form; synonyms are separate rows with `alias_of` pointing to the canonical entry.
