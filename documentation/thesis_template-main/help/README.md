# Best Practices for Theses
## Title
* https://capitalizemytitle.com/
## Writing
* https://www.quickanddirtytips.com/education/grammar/like-versus-such-as
* https://www.springer.com/gp/authors-editors/authorandreviewertutorials/writinginenglish
* http://writing2.richmond.edu/writing/wweb/trans1.html

### Latex
#### General Hints
* https://www.overleaf.com/learn/latex/Brackets_and_Parentheses
* https://tex.stackexchange.com/questions/58098/what-are-all-the-font-styles-i-can-use-in-math-mode
* Get proper bibtex: https://dblp.uni-trier.de/
* Use \usepackage[binary-units=true, per-mode=symbol]{siunitx} for units, e.g. \SI{1000}{\mega\bit\per\second}
* In float-environments, put labels after the caption (https://www.stefaanlippens.net/latexcaptionlabel/)
* Looking for a certain math symbol? Just draw it --> https://detexify.kirelabs.org/classify.html

#### Thesis Template
Please use the Template of HS Esslingen as a general layout, but you can find more inspiration here:
* https://github.com/latextemplates/scientific-thesis-template

#### Grammar Error Detection (de/en)
* LanguageTool: https://languagetool.org
* How to configure LT in TeXstudio:
    * [de] Optionen --> TeXstudio konfigurieren --> Sprache prüfen --> Server URL
    * [en] Options --> Configure TeXstudio --> Language Checking --> Server URL

#### git autocommit in TeXstudio
* Initialize a git repo in your project folder with `git init` and manually check in and commit all the files you want to track
* Configure autocommit with every compilation
    * In TeXstudio Settings -> Build, add a user command `user0:Autocommit` with the content `git commit -am "texstudio autocommit"`
    * Close the window to save it
    * Open the Build settings again, click on advanced options in the lower left corner
    * Append ` | txs:///user0` to `Default Compiler` to commit on every compile action (F6)
    * Alternatively, add it to `Build & view` to only commit with that action (F5)
* Manual commit macro
    * Create a new macro with no trigger, of type `Script` with the following content:
```
%SCRIPT
buildManager.runCommand("git commit -am \"texstudio-autosave\"", editor.fileName())
```
You may want to create a second command or amend the macro to also push your changes to a remote.

## Evaluation
* https://www.cse.unsw.edu.au/~gernot/benchmarking-crimes.html
* http://spcl.inf.ethz.ch/Publications/.pdf/hoefler-scientific-benchmarking.pdf
* https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/
* https://matplotlib.org/stable/gallery/index.html

## Figures
* Use vector graphics (pdf, svg, ...)
* Do NOT scale figures (text, labels will be skewed)
* Generate figures with correct width (--> get from template)
* Calculate height via golden cut ($` \frac{1 + \sqrt{5}}{2} * \text{width} `$) (https://www.omnicalculator.com/math/golden-rectangle)
* Use same font and font size as the template

## Reviews
* https://www.cl.cam.ac.uk/teaching/1011/R01/review-writing.pdf


## Implementation
### Python Gotchas
* https://docs.python-guide.org/writing/gotchas/
### Caching of Processing-intensive Subtasks (Python3)
```
if not os.path.isfile('/tmp/<filename>.bin'):

    # TASK (e.g. <resultvar> = ...)

    with open('/tmp/<filename>.bin', 'wb') as cache_fd:
        pickle.dump(<resultvar>, cache_fd)
else:
    with open('/tmp/<filename>.bin', 'rb') as cache_fd:
        <resultvar> = pickle.load(cache_fd)
```

# Tutorials
* Git: https://learngitbranching.js.org/

# Contributors
 * David Hellmanns (initial version for Uni Stuttgart)
 * Michel Weitbrecht (TeXStudio autocommit)
 * Lukas Wüsteney (remove specifics of Uni Stuttgart)
