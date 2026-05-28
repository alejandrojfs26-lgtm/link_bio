import os
from supabase import create_client, Client
import dotenv
from link_bio.model.featured import Featured

dotenv.load_dotenv()


class SupabaseAPI:

    def __init__(self):
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")
        if url and key:
            self.supabase: Client = create_client(url, key)
        else:
            self.supabase = None

    def featured(self) -> list[Featured]:
        if not self.supabase:
            return []
        response = self.supabase.table("features").select("*").limit(2).execute()
        return [
            Featured(
                title=item["title"],
                url=item["url"],
                image=item["image"],
            )
            for item in response.data
        ]
