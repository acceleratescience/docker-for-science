# Hello Docker!

To get us started let's run a simple Docker container. This is the `Hello World` of Docker.

In your codespace environment, you can essentially maximize the terminal by dragging it to the top of the screen. This will give you more space to work with.

In the terminal, run the following command:

```bash
docker run hello-world
```

You should then see something like the following:

```text
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete 
Digest: sha256:d211f485f2dd1dee407a80973c8f129f00d54604d2c90732e8e320e5038a0348
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
 ```

Let's have a look at each part in more detail:

```text
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete
Digest: sha256:d211f485f2dd1dee407a80973c8f129f00d54604d2c90732e8e320e5038a0348
Status: Downloaded newer image for hello-world:latest
```

This part of the output shows that Docker was unable to find the `hello-world` image locally, so it pulled it from the Docker Hub. The `hello-world` image is a very small image that is used to test that your Docker installation is working correctly.

`latest:` is a _**tag**_ for the image. Tags are used to identify different versions of an image. In this case, the `latest` tag is used to identify the latest version of the `hello-world` image.

`c1ec31eb5944: Pull complete` is the _**layer ID**_ of the image that was pulled. Docker images are made up of multiple layers, and each layer is identified by a unique ID. Since the `hello-world` image is very small, it only has one layer.

`Digest: sha256:d211f485...` is a unique hash of the image. This hash is used to uniquely identify the image and its contents.

If you try to run the `docker run hello-world` command again, you should just see the `Hello from Docker!` message without the other output. This is because Docker has already pulled the `hello-world` image and cached it locally.

The actual content of the container can be seen in the message displayed by the container.

It also gives us the following hint:

```text
To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash
```

Maybe we should try that...