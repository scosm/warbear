
# Warbear: A Work Item Board for Teams of Multiple Users (Proof of Concept)

## Overview

This project is a proof of concept of a web app to manage a board of WorkItems for a team of users,
where a WorkItem is essentially a user's task of some kind, such as a piece of code to write.
The details of the work are specified in the "description" text field of the WorkItem.

("Wibjorn", or "Wiborn", means "war bear" and is of Scandinavian origin--and it begins with "WIB",
acronymizing "Work Item Board". Compare with "Jira", which is Japanese, shortened from "Gojira",
meaning "Godzilla", which is a humorous allusion to the Jira storage as a giant repository of bugs,
hence "Bugzilla". "Jira" is in effect just "Zilla". In our case, the engineers are at war with a giant "War Bear",
which is the app in all its resistiveness and ferocity. This is akin to referring to the (bug-ridden) source code
as "the Kraken", etc.)


The app is comprised of high-level components such as the following:

- A **backend** powered by FastAPI with Redis for data storage.
- A **frontend** built with React and Material UI for a responsive and user-friendly interface.
- Lightweight cross-cutting concerns such as logging and error handling.

## Application Features

At a high-level, eventually, the plans for the app's features include:

- User authentication via a login page.
- WorkItem creation, retrieval, updating, and deletion (CRUD).
- A REST API to the backend app, exposing app functionality to a frontend client.
- Frontend integration with backend APIs.

## Setup Instructions

The app and its dependencies have been built as a Docker image. It is not necessary
for the user to install packages or configure the local machine for this web app.
All that is needed is to run the Docker image as a Docker container.
At that point, there are endpoints available through two ports, exposed from the Docker image
out to the user's local machine. One port is for the web app as a whole,
while the other port is specifically for the backend app, providing the REST API
that implements the substantive functionality of the system.

Therefore, to run and experiment with this POC app, perform the following steps.

1. Download or copy the project's zip file, which contains the Docker image and the tree of source code and related files. Unpack this wherever is convenient for you. The Docker image and the source tree are at the same level in the overall project folder.

2. Open a command prompt. You will need to install Windows Subsystem for Linux 2 (WSL 2, or just WSL), but at present 
you do not need to install a Linux distribution, such as Ubuntu, Debian, etc.

3. You will also need to have Docker Desktop installed on your machine, which can be installed on Windows. 
But note that Docker runs on Linux but not Windows. 

...  

[MORE TO COME...]  

Build image, without caching, displaying output on separate lines, not rewriting one line (for debugging):  
docker build --no-cache --progress=plain -t warbear:0.1.beta .

Clearing mthe whoel cache fully:  
docker builder prune --all -f


