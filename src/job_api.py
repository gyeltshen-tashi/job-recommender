import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Fetch linkedIn jobs based on search query and location 
def fetch_linkedin_jobs(search_query, location="india", rows=60):
  # Prepare the Actor input
  run_input = {
      "title": "search_query",
      "location": "location",
      "rows": rows,
      "proxy": {
          "useApifyProxy": True,
          "apifyProxyGroups": ["RESIDENTIAL"],
      },
  }
  # Run the Actor and wait for it to finish
  run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
  # Fetch and print Actor results from the run's dataset (if there are any)
  jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items()) 
  return jobs


# Fetch Naukri jobs based on search query and location
def fetch_naukri_jobs(search_query, location="india", rows=60):
  # Prepare the Actor input
  run_input = {
      "keyword": search_query,
      "maxJobs": rows,
      "freshness": "all",
      "sortBy": "relevance",
      "experience":"all",
  }
  run = apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)
  jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
  return jobs