import os

import datetime
import logging
from supabase import create_client
from dotenv import load_dotenv
from app.models import BusinessOut

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def insert_business_data(data):
    record = {
        "business_name": data.get("business_name", ""),
        "doc_number": data.get("doc_number", ""),
        "status": data.get("status", ""),
        "registration_date": data.get("registration_date", "") or None,
        "state_of_formation": data.get("state_of_formation", ""),
        "principals": data.get("principals", {}),
        "contact_info": data.get("contact_info", {}),
        "scraped_at": datetime.datetime.utcnow().isoformat()
    }
    response = supabase.table("florida-backend").insert(record).execute()
    logging.debug(f"Insert response: {response}")

def get_businesses_by_name(q):
    if not q:
        res = supabase.table("florida-backend").select("*").execute()
    else:
        res = supabase.table("florida-backend").select("*").ilike("business_name", f"%{q}%").execute()
    return res.data
