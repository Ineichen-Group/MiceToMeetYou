# Mice to Meet You

A system for pulling biomedical literature, classifying it as preclinical
research (animal studies, NAMs, in vitro/in silico models, etc.), and
surfacing it via a public facing dashboard.

## Annotation

The annotation is performed manually in accordance with the guidelines [here](docs/annotation.md). 

### Questions and notes 

__For the annotators:__ Please [submit an issue](/issues) if you have any questions or uncertainties; whether they relate to the annotation in general or to a specific text. 

#### To submit an issue

1. Click on the _Issues_ tab in the top bar (or use the link in the paragraph above).
1. Select _New Issue_ 
1. Give the new issue a title and description. You can include uploaded screenshots here if necessary.
    1. If the issue is related to a specific text, please include the text, keywords, title and journal (if available).
1. Assign the issue to `timchopard` in the left hand column (if you cannot find this, skip this step).
1. Submit the issue.

The issue will start a thread where I and others can respond, this will also keep a record if the same issue comes up again 

__Existing Issues__
You can close an issue of your own, or add a comment to an issue to say that you resolved it yourself. As such, it is better to submit the issue early on and then later close/comment to say that it is resolved than to hold off on submitting an issue. 

## Documentation

- [`docs/dataset.md`](docs/dataset.md):  how the corpus is sourced (OpenAlex,
  field/domain scoping, MeSH coverage findings) and how the annotation sample
  is pulled.
- [`docs/annotation.md`](docs/annotation.md): annotation guidelines used to
  label the training/eval dataset.

## License

See [`LICENSE`](LICENSE).
