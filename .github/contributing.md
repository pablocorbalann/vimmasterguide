# Contribute to the Vim Master Guide project.
So you want to contribute to VMG? Perfect, for everything to go well you have to follow some **standards**.

### Internal structure of the chapters
The chapters of the book are inside a `json` file, called `data/chapters.json`. The file contains a list of lists with all the chapters. The structure of the chapters is the following:
```
[<name of the chapter => str>, <id => int>, <minutes => int>, <difficulty => str>] 
```
So for example, the 3rd chapter called `This is my chapter` has a duration of 5 minutes and is easy to read and understand, the structure of this chapter will be:
```json
["This is my chapter", 3, 5, "easy"]
```
With that said, let's look at an example of the actual file with 2 chapters:
```json
[
  ["What is Vim?", 1, 3, "easy"],
  ["How to install Vim", 2, 3, "easy"]
]
```

The project is designed to load the HTML document corresponding to each chapter. All the chapter related documents are stored inside [this](https://github.com/PabloCorbCon/vmg/tree/main/templates/chapters) folder. Each document has the name of the chapter ID.
For example, the chapter `["How to install Vim", 2, 3, "easy"]` is assigned to the document `2.html`

There should be the **same number of chapters in the** `data/chapters.json` **file than in the folder with all the HTML documents**.

---

### Before starting:
Before contributing, **identify what type of contribution you want to make to the project**. The VMG digital book accepts the following types of contributions:
* **Internal contributions**: Contributions to the internal structure of the project.
* **Troubleshooting**: Have you found any type of error in VMG, maybe a link is not working or something like that.
* **Updating content**: The good thing about digital books is that they can be updated, just like software in general. So, you can contribute to VMG to update something about Vim.
* **Typos**: Contributions to solve typos in the project.
* **Others**: You can contribute in any other thing, any administrator of VMG will read and consider your pull request.

---

### Steps to contribute:
To contribute, follow this steps:
* Fork the repository in your profile.
* Clone the repository to your local machine.
```
git clone https://github.com/<your name>/vmg
```
* Move inside the repository.
```shell
cd vmg
```
* Activate the environment.
* Install the requirements
```shell
pip install -r requirements.txt
```
* Make your contribution.
* Commit your changes.
* Push the changes **to the dev branch**

**Remember that the repository is configured to automatically deploy the server from the** `main` **branch, so check that the code you write does not break anything once an administrator pulls the dev branch.**
Remember to follow the pull request template when creating the pull request itself.
###### NOTE: It will be a good idea to follow the [conventional commits](https://conventionalcommits.org) standard in your pull request.
