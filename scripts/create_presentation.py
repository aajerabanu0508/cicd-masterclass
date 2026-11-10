#!/usr/bin/env python3
"""
Generate a 21-slide Masterclass PowerPoint (.pptx) with large readable fonts,
clean crisp white modern UI/UX theme, Food Ordering Analogy, and Key Takeaways.
"""

import os
import re
import json
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def clean(text):
    if not isinstance(text, str):
        return "" if text is None else str(text)
    text = re.sub(r'[𐀀-􏿿]', '', text)
    return text.encode('utf-8', 'ignore').decode('utf-8')

BG_WHITE = RGBColor(255, 255, 255)
BG_SLATE_50 = RGBColor(248, 250, 252)
CARD_BG = RGBColor(255, 255, 255)
BORDER_LIGHT = RGBColor(226, 232, 240)
TEXT_DARK = RGBColor(15, 23, 42)
TEXT_BODY = RGBColor(51, 65, 85)
TEXT_MUTED = RGBColor(100, 116, 139)
BLUE_ACCENT = RGBColor(37, 99, 235)
AMBER_ACCENT = RGBColor(217, 119, 6)
EMERALD_ACCENT = RGBColor(5, 150, 105)
ROSE_ACCENT = RGBColor(225, 29, 72)

slides_data = [
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
    "keyTakeaway": "CI/CD is an evolution of collaborative engineering practices, not an invention attributable to one individual."
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
    "keyTakeaway": "CI validates changes; Continuous Delivery prepares software for release; Continuous Deployment puts it into production automatically."
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
    "keyTakeaway": "Git manages versions locally; GitHub hosts repositories centrally and connects code directly to automation engines."
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
    "keyTakeaway": "GitHub Actions is the ideal platform because it eliminates infrastructure overhead by bringing code, review, and automation together."
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
    "keyTakeaway": "A trigger starts the workflow; the runner executes its jobs and steps in an isolated, clean sandbox."
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
    "keyTakeaway": "YAML configuration files are human-readable blueprints that tell cloud runners exactly how to build and verify your software."
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
    "keyTakeaway": "CI gives developers rapid feedback within minutes, stopping broken code before it progresses toward production."
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
    "foodAnalogy": {
      "title": "Franchise Logistics Network \ud83d\ude9a",
      "story": "GitHub Actions coordinates food prep, Amazon ECR is the central cold-storage distribution hub, Amazon ECS is the network of commercial franchise kitchens, and the Load Balancer routes hungry diners.",
      "connection": "GitHub Actions orchestrates the release; AWS provides the scalable cloud infrastructure."
    },
    "keyTakeaway": "GitHub Actions automates the deployment process; cloud providers supply the scalable hosting infrastructure.",
    "image": "/slides/slide_16.png",
    "imageCaption": "AWS Cloud Deployment: GitHub Actions OIDC \u2794 Amazon ECR Registry \u2794 Amazon ECS High-Availability Clusters."
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
    "keyTakeaway": "Automate safely, not just quickly. Security checks and approval gates protect production from catastrophic leaks."
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
    "keyTakeaway": "A reliable pipeline detects failures instantly, stops unsafe rollouts, and supports rapid recovery."
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
    "foodAnalogy": {
      "title": "The Fully Automated Smart Restaurant \ud83c\udf55",
      "story": "Customer orders on phone \u2794 Smart ticket alerts kitchen \u2794 Robotic grill cooks burger \u2794 Optical sensor inspects burger \u2794 Packaged in bento box \u2794 Drone delivers to customer.",
      "connection": "This real-world project unifies version control, automation, containerization, cloud hosting, and observability into one cohesive system."
    },
    "keyTakeaway": "This end-to-end project combines code, CI/CD, containers, cloud infrastructure, and monitoring into a complete production system.",
    "image": "/slides/slide_19.png",
    "imageCaption": "End-to-End Real-World Project: Automated Food Ordering App pipeline running on GitHub Actions and AWS."
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
    "keyTakeaway": "Mastering CI/CD transforms you into a high-impact engineer capable of delivering reliable software at scale."
  }
]

