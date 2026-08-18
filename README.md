# Mice to Meet You

A system for pulling biomedical literature, classifying it as preclinical
research (animal studies, NAMs, in vitro/in silico models, etc.), and
surfacing it via a public facing dashboard.

## Status

Early stage. Data sourcing strategy and annotation guidelines are defined;
annotation and model training have not yet started.

## Repository structure

```
.
├── app/            # Django project (web app / dashboard)
├── docs/           # project documentation (see below)
├── oneshots/        # standalone investigative/test scripts, not part of the app
├── compose.yml       # Docker Compose services
├── Dockerfile
└── pyproject.toml
```

## Documentation

- [`docs/dataset.md`](docs/dataset.md):  how the corpus is sourced (OpenAlex,
  field/domain scoping, MeSH coverage findings) and how the annotation sample
  is pulled.
- [`docs/annotation.md`](docs/annotation.md): annotation guidelines used to
  label the training/eval dataset.

## Development

Setup and local development instructions will be added once the Django app
is scaffolded.

## License

See [`LICENSE`](LICENSE).
