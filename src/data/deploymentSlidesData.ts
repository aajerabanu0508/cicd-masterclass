import { MasterSlide } from './slidesData';

export const DEPLOYMENT_SLIDES_DATA: MasterSlide[] = [
  {
    num: 1,
    title: "Software Deployment: The Critical Final Mile",
    subtitle: "How Code Transitions from Developer Machines into Live User-Facing Production",
    category: "Deployment Foundations",
    image: "/slides/deployment/slide_1.png",
    imageCaption: "Deployment Journey: Source Code -> Immutable Container -> Staging -> Health Gates -> Live Traffic.",
    contentPoints: [
      "Software deployment is the operational phase of moving tested code artifacts into live server infrastructure.",
      "Spans environment provisioning, artifact transfer, runtime configuration, database migrations, and load balancer traffic routing.",
      "Vital Distinction: 'Deployment' is installing software onto servers; 'Release' is turning features on for customers.",
      "The Modern Gold Standard: 100% Zero-downtime, fully automated, version-controlled, and instantly reversible."
    ],
    detailedPoints: [
      "The Final Mile of Engineering: Writing clean code is only half the battle; how you deliver it to production determines system stability and customer trust.",
      "Artifact Lifecycle: Compiling code into immutable, versioned artifacts (Docker images, tarballs, or serverless bundles) tagged with Git commit SHA.",
      "Environment Spectrum: Code progresses through isolated stages: Local Dev -> CI Test Runner -> Staging/UAT -> Canary -> Production.",
      "DORA Research: Elite organizations deploy on-demand multiple times per day with lead times under one hour and change failure rates below 5%."
    ],
    foodAnalogy: {
      "title": "Kitchen Preparation vs. Table Serving 🍽️",
      "story": "Cooking the dish in the kitchen represents building and testing the code. Boxing it up into a sealed container is artifact packaging. The waiter bringing the dish out to the pass is deployment. Lifting the cloche lid so the diner can take a bite is the release!",
      "connection": "Just as a restaurant never serves unfinished food directly from the pan, engineering teams should never deploy untested raw code directly to live production servers."
    },
    keyTakeaway: "Deployment is the single highest-risk event in software engineering — mastering automation eliminates release anxiety."
  },
  {
    num: 2,
    title: "Manual EC2 Deployment: The 'Push & SSH' Routine",
    subtitle: "Git Push ➔ SSH into EC2 ➔ Install Packages ➔ Git Pull ➔ Nano .env ➔ Build & PM2 Restart",
    category: "Manual Process",
    image: "/slides/deployment/slide_2.png",
    imageCaption: "Manual EC2 Workflow: Push to GitHub ➔ SSH into AWS EC2 ➔ apt install tools ➔ git pull ➔ nano .env ➔ build on server ➔ restart PM2.",
    contentPoints: [
      "The most common manual deployment pattern: push code to GitHub, then manually SSH into an AWS EC2 instance.",
      "Engineers log in using private key pairs: ssh -i key.pem ubuntu@ec2-ip, then manually install Git, Node.js, and Nginx.",
      "Code is pulled directly onto the live server via git pull origin main, followed by manual nano .env editing.",
      "The application is built directly on the production server (npm run build) and restarted using PM2 or systemd."
    ],
    detailedPoints: [
      "Step 1 & 2 (Push & SSH): Developer pushes commits to GitHub (git push origin main) and opens a live terminal to SSH into EC2: ssh -i my-key.pem ubuntu@54.210.xx.xx.",
      "Step 3 & 4 (Install Tools & Git Pull): Running sudo apt update && sudo apt install -y git nodejs npm, then cd /home/ubuntu/app && git pull origin main on the live box.",
      "Step 5 & 6 (Nano .env & Server Build): Manually creating or editing .env secrets using nano, then running npm install && npm run build directly on the EC2 instance.",
      "Step 7 & 8 (PM2 Restart & Nginx Proxy): Starting or restarting process via pm2 restart app, configuring Nginx reverse proxy to port 3000, and manually checking in browser."
    ],
    problemsList: [
      "Requires manually SSHing into production with sensitive .pem private keys",
      "Building on EC2 (npm run build) causes 100% CPU spikes and OOM crashes on t2/t3.micro instances",
      "Impossible to scale: SSHing and pulling code across 10 or 20 auto-scaled EC2 instances is unmanageable",
      "Git merge conflicts or failed npm installs leave live production in a broken, half-deployed state",
      "Plaintext secrets stored directly in .env files on the EC2 file system"
    ],
    foodAnalogy: {
      "title": "Cooking Directly on the Customer's Table 🍳",
      "story": "Imagine a chef carrying raw ingredients into the restaurant dining room, setting up a portable stove right on the customer's table, chopping vegetables, and frying food while customers are trying to eat.",
      "connection": "Running git pull, npm install, and npm run build directly on a live production EC2 instance creates smoke, resource contention, and downtime right in front of your live users."
    },
    keyTakeaway: "Deploying by SSHing into EC2 and running git pull works for a single hobby server, but collapses the moment you scale to real production traffic."
  },
  {
    num: 3,
    title: "Why Manual EC2 Deployments Fail at Scale",
    subtitle: "OOM Build Crashes, Multi-Instance Bottlenecks, Secret Leaks, and Rollback Nightmares",
    category: "Failure Analysis",
    image: "/slides/deployment/slide_3.png",
    imageCaption: "The 4 Failure Pillars of Manual EC2 Delivery: OOM Server Freezes, Multi-Server Drag, SSH Key Leaks, and Rollback Paralysis.",
    contentPoints: [
      "OOM Crashes During Build: npm run build directly on EC2 consumes all RAM, freezing the server and dropping active user traffic.",
      "Multi-Instance Scaling Trap: When traffic grows and you add 5 EC2 instances behind an AWS ALB, you must SSH into all 5 servers individually.",
      "SSH Key & Credential Leaks: .pem private keys stored on developer laptops and plain text database credentials in EC2 .env files.",
      "Rollback Paralysis: If a bug is deployed, you must SSH back in and run git checkout <old-commit> manually while the site is down."
    ],
    detailedPoints: [
      "The Out-Of-Memory (OOM) Killer: Running Webpack / Vite / Next.js builds on an EC2 t2.micro (1GB RAM) triggers the Linux OOM killer, terminating both the build and the running web server.",
      "The Multi-Server Nightmare: Modern cloud architectures use AWS Auto Scaling Groups. You cannot SSH into dynamic EC2 instances that spin up and down automatically.",
      "Security Vulnerabilities: Shared root or ubuntu SSH keys without audit logs; if a developer leaves the company, private keys must be manually rotated across all servers.",
      "Zero Automated Rollback: If git pull introduces a syntax error, your production service crashes immediately. There is no instant 1-second traffic reversal."
    ],
    foodAnalogy: {
      "title": "The One-by-One Table Delivery 🛵",
      "story": "A restaurant gets 100 orders during lunch rush. Instead of an automated dispatch line, one manager runs out to each delivery bike individually, hand-typing addresses into a GPS, and fixing broken bike chains on the sidewalk.",
      "connection": "Manual SSH deployments force engineers to babysit servers one-by-one instead of leveraging automated container pipelines."
    },
    keyTakeaway: "Never build code on production servers — build immutable containers in CI, test them, and deploy pre-built artifacts."
  },
  {
    num: 4,
    title: "Automated Deployment Pipeline: Declarative & Repeatable",
    subtitle: "Transforming Fragile Manual Steps into Repeatable, Version-Controlled Automation",
    category: "CI/CD Automation",
    image: "/slides/deployment/slide_4.png",
    imageCaption: "Modern CI/CD Flow: Trigger -> Automated Tests -> Docker Build -> Staging Verification -> Zero-Downtime Prod.",
    contentPoints: [
      "Git Webhook Trigger: Code commit to `main` branch or release tag triggers automated CI/CD execution.",
      "Automated Test Gate: Unit, integration, and security scans run in isolated runner environments.",
      "Immutable Containerization: Application packaged into Docker image tagged with Git commit SHA-256.",
      "Continuous Delivery vs Deployment: CDel keeps software continuously deployable; CDep ships automatically to prod."
    ],
    detailedPoints: [
      "Declarative Pipeline-as-Code: Pipelines are defined in version-controlled YAML files (e.g. `.github/workflows/deploy.yml`), reviewed via pull requests.",
      "Automated Security Gates: Static Application Security Testing (SAST) and container vulnerability scans (Trivy/Snyk) block insecure code before deployment.",
      "Hermetic Build Runners: Builds execute in fresh, sterile virtual environments or Docker containers, eliminating host configuration drift completely.",
      "Continuous Delivery vs Continuous Deployment: Delivery requires an explicit business approval gate; Deployment pushes every green build straight to production."
    ],
    foodAnalogy: {
      "title": "The Automated Food Packaging Line 🏭",
      "story": "In a modern food plant, raw ingredients are mixed by precision robotic machines, weighed, temperature-checked, vacuum-sealed into sterile containers, and labeled with batch numbers without a human touching the food.",
      "connection": "Automated deployment pipelines package and verify software with identical robotic precision on every single commit."
    },
    keyTakeaway: "Automated pipelines turn deployments into boring, predictable, everyday non-events."
  },
  {
    num: 5,
    title: "Zero-Downtime Strategies: Rolling vs. Blue-Green",
    subtitle: "Updating Production Services Without Dropping a Single Live User Request",
    category: "Deployment Patterns",
    image: "/slides/deployment/slide_5.png",
    imageCaption: "Rolling (Incremental capacity upgrade) vs. Blue-Green (Complete isolated environment flip).",
    contentPoints: [
      "Rolling Deployment: Updates instances gradually (e.g. 25% at a time) behind load balancer without doubling hardware costs.",
      "Connection Draining: Old instances finish active HTTP requests while new instances pass readiness health probes.",
      "Blue-Green Deployment: Two identical environments; Blue runs live v1.0, Green deploys v2.0 in complete isolation.",
      "1-Second Rollback: Router flips 100% traffic instantly to Green; if errors spike, flips back to Blue with zero data loss."
    ],
    detailedPoints: [
      "Rolling Deployment Mechanics: In Kubernetes or AWS ECS, new pods are spun up. As soon as a new pod passes readiness checks, one old pod is gracefully drained and terminated.",
      "Rolling Considerations: Cost-effective because compute capacity stays stable. However, the system runs both v1 and v2 simultaneously during rollout, requiring backward-compatible APIs.",
      "Blue-Green Mechanics: Environment Green is spun up with v2.0. Full automated smoke testing runs against Green. The router or DNS switches traffic 100% to Green.",
      "Instant Blue-Green Rollback: If Prometheus detects elevated HTTP 500 error rates on Green, the router points back to Blue in less than 2 seconds."
    ],
    foodAnalogy: {
      "title": "The Twin Dining Rooms 🚪",
      "story": "Instead of repainting a restaurant while customers are sitting at the tables (downtime/fumes), the owner sets up a pristine, fully decorated second dining room next door. When it is 100% ready, the host simply guides incoming guests into the new room.",
      "connection": "Blue-Green deployment ensures customers never experience construction, downtime, or incomplete features."
    },
    keyTakeaway: "Zero-downtime releases eliminate weekend maintenance — teams comfortably deploy during normal office hours."
  },
  {
    num: 6,
    title: "Progressive Delivery: Canary Releases & Feature Flags",
    subtitle: "Safely Exposing New Code to Real Production Traffic in Increments",
    category: "Traffic Shifting",
    image: "/slides/deployment/slide_6.png",
    imageCaption: "Canary Traffic Slicing (2% -> 25% -> 100%) and Feature Flag Dark Launching Architecture.",
    contentPoints: [
      "Canary Releases: Route 2% to 5% of real user traffic to new canary instance while 95% remains on rock-solid stable version.",
      "Automated Telemetry: APM monitors HTTP 500 error rates, p99 latency, and CPU metrics before stepping traffic up.",
      "Auto-Drain: If error rate spikes, canary traffic drops to 0% in seconds, protecting 98% of users from experiencing bugs.",
      "Feature Flags: Decouple deployment from release; deploy code dark and toggle features via runtime boolean switches."
    ],
    detailedPoints: [
      "Origin of Canary: Coal miners carried a caged canary down into mines; if toxic gas accumulated, the sensitive bird alerted miners before human harm occurred.",
      "Canary Pipeline Mechanics: Service mesh (Istio, Envoy, AWS App Mesh) routes 2% of incoming production requests to the canary pod.",
      "Automated Metric Evaluation: Prometheus / Datadog checks: if error rate < 0.1% and p99 latency < 250ms for 10 minutes, traffic increases to 25%, 50%, then 100%.",
      "Feature Flag Decoupling: Code is merged and deployed dormant (`if (flags.isEnabled('checkout_v2', user))`). Features are enabled for internal staff first, then beta users, without redeploying code."
    ],
    foodAnalogy: {
      "title": "The Food Tasting Sample 🧁",
      "story": "Before replacing a signature chocolate cake on the menu, the pastry chef offers small complimentary sample bites to five curious diners to observe their reaction. If they love it, it goes on the menu; if not, the chef tweaks the recipe.",
      "connection": "Canary releases test new code against real production users with minimal blast radius and zero risk to the overall business."
    },
    keyTakeaway: "Progressive delivery shifts testing into production safely, reducing blast radius to near zero."
  },
  {
    num: 7,
    title: "Containerized & Cloud-Native Deployment",
    subtitle: "Immutable Infrastructure: Replacing Fragile Servers with Ephemeral Containers",
    category: "Cloud & Containers",
    image: "/slides/deployment/slide_7.png",
    imageCaption: "The 3 Pillars: Immutable Docker Images, Kubernetes Orchestration, and Serverless Edge Delivery.",
    contentPoints: [
      "Immutable Infrastructure: Never patch live servers in place; build a new Docker image and replace containers entirely.",
      "Secure Container Registries: AWS ECR, Docker Hub, and GitHub Packages store signed, vulnerability-scanned images.",
      "Kubernetes Orchestration: Declarative YAML manifests, self-healing pod restarts, and horizontal auto-scaling.",
      "Serverless & Edge Platforms: AWS Lambda, Vercel, and Cloudflare Workers offer atomic deploys with zero server maintenance."
    ],
    detailedPoints: [
      "Pets vs. Cattle Analogy: Traditional servers were treated like pets (given unique names, lovingly patched by hand). Containers are cattle (ephemeral, disposable, and easily replaced).",
      "Container Registry Security: Images are signed with cosign / Docker Content Trust and checked for CVE vulnerabilities before being admitted into production clusters.",
      "Kubernetes Deployment Manifests: Specifying replica count, resource limits (CPU/Memory), readiness probes, and rolling update strategy in Git-versioned YAML.",
      "Serverless & Edge Deployments: Code executes on distributed edge networks with automated scaling from 0 to 100,000 requests and instant URL previews."
    ],
    foodAnalogy: {
      "title": "Standardized Shipping Containers 🚢",
      "story": "Before shipping containers, loose cargo was loaded onto ships by hand, leading to damage, theft, and delays. Standard steel shipping containers revolutionized global trade because any crane, ship, or truck in the world can handle them identically.",
      "connection": "Docker containers provide the exact same standardization for software: run identically on a laptop, staging cluster, or global cloud."
    },
    keyTakeaway: "Containers guarantee environment parity: the exact image tested in staging executes identically in production."
  },
  {
    num: 8,
    title: "GitOps: Git as the Single Source of Truth",
    subtitle: "Declarative Cloud Delivery, Automated Drift Detection, and Self-Healing Infrastructure",
    category: "GitOps Engine",
    image: "/slides/deployment/slide_8.png",
    imageCaption: "Traditional Push vs. Modern In-Cluster GitOps Pull Model with Continuous Drift Reconciliation.",
    contentPoints: [
      "Traditional CI Push Model: CI server holds cluster credentials and runs `kubectl apply`—a security risk if compromised.",
      "GitOps Pull Model (ArgoCD / Flux): In-cluster operator pulls changes from Git without exposing cluster credentials.",
      "Automated Drift Healing: If someone manually alters a pod via `kubectl`, ArgoCD immediately reconciles it back to Git state.",
      "Instant 1-Click Rollback: Running `git revert <commit>` auto-reconciles production cloud clusters across all regions."
    ],
    detailedPoints: [
      "Declarative Everything: Infrastructure and application topology are declared as code in Git (Kubernetes YAML, Helm Charts, Kustomize).",
      "The Security Advantage of Pull: The CI runner never needs write credentials or cluster admin tokens. The cluster pulls down its own changes securely.",
      "Continuous Reconciliation Loop: The GitOps agent compares Git's 'Desired State' against the cluster's 'Actual State' every 30 seconds.",
      "Eliminating Configuration Drift: If an engineer tries to manually hotfix a pod using `kubectl edit`, ArgoCD flags the drift and automatically overwrites it back to the Git source."
    ],
    foodAnalogy: {
      "title": "The Master Recipe Ledger 📖",
      "story": "In a five-star restaurant chain, the master recipe book in the head office is the single source of truth. Every kitchen station is continuously audited against it. Any unapproved spice added by an adventurous line cook is immediately replaced with the authentic recipe.",
      "connection": "GitOps ensures that what is in your Git repository is always 100% identical to what is executing in production."
    },
    keyTakeaway: "Deploying to production cloud with GitOps is as safe, reviewed, and auditable as approving a Git Pull Request."
  },
  {
    num: 9,
    title: "Database Migrations, Secrets & Health Verification",
    subtitle: "Solving the Toughest Challenges in Automated Zero-Downtime Deployment",
    category: "Zero-Downtime Data",
    image: "/slides/deployment/slide_9.png",
    imageCaption: "Expand-and-Contract Zero-Downtime Database Pattern & Health Probe Rollback Triggers.",
    contentPoints: [
      "Expand-and-Contract Pattern: Add nullable column -> deploy code reading both -> backfill data -> drop old column.",
      "Secrets Externalization: Never store credentials in Git; inject at runtime via HashiCorp Vault, AWS Secrets Manager, or OIDC.",
      "Liveness vs Readiness Probes: Liveness restarts crashed processes; Readiness checks DB connectivity before routing traffic.",
      "Automated Rollback Triggers: If HTTP 5xx errors exceed 1% for 60 seconds, pipeline auto-rolls back without human delay."
    ],
    detailedPoints: [
      "The Database Dilemma: Code can be rolled back in seconds, but databases cannot lose live customer transactions. Schema changes must always be backward and forward compatible.",
      "Expand-and-Contract Phasing: Never rename a column in one step. Add the new column (Expand), deploy application code writing to both, backfill legacy rows, switch readers to new column, then drop old column (Contract).",
      "Zero Secrets in Repositories: Avoid storing passwords in Git. Use short-lived cloud IAM tokens via OpenID Connect (OIDC) between GitHub Actions and AWS/GCP.",
      "Health Probes in Production: Readiness probes prevent traffic from hitting containers while connection pools are initializing or caches are warming up."
    ],
    foodAnalogy: {
      "title": "The Dual-Tank Water Filter 💧",
      "story": "To clean a municipal water filtration system without shutting off city water, engineers run water through Tank A while inspecting Tank B, then gently open valves to Tank B before closing Tank A. Clean water never stops flowing.",
      "connection": "Zero-downtime database patterns keep live customer data flowing smoothly while underlying schemas evolve."
    },
    keyTakeaway: "Production safety requires decoupled databases, externalized secrets, and automated health checks."
  },
  {
    num: 10,
    title: "Manual vs. Automated Deployment: The Master Comparison",
    subtitle: "Metrics, Cultural Transformation, and Golden Rules for Production Excellence",
    category: "Master Comparison",
    image: "/slides/deployment/slide_10.png",
    imageCaption: "8-Dimension Comparison Matrix: Manual Delivery Breakdown vs. Modern CI/CD Automated Excellence.",
    contentPoints: [
      "Release Frequency: Manual (1x per 3 months) vs. Automated (multiple times per day on-demand).",
      "Lead Time for Changes: Manual (weeks/months of planning) vs. Automated (< 15 minutes from commit to production).",
      "Change Failure Rate: Manual (30% - 50% defect rate) vs. Automated (< 5% elite DORA standard).",
      "Mean Time to Recovery (MTTR): Manual (hours/days of outage) vs. Automated (< 60 seconds instant rollback)."
    ],
    detailedPoints: [
      "Downtime: Manual releases cause planned 2:00 AM outages; modern CI/CD delivers 100% zero-downtime rolling and blue-green updates.",
      "Audit Trail & Compliance: Manual releases leave no logs; CI/CD links every production deployment to a Git commit, pull request review, and test report.",
      "Engineering Culture: Manual deployments cause fear, exhaustion, and finger-pointing. Automated delivery breeds psychological safety, confidence, and high engineering velocity.",
      "The Golden Rules of Deployment: 1) Build immutable artifacts once. 2) Decouple deploy from release. 3) Automate health probes. 4) Fast rollback beats slow debugging."
    ],
    foodAnalogy: {
      "title": "The Horse Cart vs. The Electric Bullet Train 🚄",
      "story": "Manual delivery is a wooden horse cart bumping across a dirt road, vulnerable to rain, flat wheels, and exhausted horses. Automated CI/CD deployment is a high-speed magnetic bullet train operating on precision tracks with automated signals and safety sensors.",
      "connection": "Automating your deployment pipeline transforms your engineering team from struggling transport to world-class velocity."
    },
    keyTakeaway: "Automating deployment is not just a tooling change — it is a cultural revolution that enables fearless innovation."
  }
];
