# tutorial
> Do you even git bro?

Welcome to PiE's Git tutorial!
Today, we are going to learn how to use Git to start developing within PiE!
PiE's main active repos are:
* [PieCentral](https://github.com/pioneers/PieCentral) - Contains DevOps, Shepherd, Dawn, Hibike, and Runtime
* [PiElectrical](https://github.com/pioneers/PiElectrical) - Contains PiESens and PDB boards and documentation

## Setup
Git is industry-standard version control software.
It allows developers to save their work and collaborate on many features simultaneously with minimal complexity.
You should sign up for an [account](https://github.com/join), then ask a PiE staff member to be invited to the @pioneers organization.

Github, like GitLab and Bitbucket, are private companies that host developers's Git repos online.
PiE uses GitHub to host all of its software.

First, open up a terminal, then run:
```sh
$ git clone https://github.com/pioneers/tutorial.git
```

This downloads the `tutorial` repo (project) locally on your machine in a folder called `tutorial`.
Your machine will always store its own version of the code, and Github will also stores a separate version of the code on a remote server.
These could be the same version, if everything is up-to-date.
To navigate into your newly downloaded repo, run:
```sh
$ cd tutorial
```

## Creating a branch
Git repos also support another nifty feature called branches.
A branch is .
In PiE, everyone will develop features on their own branches and eventually merge these branches back together with a `master` branch.
As the name suggests, `master` is the main "authoritative" branch that contains the most recent stable code.

```sh
$ git checkout -b tutorial/YourName  # (Replace YourName with your name, so e.g. `git checkout -b tutorial/vivien`
```

You have now created a new branch, named whatever you named it.
We are ready now to make changes.

## Making and committing changes
Now lets actually make a change!
This might be making a bugfix or adding a feature.
Today, we are going to simply edit a text file.
Go ahead and open up `yourName.txt` with your favorite text editor and delete the lines and type in your name.
Save this file, and go back to your terminal window.
Now we have to tell Git that we've made a change.
The process always goes:
```sh
$ git add yourName.txt  # "Stage" new or modified files
$ git commit -m "Changed yourName.txt to include my name"  # Use a descriptive message
```

This stages the file you just changed, and then creates a snapshot of your repo at that point in time.
These messages are very important for other people, and future you, to understand what exactly you changed.
Another useful command is `git status`, which you can type at any time to check the current status of the repo: which files have been modified but have yet to be added, and which files have been added but have yet to be committed.

## Push code online
```sh
$ git push origin tutorial/YourName  # Replace YourName with what you typed earlier when you created the branch
```

## Pull Request and Code Review
Navigate to the tutorial repo.
On the top left side of the screen, where it says `branch:master`, click the dropdown and select your branch.
Click the Pull Request button that just appeared in the gray bar on the right side.
Fill out the title with `[TUTORIAL] Update Name`, or some other useful title
Write in a useful description.
Click on Reviewers, and add a reviewer. This person will look at your change, and either approve it or request changes.
Click the green "Create Pull Request" button.

## Merge Conflict
Run this command to
```sh
$ git pull origin master
```

You may get an error message about a merge conflict.
The issue is that you and someone else have edited the same file in two separate branches.

Open up the text file and edit it to reconcile the concurrent edits.
Then, save with:
```
$ git add yourName.txt
$ git commit -m "[TUTORIAL] Fix merge conflict to include both names"`
$ git push origin tutorial/YourName
```

Check GitHub; you should now be able to merge once someone approves your pull request.
