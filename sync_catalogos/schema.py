"""Catalog file schema — JSON con `{metadata, entries}`."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal


SourceKind = Literal["socrata", "sispro_aspx", "reps_export", "manual"]


@dataclass
class CatalogMetadata:
    name: str                              # short id (e.g. "divipola_municipios")
    description: str = ""
    source: SourceKind = "manual"
    source_url: str = ""                   # canonical URL of the upstream source
    source_id: str | None = None           # Socrata dataset id / SISPRO Code value
    version: str | None = None             # remote version string if available
    license: str = ""                      # short license tag
    row_count: int | None = None
    last_synced: str | None = None         # ISO 8601 UTC of the last sync write
    sha256: str | None = None              # hash of the entries serialization
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class CatalogFile:
    metadata: CatalogMetadata
    entries: list[Any] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "metadata": self.metadata.to_dict(),
            "entries": self.entries,
        }
