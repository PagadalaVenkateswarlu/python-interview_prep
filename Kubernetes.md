1. Kubernetes — “Operating System for Containers”

    Kubernetes is a container orchestration platform used to deploy, scale, manage, heal, and monitor containerized applications automatically across multiple servers.

    Think of Kubernetes as:

        Docker runs one container
        Kubernetes manages thousands of containers across many machines

    It handles:

        Scheduling
        Scaling
        Load balancing
        Self-healing
        Rolling updates
        Service discovery
        High availability

    Real-World Analogy

        Imagine you own a food delivery company.

        Docker = one food truck
        Kubernetes = entire city-wide logistics system

    Kubernetes decides:
        Where trucks should go
        How many trucks are needed
        Replacing broken trucks
        Handling rush hour traffic
        Scaling during festivals

-----------------------------------------------------------------
Kubernetes Architecture (Tech Lead Level)
    1. Control Plane (Brain)

    API Server

        Main entry point.

        All commands go through API server:
            kubectl apply -f deployment.yaml

    Scheduler

        Decides:

            “Which node should run this pod?”

        Checks:

            CPU
            Memory
            Affinity
            Taints
            Resource limits
            Controller Manager

        Keeps desired state.

        Example:
            You want:

            replicas: 5

            If 2 pods crash:

                Controller creates 2 new pods automatically
    ETCD

        Distributed key-value database.

        Stores:
            Cluster state
            Secrets
            Configurations
            Pod metadata

        Critical component.
-------------------------------------------------------------------------
Kubernetes Pods are ephemeral by nature.

    That means a Pod can be created, deleted, replaced, or restarted at any time. When that happens, its IP address can change.

    So the problem is simple:

        How do other applications reliably communicate with a Pod if the Pod itself is temporary?

        That’s where Kubernetes Services come in.

        A Service provides a stable networking layer in front of Pods. Instead of connecting directly to a Pod IP, traffic goes through the Service, and Kubernetes routes it to the correct healthy Pods behind it.

    There are three common Service types:

    1. ClusterIP
        Used for internal communication inside the cluster.
        This is the default Service type.

    2. NodePort
        Exposes the Service on a port across every worker node.

        Useful for testing or learning, but generally not recommended for production because it exposes node-level ports directly and is harder to manage securely.

    3. LoadBalancer
        Creates an external load balancer through the cloud provider.
        This is commonly used in production when you need to expose an application to external users.

    In simple terms:

        Pods come and go.
        Services give them a stable address.

        That is one of the key reasons Kubernetes can handle scaling, self-healing, and rolling deployments without breaking communication between applications.

------------------------------------------------------------------------------------------------------------
When a Pod is created in Kubernetes, a lot happens behind the scenes across control plane and node components. Here’s a clean, step-by-step technical flow:

🚀 Step-by-Step Pod Creation Flow

    1. User submits Pod spec
    You run:

        kubectl apply -f pod.yaml

    The request goes to kube-apiserver

    2. API Server validates & stores
    Validates YAML (schema, auth, quotas)

    Stores Pod definition in etcd

    Pod is now in Pending state

    3. Scheduler assigns node
    kube-scheduler:

    Watches for unscheduled Pods

    Selects a suitable node based on:

    CPU/Memory availability

    Affinity/anti-affinity rules

    Taints & tolerations

    Updates Pod with nodeName

    4. Kubelet detects Pod assignment
    kubelet on the chosen node:

    Watches API Server

    Sees Pod assigned to its node

    Starts Pod creation process locally

    5. Pod networking setup
    Kubelet interacts with Container Network Interface (CNI)

    Tasks:

    Assign Pod IP

    Configure network namespace

    Connect Pod to cluster network

    6. Container runtime pulls images
    Kubelet calls container runtime like:

    containerd

    or CRI-O

    Steps:

    Pull image from registry (if not cached)

    Create container

    7. Pod sandbox (pause container) created
    A special “pause” container is created:

    Holds network namespace

    All containers share it

    8. Application containers start
    Containers defined in Pod spec are started

    Init containers (if any) run first

    Then main containers run

    9. Volume mounting
    Kubelet mounts volumes:

    emptyDir

    ConfigMaps

    Secrets

    PersistentVolumes

    10. Health checks begin
    Liveness & readiness probes start

    Determines:

    When container is healthy

    When it can receive traffic

    11. Pod status updated
    Kubelet updates status to API Server:

    Pending → Running

    Stored again in etcd

    12. Service discovery & traffic routing
    kube-proxy:

    Updates iptables/IPVS rules

    Pod becomes reachable via:

    Services (ClusterIP, NodePort, etc.)

    🧠 Visual Mental Model (Simplified Flow)
    kubectl → API Server → etcd
                    ↓
               Scheduler
                    ↓
                 Node
                    ↓
                Kubelet
          ↓        ↓        ↓
       CNI     Runtime    Volumes
          ↓
      Containers Start
          ↓
       Pod Running
    ⚡ Key Insights (Real-world understanding)
    Control Plane = decision-making

    Worker Node = execution

    API Server = central brain

    Kubelet = node-level executor

    CNI = networking backbone

    Runtime = container engine

    🔥 Pro Tip (Important for DevOps/Interviews)
    If something fails:

    Pod Pending → Scheduler issue

    ImagePullBackOff → Runtime/registry issue

    CrashLoopBackOff → App issue

    No network → CNI issue
