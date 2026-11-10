export interface PresenterExperienceItem {
  role: string;
  company: string;
  type: string;
  badge: string;
  badgeClass: string;
  description: string;
}

export interface PresenterBio {
  name: string;
  role: string;
  company: string;
  previousRole: string;
  venture: string;
  ventureDetail: string;
  bio: string;
  experiences: PresenterExperienceItem[];
}

export const PRESENTER_INFO: PresenterBio = {
  name: "Aajera Banu S",
  role: "AWS & Networking Trainer",
  company: "LIVEWIRE Salem",
  previousRole: "Ex-Cloud Engineer Intern at Codec Technologies",
  venture: "Redis Certified Associate Cloud Operator",
  ventureDetail: "DevOps, Containerization & AWS Infrastructure Automation",
  bio: "AWS & Networking Trainer and Redis Certified Associate Cloud Operator with deep hands-on expertise in Docker containerization, Jenkins & GitHub Actions CI/CD pipelines, Linux administration, AWS ECS Fargate, and production network troubleshooting.",
  experiences: [
    {
      role: "AWS & Networking Trainer",
      company: "LIVEWIRE Salem",
      type: "Current Leadership & Training",
      badge: "Trainer @ LIVEWIRE Salem",
      badgeClass: "bg-blue-100 text-blue-900 border-blue-300 font-bold",
      description: "Training students and engineers in AWS Cloud (EC2, S3, VPC, IAM) and Cisco CCNA networking (routing, switching, subnetting, TCP/IP, VLANs, ACLs, and NAT) with comprehensive hands-on labs."
    },
    {
      role: "Redis Certified Cloud Operator",
      company: "Redis Certified",
      type: "Industry Certification",
      badge: "Redis Certified Associate",
      badgeClass: "bg-amber-100 text-amber-950 border-amber-300 font-bold",
      description: "Certified Cloud Operator specializing in Redis Cloud architecture, high-availability in-memory caching, performance optimization, and distributed cloud systems."
    },
    {
      role: "Cloud Engineer Intern",
      company: "Codec Technologies India",
      type: "DevOps & Cloud Engineering",
      badge: "Ex-Cloud Intern @ Codec",
      badgeClass: "bg-emerald-100 text-emerald-950 border-emerald-300 font-bold",
      description: "Architected microservices e-commerce platform using Docker, Docker Compose, AWS ECS Fargate, Nginx reverse proxy, and Prometheus/Grafana real-time monitoring."
    }
  ]
};

export interface MasterSlide {
  num: number;
  title: string;
  subtitle: string;
  category: string;
  image?: string;
  imageCaption?: string;
  detailedPoints?: string[];
  contentPoints?: string[];
  foodAnalogy?: {
    title: string;
    story: string;
    connection?: string;
  };
  keyTakeaway: string;
  problemsList?: string[];
  timeline?: { era: string; title: string; desc: string }[];
  comparisonTable?: { aspect: string; before: string; after: string }[];
  concepts?: { term: string; purpose: string; desc: string; analogy: string }[];
  gitConcepts?: { term: string; desc: string }[];
  exampleCommand?: string;
  comparison?: { aspect: string; git: string; github: string }[];
  features?: string[];
  toolsTable?: { stage: string; tools: string }[];
  advantages?: { title: string; desc: string }[];
  components?: { term: string; desc: string }[];
  lifecycleSteps?: { step: string; desc: string }[];
  triggers?: string[];
  code?: string;
  explanations?: { key: string; desc: string }[];
  narrative?: string;
  steps?: string[];
  scenarios?: { result: string; outcome: string }[];
  stages?: { num: string; name: string; purpose: string; foodEquivalent: string }[];
  terms?: { term: string; desc: string }[];
  flowSteps?: string[];
  services?: { service: string; role: string }[];
  securityRules?: { rule: string; desc: string }[];
  failureMatrix?: { failure: string; cause: string; action: string }[];
  architectureSteps?: { step: string; detail: string }[];
  projectTasks?: string[];
  summaryMapping?: { tool: string; role: string }[];
  finalAnalogy?: string;
  finalPhilosophy?: string;
  qaTopics?: { icon: string; title: string; desc: string; sampleQuestions: string[] }[];
  thankYouHighlights?: { title: string; desc: string }[];
  contactChannels?: { label: string; value: string; note: string }[];
}

