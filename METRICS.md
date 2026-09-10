# What the profile numbers mean

All data belongs to **Abhilasha-Ahingare**. The initial snapshot is fetched from
public GitHub endpoints; the JSON records the exact UTC update time and sources.
The package never copies contribution numbers out of the design reference.

| Card | Scope |
| :-- | :-- |
| Contributions | Sum of daily counts visible on the public profile for the latest 365 dates, including today in UTC. |
| Public repositories | All public repositories owned by the username, including forks. |
| Stars | Stars on owned public original repositories; forks excluded. |
| Pull requests / issues | Public issues-search counts authored by the username, separated by type. |
| Active days | Dates with at least one visible contribution within the same 365-day window. |
| Total contributions / longest streak | Visible calendar history from January of the account-creation year through today. |
| Current streak | Consecutive active dates ending today; if today is still zero, yesterday may continue the streak. |
| Languages | Aggregated language bytes in public, non-fork, non-archived owned repositories. Profile repository excluded. |
| Top contributed repositories | GitHub-attributed commits in owned public, non-fork repositories, profile repository excluded. Top five are shown; the full ranking is linked below the cards. |

## Contribution calendar

The calendar uses public GitHub contribution HTML, not a private-account API.
Counts may include anonymized private activity if the profile owner has made
those counts visible. Private repository names, contents and endpoints are not
requested. Public and private contribution visibility can cause counts to
differ from what a signed-in owner sees elsewhere.

The calendar markup is not a versioned API. The parser validates every date and
its numerical count. Missing counts, conflicting duplicates, malformed HTML or
HTTP failures abort the refresh before any previous metric card is replaced.
If GitHub changes the markup, the parser may need maintenance. A failed run keeps
the last successful dated snapshot; it never silently replaces failures with zero.

Daily counts are also available as Markdown in `data/ACTIVITY.md`, and all parsed
historical dates are retained in `data/metrics.json`. These are per-day activity
counts, not hours worked or skill ratings.

## Repository ranking

The [contributors API](https://docs.github.com/en/rest/repos/repos#list-repository-contributors)
groups commit counts by the GitHub account associated with author email addresses.
These are API-reported commit totals, not the number of all GitHub contribution
events. The result is **limited to owned public original repositories**; it does
not claim to rank contributions across every organization or private repository.

GitHub caches this endpoint for hours. Only its first 500 author email addresses
in a repository link to GitHub users; remaining authors can be anonymous. The
generator does not guess ownership of anonymous commits. It handles pagination,
case-insensitive usernames and the documented empty-repository response.

## Quote and views

The daily quote card rotates among seven original development notes included in
the generator. They are not attributed to a famous developer or represented as
Abhilasha's own quotations. This avoids depending on the old external quote API.

The optional Komarev image is the only external visual dependency. It counts
image requests, subject to caching; it is not a count of unique visitors. No old
visitcount total is transferred or invented. Remove the final `<p>` containing
`komarev.com` from README.md if you do not want this counter.

## Data sources

- [Public profile API](https://api.github.com/users/Abhilasha-Ahingare)
- [Public repository API](https://api.github.com/users/Abhilasha-Ahingare/repos)
- [Public contribution calendar](https://github.com/users/Abhilasha-Ahingare/contributions)
- [Repository languages API](https://docs.github.com/en/rest/repos/repos#list-repository-languages)
- [Repository contributors API](https://docs.github.com/en/rest/repos/repos#list-repository-contributors)
- [Issues and pull requests search API](https://docs.github.com/en/rest/search/search#search-issues-and-pull-requests)
- [View counter source](https://github.com/antonkomarev/github-profile-views-counter)

Network fetching uses the Python standard library. A token, if provided via
`GH_TOKEN`, is attached only to `api.github.com` requests and is never embedded in
the README, JSON or image files. No credentials are shipped in this package.
