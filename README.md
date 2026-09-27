# partlens

An AI-powered electronics inventory manager — scan a component to identify it, track what you own, and get real substitution suggestions when you're missing a value.

Most inventory tools make you manually type in every part you own. partlens uses a trained image classifier to identify components from a photo, and uses correct series/parallel combination math to find substitutions from your *own* inventory when you're missing a value — with an LLM layer that explains *why* a substitution works and what tradeoffs it introduces.

## Why this exists

Every hobbyist has hit this: you need a 220Ω resistor and only have 100Ω and 47Ω in your bin. partlens knows those combine to something close enough, tells you the tolerance impact, and saves you a trip to the store.

## Architecture

```
Photo → Scanner (CV model) → identified component + specs
                                     │
                                     ▼
                          Personal Inventory (store)
                                     │
              ┌──────────────────────┴──────────────────────┐
              ▼                                              ▼
   Project Stock-Check                          Substitution Solver
   (parts list vs. inventory)                   (series/parallel combinatorics)
                                                              │
                                                              ▼
                                                  Agent / Explainer layer
                                              (LLM reasons over solver output,
                                               explains tradeoffs in plain English)
```

- **Deterministic core** (scanner inference, inventory CRUD, combination math) does the actual work and is fully testable without any API calls.
- **Agent layer** sits on top and is the only place that talks to an LLM — it takes structured output (candidate substitutions, component metadata) and turns it into an explanation or comparison. This keeps the "AI agent" part honest: it's doing reasoning/explanation over real structured data, not standing in for logic it should own.

## Project structure

```
partlens/
├── src/
│   ├── scanner/      # image classifier: photo -> component label + specs
│   ├── inventory/     # CRUD + storage for owned components
│   ├── solver/        # series/parallel substitution math
│   ├── agent/         # LLM calls: explain substitutions, compare component types
│   └── api/           # FastAPI app tying it together
├── data/               # sample component data / labels
├── tests/
└── requirements.txt
```

## Status

Early scaffold — module stubs with TODOs, not a working build yet. See each file's docstring for what it needs to do and why.

## Roadmap

- [ ] Component Scanner (image classifier)
- [ ] Personal Inventory (CRUD + storage)
- [ ] Project Stock-Check
- [ ] Substitution Solver (series/parallel math)
- [ ] Agent / Explainer layer (LLM tool-calling over solver + inventory)
- [ ] Component Info Layer (category comparisons, e.g. NPN vs MOSFET)
- [ ] Stretch: Circuit Mini-Explainers (pre-built animated walkthroughs)

## Setup

```bash
pip install -r requirements.txt
```

(Model weights and API key setup instructions to be added once the scanner and agent modules are implemented.)
