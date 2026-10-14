# Free Tier Finder data

Verified free tiers, promos and startup credits for AI and developer tools. This is the source data for [freetierfinder.com](https://freetierfinder.com).

![Last checked](https://img.shields.io/badge/last%20checked-{{BADGE_DATE}}-blue) ![Tools](https://img.shields.io/badge/tools-{{TOOLS}}-informational) ![Promos](https://img.shields.io/badge/promos-{{PROMOS}}-informational) ![License: CC BY 4.0](https://img.shields.io/badge/data%20license-CC%20BY%204.0-lightgrey)

- Site: https://freetierfinder.com
- Machine-readable summary: https://freetierfinder.com/llms.txt

## Files

| File | Contents |
| --- | --- |
| `data/tools.json`, `data/tools.csv` | {{TOOLS}} tools with active free tiers |
| `data/promos.json`, `data/promos.csv` | {{PROMOS}} promos, credits and startup programs |
| `data/dropped.json` | Entries removed after their free tier ended or could not be confirmed |
| `scripts/export.py` | Regenerates the data files, this README and the changelog |

### Fields

| Field | Meaning |
| --- | --- |
| `name` | Tool or offer name |
| `category` | Tool category, or offer type for promos |
| `what_you_get` | What the free tier or offer includes |
| `how_to_get_it` | How to claim it |
| `requirements` | Eligibility or account requirements |
| `catch` | Main limitation |
| `no_card_status` | Whether a payment card is required, as stated by the vendor |
| `official_source_url` | Vendor page the facts were taken from |
| `date_checked` | Date the facts were last checked (YYYY-MM-DD) |
| `page_url` | Entry page on freetierfinder.com |

## Methodology

- Every entry is verified on the vendor's official pricing, documentation or announcement page. Third-party sources are not used.
- Each entry records the source URL and the date it was checked.
- Where the vendor does not state a fact (for example, whether a card is required), the field says so instead of guessing.
- Entries are removed when the free tier or offer is no longer active. Removed entries are listed in `data/dropped.json`.
- Source URLs are official vendor URLs only. No affiliate or referral links are included.

## Tools by category

{{TABLE}}

## Report an outdated entry

Open an issue with the [Report outdated entry](../../issues/new?template=report-outdated.md) template and include a link to the vendor's official page. To propose a new tool, use [Suggest a tool](../../issues/new?template=suggest-tool.md).

## License

The data in `data/` is licensed under [CC BY 4.0](LICENSE). Attribute "Free Tier Finder (https://freetierfinder.com)". Scripts in `scripts/` are MIT licensed.

## Citation

See [CITATION.cff](CITATION.cff).
