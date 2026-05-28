from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from .TwitchAPI import TwitchAPI
from .configcat import ConfigCatAPI
from .SupabaseAPI import SupabaseAPI
from link_bio.model.featured import Featured

TWITCH_API = TwitchAPI()
CONFIGCAT_API = ConfigCatAPI()
SUPABASE_API = SupabaseAPI()

def hello_content() -> str:
    return "Hola"


def hello(_request: Request) -> Response:
    return Response(content=hello_content())


async def live(request: Request) -> JSONResponse:
    user = request.path_params.get("user", "")
    print("user", user)
    live_status = TWITCH_API.live(user)
    return JSONResponse(content={"live": live_status.live, "title": live_status.title})


async def schedule() -> dict:
    return CONFIGCAT_API.schedule()

async def featured() -> list[Featured]:
    return SUPABASE_API.featured()
