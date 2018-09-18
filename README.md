# tutorial
Do you even git bro

Welcome to PiE's git tutorial! Today we are going to learn hands-on how to use git, enough to start developing within PiE! PiE's main repo is hosted at https://github.com/pioneers/PieCentral

## Setup your local repo

Git is the industry standard version control software. It allows developers to save and collobrate their work.

Github, and other websites such as gitlab and bitbucket, is a private comapany that hosts developers's git repos online. PiE uses github to host all of its software.

The first command we are going to run is

`git clone https://github.com/pioneers/tutorial.git` (Go ahead and copy and paste this into your terminal)

This creates a copy of this repo (project) onto your local machine. Your local machine will always store its own version of the code, and Github will also stores a seperate version of the code (these could be the same version, if everything is up to date). Compare it to you having two copies of the a folder on your desktop. Now type 

`cd tutorial`

in order to navigate into your newly copied repo (its really just a special folder)

## Creating a branch

Git repos also support another nifty feature, called branches. A branch is [what is a branch]. In PiE, everyone will develop on their own branches and eventually merge these branches back together with master. Master is simple the name of our main branch, which contains the most stable up-to-date code. 

`git checkout -b gittutorial/YourName` (Replace YourName with your name, so e.g. `git checkout -b gittutorial/Vivien`

You have now created a new branch, named whatever you named it. We are ready now to make changes~

## Making and committing changes

Now lets actually make a change! This might be making a bugfix or adding a feacture, or updating some text file. Today, we are going to simply edit a text file. Go ahead and open up yourName.txt with your favorite text editor and delete the lines and type in your name. Save this file, and go back to your terminal window. Now we have to tell git that we've made a change. The process always goes:

`git add yourName.txt`
`git commit -m "[TUTORIAL] Change yourName.txt to include my name"`

This adds the file you just changed, and then commits it with a message. These messages are very important for other people, and future you, to understand what exactly you changed. Another useful command is `git status` which you can type at any time to check the current status: which files have yet to be added and which files have yet to be committed. 

## Push code online

`git push origin gittutorial/YourName` (Replace YourName with what you typed earlier when you created the branch)


## Pull Request and Code Review

Navigate to github.com/pioneers/tutorial
On the top left side of the screen, where it says Branch:master, click the dropdown and select your branch.
Click the Pull Request button that just appeared in the gray bar on the right side.
Fill out the title with [TUTORIAL] Update Name, or some other useful title
Write in a useful description
Click on Reviewers, and add [REVIEWER]. This person will look at your change, and either approve it or request changes.
Click the green "Create Pull Request" button.



## Merge Conflict

Oh no it says unable to merge. What do we do?

`git pull origin master`
MERGE CONFLICT

Open up the textfile, make it so its the two names with the word and between them. Save
`git add yourName.txt`
`git commit -m "[TUTORIAL] Fix merge conflict to include both names"`
`git push origin gittutorial/YourName`

Check github, should now be able to merge once someone approves your pull request.
