# Policy for Retiring Terms & Handling Words

1. **Deprecation window**: Terms flagged as `deprecated=true` remain in the lexicon for one release after deprecation with a `deprecated_in_version` field. They are then removed in the next release; a mapping is kept in `docs/deprecated_map.csv`.
2. **Short‑lived buzzwords**: Across the entire dataset, terms with a frequency lower than 30 occurrences are excluded.
3. **Audit trail**: Every addition, removal, or label change must reference a GitHub Issue/PR and the supporting sources.
4. **Consistency rules**: One term → one canonical form; synonyms are separate rows with `alias_of` pointing to the canonical entry.
