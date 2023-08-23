# Example of FastAPI, Docker and Github Actions

- FastAPI app in `/app/main.py`. Some tests in `/app/tests`.
- Dockerfile for building image with app. Two stage build, separating out dev and prod requirements.
- Github Actions for CI/CD: checkout, test, and build.
