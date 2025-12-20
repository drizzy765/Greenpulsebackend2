import urllib.request
import json
import uuid
import datetime

BASE_URL = "http://localhost:8000"
TOKEN = "dev-token" # Mock token for DevUser

def get_headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

def create_entry():
    url = f"{BASE_URL}/manual_entry"
    data = {
        "business_type": "TestCorp",
        "date": datetime.date.today().isoformat(),
        "source_category": "electricity",
        "activity": "Grid usage",
        "amount": 100,
        "unit": "kWh",
        "emission_factor": 0.5,
        "scope": "Scope 2"
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=get_headers(), method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except Exception as e:
        print(f"Create Entry Failed: {e}")
        return None

def get_insights(business_id):
    url = f"{BASE_URL}/insights/{business_id}"
    req = urllib.request.Request(url, headers=get_headers(), method="GET")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        print(f"Get Insights HTTP Error: {e.code} {e.reason}")
        print(e.read().decode())
    except Exception as e:
        print(f"Get Insights Failed: {e}")

def main():
    print("Creating entry...")
    entry_resp = create_entry()
    if not entry_resp:
        return
    
    business_id = entry_resp.get("business_id")
    print(f"Entry created. Business ID: {business_id}")
    
    print("Requesting insights...")
    insights = get_insights(business_id)
    if insights:
        print("Insights Response:")
        print(json.dumps(insights, indent=2))

if __name__ == "__main__":
    main()
