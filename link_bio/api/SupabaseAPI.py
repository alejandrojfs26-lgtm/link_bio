import os
from supabase import create_client, Client
import dotenv
from link_bio.model.featured import Featured


dotenv.load_dotenv()

class SupabaseAPI:

    def __init__(self):
        self.supabase: Client = create_client(
            os.environ["SUPABASE_URL"],
            os.environ["SUPABASE_PUBLISHABLE_KEY"],
        )

    def featured(self) -> list[Featured]:
        response = self.supabase.table("features").select("*").limit(2).execute()
        return [
            Featured(
                title=item["title"],
                url=item["url"],
                image=item["image"],
            )
            for item in response.data
        ]
