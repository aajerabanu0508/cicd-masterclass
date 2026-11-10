#!/usr/bin/env python3
"""
Generate a 10-slide Deployment Masterclass PowerPoint (.pptx)
Covering Manual Deployment vs Automated CI/CD Deployment with modern UI/UX theme,
embedded high-resolution diagram images, Food & Real-World Analogies, and Key Takeaways.
"""

import os
import re
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def clean(text):
    if not isinstance(text, str):
        return "" if text is None else str(text)
    text = re.sub(r'[𐀀-]', '', text)
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
PURPLE_ACCENT = RGBColor(124, 58, 237)

deployment_slides_data = [
    {
        "num": 1,
        "title": "Software Deployment: The Critical Final Mile",
        "subtitle": "How Code Transitions from Developer Repositories into Live User-Facing Services",
        "category": "Deployment Core",
        "contentPoints": [
            "Software deployment is the operational process of transferring built artifacts into live execution environments.",
            "Covers artifact compilation, environment provisioning, database migrations, runtime configuration, and service startup.",
            "Crucial Distinction: 'Deployment' is technical installation onto servers; 'Release' is exposing features to customers.",
            "The Modern Benchmark: Zero-downtime, fully automated, version-controlled, and instantly reversible."
        ],
        "keyTakeaway": "Deployment is the single highest-risk event in software engineering—mastering automation eliminates release anxiety.",
        "image": "/slides/deployment/slide_1.png",
        "imageCaption": "Continuous Deployment Path: Local Build -> Container Package -> Cloud Target -> Health Checks -> Live Traffic (200 OK)."
    },
    {
        "num": 2,
        "title": "The Manual Deployment Era: The 8-Step Gauntlet",
        "subtitle": "The Risky, Multi-Hour Release Ceremony Before DevOps Automation",
        "category": "Manual Process",
        "contentPoints": [
            "Step 1 & 2: Local build on developer laptop followed by manual FTP/SCP zip transfer to servers.",
            "Step 3 & 4: Root terminal SSH login (`ssh root@prod`) and manual tarball extraction into web directories.",
            "Step 5 & 6: Live nano/vim edits of production `.env` files and manual execution of SQL database migrations.",
            "Step 7 & 8: Manual service restart (`systemctl restart nginx && pm2 restart all`) dropping active user requests."
        ],
        "keyTakeaway": "Manual deployment relies 100% on human perfection under stress—an inevitable recipe for production failure.",
        "image": "/slides/deployment/slide_2.png",
        "imageCaption": "The 8-Step Manual Gauntlet: High human friction, zero automated audit trail, and frequent outages."
    },
    {
        "num": 3,
        "title": "Fatal Bottlenecks: Why Manual Deployments Fail",
        "subtitle": "Downtime, Rollback Nightmares, Configuration Drift, and Team Burnout",
        "category": "Failure Analysis",
        "contentPoints": [
            "Configuration Drift: Staging OS or Node versions differ from prod; code works on dev machines but fails live.",
            "Typo Disasters: A single misplaced semicolon, bad path, or `chmod -R 777` introduces catastrophic security leaks.",
            "2:00 AM Maintenance Windows: Engineers deploy late at night during weekends, leading to sleep deprivation and errors.",
            "Rollback Paralysis: Reverting broken releases requires re-uploading old zips and manual database reversals."
        ],
        "keyTakeaway": "Manual deployments don't just cause downtime—they create release fear that paralyzes business velocity.",
        "image": "/slides/deployment/slide_3.png",
        "imageCaption": "The 4 Pillars of Manual Release Failure: Drift, Typos, 2 AM Downtime, and Rollback Nightmares."
    },
    {
        "num": 4,
        "title": "Automated Deployment Pipeline: Declarative & Repeatable",
        "subtitle": "Transforming Fragile Manual Steps into Repeatable, Version-Controlled Automation",
        "category": "CI/CD Automation",
        "contentPoints": [
            "Git Webhook Trigger: Code commit to `main` branch or release tag triggers automated CI/CD execution.",
            "Automated Test Gate: Unit, integration, and security scans run in isolated runner environments.",
            "Immutable Containerization: Application packaged into Docker image tagged with Git commit SHA-256.",
            "Continuous Delivery vs Deployment: CDel keeps software continuously deployable; CDep ships automatically to prod."
        ],
        "keyTakeaway": "Automated pipelines turn deployments into boring, predictable, everyday non-events.",
        "image": "/slides/deployment/slide_4.png",
        "imageCaption": "Modern CI/CD Flow: Trigger -> Automated Tests -> Docker Build -> Staging Verification -> Zero-Downtime Prod."
    },
    {
        "num": 5,
        "title": "Zero-Downtime Strategies: Rolling vs. Blue-Green",
        "subtitle": "Updating Production Services Without Dropping a Single Live User Request",
        "category": "Deployment Patterns",
        "contentPoints": [
            "Rolling Deployment: Updates instances gradually (e.g. 25% at a time) behind load balancer without doubling hardware costs.",
            "Connection Draining: Old instances finish active HTTP requests while new instances pass readiness health probes.",
            "Blue-Green Deployment: Two identical environments; Blue runs live v1.0, Green deploys v2.0 in complete isolation.",
            "1-Second Rollback: Router flips 100% traffic instantly to Green; if errors spike, flips back to Blue with zero data loss."
        ],
        "keyTakeaway": "Zero-downtime releases eliminate weekend maintenance—teams comfortably deploy during normal office hours.",
        "image": "/slides/deployment/slide_5.png",
        "imageCaption": "Rolling (Incremental capacity upgrade) vs. Blue-Green (Complete isolated environment flip)."
    },
    {
        "num": 6,
        "title": "Progressive Delivery: Canary Releases & Feature Flags",
        "subtitle": "Safely Exposing New Code to Real Production Traffic in Increments",
        "category": "Traffic Shifting",
        "contentPoints": [
            "Canary Releases: Route 2% to 5% of real user traffic to new canary instance while 95% remains on rock-solid stable version.",
            "Automated Telemetry: APM monitors HTTP 500 error rates, p99 latency, and CPU metrics before stepping traffic up.",
            "Auto-Drain: If error rate spikes, canary traffic drops to 0% in seconds, protecting 98% of users from experiencing bugs.",
            "Feature Flags: Decouple deployment from release; deploy code dark and toggle features via runtime boolean switches."
        ],
        "keyTakeaway": "Progressive delivery shifts testing into production safely, reducing blast radius to near zero.",
        "image": "/slides/deployment/slide_6.png",
        "imageCaption": "Canary Traffic Slicing (2% -> 25% -> 100%) and Feature Flag Dark Launching Architecture."
    },
    {
        "num": 7,
        "title": "Containerized & Cloud-Native Deployment",
        "subtitle": "Immutable Infrastructure: Replacing Fragile Servers with Ephemeral Containers",
        "category": "Cloud & Containers",
        "contentPoints": [
            "Immutable Infrastructure: Never patch live servers in place; build a new Docker image and replace containers entirely.",
            "Secure Container Registries: AWS ECR, Docker Hub, and GitHub Packages store signed, vulnerability-scanned images.",
            "Kubernetes Orchestration: Declarative YAML manifests, self-healing pod restarts, and horizontal auto-scaling.",
            "Serverless & Edge Platforms: AWS Lambda, Vercel, and Cloudflare Workers offer atomic deploys with zero server maintenance."
        ],
        "keyTakeaway": "Containers guarantee environment parity: the exact image tested in staging executes identically in production.",
        "image": "/slides/deployment/slide_7.png",
        "imageCaption": "The 3 Pillars: Immutable Docker Images, Kubernetes Orchestration, and Serverless Edge Delivery."
    },
    {
        "num": 8,
        "title": "GitOps: Git as the Single Source of Truth",
        "subtitle": "Declarative Cloud Delivery, Automated Drift Detection, and Self-Healing Infrastructure",
        "category": "GitOps Engine",
        "contentPoints": [
            "Traditional CI Push Model: CI server holds cluster credentials and runs `kubectl apply`—a security risk if compromised.",
            "GitOps Pull Model (ArgoCD / Flux): In-cluster operator pulls changes from Git without exposing cluster credentials.",
            "Automated Drift Healing: If someone manually alters a pod via `kubectl`, ArgoCD immediately reconciles it back to Git state.",
            "Instant 1-Click Rollback: Running `git revert <commit>` auto-reconciles production cloud clusters across all regions."
        ],
        "keyTakeaway": "Deploying to production cloud with GitOps is as safe, reviewed, and auditable as approving a Git Pull Request.",
        "image": "/slides/deployment/slide_8.png",
        "imageCaption": "Traditional Push vs. Modern In-Cluster GitOps Pull Model with Continuous Drift Reconciliation."
    },
    {
        "num": 9,
        "title": "Database Migrations, Secrets & Health Verification",
        "subtitle": "Solving the Toughest Challenges in Automated Zero-Downtime Deployment",
        "category": "Zero-Downtime Data",
        "contentPoints": [
            "Expand-and-Contract Pattern: Add nullable column -> deploy code reading both -> backfill data -> drop old column.",
            "Secrets Externalization: Never store credentials in Git; inject at runtime via HashiCorp Vault, AWS Secrets Manager, or OIDC.",
            "Liveness vs Readiness Probes: Liveness restarts crashed processes; Readiness checks DB connectivity before routing traffic.",
            "Automated Rollback Triggers: If HTTP 5xx errors exceed 1% for 60 seconds, pipeline auto-rolls back without human delay."
        ],
        "keyTakeaway": "Production safety requires decoupled databases, externalized secrets, and automated health checks.",
        "image": "/slides/deployment/slide_9.png",
        "imageCaption": "Expand-and-Contract Zero-Downtime Database Pattern & Health Probe Rollback Triggers."
    },
    {
        "num": 10,
        "title": "Manual vs. Automated Deployment: The Master Comparison",
        "subtitle": "Metrics, Cultural Transformation, and Golden Rules for Production Excellence",
        "category": "Master Comparison",
        "contentPoints": [
            "Release Frequency: Manual (1x per 3 months) vs. Automated (multiple times per day on-demand).",
            "Lead Time for Changes: Manual (weeks/months of planning) vs. Automated (< 15 minutes from commit to production).",
            "Change Failure Rate: Manual (30% - 50% defect rate) vs. Automated (< 5% elite DORA standard).",
            "Mean Time to Recovery (MTTR): Manual (hours/days of outage) vs. Automated (< 60 seconds instant rollback)."
        ],
        "keyTakeaway": "Automating deployment is not just a tooling change—it is a cultural revolution that enables fearless innovation.",
        "image": "/slides/deployment/slide_10.png",
        "imageCaption": "8-Dimension Comparison Matrix: Manual Delivery Breakdown vs. Modern CI/CD Automated Excellence."
    }
]

