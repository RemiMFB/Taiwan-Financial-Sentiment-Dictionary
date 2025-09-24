# Policy for Retiring Terms & Handling Words

1. **Deprecation window**: Terms in the 'Deprecated next year' spreadsheet will be removed in the next release.  
2. **Short‑lived buzzwords**: Across the entire dataset, terms with a frequency lower than 30 occurrences are excluded.
3. **Audit trail**: Every addition, removal, or label change must reference a GitHub Issue/PR and the supporting sources.
4. **Consistency rules**: One term → one canonical form; synonyms are separate rows with `alias_of` pointing to the canonical entry.