def generate_master_powerpoint():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 0: TITLE & PRESENTER INTRODUCTION (KERTHIK)
    # =========================================================================
    s0 = prs.slides.add_slide(blank_layout)
    bg0 = s0.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg0.fill.solid()
    bg0.fill.fore_color.rgb = BG_WHITE
    bg0.line.fill.background()

    acc0 = s0.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.06))
    acc0.fill.solid()
    acc0.fill.fore_color.rgb = BLUE_ACCENT
    acc0.line.fill.background()

    tb0 = s0.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.733), Inches(1.3))
    tf0 = tb0.text_frame
    tf0.word_wrap = True
    p0 = tf0.paragraphs[0]
    p0.text = clean("CI/CD: From Manual Software Delivery ")
    p0.font.size = Pt(28)
    p0.font.bold = True
    p0.font.color.rgb = TEXT_DARK

    p0_sub = tf0.add_paragraph()
    p0_sub.text = clean("A Complete 20-Slide Masterclass on Continuous Integration, Delivery, and GitHub Actions")
    p0_sub.font.size = Pt(14)
    p0_sub.font.color.rgb = BLUE_ACCENT
    p0_sub.space_before = Pt(4)

    # Left Bio Card
    c0_bio = s0.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.1), Inches(6.0), Inches(4.5))
    c0_bio.fill.solid()
    c0_bio.fill.fore_color.rgb = RGBColor(248, 250, 252)
    c0_bio.line.color.rgb = BLUE_ACCENT
    c0_bio.line.width = Pt(1.5)

    tf_bio = c0_bio.text_frame
    tf_bio.word_wrap = True
    tf_bio.margin_top = Inches(0.25)
    tf_bio.margin_left = Inches(0.3)
    tf_bio.margin_right = Inches(0.3)

    p_badge = tf_bio.paragraphs[0]
    p_badge.text = clean("COURSE CREATOR & INSTRUCTOR")
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = BLUE_ACCENT

    p_name = tf_bio.add_paragraph()
    p_name.text = clean("KERTHIK")
    p_name.font.size = Pt(24)
    p_name.font.bold = True
    p_name.font.color.rgb = TEXT_DARK
    p_name.space_before = Pt(4)

    p_role = tf_bio.add_paragraph()
    p_role.text = clean("Project Manager at TNQ")
    p_role.font.size = Pt(14)
    p_role.font.bold = True
    p_role.font.color.rgb = BLUE_ACCENT
    p_role.space_before = Pt(4)

    p_past = tf_bio.add_paragraph()
    p_past.text = clean("Worked as DevOps Engineer at SentinelFox")
    p_past.font.size = Pt(13)
    p_past.font.color.rgb = TEXT_BODY
    p_past.space_before = Pt(4)

    p_venture = tf_bio.add_paragraph()
    p_venture.text = clean("Building OrivianLabs (DevOps & Cloud Systems Fellowship)")
    p_venture.font.size = Pt(13)
    p_venture.font.bold = True
    p_venture.font.color.rgb = AMBER_ACCENT
    p_venture.space_before = Pt(4)

    p_desc = tf_bio.add_paragraph()
    p_desc.text = clean("Engineering leader focused on production cloud architectures, zero-downtime pipelines, and developer productivity.")
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = TEXT_BODY
    p_desc.space_before = Pt(8)

    # Right Hero Image Card on Slide 0
    hero_img = "/Users/kerthik/Downloads/Playground/cicd-masterclass/public/devops_cicd_intro.jpg"
    if os.path.exists(hero_img):
        s0.shapes.add_picture(hero_img, Inches(7.1), Inches(2.1), width=Inches(5.433), height=Inches(3.8))
        c_hero_cap = s0.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(6.05), Inches(5.433), Inches(0.55))
        c_hero_cap.fill.solid()
        c_hero_cap.fill.fore_color.rgb = RGBColor(240, 249, 255)
        c_hero_cap.line.color.rgb = BLUE_ACCENT
        c_hero_cap.line.width = Pt(1)
        tf_cap = c_hero_cap.text_frame
        tf_cap.word_wrap = True
        p_c = tf_cap.paragraphs[0]
        p_c.text = clean("DevOps CI/CD Conveyor: Git Commit -> Test -> Docker -> AWS")
        p_c.font.size = Pt(9.5)
        p_c.font.color.rgb = TEXT_BODY

    f0 = s0.shapes.add_textbox(Inches(0.8), Inches(6.85), Inches(11.733), Inches(0.35))
    f0.text_frame.paragraphs[0].text = clean("CI/CD Masterclass • Presented by Kerthik (Project Manager at TNQ) • Food Delivery Analogy")
    f0.text_frame.paragraphs[0].font.size = Pt(10)
    f0.text_frame.paragraphs[0].font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDES 1 - 20: LESSON SLIDES
    # =========================================================================
    json_path = "/Users/kerthik/Downloads/Playground/cicd-masterclass/slides_data_content.json"
    active_slides = slides_data
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                active_slides = json.load(f)
        except Exception as e:
            print(f"Using fallback slides_data: {e}")

    for slide_data in active_slides:
        s = prs.slides.add_slide(blank_layout)

        bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_WHITE
        bg.line.fill.background()

        acc = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.35), Inches(11.733), Inches(0.05))
        acc.fill.solid()
        acc.fill.fore_color.rgb = BLUE_ACCENT
        acc.line.fill.background()

        meta = s.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(11.733), Inches(0.3))
        tf_m = meta.text_frame
        p_m = tf_m.paragraphs[0]
        p_m.text = clean(f"SLIDE {slide_data['num']:02d} / 20  •  {slide_data['category'].upper()}")
        p_m.font.size = Pt(11)
        p_m.font.bold = True
        p_m.font.color.rgb = BLUE_ACCENT

        tb = s.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.733), Inches(1.1))
        tf_t = tb.text_frame
        tf_t.word_wrap = True
        p_title = tf_t.paragraphs[0]
        p_title.text = clean(f"Slide {slide_data['num']} — {slide_data['title']}")
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_DARK

        p_sub = tf_t.add_paragraph()
        p_sub.text = clean(slide_data['subtitle'])
        p_sub.font.size = Pt(13)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(3)

        has_image = "image" in slide_data and slide_data["image"]
        left_w = Inches(6.0) if has_image else Inches(11.733)

        c_left = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), left_w, Inches(4.3))
        c_left.fill.solid()
        c_left.fill.fore_color.rgb = RGBColor(248, 250, 252)
        c_left.line.color.rgb = BLUE_ACCENT
        c_left.line.width = Pt(1.5)

        tf_l = c_left.text_frame
        tf_l.word_wrap = True
        tf_l.margin_top = Inches(0.2)
        tf_l.margin_left = Inches(0.25)
        tf_l.margin_right = Inches(0.25)

        p_lh = tf_l.paragraphs[0]
        p_lh.text = clean("CORE CURRICULUM & PRINCIPLES")
        p_lh.font.size = Pt(11)
        p_lh.font.bold = True
        p_lh.font.color.rgb = BLUE_ACCENT

        # Render points
        pts = slide_data.get("detailedPoints") or slide_data.get("contentPoints") or []
        if pts:
            for pt in pts:
                p = tf_l.add_paragraph()
                p.text = clean(f"• {pt}")
                p.font.size = Pt(11.5)
                p.font.color.rgb = TEXT_BODY
                p.space_before = Pt(4)
        elif "problemsList" in slide_data:
            p_subh = tf_l.add_paragraph()
            p_subh.text = clean("Traditional Delivery Breakdowns:")
            p_subh.font.size = Pt(12)
            p_subh.font.bold = True
            p_subh.font.color.rgb = ROSE_ACCENT
            for prob in slide_data["problemsList"]:
                p = tf_l.add_paragraph()
                p.text = clean(f"- {prob}")
                p.font.size = Pt(11)
                p.font.color.rgb = TEXT_BODY
                p.space_before = Pt(2)
        elif "timeline" in slide_data:
            for item in slide_data["timeline"]:
                p = tf_l.add_paragraph()
                p.text = clean(f"* {item['era']} — {item['title']}: {item['desc']}")
                p.font.size = Pt(10.5)
                p.font.color.rgb = TEXT_BODY
                p.space_before = Pt(3)
        elif "comparisonTable" in slide_data:
            for row in slide_data["comparisonTable"]:
                p = tf_l.add_paragraph()
                p.text = clean(f"• {row['aspect']}: {row['after']}")
                p.font.size = Pt(11)
                p.font.bold = True
                p.font.color.rgb = TEXT_DARK
                p.space_before = Pt(3)
        elif "concepts" in slide_data:
            for c in slide_data["concepts"]:
                p = tf_l.add_paragraph()
                p.text = clean(f"• {c['term']}: {c['desc']}")
                p.font.size = Pt(10.5)
                p.font.color.rgb = TEXT_BODY
                p.space_before = Pt(3)

        # Right side: Image if present, else Food Analogy card
        if has_image:
            img_rel = slide_data["image"].lstrip("/")
            img_abs = os.path.join("/Users/kerthik/Downloads/Playground/cicd-masterclass/public", img_rel)
            if os.path.exists(img_abs):
                s.shapes.add_picture(img_abs, Inches(7.1), Inches(1.85), width=Inches(5.433), height=Inches(3.75))
                c_cap = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(5.65), Inches(5.433), Inches(0.55))
                c_cap.fill.solid()
                c_cap.fill.fore_color.rgb = RGBColor(240, 249, 255)
                c_cap.line.color.rgb = BLUE_ACCENT
                c_cap.line.width = Pt(1)
                tf_cap = c_cap.text_frame
                tf_cap.word_wrap = True
                p_c = tf_cap.paragraphs[0]
                p_c.text = clean(f"Architecture Diagram: {slide_data.get('imageCaption', '')}")
                p_c.font.size = Pt(9.5)
                p_c.font.color.rgb = TEXT_BODY
        elif "foodAnalogy" in slide_data:
            c_right = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(1.85), Inches(4.733), Inches(4.3))
            c_right.fill.solid()
            c_right.fill.fore_color.rgb = RGBColor(254, 252, 246)
            c_right.line.color.rgb = AMBER_ACCENT
            c_right.line.width = Pt(1.5)

            tf_r = c_right.text_frame
            tf_r.word_wrap = True
            tf_r.margin_top = Inches(0.2)
            tf_r.margin_left = Inches(0.25)
            tf_r.margin_right = Inches(0.25)

            fa = slide_data["foodAnalogy"]
            p_rh = tf_r.paragraphs[0]
            p_rh.text = clean("FOOD-ORDERING ANALOGY")
            p_rh.font.size = Pt(11)
            p_rh.font.bold = True
            p_rh.font.color.rgb = AMBER_ACCENT

            p_fa_title = tf_r.add_paragraph()
            p_fa_title.text = clean(fa.get("title", "Restaurant Analogy"))
            p_fa_title.font.size = Pt(13)
            p_fa_title.font.bold = True
            p_fa_title.font.color.rgb = TEXT_DARK
            p_fa_title.space_before = Pt(3)

            p_fa_story = tf_r.add_paragraph()
            p_fa_story.text = clean(fa.get("story", ""))
            p_fa_story.font.size = Pt(11.5)
            p_fa_story.font.color.rgb = TEXT_BODY
            p_fa_story.space_before = Pt(3)

        # Bottom Takeaway Card
        c_bot = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.7))
        c_bot.fill.solid()
        c_bot.fill.fore_color.rgb = RGBColor(240, 253, 244)
        c_bot.line.color.rgb = EMERALD_ACCENT
        c_bot.line.width = Pt(1)

        tf_b = c_bot.text_frame
        tf_b.word_wrap = True
        tf_b.margin_top = Inches(0.12)
        tf_b.margin_left = Inches(0.2)
        tf_b.margin_right = Inches(0.2)

        p_bot = tf_b.paragraphs[0]
        p_bot.text = clean(f"KEY TAKEAWAY: {slide_data['keyTakeaway']}")
        p_bot.font.size = Pt(12)
        p_bot.font.bold = True
        p_bot.font.color.rgb = RGBColor(6, 95, 70)

    pub_path = "/Users/kerthik/Downloads/Playground/cicd-masterclass/public/CICD_Masterclass_20_Slides.pptx"
    root_path = "/Users/kerthik/Downloads/Playground/cicd-masterclass/CICD_Masterclass_20_Slides.pptx"
    prs.save(pub_path)
    prs.save(root_path)
    print("Master 21-slide PowerPoint file successfully regenerated with embedded images!")

if __name__ == "__main__":
    generate_master_powerpoint()