export const MASTER_SLIDES_DATA: MasterSlide[] = [
  {
    "num": 1,
    "title": "CI/CD: From Manual Work to Automated Software Delivery",
    "subtitle": "Introduction to Continuous Integration and Continuous Delivery/Deployment",
    "category": "Foundations",
    "contentPoints": [
      "CI/CD stands for Continuous Integration and Continuous Delivery/Deployment.",
      "It is a software development practice that automates the process of integrating, testing, and releasing code.",
      "The primary goal is to deliver software faster, more reliably, and with fewer human errors.",
      "Instead of manually performing every release step, teams configure an automated, repeatable pipeline."
    ],
    "foodAnalogy": {
      "title": "Food-Ordering Analogy \ud83c\udf54",
      "story": "Imagine a customer orders a burger through a food delivery app. The customer places the order \u2794 The restaurant receives it \u2794 The kitchen prepares the food \u2794 The food passes a quality check \u2794 The order is packaged and delivered.",
      "connection": "Now imagine every single step happens automatically after the customer places the order. CI/CD follows the exact same idea: a developer pushes code, and an automated pipeline builds, tests, packages, and deploys the application."
    },
    "keyTakeaway": "CI/CD turns software delivery into a repeatable, automated process.",
    "image": "/slides/slide_1.png",
    "imageCaption": "CI/CD Pipeline Flow: Code Commit \u2794 Webhook Trigger \u2794 Automated Tests \u2794 Docker Package \u2794 Live Cloud Deploy (200 OK).",
    "detailedPoints": [
      "Continuous Integration (CI): Developers merge code changes into the shared branch multiple times a day. Every commit triggers automated builds and tests, catching defects in < 10 minutes.",
      "Continuous Delivery (CDel): The application is continuously packaged and deployed to staging environments. Release to production is kept ready as a 1-click human business decision.",
      "Continuous Deployment (CDep): Every passing commit is automatically deployed directly to production cloud servers with zero human intervention.",
      "Business Impact: According to DORA (DevOps Research & Assessment), elite CI/CD teams deploy 208x more frequently and recover from downtime 2,604x faster."
    ]
  },
  {
    "num": 2,
    "title": "Traditional Software Development: The Manual Era",
    "subtitle": "What Happens Before CI/CD? The High-Risk Manual Delivery Process",
    "category": "The Problem",
    "contentPoints": [
      "Before modern CI/CD practices became widespread, software releases involved tedious, error-prone manual steps.",
      "A developer would write the code, copy it to a shared server, and ask someone to manually build the application.",
      "Teams waited for manual testing, fixed bugs late, manually FTP'd files to production, and restarted servers praying it worked.",
      "This chaotic process could take hours, days, or even weeks depending on team size and complexity."
    ],
    "problemsList": [
      "Slow and infrequent releases (months apart)",
      "High frequency of human typos and misconfigurations",
      "Inconsistent deployment steps between environments",
      "Late discovery of catastrophic regression bugs",
      "Painful coordination friction between Dev and Ops",
      "Extremely risky releases with complicated rollbacks"
    ],
    "foodAnalogy": {
      "title": "The Manual Kitchen Analogy \ud83d\udcdd",
      "story": "Imagine a restaurant where the cashier writes orders on paper, walks to the kitchen, checks every dish personally, packs each order, and calls a delivery rider manually.",
      "connection": "As the number of orders increases, delays, mistakes, and cold food become inevitable. Manual delivery collapses as teams grow."
    },
    "keyTakeaway": "Manual delivery can work for small hobby projects, but becomes unmanageable as applications and teams scale.",
    "image": "/slides/slide_2.png",
    "imageCaption": "Manual Delivery 'Integration Hell' vs. Automated CI/CD Continuous Flow Comparison.",
    "detailedPoints": [
      "The 6-Month 'Big Bang' Release: Teams wrote code in isolated branches for months. Merging resulted in 'Integration Hell' with thousands of conflicting code lines.",
      "The 'Works on My Machine' Trap: A feature worked on the developer's MacBook, but immediately crashed on Linux production servers due to missing packages or different OS libraries.",
      "Late-Night Production Panic: Releases were scheduled at 2:00 AM on weekends. Engineers manually ran SSH commands and SQL scripts, leading to multi-hour downtime."
    ]
  },
  {
    "num": 3,
    "title": "The History and Evolution of CI/CD",
    "subtitle": "Who Introduced CI/CD? A Decades-Long Evolution of Engineering Practices",
    "category": "History & Origins",
    "timeline": [
      {
        "era": "1990s",
        "title": "Continuous Integration Emerges",
        "desc": "Kent Beck established Continuous Integration as a core practice of Extreme Programming (XP), mandating daily code merges."
      },
      {
        "era": "2000",
        "title": "CI Documented & Codified",
        "desc": "Martin Fowler and Matthew Foemmel published seminal papers describing practical automated build-and-test workflows."
      },
      {
        "era": "2001+",
        "title": "First Automated CI Tools",
        "desc": "ThoughtWorks engineers created CruiseControl, the first open-source daemon automating scheduled builds and test runs."
      },
      {
        "era": "2010s",
        "title": "Continuous Delivery Book",
        "desc": "Jez Humble and David Farley published 'Continuous Delivery', extending automation from code compilation to cloud production releases."
      },
      {
        "era": "Modern",
        "title": "Cloud-Native CI/CD Mainstream",
        "desc": "Jenkins, GitLab CI, and GitHub Actions bring native, serverless workflow automation to millions of developers worldwide."
      }
    ],
    "foodAnalogy": {
      "title": "Restaurant Modernization Analogy \ud83d\udccb",
      "story": "Initially, a diner used paper slips and shoutouts. Over time, restaurants introduced digital point-of-sale systems, kitchen display screens, automated order tracking, and drone delivery.",
      "connection": "CI/CD evolved the same way: not as a single overnight invention, but as continuous improvements in tools, testing, and automation."
    },
    "keyTakeaway": "CI/CD is an evolution of collaborative engineering practices, not an invention attributable to one individual.",
    "image": "/slides/slide_3.png",
    "imageCaption": "Historical Evolution: Grady Booch (1991), Kent Beck XP (1999) to Modern CI/CD."
  },
  {
    "num": 4,
    "title": "From Manual Releases to Automated Delivery",
    "subtitle": "What Changed After CI/CD? The Paradigm Shift in Velocity & Reliability",
    "category": "Transformation",
    "comparisonTable": [
      {
        "aspect": "Build Phase",
        "before": "Manual compilation on developer laptop",
        "after": "Automated clean build triggered on code push"
      },
      {
        "aspect": "Testing",
        "before": "Infrequent manual QA testing before release",
        "after": "Instant automated test suites run on every commit"
      },
      {
        "aspect": "Deployment",
        "before": "Manual FTP/SSH file copy late at night",
        "after": "Automated zero-downtime pipeline deployment"
      },
      {
        "aspect": "Bug Detection",
        "before": "Discovered weeks or months later in prod",
        "after": "Detected within minutes; build fails immediately"
      },
      {
        "aspect": "Team Stress",
        "before": "High-risk, terrifying weekend releases",
        "after": "Routine, predictable, non-event daytime releases"
      }
    ],
    "foodAnalogy": {
      "title": "Order Slip vs. Automated Conveyor \ud83c\udf54",
      "story": "Before automation, staff physically ran slips between stations. After automation, tapping 'Order' triggers the prep screen, oven timer, and rider notification seamlessly.",
      "connection": "CI/CD does not eliminate human work (developers still write code, review PRs, and design features), but it removes all repetitive manual release toil."
    },
    "keyTakeaway": "CI/CD reduces repetitive manual friction, allowing teams to ship higher-quality software with complete confidence.",
    "image": "/slides/slide_4.png",
    "imageCaption": "Before vs. After Transformation: Shifting from 6-month manual release panic to automated daily non-event deployments."
  },
  {
    "num": 5,
    "title": "Understanding CI, Continuous Delivery, and Continuous Deployment",
    "subtitle": "What Is CI/CD? Dissecting the Three Core Stages of the Pipeline",
    "category": "Core Concepts",
    "concepts": [
      {
        "term": "Continuous Integration (CI)",
        "purpose": "Integrate and Validate Code Frequently",
        "desc": "Developers regularly merge code into a shared repository. Every commit automatically triggers clean builds, linters, and unit test suites to detect regressions early.",
        "analogy": "Prepare the ingredients and thoroughly inspect food quality before cooking."
      },
      {
        "term": "Continuous Delivery (CD)",
        "purpose": "Keep Software Always Ready to Release",
        "desc": "After passing all automated checks and staging dry-runs, the software artifact is packaged and ready to deploy. Release to production requires a 1-click human approval.",
        "analogy": "The meal is packaged in an insulated container, waiting on the counter for the manager's dispatch approval."
      },
      {
        "term": "Continuous Deployment (CD)",
        "purpose": "Automatically Release Qualifying Changes",
        "desc": "Every qualifying change that passes all automated test gates is deployed directly to production cloud servers with zero human intervention.",
        "analogy": "An autonomous delivery drone dispatches the order the instant quality checks pass."
      }
    ],
    "keyTakeaway": "CI validates changes; Continuous Delivery prepares software for release; Continuous Deployment puts it into production automatically.",
    "image": "/slides/slide_5.png",
    "imageCaption": "CI, Continuous Delivery, and Continuous Deployment: Validating, Packaging, and Autonomous Cloud Rollout."
  },
  {
    "num": 6,
    "title": "Git: Tracking Every Change in the Code",
    "subtitle": "What Is Git? The Distributed Foundation of Version Control",
    "category": "Version Control",
    "contentPoints": [
      "Git is a distributed version control system that records changes to files over time.",
      "It enables multiple software engineers to work concurrently on the same codebase without overwriting each other's work.",
      "Every developer has a full, cryptographic copy of the repository history locally on their machine."
    ],
    "gitConcepts": [
      {
        "term": "Repository",
        "desc": "The project folder and its entire tracked commit history."
      },
      {
        "term": "Commit",
        "desc": "An immutable, cryptographic snapshot of changes at a point in time."
      },
      {
        "term": "Branch",
        "desc": "An independent line of development to isolate new features."
      },
      {
        "term": "Merge",
        "desc": "Combining changes from one branch into another (e.g. feature to main)."
      },
      {
        "term": "Push & Pull",
        "desc": "Push transmits local commits to remote; Pull downloads remote updates."
      }
    ],
    "exampleCommand": "git init\ngit add .\ngit commit -m \"Add food ordering feature\"\ngit push origin main",
    "foodAnalogy": {
      "title": "The Master Kitchen Recipe Ledger \ud83d\udcd6",
      "story": "Git is like the restaurant's master recipe history book. It tracks every ingredient tweak, records who made the change, and allows instant rollback to yesterday's recipe if a new spice ruins the flavor.",
      "connection": "Git manages code history and collaboration, providing the triggers that ignite automated CI/CD pipelines."
    },
    "keyTakeaway": "Git manages code history and team collaboration. It is the necessary starting point for CI/CD.",
    "image": "/slides/slide_6.png",
    "imageCaption": "Git Version Control: Cryptographic snapshot commits, lightweight branching, and mainline collaboration."
  },
  {
    "num": 7,
    "title": "GitHub: A Central Place for Code and Collaboration",
    "subtitle": "What Is GitHub? The Cloud Collaboration Platform for Modern Teams",
    "category": "Platforms",
    "contentPoints": [
      "GitHub is a cloud-based hosting platform for Git repositories, serving over 100 million developers globally.",
      "It provides the centralized remote hub where distributed teams store code, discuss features, and automate workflows."
    ],
    "comparison": [
      {
        "aspect": "Core Nature",
        "git": "A command-line version control system tool",
        "github": "A cloud platform hosting Git repositories"
      },
      {
        "aspect": "Execution",
        "git": "Runs locally on your computer with or without internet",
        "github": "Hosted in the cloud for team collaboration"
      },
      {
        "aspect": "Primary Purpose",
        "git": "Records file history and branches",
        "github": "Adds Pull Requests, Issue tracking, Reviews & Actions"
      }
    ],
    "features": [
      "Centralized Remote Git Hosting",
      "Interactive Pull Requests with Inline Code Reviews",
      "Issue Trackers & Project Boards",
      "Branch Protection Rules (Requiring approvals & passing tests)",
      "Native Event Webhooks that trigger GitHub Actions"
    ],
    "foodAnalogy": {
      "title": "Restaurant Management Hub \ud83c\udfea",
      "story": "If Git is the chef's personal notebook recording recipe steps, GitHub is the shared digital kitchen portal where recipes are stored, team members propose changes, and managers approve menus.",
      "connection": "Git tracks the versions; GitHub coordinates the team and ignites automation."
    },
    "keyTakeaway": "Git manages versions locally; GitHub hosts repositories centrally and connects code directly to automation engines.",
    "image": "/slides/slide_7.png",
    "imageCaption": "Git vs. GitHub Comparison: Distributed Local Revision Control vs. Central Collaboration & CI/CD Hub."
  },
  {
    "num": 8,
    "title": "CI/CD Tool Ecosystem: Specialized Tools for Every Stage",
    "subtitle": "What Tools Are Used for CI/CD? Combining Specialized Tools into One Pipeline",
    "category": "Ecosystem",
    "toolsTable": [
      {
        "stage": "Version Control",
        "tools": "Git, GitHub, GitLab, Bitbucket"
      },
      {
        "stage": "CI/CD Automation",
        "tools": "GitHub Actions, Jenkins, GitLab CI, CircleCI"
      },
      {
        "stage": "Build & Package",
        "tools": "npm, Vite, Maven, Gradle, PyTest"
      },
      {
        "stage": "Code Quality & Security",
        "tools": "ESLint, SonarQube, Snyk, CodeQL"
      },
      {
        "stage": "Containerization",
        "tools": "Docker, Podman"
      },
      {
        "stage": "Container Registry",
        "tools": "GitHub Packages (GHCR), Amazon ECR, Docker Hub"
      },
      {
        "stage": "Cloud Deployment",
        "tools": "AWS (ECS, S3, CloudFront), Azure, Google Cloud"
      },
      {
        "stage": "Infrastructure as Code",
        "tools": "Terraform, Ansible, CloudFormation"
      },
      {
        "stage": "Monitoring & SRE",
        "tools": "CloudWatch, Datadog, Prometheus, Grafana"
      }
    ],
    "foodAnalogy": {
      "title": "Specialized Commercial Kitchen Equipment \ud83c\udf73",
      "story": "One machine kneads dough, an oven bakes buns, a slicer prepares vegetables, an automated sealer packs boxes, and GPS tracks delivery riders. Each device excels at its designated station.",
      "connection": "CI/CD connects these specialized tools into one unified pipeline. You do not need every tool in every project \u2014 start simple and add as needed."
    },
    "keyTakeaway": "CI/CD is a coordinated process combining specialized tools across the entire software delivery lifecycle.",
    "image": "/slides/slide_8.png",
    "imageCaption": "CI/CD Tool Ecosystem: Specialized tools coordinated across Version Control, CI, Docker, AWS, and Monitoring."
  },
  {
    "num": 9,
    "title": "Why Choose GitHub Actions for Our CI/CD Project?",
    "subtitle": "The Practical Advantage of Native, Serverless Repository Automation",
    "category": "GitHub Actions",
    "advantages": [
      {
        "title": "Native GitHub Integration",
        "desc": "Workflows trigger seamlessly on code pushes, pull requests, issue creation, or releases with zero webhook configuration."
      },
      {
        "title": "Zero Server Maintenance",
        "desc": "GitHub provides managed, ephemeral virtual machine runners (Ubuntu, Windows, macOS). No need to maintain a dedicated Jenkins server."
      },
      {
        "title": "Configuration as Code in YAML",
        "desc": "Pipeline workflows live directly in `.github/workflows/` inside your repository, version-controlled alongside your code."
      },
      {
        "title": "Rich Marketplace Ecosystem",
        "desc": "Thousands of pre-built, community-vetted actions for Docker, AWS, Node, Python, and security scanning."
      },
      {
        "title": "Clear Visibility & Logs",
        "desc": "Real-time streaming terminal logs and status badges appear directly inside Pull Requests, pinpointing errors instantly."
      },
      {
        "title": "Generous Free Tier",
        "desc": "Free for public repositories and provides 2,000 free runner minutes per month for private projects."
      }
    ],
    "foodAnalogy": {
      "title": "The All-in-One Restaurant Platform \ud83c\udf54",
      "story": "Instead of leasing extra real estate and hiring technicians to maintain custom kitchen machinery, you use a modern kitchen facility with built-in power, appliances, and automated stations ready on demand.",
      "connection": "GitHub Actions eliminates tool fragmentation by embedding enterprise CI/CD directly inside your code repository."
    },
    "keyTakeaway": "GitHub Actions is the ideal platform because it eliminates infrastructure overhead by bringing code, review, and automation together.",
    "image": "/slides/slide_9.png",
    "imageCaption": "Why GitHub Actions: Native Repo Integration, Ephemeral Runners, Marketplace Actions & Zero Infra Maintenance."
  },
  {
    "num": 10,
    "title": "GitHub Actions: The Automation Engine",
    "subtitle": "What Is GitHub Actions? The Core Architecture & Key Components",
    "category": "GitHub Actions",
    "contentPoints": [
      "GitHub Actions is an event-driven automation platform built directly into GitHub.",
      "Workflows are declared in YAML files stored inside the `.github/workflows/` directory of the repository.",
      "When a developer pushes code, GitHub automatically detects the event, spins up a fresh runner, executes jobs, and reports results."
    ],
    "components": [
      {
        "term": "Event",
        "desc": "The trigger that initiates the workflow (e.g. `push`, `pull_request`, `schedule`)."
      },
      {
        "term": "Workflow",
        "desc": "The top-level automated process defined in a `.github/workflows/*.yml` file."
      },
      {
        "term": "Job",
        "desc": "A set of steps that execute on the same runner. Multiple jobs run in parallel by default."
      },
      {
        "term": "Step",
        "desc": "An individual task that can run commands or call a reusable action."
      },
      {
        "term": "Action",
        "desc": "A reusable standalone command or plugin from the GitHub Marketplace."
      },
      {
        "term": "Runner",
        "desc": "A virtual machine or container hosted by GitHub that executes your jobs."
      }
    ],
    "foodAnalogy": {
      "title": "Kitchen Hierarchy Analogy \ud83d\udece\ufe0f",
      "story": "Event \u2794 Order received. Workflow \u2794 Full meal preparation process. Job \u2794 Burger grill station. Step \u2794 Flip the patty. Action \u2794 Standard seasoning recipe. Runner \u2794 The clean kitchen workstation.",
      "connection": "GitHub Actions executes the exact sequence of instructions you define with deterministic precision."
    },
    "keyTakeaway": "GitHub Actions executes the automation rules you define in YAML using ephemeral, secure cloud runners.",
    "image": "/slides/slide_10.png",
    "imageCaption": "GitHub Actions Architecture: Event Triggers \u2794 Ephemeral Runner VMs \u2794 Parallel Jobs \u2794 Sequential Step Execution."
  },
  {
    "num": 11,
    "title": "How Does GitHub Actions Work? From Code Push to Execution",
    "subtitle": "Step-by-Step Lifecycle: What Happens When a Developer Commits Code",
    "category": "Execution Lifecycle",
    "lifecycleSteps": [
      {
        "step": "1. Developer Edits Code",
        "desc": "An engineer updates features (e.g. adds discount logic to checkout)."
      },
      {
        "step": "2. Git Commit & Push",
        "desc": "Code is pushed to a branch or opened as a Pull Request on GitHub."
      },
      {
        "step": "3. Event Trigger Fired",
        "desc": "GitHub webhook detects the push event and matches active workflow rules."
      },
      {
        "step": "4. Runner Allocation",
        "desc": "GitHub provisions an isolated, clean virtual machine (e.g. Ubuntu 22.04)."
      },
      {
        "step": "5. Code Checkout",
        "desc": "Runner downloads the repository source code via `actions/checkout`."
      },
      {
        "step": "6. Dependency Install",
        "desc": "Environment installs runtime dependencies (npm ci, pip install)."
      },
      {
        "step": "7. Automated Testing",
        "desc": "Unit and integration test suites execute; checks pass or fail."
      },
      {
        "step": "8. Status Reporting",
        "desc": "Green checkmark or red failure appears on the GitHub PR in real time."
      }
    ],
    "triggers": [
      "`push` \u2014 Runs whenever commits are pushed to specified branches.",
      "`pull_request` \u2014 Runs when a PR is opened, updated, or synchronized.",
      "`workflow_dispatch` \u2014 Enables a manual 'Run workflow' button in GitHub UI.",
      "`schedule` \u2014 Runs on a cron schedule (e.g., nightly security scan)."
    ],
    "foodAnalogy": {
      "title": "Order Ticket to Cooking Pipeline \ud83d\udc68\u200d\ud83c\udf73",
      "story": "The moment an order arrives on the tablet, a kitchen ticket prints, station lights illuminate, cooks wash hands, ingredients are assembled, and food is prepared according to strict timers.",
      "connection": "The push trigger starts the pipeline; the runner executes the steps in strict, reliable sequence."
    },
    "keyTakeaway": "A trigger starts the workflow; the runner executes its jobs and steps in an isolated, clean sandbox.",
    "image": "/slides/slide_11.png",
    "imageCaption": "GitHub Actions Lifecycle: Event Trigger \u2794 Runner Spin-Up \u2794 Checkout \u2794 Test Execution \u2794 Status Report."
  },
  {
    "num": 12,
    "title": "Understanding the GitHub Actions Workflow File",
    "subtitle": "Our First CI/CD Workflow: Deconstructing the YAML Syntax Line by Line",
    "category": "Workflow Syntax",
    "code": "name: Food App CI\n\non:\n  push:\n    branches: [main]\n  pull_request:\n    branches: [main]\n\npermissions:\n  contents: read\n\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Checkout code\n        uses: actions/checkout@v4\n\n      - name: Set up Python\n        uses: actions/setup-python@v5\n        with:\n          python-version: \"3.12\"\n\n      - name: Install dependencies\n        run: pip install -r requirements.txt\n\n      - name: Run tests\n        run: pytest",
    "explanations": [
      {
        "key": "name",
        "desc": "Human-readable label displayed in the GitHub Actions tab."
      },
      {
        "key": "on",
        "desc": "Defines webhook trigger events (pushes and PRs to main branch)."
      },
      {
        "key": "permissions",
        "desc": "Applies principle of least privilege (read-only repository access)."
      },
      {
        "key": "jobs",
        "desc": "Contains one or more jobs; 'test' runs on a clean Ubuntu runner."
      },
      {
        "key": "steps",
        "desc": "Ordered sequence of tasks: checkout repo, configure Python, install, and test."
      },
      {
        "key": "uses vs run",
        "desc": "'uses' executes a pre-built marketplace action; 'run' executes shell commands."
      }
    ],
    "foodAnalogy": {
      "title": "Kitchen Standard Operating Procedure (SOP) \ud83d\udccb",
      "story": "The laminated kitchen SOP sheet lists instructions step by step: 1) Wash hands, 2) Set grill to 350\u00b0F, 3) Cook patty for 3 minutes, 4) Check internal temperature with thermometer.",
      "connection": "The YAML file tells GitHub Actions what to automate; the runner carries out those exact instructions every time."
    },
    "keyTakeaway": "YAML configuration files are human-readable blueprints that tell cloud runners exactly how to build and verify your software.",
    "image": "/slides/slide_12.png",
    "imageCaption": "GitHub Actions YAML Anatomy: Events, Permissions, Jobs, Ephemeral Runners & Sequential Steps."
  },
  {
    "num": 13,
    "title": "What Happens When We Push Code? The Complete CI Pipeline",
    "subtitle": "Tracing a Real Code Change: Rapid Feedback Loops & Defect Prevention",
    "category": "CI Pipeline",
    "narrative": "Let's trace a real feature update: A developer adds a promotional discount code feature to the food delivery application and pushes code to GitHub.",
    "steps": [
      "GitHub detects the push event immediately.",
      "A fresh Ubuntu runner VM is allocated within seconds.",
      "The runner downloads the source code and cached dependencies.",
      "Static analysis and linters inspect code style and detect syntax errors.",
      "Automated unit and integration test suites run against the changes.",
      "Real-time logs stream directly to the developer's GitHub interface."
    ],
    "scenarios": [
      {
        "result": "\u274c Tests Fail",
        "outcome": "Pipeline turns red. PR is blocked from merging. Developer receives an instant notification with exact line numbers of failure. Dependent packaging jobs abort immediately."
      },
      {
        "result": "\u2705 Tests Pass",
        "outcome": "Green checkmark appears on PR. Code is certified healthy and immediately ready for container packaging, staging deployment, or release."
      }
    ],
    "foodAnalogy": {
      "title": "Sous-Chef Quality Inspection \ud83d\udd2c",
      "story": "The sous-chef tastes the soup before it leaves the kitchen. If too salty, it is rejected right at the pot \u2014 preventing an unhappy customer and negative review.",
      "connection": "CI provides developers rapid feedback in minutes, catching bugs when they are easiest and cheapest to fix."
    },
    "keyTakeaway": "CI gives developers rapid feedback within minutes, stopping broken code before it progresses toward production.",
    "image": "/slides/slide_13.png",
    "imageCaption": "Real Code Push Tracing: Push Event \u2794 Fast Feedback Loop \u2794 Automated Guardrails Block Defective Code."
  },
  {
    "num": 14,
    "title": "The Four Major Stages of Delivery: Build, Test, Package, Deploy",
    "subtitle": "The Universal Pipeline Progression from Source Code to Production",
    "category": "Pipeline Stages",
    "stages": [
      {
        "num": "1",
        "name": "BUILD",
        "purpose": "Compile code, resolve dependencies, and generate release binaries.",
        "foodEquivalent": "Preheat oven, wash fresh ingredients, and cook the raw food."
      },
      {
        "num": "2",
        "name": "TEST",
        "purpose": "Execute unit, integration, and security scans to verify behavior.",
        "foodEquivalent": "Taste test food and check internal temperatures with thermometer."
      },
      {
        "num": "3",
        "name": "PACKAGE",
        "purpose": "Bundle code, dependencies, and OS into an immutable container image.",
        "foodEquivalent": "Place hot food into an insulated, sealed, and labeled takeout box."
      },
      {
        "num": "4",
        "name": "DEPLOY",
        "purpose": "Release packaged artifact to target cloud servers with zero downtime.",
        "foodEquivalent": "Hand sealed bag to delivery driver who transports it to customer."
      }
    ],
    "foodAnalogy": {
      "title": "Assembly Line Station Separation \ud83c\udf71",
      "story": "A kitchen cannot pack food before cooking it, nor can it deliver food before boxing it. Each station has a distinct quality mandate.",
      "connection": "A successful build does not guarantee a successful deployment. Each stage has a specific verification responsibility."
    },
    "keyTakeaway": "A reliable CI/CD pipeline enforces progressive trust: Build \u2794 Test \u2794 Package \u2794 Deploy.",
    "image": "/slides/slide_14.png",
    "imageCaption": "The 4 Major Delivery Stages: 1. Build (Cook) \u2794 2. Test (Inspect) \u2794 3. Package (Bento Box) \u2794 4. Deploy (Deliver)."
  },
  {
    "num": 15,
    "title": "Docker and Container Images: Packaging Our Application",
    "subtitle": "Curing 'Works on My Machine' by Standardizing the Packaging Layer",
    "category": "Containerization",
    "contentPoints": [
      "Docker packages an application, its runtime dependencies, libraries, and system tools into an immutable container image.",
      "This eliminates the infamous 'Works on my machine' bug: if a container runs on your laptop, it runs identically on staging and production."
    ],
    "terms": [
      {
        "term": "Dockerfile",
        "desc": "Text blueprint containing step-by-step instructions for assembling an image."
      },
      {
        "term": "Image",
        "desc": "An immutable, portable, read-only package containing application code and OS."
      },
      {
        "term": "Container",
        "desc": "A running instance of a Docker image operating in an isolated sandbox."
      },
      {
        "term": "Registry",
        "desc": "A secure cloud storage repository for container images (Docker Hub, Amazon ECR)."
      },
      {
        "term": "Tag",
        "desc": "A version label identifying specific releases (e.g. `food-app:v1.2.0` or git SHA)."
      }
    ],
    "foodAnalogy": {
      "title": "Standardized Sealed Bento Box \ud83c\udf71",
      "story": "Instead of handing loose pasta to a delivery driver, the kitchen seals the meal in a standardized, leak-proof bento box that fits any delivery bag identically.",
      "connection": "Docker packages applications into standardized units ready for transport to any cloud platform."
    },
    "keyTakeaway": "Docker creates immutable, portable packages; cloud platforms provide the infrastructure to run them.",
    "image": "/slides/slide_15.png",
    "imageCaption": "Docker Containerization: Packaging code, libraries, and OS into standardized immutable images."
  },
  {
    "num": 16,
    "title": "Deploying to AWS: From GitHub Actions to the Cloud",
    "subtitle": "Publishing Container Images to Amazon ECR and Running on Amazon ECS",
    "category": "Cloud Deployment",
    "flowSteps": [
      "1. Developer pushes code to GitHub mainline branch.",
      "2. GitHub Actions builds and passes all automated tests.",
      "3. Docker builds container image tagged with the Git commit SHA.",
      "4. GitHub Actions authenticates with AWS via OpenID Connect (OIDC).",
      "5. Image is pushed securely to Amazon Elastic Container Registry (ECR).",
      "6. Deployment workflow updates task definition on Amazon Elastic Container Service (ECS).",
      "7. Application Load Balancer shifts incoming traffic to healthy containers with zero downtime."
    ],
    "services": [
      {
        "service": "Amazon ECR",
        "role": "Private, high-availability container image registry."
      },
      {
        "service": "Amazon ECS",
        "role": "Container orchestration service managing cluster containers."
      },
      {
        "service": "Application Load Balancer",
        "role": "Distributes customer traffic and conducts health checks."
      },
      {
        "service": "AWS CloudWatch",
        "role": "Aggregates logs, latency metrics, and automated alerts."
      }
    ],
    "detailedPoints": [
      "AWS Cloud Infrastructure: Provides high-availability compute, container orchestration, and automated auto-scaling for modern microservices.",
      "Keyless OIDC Authentication: GitHub Actions assumes an IAM Role via OpenID Connect (OIDC), eliminating the dangerous need for stored static access keys.",
      "Amazon ECR (Elastic Container Registry): Private, encrypted Docker image registry that automatically scans every container image for CVE vulnerabilities on push.",
      "Amazon ECS (Elastic Container Service): Serverless container orchestration using AWS Fargate that launches and manages tasks without managing EC2 servers.",
      "Application Load Balancer (ALB): Distributes traffic across multi-AZ container tasks, conducts continuous /health checks, and shifts traffic with zero downtime."
    ],
    "code": "# .github/workflows/deploy-aws.yml\nname: Deploy to Amazon ECS\non:\n  push:\n    branches: [ main ]\npermissions:\n  id-token: write\n  contents: read\njobs:\n  deploy:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - name: Authenticate with AWS via OIDC\n        uses: aws-actions/configure-aws-credentials@v4\n        with:\n          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole\n          aws-region: us-east-1\n      - name: Login to Amazon ECR\n        uses: aws-actions/amazon-ecr-login@v2\n      - name: Build & Push Docker Image\n        run: |\n          docker build -t $ECR_REGISTRY/food-order-api:${{ github.sha }} .\n          docker push $ECR_REGISTRY/food-order-api:${{ github.sha }}\n      - name: Deploy to Amazon ECS Fargate\n        run: |\n          aws ecs update-service --cluster prod --service food-api --force-new-deployment",
    "foodAnalogy": {
      "title": "Franchise Logistics Network \ud83d\ude9a",
      "story": "GitHub Actions coordinates food prep, Amazon ECR is the central cold-storage distribution hub, Amazon ECS is the network of commercial franchise kitchens, and the Load Balancer routes hungry diners.",
      "connection": "GitHub Actions orchestrates the release; AWS provides the scalable cloud infrastructure."
    },
    "keyTakeaway": "GitHub Actions automates the deployment process; cloud providers supply the scalable hosting infrastructure.",
    "image": "/slides/slide_16.png",
    "imageCaption": "AWS Cloud Architecture: GitHub Actions OIDC \u2794 Amazon ECR Registry \u2794 Amazon ECS Fargate \u2794 ALB Load Balancer (200 OK)."
  },
  {
    "num": 17,
    "title": "Security and Approval in CI/CD: Automate Safely, Not Just Quickly",
    "subtitle": "DevSecOps: Principle of Least Privilege, Secret Protection, and Release Gates",
    "category": "Security & Governance",
    "securityRules": [
      {
        "rule": "Never Commit Secrets to Git",
        "desc": "Never hardcode database passwords or AWS keys in code. Store credentials in GitHub Encrypted Secrets."
      },
      {
        "rule": "Least-Privilege Permissions",
        "desc": "Grant workflow tokens only the exact permissions needed (e.g. read-only code access unless writing packages)."
      },
      {
        "rule": "Automated Security Scanning",
        "desc": "Use Snyk, Trivy, and CodeQL to scan third-party npm/pip dependencies and container images for known vulnerabilities."
      },
      {
        "rule": "Branch Protection & Reviews",
        "desc": "Require peer code review approvals and passing CI status checks before allowing merges into main."
      },
      {
        "rule": "Protected Environments & Approvals",
        "desc": "Configure manual approval gates for production deployments, ensuring manager authorization."
      },
      {
        "rule": "Short-Lived Cloud Credentials (OIDC)",
        "desc": "Use OpenID Connect instead of permanent, long-lived AWS IAM access keys that can leak."
      }
    ],
    "foodAnalogy": {
      "title": "Kitchen Health & Hygiene Protocols \ud83d\udee1\ufe0f",
      "story": "A restaurant automates order cooking, but still locks cash registers, requires hairnets, tests food temperatures, and restricts kitchen entry to authorized personnel.",
      "connection": "Speed without security is reckless. Pipelines must halt immediately if security checks fail or unapproved code tries to ship."
    },
    "keyTakeaway": "Automate safely, not just quickly. Security checks and approval gates protect production from catastrophic leaks.",
    "image": "/slides/slide_17.png",
    "imageCaption": "DevSecOps & AWS OIDC Security: Least-Privilege, Ephemeral Tokens, and Automated Container Scans."
  },
  {
    "num": 18,
    "title": "Failure Handling, Monitoring, and Rollback",
    "subtitle": "What Happens When a Pipeline Fails? Embracing Failure Systematically",
    "category": "Resilience & SRE",
    "failureMatrix": [
      {
        "failure": "Build Failure",
        "cause": "Missing dependency or syntax compilation error",
        "action": "Inspect build logs; fix code locally; re-push commit"
      },
      {
        "failure": "Test Failure",
        "cause": "Regression bug or broken business logic",
        "action": "PR is blocked immediately; prevent release progression"
      },
      {
        "failure": "Registry Auth Failure",
        "cause": "Expired AWS credentials or IAM permission issue",
        "action": "Verify GitHub Secrets and cloud role access policies"
      },
      {
        "failure": "Deploy Failure",
        "cause": "Cloud quota exceeded or cluster timeout",
        "action": "Inspect ECS service deployment logs and container events"
      },
      {
        "failure": "Health-Check Failure",
        "cause": "Application crashes on boot (500 Internal Error)",
        "action": "Load balancer halts traffic; trigger immediate automated rollback"
      }
    ],
    "foodAnalogy": {
      "title": "Kitchen Quality Incident Response \ud83d\udea8",
      "story": "If food burns on the grill, it stays in the kitchen. If a rider drops a package, the system alerts the team, logs the refund, and dispatches a fresh meal immediately.",
      "connection": "Automation doesn't mean errors disappear \u2014 it means errors are detected and contained before they affect customers."
    },
    "keyTakeaway": "A reliable pipeline detects failures instantly, stops unsafe rollouts, and supports rapid recovery.",
    "image": "/slides/slide_18.png",
    "imageCaption": "Deployment Strategies: Blue-Green Instant Cutover vs. Canary Progressive Traffic Shifting."
  },
  {
    "num": 19,
    "title": "Real-World Project: Automated Food Ordering Application",
    "subtitle": "Build Your First End-to-End CI/CD Pipeline on GitHub Actions, Docker & AWS",
    "category": "Hands-On Architecture",
    "architectureSteps": [
      {
        "step": "STEP 1: Developer",
        "detail": "Writes application code in Python/Node with automated test suites."
      },
      {
        "step": "STEP 2: GitHub Repository",
        "detail": "Stores source code, branch protection rules, and `.github/workflows/`."
      },
      {
        "step": "STEP 3: GitHub Actions",
        "detail": "Triggers on push, allocates runner, runs linters, and executes tests."
      },
      {
        "step": "STEP 4: Docker & Amazon ECR",
        "detail": "Builds immutable container image tagged with commit SHA and pushes to registry."
      },
      {
        "step": "STEP 5: Amazon ECS",
        "detail": "Deploys updated container task definitions across high-availability clusters."
      },
      {
        "step": "STEP 6: Health Checks & CloudWatch",
        "detail": "Load balancer validates container health; CloudWatch monitors live telemetry."
      }
    ],
    "projectTasks": [
      "1. Initialize repository with food ordering web application and test suite.",
      "2. Create `.github/workflows/ci-cd.yml` defining test, build, and deploy jobs.",
      "3. Configure GitHub Secrets for AWS authentication via OIDC.",
      "4. Push code and observe green checkmarks stream across the pipeline.",
      "5. Introduce a deliberate test defect and verify the pipeline halts automatically.",
      "6. Fix the defect, re-push, and celebrate your first zero-downtime cloud deployment!"
    ],
    "detailedPoints": [
      "End-to-End Real World Pipeline: From Git commit to live production cloud on AWS in under 4 minutes.",
      "Automated CI Gates: Code linting, type-checking, and 80%+ test coverage enforced before any container image is compiled.",
      "Immutable Packaging: Docker multi-stage build creates a tiny, secure container image pushed directly to Amazon ECR.",
      "Zero-Downtime Deployment: Amazon ECS rolls out new tasks using rolling updates or blue-green switching via the Application Load Balancer.",
      "SRE Telemetry & Observability: AWS CloudWatch tracks latency and 5xx error rates, triggering automated rollbacks if any defects emerge."
    ],
    "foodAnalogy": {
      "title": "The Fully Automated Smart Restaurant \ud83c\udf55",
      "story": "Customer orders on phone \u2794 Smart ticket alerts kitchen \u2794 Robotic grill cooks burger \u2794 Optical sensor inspects burger \u2794 Packaged in bento box \u2794 Drone delivers to customer.",
      "connection": "This real-world project unifies version control, automation, containerization, cloud hosting on AWS, and observability into one cohesive system."
    },
    "keyTakeaway": "This end-to-end project combines code, CI/CD, containers, AWS cloud infrastructure, and monitoring into a complete production system.",
    "image": "/slides/slide_19.png",
    "imageCaption": "End-to-End Real-World Project: Automated Food Ordering App pipeline running on GitHub Actions, Docker, and AWS."
  },
  {
    "num": 20,
    "title": "From Beginner to CI/CD Practitioner: One Code Push, Automated Delivery",
    "subtitle": "Final Summary & Next Steps: Mastering the Continuous Delivery Mindset",
    "category": "Mastery & Summary",
    "summaryMapping": [
      {
        "tool": "Git",
        "role": "Tracks every change to code with immutable commit history"
      },
      {
        "tool": "GitHub",
        "role": "Hosts repositories, coordinates team review via Pull Requests"
      },
      {
        "tool": "GitHub Actions",
        "role": "Automates testing, building, and deployment workflows"
      },
      {
        "tool": "Build & Test Tools",
        "role": "Compile code and validate business logic automatically"
      },
      {
        "tool": "Docker",
        "role": "Packages code and dependencies into standardized containers"
      },
      {
        "tool": "Amazon ECR",
        "role": "Securely stores versioned container image artifacts"
      },
      {
        "tool": "Amazon ECS & Cloud",
        "role": "Hosts and scales containerized web services reliably"
      },
      {
        "tool": "Monitoring Tools",
        "role": "Observe metrics, error rates, and trigger automatic rollbacks"
      }
    ],
    "finalAnalogy": "A customer places an order, and the restaurant coordinates prep, taste checks, packaging, and delivery. In software, a developer pushes code, and the pipeline coordinates building, testing, packaging, and cloud deployment.",
    "finalPhilosophy": "CI/CD is not about replacing developers. It is about eliminating repetitive manual delivery friction so engineers can focus on building innovative software.",
    "keyTakeaway": "Mastering CI/CD transforms you into a high-impact engineer capable of delivering reliable software at scale.",
    "image": "/slides/slide_20.png",
    "imageCaption": "Mastery Summary: The Complete DevOps & CI/CD Conveyor Belt from Git Commit to Production Monitoring."
  },
  {
    "num": 21,
    "title": "Thank You & Q&A: Open Questions & Discussion",
    "subtitle": "Congratulations on completing the CI/CD Masterclass! The floor is open for any questions, architecture guidance, and career discussions.",
    "category": "Conclusion & Q&A",
    "detailedPoints": [
      "Congratulations! You have completed the comprehensive 21-slide CI/CD Masterclass from manual friction to automated AWS cloud delivery.",
      "Open Floor for Any Questions: Ask about GitHub Actions, Docker containers, AWS ECS/ECR deployment architectures, or security best practices.",
      "Connect with Instructor Aajera Banu S: AWS & Networking Trainer at LIVEWIRE Salem, Redis Certified Cloud Operator, and Ex-Cloud Engineer Intern at Codec Technologies."
    ],
    "keyTakeaway": "Continuous delivery is an engineering superpower. Automate relentlessly, test thoroughly, and ship to production with fearless confidence!",
    "image": "/slides/slide_21.png",
    "imageCaption": "Thank You & Q&A: Open discussion on CI/CD pipelines, AWS cloud delivery, and modern DevOps careers.",
    "qaTopics": [
      {
        "icon": "GitBranch",
        "title": "1. CI/CD & Pipeline Design",
        "desc": "Questions about GitHub Actions workflows, trunk-based branching, matrix builds, artifact caching, and flaky test mitigation.",
        "sampleQuestions": [
          "How to structure multi-environment stages (Dev -> Staging -> Prod)?",
          "What is the best way to manage reusable GitHub Actions composite steps?"
        ]
      },
      {
        "icon": "Cloud",
        "title": "2. Cloud & Containers (AWS + Docker)",
        "desc": "Questions on multi-stage Docker builds, Amazon ECR registries, ECS Fargate serverless containers, and ALB zero-downtime traffic routing.",
        "sampleQuestions": [
          "How does blue-green deployment compare to canary deployments?",
          "How do we configure zero-downtime rolling updates with ALB health checks?"
        ]
      },
      {
        "icon": "ShieldCheck",
        "title": "3. DevSecOps & Governance",
        "desc": "Questions on eliminating long-lived AWS IAM secret keys via GitHub OIDC OpenID Connect, SAST vulnerability scanning, and audit trails.",
        "sampleQuestions": [
          "How does AWS OIDC temporary token exchange work under the hood?",
          "How to prevent secret leaks and enforce signed commits in team PRs?"
        ]
      },
      {
        "icon": "Compass",
        "title": "4. Career Path & Engineering Leadership",
        "desc": "Discussion on navigating DevOps engineering, AWS Cloud certifications, CCNA networking foundations, and hands-on containerized applications.",
        "sampleQuestions": [
          "How to transition from software engineering into DevOps / Cloud?",
          "How does understanding networking (VLANs, DNS, NAT) accelerate cloud architecture mastery?"
        ]
      }
    ],
    "thankYouHighlights": [
      {
        "title": "Masterclass Complete! 🎉",
        "desc": "You have mastered the mental models, analogies, Git workflows, Docker packaging, and AWS cloud delivery automation."
      },
      {
        "title": "Mentorship & Community 🚀",
        "desc": "Connect with Aajera Banu S on LinkedIn to explore AWS cloud, CCNA networking, Redis, and containerized deployments."
      }
    ],
    "contactChannels": [
      {
        "label": "Instructor",
        "value": "Aajera Banu S",
        "note": "AWS & Networking Trainer at LIVEWIRE Salem"
      },
      {
        "label": "Certification",
        "value": "Redis Certified",
        "note": "Redis Certified Associate Cloud Operator"
      },
      {
        "label": "Experience",
        "value": "Cloud & DevOps",
        "note": "Ex-Cloud Engineer Intern at Codec Technologies India"
      }
    ]
  }
];
