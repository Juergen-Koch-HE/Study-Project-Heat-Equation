# Automatic Compile via Pipeline
With every push, the gitlab CI/CD pipeline will compile abstract, poster and thesis for you.
You can find the artifacts (i.e., the results of the compilation) by navigating on the left to "Build/Articfacts" or use one of the following links:

* [Abstract](https://gitlab.hs-esslingen.de/it-sec-research-public/thesis_template/-/jobs/artifacts/main/browse?job=abstract)
* [Poster](https://gitlab.hs-esslingen.de/it-sec-research-public/thesis_template/-/jobs/artifacts/main/browse?job=poster)
* [Thesis](https://gitlab.hs-esslingen.de/it-sec-research-public/thesis_template/-/jobs/artifacts/main/browse?job=thesis)


# Template Repository

This is an unofficial repository for templates of the HS Esslingen.
Feel free to use and modify the templates. 
Please contribute, by creating a fork and then a merge request.


## Abstract
All you need for the abstract before starting your thesis.

```
cd abstract/tex
make abstract
```


## Code
Store your code here...


## Help
This is a folder with a lot of useful help for writing. 
There is more help in the Abstract Template and Thesis Template as well.


## Poster
All you need for your Posters.

```
cd poster/tex
make poster
```


## Thesis
All you need for your Thesis and some help for writing.

```
cd thesis/tex
make thesis
```


## Wiki
Check out the [Wiki](https://gitlab.hs-esslingen.de/it-sec-research-public/thesis_template/-/wikis/home) for some information on compilint the Wiki to a PDF.
This is very useful for your ```Forschungsprojekt```.

