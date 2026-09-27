"""
API layer
=========

Ties the modules together behind a small FastAPI app. Not the interesting
part of this project — build this last, once scanner/inventory/solver/agent
each work on their own.

Rough endpoint shape to implement once the modules above exist:

  POST /scan            -> upload photo, returns ComponentPrediction
  POST /inventory        -> add a component (manual or from a scan result)
  GET  /inventory         -> list everything owned
  POST /stock-check       -> given a parts list, return owned vs missing
  POST /substitute        -> given a missing component, return solver
                             candidates + agent explanation

TODO(you): implement once scanner/inventory/solver/agent stubs are filled in.
"""

from fastapi import FastAPI

app = FastAPI(title="partlens")


@app.get("/health")
def health():
    return {"status": "ok"}
