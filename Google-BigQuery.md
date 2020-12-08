# BigQuery Exercise Solution

> My solution is avaliable
> [at Google's Console](https://console.cloud.google.com/bigquery?sq=715042235681:be67fe101a49483586602c663335058e).

### Question

In BigQuery, use dataset “interviews” to query “demo_requests” table in order to
get aggregations of revenue, ad_served, session_start, cpm, rps and page_views
for each utm_campaign.

CPM = (revenue / ad_served) \* 1000 RPS = revenue / session_starts

### Solution

```sql
WITH params AS (
  SELECT
    IFNULL(SAFE_CAST(REGEXP_EXTRACT(httpRequest.requestUrl, r"revenue=([^&]+)") AS NUMERIC), 0) AS revenue,
    REGEXP_EXTRACT(httpRequest.requestUrl, r"event=([^&]+)") AS event,
    REGEXP_EXTRACT(httpRequest.requestUrl, r"utm_campaign=([^&]+)") AS utm_campaign
  FROM `rnd-interviews.interviews.demo_requests`
)
SELECT
  SUM(revenue) AS revenue,
  COUNTIF(event="ad_served") AS ad_served,
  COUNTIF(event="session_start") AS session_start,
  SAFE_MULTIPLY(SAFE_DIVIDE(SUM(revenue), COUNTIF(event="ad_served")), 1000) AS cpm,
  SAFE_DIVIDE(SUM(revenue), COUNTIF(event="session_start")) AS rps,
  COUNTIF(event="page_view") AS page_views
FROM params
GROUP BY utm_campaign
```

### Explanation

The first part of the query (the one enclosed in `with` clause), will extract
from the `httpRequest.requestUrl` 3 properties: utm_campaign identifier, event
name and revenue as a number.

Then, from the results of the previous request, we sum up the revenue, number of
advertisements served, number of page views, and number of session started for
each campaign. We also calculate the CPM and RPS for each campaign as well.

### My Approach

To solve this problem, I've first looked at a few samples of the data in order
to find the relevant properties. It led me to the conclusion, that the only
property that I've needed to use was `httpRequest.requestUrl`.

Then, I've searched the internet and Google's documentation to find the SQL
flavor that BigQuery is using, to help me parse `requestUrl`. I've found
Google's
[reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#limit_and_offset_clause)
for BigQuery's SQL, and with the help of
[Regex Planet](https://www.regexplanet.com/advanced/golang/index.html) I was
able to extract the basic properties. Then it was just counting and filtering
the events to get the solution.

### Relevant Links

- **My Solution:**  
  https://console.cloud.google.com/bigquery?authuser=1&project=rnd-interviews&page=savedqueries&sq=715042235681:be67fe101a49483586602c663335058e
- **BigQuery's Reference:**  
  https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators

  https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#top_of_page

- **`re2` syntax (BigQuery's regex type):**  
  https://github.com/google/re2/wiki/Syntax
- **RegexPlanet:** https://www.regexplanet.com/advanced/golang/index.html