def generate_deployment_powerpoint():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Slide 0: Title & Presenter Intro Slide
    s0 = prs.slides.add_slide(blank_layout)
    bg0 = s0.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg0.fill.solid()
    bg0.fill.fore_color.rgb = BG_SLATE_50
    bg0.line.fill.background()

    # Title Card
    c_title = s0.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.8), Inches(11.333), Inches(2.2))
    c_title.fill.solid()
    c_title.fill.fore_color.rgb = BG_WHITE
    c_title.line.color.rgb = BLUE_ACCENT
    c_title.line.width = Pt(2)
    tf0 = c_title.text_frame
    tf0.word_wrap = True

    p0_cat = tf0.paragraphs[0]
    p0_cat.text = "DEVOPS & CLOUD ARCHITECTURE MASTERCLASS"
    p0_cat.font.size = Pt(12)
    p0_cat.font.bold = True
    p0_cat.font.color.rgb = BLUE_ACCENT

    p0_t = tf0.add_paragraph()
    p0_t.text = "Software Deployment Masterclass: Manual vs. Automated CI/CD"
    p0_t.font.size = Pt(26)
    p0_t.font.bold = True
    p0_t.font.color.rgb = TEXT_DARK
    p0_t.space_before = Pt(6)

    p0_sub = tf0.add_paragraph()
    p0_sub.text = "From High-Risk 2:00 AM Manual FTP/SSH Scripts to Zero-Downtime Automated Kubernetes & GitOps Delivery"
    p0_sub.font.size = Pt(14)
    p0_sub.font.color.rgb = TEXT_MUTED
    p0_sub.space_before = Pt(4)

    # Presenter Card
    c_pres = s0.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(3.2), Inches(11.333), Inches(3.5))
    c_pres.fill.solid()
    c_pres.fill.fore_color.rgb = BG_WHITE
    c_pres.line.color.rgb = BORDER_LIGHT
    c_pres.line.width = Pt(1.5)
    tf_p = c_pres.text_frame
    tf_p.word_wrap = True

    p_phead = tf_p.paragraphs[0]
    p_phead.text = "INSTRUCTOR & INDUSTRY TRACK RECORD"
    p_phead.font.size = Pt(12)
    p_phead.font.bold = True
    p_phead.font.color.rgb = AMBER_ACCENT

    p_pname = tf_p.add_paragraph()
    p_pname.text = "Aajera Banu S (She/Her) — AWS & Networking Trainer"
    p_pname.font.size = Pt(20)
    p_pname.font.bold = True
    p_pname.font.color.rgb = TEXT_DARK
    p_pname.space_before = Pt(4)

    experiences = [
        ("Current Leadership Role", "AWS & Networking Trainer at LIVEWIRE Salem", "Training students in AWS Cloud (EC2, S3, VPC, IAM) and Cisco CCNA networking (routing, switching, subnetting, TCP/IP, VLANs, ACLs, and NAT)."),
        ("Industry Certification", "Redis Certified Associate Cloud Operator", "Specializing in Redis Cloud architecture, high availability, in-memory caching, and distributed performance optimization."),
        ("DevOps & Cloud Roots", "Ex-Cloud Engineer Intern at Codec Technologies India", "Architected microservices e-commerce platform using Docker, Docker Compose, AWS ECS Fargate, Nginx reverse proxy, and Prometheus/Grafana.")
    ]

    for badge, title, desc in experiences:
        p_exp = tf_p.add_paragraph()
        p_exp.text = f"• [{badge}] {title}: {desc}"
        p_exp.font.size = Pt(12)
        p_exp.font.color.rgb = TEXT_BODY
        p_exp.space_before = Pt(6)

    # 10 Content Slides
    for slide_data in deployment_slides_data:
        s = prs.slides.add_slide(blank_layout)

        # Background
        bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_SLATE_50
        bg.line.fill.background()

        # Header Card
        c_top = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.25))
        c_top.fill.solid()
        c_top.fill.fore_color.rgb = BG_WHITE
        c_top.line.color.rgb = BORDER_LIGHT
        c_top.line.width = Pt(1)

        tf_t = c_top.text_frame
        tf_t.word_wrap = True
        tf_t.margin_top = Inches(0.12)
        tf_t.margin_left = Inches(0.2)
        tf_t.margin_right = Inches(0.2)

        p_cat = tf_t.paragraphs[0]
        p_cat.text = clean(f"SLIDE {slide_data['num']} OF 10  •  {slide_data['category'].upper()}  •  DEPLOYMENT MASTERCLASS")
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = BLUE_ACCENT

        p_title = tf_t.add_paragraph()
        p_title.text = clean(f"{slide_data['num']}. {slide_data['title']}")
        p_title.font.size = Pt(17)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_DARK
        p_title.space_before = Pt(2)

        p_sub = tf_t.add_paragraph()
        p_sub.text = clean(slide_data['subtitle'])
        p_sub.font.size = Pt(11.5)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(2)

        # Left Side: Content Points Card
        c_left = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.9), Inches(4.35))
        c_left.fill.solid()
        c_left.fill.fore_color.rgb = RGBColor(248, 250, 252)
        c_left.line.color.rgb = BLUE_ACCENT
        c_left.line.width = Pt(1.5)

        tf_l = c_left.text_frame
        tf_l.word_wrap = True
        tf_l.margin_top = Inches(0.18)
        tf_l.margin_left = Inches(0.22)
        tf_l.margin_right = Inches(0.22)

        p_lh = tf_l.paragraphs[0]
        p_lh.text = clean("KEY CONCEPTS & ARCHITECTURE")
        p_lh.font.size = Pt(11)
        p_lh.font.bold = True
        p_lh.font.color.rgb = BLUE_ACCENT

        pts = slide_data.get("contentPoints", [])
        for pt in pts:
            p = tf_l.add_paragraph()
            p.text = clean(f"• {pt}")
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_BODY
            p.space_before = Pt(6)

        # Right Side: Image Card
        img_rel = slide_data["image"].lstrip("/")
        img_abs = os.path.join("/Users/kerthik/Downloads/Playground/cicd-masterclass/public", img_rel)
        if os.path.exists(img_abs):
            s.shapes.add_picture(img_abs, Inches(6.9), Inches(1.8), width=Inches(5.633), height=Inches(3.7))
            c_cap = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(5.6), Inches(5.633), Inches(0.55))
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

        # Bottom Takeaway Card
        c_bot = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.7))
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
        p_bot.font.size = Pt(11.5)
        p_bot.font.bold = True
        p_bot.font.color.rgb = RGBColor(6, 95, 70)

    pub_path = "/Users/kerthik/Downloads/Playground/cicd-masterclass/public/Deployment_Masterclass_10_Slides.pptx"
    root_path = "/Users/kerthik/Downloads/Playground/cicd-masterclass/Deployment_Masterclass_10_Slides.pptx"
    prs.save(pub_path)
    prs.save(root_path)
    print("Deployment Masterclass 10-slide PowerPoint file successfully generated!")

if __name__ == "__main__":
    generate_deployment_powerpoint()

