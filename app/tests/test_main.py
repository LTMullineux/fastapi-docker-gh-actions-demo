from app.tests.conftest import BaseTestRouter


class TestMain(BaseTestRouter):
    async def test_health(self, client):
        r = await client.get("/")
        assert r.status_code == 200

        payload = r.json()
        assert payload["status"] == "OK"
        assert payload["message"] == "Visit /docs for more information."

    async def test_hire_me(self, client):
        r = await client.get("/hire-me")
        assert r.status_code == 200

        payload = r.json()
        assert payload["message"] == "Hire me!"
        assert payload["email"] == "lawsontaylor@hotmail.co.uk"
        assert payload["phone"] == "+44 7540077944"
