# 📆 Datetime of Workflow <br> [![GitHub License](https://img.shields.io/github/license/ZekeriyaAY/workflow-datetime?logo=GNU)](/LICENSE) [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ZekeriyaAY/workflow-datetime/Datetime%20of%20Workflow?label=Test%20Workflow&logo=GitHub)](https://github.com/ZekeriyaAY/workflow-datetime/actions?query=workflow%3A%22Datetime+of+Workflow%22)

***💫 Last Update:*** &nbsp; <!-- DEFAULT-TAG:START -->
Tue  06 Sep 2022  12:32:44 UTC
<!-- DEFAULT-TAG:END -->

![preview](/example.png)


## 📝 How to use
1. Star this repo 😉 
1. Go to your repository
1. Add the following tag to your **README.md** file, you can give whatever title you want. Just make sure that you use `<!-- DEFAULT-TAG:START --> <!-- DEFAULT-TAG:END -->` in your readme. The workflow will replace this comment with the datetime of workflow: 
    ```markdown
    # 💫 Last Update
    <!-- DEFAULT-TAG:START -->
    <!-- DEFAULT-TAG:END -->
    ```
1. Create a folder named `.github` and create a `workflows` folder inside it, if it doesn't exist.
1. Create a new file named `workflow-datetime.yml` with the following contents inside the workflows folder:
    ```yaml
    name: Datetime of Workflow
    on:
      push:
        branches:
          - main
        workflow_dispatch:
    jobs:
      workflow-date:
        name: Update the datetime of workflow in the README
        runs-on: ubuntu-latest
        steps:
          - name: Checkout
            uses: actions/checkout@v3

          - name: Update with Datetime of Workflow
            uses: ZekeriyaAY/workflow-date@main
            with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
              # date_format: '%a  %d %b %Y  %H:%M:%S%Z'
              # timezone: 'UTC'
              # tag: 'DEFAULT-TAG'
              # markdown_path: './README.md'
              # commit_branch: 'main'
              # commit_username: 'github-actions[bot]'
              # commit_email: 'github-actions[bot]@users.noreply.github.com'
              # commit_message: '🚀 Datetime of Workflow Updated'
    ```
1. Update the above input parameters with your own information. See [options](#options) for a list of input parameters.
1. Commit and wait for it to run automatically or you can also trigger it manually to see the result instantly.


## 🔧 Options
This workflow has additional options that you can use to customize it for your use case. The following are the list of options available:

| Option | Default Value | Description | Required |
|--------|--------|--------|--------|
| `github_token` | `-` | Token for the repo. Can be passed in using `${{ secrets.GITHUB_TOKEN }}` | Yes |
| `date_format` | `%a  %d %b %Y  %H:%M:%S %Z` | Allows you to change the format of the date or time displayed | No  |
| `timezone` | `UTC` | Timezone Region | No |
| `tag` | `DEFAULT-TAG` | The name of the tag to be updated in the Markdown | No |
| `markdown_path` | `./README.md` | Path to Markdown file | No | 
| `commit_branch` | `main` | Destination branch to push changes | No |
| `commit_username` | `github-actions[bot]` | Username of the user to commit | No  |
| `commit_email` | `github-actions[bot]@users.noreply.github.com` | Email of the user to commit | No |
| `commit_message` | `🚀 Datetime of Workflow Updated` | Commit message | No |


### 🚀 Examples 
* [This README](https://github.com/ZekeriyaAY/workflow-datetime/blob/main/README.md) - [YML File](https://github.com/ZekeriyaAY/workflow-datetime/blob/main/.github/workflows/example-workflow-datetime.yml)
* [My own GitHub profile readme](https://github.com/ZekeriyaAY) - [YML File](https://github.com/ZekeriyaAY/ZekeriyaAY/blob/main/.github/workflows/latest-x-workflow.yml)
* [My portfolio website](https://zekeriyaay.com) - [YML File](https://github.com/ZekeriyaAY/zekeriyaay.com/blob/mainResearcher/.github/workflows/researcher-gh-pages.yml)


## 🚧 Contributing
Please see [CONTRIBUTING.md](/CONTRIBUTING.md) for getting started with the contribution. 

Make sure that you follow [CODE_OF_CONDUCT.md](/CODE_OF_CONDUCT.md) while contributing and engaging in the discussions. 

**When contributing, please first discuss the change you wish to make via an issue on this repository before making the actual change**.


## 🐛 Bugs
If you are experiencing any bugs, don’t forget to open a [new issue](https://github.com/ZekeriyaAY/workflow-datetime/issues/new/choose).
