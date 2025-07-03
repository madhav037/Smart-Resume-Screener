import os
import uvicorn
import sys

# Add apps/backend to PYTHONPATH so `app.main` becomes importable
sys.path.insert(0, os.path.abspath("apps/backend"))

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
