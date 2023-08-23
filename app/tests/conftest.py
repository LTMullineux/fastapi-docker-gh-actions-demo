import pytest_asyncio
from httpx import AsyncClient

from app.main import app


class BaseTestRouter:
    @pytest_asyncio.fixture(scope="function")
    async def client(self):
        async with AsyncClient(app=app, base_url="http://test") as c:
            yield c
