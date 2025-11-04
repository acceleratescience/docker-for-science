# More Commands
After looking at how to run containers interactively, let's look at some other images, and play around with some other commands.

## Python in a Container
Let's grab a python container:

```bash
docker run -it python bash
```

We are now inside a docker container with python, and we can run python commands:

```bash
python --version
Python 3.13.0
```

We can also run python and play around with it:

```bash
python
```
    
```python
>>> print("Hello, Docker!")
Hello, Docker!
>>> exit()
```

You can directly access the Python REPL while running the container:

```bash
docker run -it python python
```

If you exit the REPL in the usual way, then you will also exit the container.

## Seeing the Containers and Images
In order to see a list of images that we have pulled, we can run:
   
```bash
docker images
```
and the output should be something like:
```text
REPOSITORY    TAG                  IMAGE ID       CREATED         SIZE
python        latest               c41ea8273365   4 weeks ago     1.02GB
python        3.12-slim-bookworm   668757ec60ef   4 weeks ago     124MB
ubuntu        latest               fec8bfd95b54   5 weeks ago     78.1MB
hello-world   latest               d2c94e258dcb   18 months ago   13.3kB
```

To see a list of all containers, we run:
```bash
docker ps -a
```

You should see something like this:
```text
CONTAINER ID   IMAGE                       COMMAND    CREATED          STATUS                        PORTS     NAMES
5cb8b1bbe52f   ubuntu                      "bash"     13 minutes ago   Exited (127) 13 minutes ago             wizardly_cartwright
80040792ac55   python:3.12-slim-bookworm   "bash"     14 minutes ago   Exited (0) 13 minutes ago               heuristic_kilby
42129b1076cd   python                      "python"   28 minutes ago   Exited (0) 20 minutes ago               peaceful_raman
112c227987a6   python                      "zsh"      28 minutes ago   Created                                 confident_lalande
724386298bc2   python                      "sh"       28 minutes ago   Exited (0) 28 minutes ago               nervous_brahmagupta
4e490eb53aaf   python                      "bash"     34 minutes ago   Exited (0) 28 minutes ago               quirky_bohr
21eea7f7d3b4   ubuntu                      "bash"     35 minutes ago   Exited (0) 34 minutes ago               admiring_payne
19379f07e484   hello-world                 "/hello"   35 minutes ago   Exited (0) 35 minutes ago               adoring_keller
```

note the colourful names...

We can remove containers with:

```bash
docker rm <container_id>
```
and all unused containers with:

```bash
docker container prune
```

Remove all images with:
   
```bash
docker rmi -f $(docker images -aq)
```

Now if you run `docker ps -a` you should see an empty list.

## Naming containers
You might have noticed that the containers have random names, and that if you want to stop them, you have to use the ID, which is cumbersome. So instead, you can name the container when you run it:

```bash
docker run -it --name mycontainer -it python bash
```

Now I can remove the container with:

```bash
docker rm mycontainer
```

## Preserving information
Let's run the python container again

```bash
docker run -it python bash
```

and try to create a directory:

```bash
cd home
mkdir mydir
```

If you run `ls` you should see the `mydir` directory. Now see what happens when you close down the container and start it again:

```bash
docker run -it python bash
cd home
ls
```

There is nothing there! What is going on? First we need to see exactly why this is happening. Run the `docker ps -a` command, and you should see the following:
```test
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS                      PORTS     NAMES
0b89d0ef62fa   python    "bash"    17 seconds ago   Exited (0) 4 seconds ago              vigorous_gould
90ff3f1f1085   python    "bash"    34 seconds ago   Exited (0) 25 seconds ago             distracted_bohr
```

So we have actually created two containers, and we are not using the same one. This is because when we run the `docker run` command, we are creating a new container each time. This is why the changes we made in the first container are not present in the second container.

So instead I can restart my previous container and attach to it:

```bash
docker start -ai distracted_bohr
```

Now when I change into the `home` directory and run `ls`, I should see the `mydir` directory. The above command is saying "start the container `distracted_bohr` and attach to it interactively".

Generally speaking, we **do not** want to store data in a container. This includes creating files, directories, and databases. If we store files inside the container, they will be lost when the container is stopped or removed:

1. **Persistence Beyond the Lifecycle of the Container**
Containers are ephemeral by design. If you need to update or recreate a container (e.g., pulling a new image), the data stored directly in the container is lost unless explicitly backed up. Mounted volumes persist independently of the container lifecycle, ensuring your data is safe even if the container is removed.

2. **Ease of Data Sharing**
Mounted volumes allow data to be shared between multiple containers. For example, if you have one container for a database and another for a web application, both can share a mounted volume for logs or configurations.

3. **Integration with Host Filesystem**
With a mounted volume, you can directly edit files from your host system (e.g., code tracked in Git), and changes will be reflected in the container in real-time. This makes development workflows more efficient and eliminates the need for repeated docker cp commands.

4. **Simplified Version Control with Git**
If you're using Git, you likely want your working directory (e.g., /app in the container) to correspond to your Git repository on the host. Mounting the directory ensures that any changes made in the container are tracked by Git on the host, simplifying version control and collaboration.

5. **Backup and Portability**
Mounted volumes are easier to back up and migrate. You can copy a directory from your host system for safekeeping or move it to another machine. Data stored inside a container is harder to extract and manage outside of Docker.

6. **Security and Isolation**
Using mounted volumes can help isolate the container's internal state from persistent data. This separation reduces the risk of accidental data loss due to container mismanagement.

This is why containers are often used for running stateless applications that do not need to store data between runs. So how can we store data in a container? We can use _**volumes**_.