-----------------------------------------------------------------------------
Kubernetes fundamental concepts every DevOps or cloud engineer should know

    1️⃣ Pod – The smallest unit in Kubernetes. A pod can contain one or more containers that share storage and networking

    2️⃣ Node – A worker machine (virtual or physical) where pods run, managed by the control plane

    3️⃣ Cluster – A group of nodes working together as a single Kubernetes system

    4️⃣ Deployment – Keeps your applications running in the desired state and handles rolling updates without downtime

    5️⃣ ReplicaSet – Ensures a fixed number of identical pods are always running

    6️⃣ Service – Provides stable networking and a consistent way to access a group of pods

    7️⃣ Ingress – Manages external HTTP and HTTPS traffic to services using routing rules

    8️⃣ ConfigMap – Stores non-sensitive configuration data separately from container images

    9️⃣ Secret – Stores sensitive data like passwords and tokens securely

    🔟 Namespace – Organizes and isolates resources within the cluster

    1️⃣1️⃣ Kubelet – An agent on each node that ensures containers are running as expected

    1️⃣2️⃣ kubectl – The command-line tool used to interact with Kubernetes clusters

    1️⃣3️⃣ Control plane – The core component that manages the overall cluster state

    1️⃣4️⃣ Scheduler – Decides which node a pod should run on based on resource availability

    1️⃣5️⃣ Controller manager – Runs background controllers to maintain the desired state

    1️⃣6️⃣ etcd – A distributed key-value store that holds all cluster data

    1️⃣7️⃣ Taints and tolerations – Control which pods can run on specific nodes

    1️⃣8️⃣ Labels and selectors – Help group and filter Kubernetes objects dynamically

    1️⃣9️⃣ Resource requests and limits – Define how much CPU and memory a container can request and use

    2️⃣0️⃣ Helm – A package manager used to deploy and manage applications easily

    2️⃣1️⃣ CRD (custom resource definition) – Allows you to define your own resource types

    2️⃣2️⃣ Operator – Automates complex application lifecycle management using CRDs

    2️⃣3️⃣ DaemonSet – Ensures a pod runs on every node or selected nodes

    2️⃣4️⃣ Logs and events – Essential for debugging and understanding what’s happening in the cluster

    Mastering these concepts gives you confidence to work with Kubernetes in real-world projects.

-------------------------------------------------------------------------------------------
What actually happens when you run kubectl apply.

Most engineers use this command 20 times a day. Very few know what it's actually doing behind the scenes.

Here's the real flow:

1. kubectl reads your YAML file and validates it client-side. Basic schema checks. No API calls yet.

2. kubectl sends the manifest to the kube-apiserver as an HTTP POST or PATCH request. This is where authentication happens. Your kubeconfig credentials get attached to the request.

3. The API server validates the request. Authentication first (who are you), then authorization (what can you do). RBAC rules check here. If you don't have permission, this is where it fails.

4. Admission controllers run. Mutating ones modify your request. Validating ones can reject it. This is where your policies (Kyverno, OPA, Pod Security) actually enforce.

5. The API server writes the desired state to etcd. This is the source of truth for your cluster.

6. Controllers (like the Deployment controller) watch etcd and notice the change. They start working to make actual state match desired state.

7. The scheduler assigns Pods to nodes if needed.

8. The kubelet on each node pulls the work assigned to it and tells the container runtime to actually create the containers.

The thing that blew my mind when I first understood this: kubectl apply doesn't create anything. It just tells the API server what you want. Everything else is asynchronous. That's why kubectl apply returns immediately but your pods might not be running for another 30 seconds.

Understanding this flow is what makes debugging "why isn't my thing running" faster. You can ask yourself: which step in this chain is failing?

-----------------------------------------------------------------------------------------------------------------------------
