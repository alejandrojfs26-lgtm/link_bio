import os
from supabase import create_client, Client
import dotenv

class SupabaseAPI:
    dotenv.load_dotenv()
 
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_PUBLISHABLE_KEY")

    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


    def featured(self) -> list:
        
        response = self.supabase.table('featured').select("*").execute()
        
        featured_data = []

        if len(response.data) > 0:
            for featured_item in response.data:
                featured_data.append(featured_item)
        print(featured_data)

        return featured_data
      
