from dataclasses import dataclass


@dataclass
class SearchResult:
    id: str
    name: str
    url: str
    type: str
    pwd: str
    from_site: str

    def __getitem__(self, field_name: str) -> any:
        return getattr(self, field_name)