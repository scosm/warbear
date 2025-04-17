# warbear
Beginnings of a proof of concept web app, which kis designed to run in Docker, to manage work items (tasks) for multiple users.
Implemented with: Python 3, FastAPI, Redis, React, TypeScriptm (JS for now, but TS coming imminently), MaterialUI, CSS, and Docker.

To run the web app from the Docker container, do the following:

docker run -d -p 8000:8000 -p 3000:3000 warbear:0.1.beta

You can confirm that the container is running using the ps command: docker ps

Given that the container is indeed running, then launch the web app in your local browser by navigating to the address,
with the mapped port number for the frontend (3000):

http://localhost:3000

This will exhibit the current landing page of the web app. At present, the UI HTML pages still need a lot of work, so the landing page is not what
makes the most sense at present. But the existing page and its code show the architecture, so that it is clear what is necessary to be done
to flesh out the rest of the web app.

To stop the container, you sijmply say:

docker stop warbear:0.1.beta

(or whatever name and tag that you gave to the container when you launched it at the beginning).

Next, the backend is accessible through port 8000. So, the REST API can be tested by using an API tool,
such as Postman or SwaggerUI, and providing a URL to an API method with a format such as the following:

http://localhost:8000/v0.1/api/my_favorite_method_01

And the output of the method
will be available in the payload of the JSON data that is passed back to the caller.

Obviously, more documentation is needed, to explicate the semantics of each API method.

