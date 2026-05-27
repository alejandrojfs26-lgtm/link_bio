from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()
TWITCH_API = TwitchAPI()

def hello_content() -> str:
    return "Hola"


def hello(_request: Request) -> Response:
    return Response(content=hello_content())


async def live(request: Request) -> JSONResponse:
    user = request.path_params.get("user", "")
    live, title = TWITCH_API.live(user)
    return JSONResponse(content={"live": live, "title": title})


async def featured() -> JSONResponse:
    return JSONResponse(SUPABASE_API.featured())
