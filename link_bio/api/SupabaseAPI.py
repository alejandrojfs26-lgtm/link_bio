import os
from supabase import create_client, Client
import dotenv

dotenv.load_dotenv()

class SupabaseAPI:

    def __init__(self):
        self.supabase: Client = create_client(
            os.environ["SUPABASE_URL"],
            os.environ["SUPABASE_PUBLISHABLE_KEY"],
        )

    def featured(self) -> list:
        response = self.supabase.table("featured").select("*").execute()
        return response.data
      
