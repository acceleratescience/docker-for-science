# A Deeper Dive
In the `hello-world` example we were told to play around with something more ambitious. So let's do that...

## Ubuntu in a Container

```bash
docker run -it ubuntu bash
```

You should now see a new prompt that looks something like this:

```text
root@f4b5c7e4b6b4:/#
```

This prompt indicates that you are now inside a Docker container running a Ubuntu image. The `root@f4b5c7e4b6b4` part is the hostname of the container (yours may be different), and the `/#` part is the command prompt.

Here is an overview of the commands we used:

```bash
docker run   # Base command to create and start a new container
-i           # Interactive - keep STDIN open (allows you to type into container)
-t           # Allocate a pseudo-Terminal (gives you the shell prompt)
ubuntu       # The image to use (in this case, official Ubuntu image)
bash         # The command to run inside container (start a bash shell)
```

We can combine tags to make the command shorter: `-it` is the same as `-i -t`. Without `-it`:

- `-i` only: You can send input but display will be weird
- `-t` only: You get nice formatting but can't type input
- neither: Container runs the command and exits unless it has a foreground process

A "bash shell" is the command line interface (CLI). It so happens that if we run:

```bash
docker run -it ubuntu
```
we'll also get a bash shell anyway, because this is the default command for the Ubuntu image. However, you can also do:

```bash
docker run -it ubuntu sh
```

to get a simple shell instead of bash. You can also do

```bash
docker run -it ubuntu zsh
```
to get the interface that macOS uses. It is not available for this image, but you can install it in your own images. 

When we are inside the container, if we run:
    
```bash
cat /etc/os-release
```

You should see the following output:

```text
PRETTY_NAME="Ubuntu 24.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
```

confirming that you are indeed running a Ubuntu container. This container does not have any additional software installed, so you have a clean Ubuntu environment to work with. To exit the container, you can type `exit` and press `Enter`.

## What can we see?
Currently, in VS Code, we have a single terminal open. If we run
```bash
ps
```
We can see all processes inside our current terminal. It will probably read something like:
```bash
    PID TTY          TIME CMD
   1030 pts/0    00:00:00 bash
  34776 pts/0    00:00:00 ps
```

To see all processes, we can either run `htop` for an interactive view, or run
```bash
ps aux
```

The number in the left column `PID` is the Process ID, and everything that is running has a unique ID. To demonstrate, check out the script `continuous.py`. This script simply writes the date and iteration number to a log file. It will keep running until we terminate it.

To run it:
```bash
python continuous.py &
```

The `&` makes sure we are spat back out into the terminal. Now run
```bash
ps
```
and you should see something like
```bash
    PID TTY          TIME CMD
   1035 pts/0    00:00:00 bash
   1815 pts/0    00:00:00 python
   2065 pts/0    00:00:00 ps
```
If we run `ps aux` we can also find our process:
```bash
codespa+    1815  0.0  0.1  17172  9984 pts/0    S    15:47   0:00 python continuous.py
```
You should also see the log file getting written too. Notice that if we open up another terminal, we can no longer see this process running when we use `ps`, but we can see it when we run `ps aux`.

OK, now let's go back into our ubuntu container:
```bash
docker run -it ubuntu
```
Once again, we are back at our bash terminal. Now run the `ps` command.
```bash
root@b752bb229154:/# ps
    PID TTY          TIME CMD
      1 pts/0    00:00:00 bash
      9 pts/0    00:00:00 ps
```

Well OK, fine, but we're not in the same terminal, so of course we wouldn't see it. But now try running `ps aux`...
```bash
root@b752bb229154:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   4588  3840 pts/0    Ss   15:49   0:00 /bin/bash
root          10  0.0  0.0   7888  3968 pts/0    R+   15:52   0:00 ps aux
```

You find that you have access to no information about any processes running outside of your container. If you install and run `htop` you will find the same level of visibility.

Notice that if you run `lscpu` you can still see the system level resources, but it is possible to limit this aswell.

## Further reading
If you want a **real** deep dive into namespaces and cgroups, I strongly recommend you check out the brilliant video from Liz Rice, [Containers From Scratch](https://www.youtube.com/watch?v=8fi7uSYlOdc). There are three versions of this lecture, but they are all good.