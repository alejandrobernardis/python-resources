# Containers

## Wikipedia says...

> OS-level virtualization refers to an operating system paradigm in which the kernel allows the existence of multiple isolated user space instances. Such instances, called containers (Solaris, Docker), Zones (Solaris), virtual private servers (OpenVZ), partitions, virtual environments (VEs), virtual kernel (DragonFly BSD) or jails (FreeBSD jail or chroot jail), may look like real computers from the point of view of programs running in them. A computer program running on an ordinary operating system can see all resources (connected devices, files and folders, network shares, CPU power, quantifiable hardware capabilities) of that computer. However, programs running inside of a container can only see the container's contents and devices assigned to the container.
>
> ...

Read more https://en.wikipedia.org/wiki/OS-level_virtualization

## Virtual machine

> In computing, a virtual machine (VM) is an emulation of a computer system. Virtual machines are based on computer architectures and provide functionality of a physical computer. Their implementations may involve specialized hardware, software, or a combination.
>
> ...

Read more https://en.wikipedia.org/wiki/Virtual_machine

### Software

* VirtualBox https://www.virtualbox.org
* VM Ware Workstation Player https://www.vmware.com/products/workstation-player.html

## Docker

https://www.docker.com/

> Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. All containers are run by a single operating-system kernel and are thus more lightweight than virtual machines.
>
> ...

Read more https://en.wikipedia.org/wiki/Docker_(software)

### Hub

https://hub.docker.com

Docker Hub is a service provided by Docker for finding and sharing container images with your team. It provides the following major features:

* **Repositories:** Push and pull container images.
* **Teams & Organizations:** Manage access to private repositories of container images.
* **Official Images:** Pull and use high-quality container images provided by Docker.
* **Publisher Images:** Pull and use high-quality container images provided by external vendors. Certified images also include support and guarantee compatibility with Docker Enterprise.
* **Builds:** Automatically build container images from GitHub and Bitbucket and push them to Docker Hub.
* **Webhooks:** Trigger actions after a successful push to a repository to integrate Docker Hub with other services.

[read more][1]

### Swarm

https://docs.docker.com/swarm/

Docker Swarm is native clustering for Docker. It turns a pool of Docker hosts into a single, virtual Docker host. Because Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts. Supported tools include, but are not limited to, the following:

* Dokku
* Docker Compose
* Docker Machine
* Jenkins

[read more][5]

### Docker Compose

https://docs.docker.com/compose

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about all the features of Compose, see [the list of features][4].... [read more][2]

### Registry

https://docs.docker.com/registry

The Registry is a stateless, highly scalable server side application that stores and lets you distribute Docker images. The Registry is open-source, under the permissive Apache license... [read more][3]

[1]: https://docs.docker.com/docker-hub/
[2]: https://docs.docker.com/compose
[3]: https://docs.docker.com/registry
[4]: https://docs.docker.com/compose/#features
[5]: https://docs.docker.com/swarm/overview/

## Links

* DevOps https://en.wikipedia.org/wiki/DevOps
