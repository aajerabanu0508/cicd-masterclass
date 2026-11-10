#!/usr/bin/env python3
"""
Generate 10 ultra-clear, high-resolution diagram images for the Deployment Masterclass
(Manual Deployment vs Automated CI/CD Deployment).
Saved to: public/slides/deployment/slide_1.png ... slide_10.png
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "/Users/kerthik/Downloads/Playground/cicd-masterclass/public/slides/deployment"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1600x1000 High-Resolution Canvas
W, H = 1600, 1000

# TrueType Fonts
FONT_BOLD_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BLACK_PATH = "/System/Library/Fonts/Supplemental/Arial Black.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        try:
            return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", size)
        except Exception:
            return ImageFont.load_default()

font_title = get_font(FONT_BLACK_PATH, 32)
font_cat = get_font(FONT_BOLD_PATH, 20)
font_head = get_font(FONT_BOLD_PATH, 24)
font_sub = get_font(FONT_BOLD_PATH, 20)
font_body = get_font(FONT_REG_PATH, 19)
font_body_bold = get_font(FONT_BOLD_PATH, 20)
font_badge = get_font(FONT_BOLD_PATH, 18)
font_footer = get_font(FONT_BOLD_PATH, 22)
font_mono = get_font(FONT_BOLD_PATH, 17)

def draw_wrapped_text(d, text, x, y, max_width, font, fill, line_spacing=6):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = d.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                lines.append(word)
                current_line = []
    if current_line:
        lines.append(' '.join(current_line))
    
    curr_y = y
    for line in lines:
        d.text((x, curr_y), line, font=font, fill=fill)
        bbox = d.textbbox((0, 0), line, font=font)
        curr_y += (bbox[3] - bbox[1]) + line_spacing
    return curr_y

def draw_base_card(title, category, badge_color=(37, 99, 235)):
    img = Image.new('RGB', (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Clean gradient background
    for y in range(H):
        r = int(248 + (255 - 248) * (y / H))
        g = int(250 + (255 - 250) * (y / H))
        b = int(252 + (255 - 252) * (y / H))
        d.line([(0, y), (W, y)], fill=(r, g, b))

    # Outer border
    d.rounded_rectangle([(16, 16), (W - 16, H - 16)], radius=24, outline=(226, 232, 240), width=3)

    # Top banner container
    d.rounded_rectangle([(36, 36), (W - 36, 126)], radius=18, fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    
    # Category pill
    cat_text = category.upper()
    cat_bbox = d.textbbox((0, 0), cat_text, font=font_cat)
    cat_w = cat_bbox[2] - cat_bbox[0] + 36
    d.rounded_rectangle([(56, 52), (56 + cat_w, 110)], radius=12, fill=badge_color)
    d.text((74, 66), cat_text, fill=(255, 255, 255), font=font_cat)
    
    # Title in banner
    d.text((56 + cat_w + 24, 62), title, fill=(15, 23, 42), font=font_title)

    return img, d

def draw_footer_badge(d, text, color=(37, 99, 235), bg_color=(239, 246, 255)):
    foot_y = 880
    d.rounded_rectangle([(46, foot_y + 4), (W - 46, foot_y + 84)], radius=18, fill=(226, 232, 240))
    d.rounded_rectangle([(50, foot_y), (W - 50, foot_y + 80)], radius=18, fill=bg_color, outline=color, width=3)
    bbox = d.textbbox((0, 0), text, font=font_footer)
    tw = bbox[2] - bbox[0]
    d.text(((W - tw) // 2, foot_y + 26), text, fill=color, font=font_footer)


# =========================================================================
# 10 SLIDES CONFIGURATION & GENERATOR
# =========================================================================

slides = [
    # ---------------------------------------------------------------------
    # Slide 1: Software Deployment Architecture & Overview
    # ---------------------------------------------------------------------
    {
        "id": 1,
        "title": "Software Deployment: Transition from Code to Live Service",
        "category": "Deployment Core",
        "color": (37, 99, 235),
        "draw": "flow_5",
        "steps": [
            ("1. Local Build", "Compile & Bundle", "npm run build / jar", (37, 99, 235)),
            ("2. Packaging", "Immutable Artifact", "Docker / Tarball / Zip", (14, 165, 233)),
            ("3. Target Cloud", "Staging / Prod", "AWS / K8s / ECS / VM", (139, 92, 246)),
            ("4. Health Check", "Liveness & Probes", "200 OK Verification", (16, 185, 129)),
            ("5. Live Traffic", "Load Balancer Switch", "Live to End Users", (245, 158, 11))
        ],
        "footer": "Deployment is the technical installation of software; Release is exposing it to end users."
    },

    # ---------------------------------------------------------------------
    # Slide 2: Manual EC2 Deployment: Push & SSH Routine
    # ---------------------------------------------------------------------
    {
        "id": 2,
        "title": "Manual EC2 Deployment: The 'Push & SSH' Routine",
        "category": "Manual Process",
        "color": (225, 29, 72),
        "draw": "grid_8",
        "items": [
            ("1. Push to GitHub", "Developer runs git add, commit, and git push origin main.", (37, 99, 235)),
            ("2. SSH into EC2", "Run ssh -i my-key.pem ubuntu@ec2-ip in live terminal.", (225, 29, 72)),
            ("3. Install Tools", "Run sudo apt update && apt install -y git nodejs npm.", (217, 119, 6)),
            ("4. Git Pull Code", "cd /home/ubuntu/app && git pull origin main (resolve conflicts).", (234, 88, 12)),
            ("5. Nano .env Setup", "Live typing DB password & secret keys into .env with nano.", (225, 29, 72)),
            ("6. Build on EC2", "Run npm install && npm run build (100% CPU/RAM spike).", (219, 39, 119)),
            ("7. Restart Service", "Run pm2 restart app or systemctl restart (Drops active requests).", (147, 51, 234)),
            ("8. Nginx Proxy & Test", "Configure Nginx proxy to :3000 and refresh browser manually.", (100, 116, 139))
        ],
        "footer": "Manual SSH deployments force engineers to babysit servers by hand — fragile and risky."
    },

    # ---------------------------------------------------------------------
    # Slide 3: Why Manual EC2 Deployments Fail at Scale
    # ---------------------------------------------------------------------
    {
        "id": 3,
        "title": "Why Manual EC2 Deployments Fail at Scale",
        "category": "Failure Analysis",
        "color": (225, 29, 72),
        "draw": "cards_4",
        "cards": [
            ("1. OOM Server Freezes on Build", "Running npm run build directly on EC2 consumes all RAM, triggering Linux OOM Killer. The build crashes and the live web server is terminated.", (225, 29, 72)),
            ("2. Multi-Server Scaling Nightmare", "When you have 5 or 10 EC2 instances behind an AWS Load Balancer, you must SSH into each server individually and run git pull 10 times by hand.", (234, 88, 12)),
            ("3. SSH Key & Plaintext Credential Leaks", "Sensitive .pem private keys stored on unencrypted laptops. Production database passwords and API tokens sit in plaintext .env files on EC2.", (147, 51, 234)),
            ("4. Broken Half-State & Zero Rollback", "If git pull has a merge conflict or npm install fails midway, production is left in a broken half-deployed state with no automated rollback mechanism.", (219, 39, 119))
        ],
        "footer": "Never build code on production servers — build immutable containers in CI and deploy pre-built artifacts."
    },

    # ---------------------------------------------------------------------
    # Slide 4: Automated Deployment: Modern CI/CD Pipeline
    # ---------------------------------------------------------------------
    {
        "id": 4,
        "title": "Automated Deployment Pipeline: Declarative & Repeatable",
        "category": "CI/CD Automation",
        "color": (16, 185, 129),
        "draw": "flow_5",
        "steps": [
            ("1. Git Commit", "Push to main/tag", "Webhook Triggered", (37, 99, 235)),
            ("2. Automated CI", "Jest, PyTest & Lint", "100% Tests Pass", (16, 185, 129)),
            ("3. Container Build", "Docker SHA Image", "Push to AWS ECR", (139, 92, 246)),
            ("4. Staging Deploy", "Automated E2E Run", "Sanity Verified", (14, 165, 233)),
            ("5. Zero-Downtime Prod", "Rolling / Blue-Green", "Auto Health Probe", (5, 150, 105))
        ],
        "footer": "Continuous Delivery keeps code releasable; Continuous Deployment ships it automatically."
    },

    # ---------------------------------------------------------------------
    # Slide 5: Zero-Downtime: Rolling vs. Blue/Green Deployments
    # ---------------------------------------------------------------------
    {
        "id": 5,
        "title": "Zero-Downtime Strategies: Rolling vs. Blue-Green",
        "category": "Deployment Patterns",
        "color": (79, 70, 229),
        "draw": "split_2",
        "left_title": "Rolling Deployment (Incremental)",
        "left_badge": "Cost Efficient • Zero Downtime",
        "left_color": (37, 99, 235),
        "left_items": [
            "• Instances updated gradually behind load balancer (e.g. 25% at a time)",
            "• Old instances drain existing connections cleanly before termination",
            "• New instances must pass readiness probes before receiving traffic",
            "• Advantage: Uses existing cluster capacity without doubling cloud costs",
            "• Requirement: API and database must support v1 and v2 simultaneously"
        ],
        "right_title": "Blue-Green Deployment (Environment Swap)",
        "right_badge": "Instant Rollback • 100% Isolation",
        "right_color": (16, 185, 129),
        "right_items": [
            "• Two identical environments: Blue (active v1.0) and Green (idle v2.0)",
            "• Deploy v2.0 onto Green; execute full automated smoke tests in isolation",
            "• Router / Load balancer switches 100% of live traffic to Green instantly",
            "• Instant 1-Second Rollback: Flip router back to Blue if errors spike",
            "• Advantage: Zero downtime and zero mixed-version traffic state"
        ],
        "footer": "Zero-downtime releases eliminate scheduled maintenance windows — deploy during normal working hours."
    },

    # ---------------------------------------------------------------------
    # Slide 6: Progressive Delivery: Canary Releases & Feature Flags
    # ---------------------------------------------------------------------
    {
        "id": 6,
        "title": "Progressive Delivery: Canary Releases & Feature Flags",
        "category": "Traffic Shifting",
        "color": (217, 119, 6),
        "draw": "split_2",
        "left_title": "Canary Releases (Traffic Slicing)",
        "left_badge": "Risk Mitigation • 2% to 100%",
        "left_color": (217, 119, 6),
        "left_items": [
            "• Route small % of real traffic (e.g. 2% to 5%) to new version (Canary)",
            "• 98% of users remain on verified, rock-solid stable production version",
            "• APM monitors real-time telemetry: HTTP 500 error rates, latency (p99)",
            "• Automated Scaling: Step up traffic 5% -> 25% -> 50% -> 100% automatically",
            "• Auto-Drain: If error rate spikes, canary traffic drops to 0% in seconds"
        ],
        "right_title": "Feature Flags (Decoupled Release)",
        "right_badge": "Dark Launching • Instant Toggle",
        "right_color": (139, 92, 246),
        "right_items": [
            "• Code is deployed dormant behind a runtime boolean toggle switch",
            "• Decouples technical deployment from user-facing feature release",
            "• Enable feature for internal QA, beta users, or specific geographic regions",
            "• Kill Switch: Disable broken features in milliseconds without redeployment",
            "• Tools: LaunchDarkly, Unleash, Flagsmith, PostHog"
        ],
        "footer": "Testing in production safely: limit blast radius so any defect only affects a tiny fraction of users."
    },

    # ---------------------------------------------------------------------
    # Slide 7: Containers & Cloud Orchestration: Docker, Kubernetes & Serverless
    # ---------------------------------------------------------------------
    {
        "id": 7,
        "title": "Containerized & Cloud-Native Deployment",
        "category": "Cloud & Containers",
        "color": (14, 165, 233),
        "draw": "pillars_3",
        "pillars": [
            ("1. Immutable Containers", "Docker & OCI Images", [
                "• Never SSH into live servers to patch code",
                "• Package OS, runtime & code into image",
                "• Tagged with git commit SHA-256",
                "• Stored in secure registry (ECR, DockerHub)",
                "• 100% environment parity (dev = prod)"
            ], (14, 165, 233)),
            ("2. Kubernetes Orchestration", "Pods, Replicas & Probes", [
                "• Declarative YAML manifests in git",
                "• Auto-healing: restarts failed containers",
                "• Rolling updates with zero dropped requests",
                "• Horizontal Pod Autoscaler (HPA)",
                "• Ingress routing & TLS termination"
            ], (37, 99, 235)),
            ("3. Serverless & Edge", "AWS Lambda, Vercel & Workers", [
                "• Zero server management or patching",
                "• Atomic deployments with instant preview URLs",
                "• Automatic scaling from 0 to 100k requests",
                "• Instant global edge CDN distribution",
                "• Pay strictly for execution milliseconds"
            ], (139, 92, 246))
        ],
        "footer": "Containers make deployments disposable and reproducible — replace entire containers, never patch in place."
    },

    # ---------------------------------------------------------------------
    # Slide 8: GitOps & Declarative Delivery: ArgoCD & Flux
    # ---------------------------------------------------------------------
    {
        "id": 8,
        "title": "GitOps: Git as the Single Source of Truth",
        "category": "GitOps Engine",
        "color": (234, 88, 12),
        "draw": "split_2",
        "left_title": "Traditional CI Push Model",
        "left_badge": "External Runner • Security Risk",
        "left_color": (225, 29, 72),
        "left_items": [
            "• CI server (GitHub Actions / Jenkins) runs kubectl apply over internet",
            "• Requires storing cluster admin credentials inside CI runner (high risk)",
            "• Vulnerable to credential leakage if CI build runner is compromised",
            "• No automated detection if someone makes manual changes in cluster",
            "• Hard to audit who modified live production manifests"
        ],
        "right_title": "Modern GitOps Pull Model (ArgoCD / Flux)",
        "right_badge": "In-Cluster Operator • Self-Healing",
        "right_color": (16, 185, 129),
        "right_items": [
            "• Git repository holds 100% of desired state (Kubernetes YAML / Helm)",
            "• Operator runs INSIDE cluster: no external credentials exposed",
            "• Continuously compares desired state in Git with live cluster state",
            "• Automated Drift Healing: reverts unauthorized manual changes immediately",
            "• Instant Rollback: git revert <commit> auto-reconciles production cluster"
        ],
        "footer": "Deploying to production cloud is as simple and auditable as approving a Git Pull Request."
    },

    # ---------------------------------------------------------------------
    # Slide 9: Database Migrations, Secrets & Health Verification
    # ---------------------------------------------------------------------
    {
        "id": 9,
        "title": "Database Migrations, Secrets & Health Verification",
        "category": "Zero-Downtime Data",
        "color": (147, 51, 234),
        "draw": "pillars_3",
        "pillars": [
            ("1. DB Expand / Contract", "Zero-Downtime Schema", [
                "• Phase 1: Add new nullable column",
                "• Phase 2: Deploy code writing to both",
                "• Phase 3: Background backfill data",
                "• Phase 4: Deploy code reading new",
                "• Phase 5: Drop old column safely"
            ], (147, 51, 234)),
            ("2. Secrets Management", "Zero Secrets in Git", [
                "• Never hardcode passwords in repos",
                "• Injected at runtime via Vault / AWS SM",
                "• Short-lived OIDC tokens for CI/CD",
                "• Encrypted at rest and in transit",
                "• Automatic secret rotation support"
            ], (217, 119, 6)),
            ("3. Health Probes & Rollback", "Automated Safety Net", [
                "• Liveness Probe: process alive check",
                "• Readiness Probe: DB & cache connected",
                "• Automated Rollback: error > 1%",
                "• Telemetry: Prometheus & Datadog",
                "• Instant alerts to Slack & PagerDuty"
            ], (16, 185, 129))
        ],
        "footer": "Production safety requires decoupled databases, externalized secrets, and automated health checks."
    },

    # ---------------------------------------------------------------------
    # Slide 10: Manual vs Automated Deployment: The Definitive Comparison
    # ---------------------------------------------------------------------
    {
        "id": 10,
        "title": "Manual vs. Automated Deployment: The Master Comparison",
        "category": "Master Comparison",
        "color": (37, 99, 235),
        "draw": "matrix_8",
        "rows": [
            ("Deployment Frequency", "Once every 1 - 3 months", "Multiple times per day (on-demand)", (225, 29, 72), (16, 185, 129)),
            ("Lead Time for Changes", "Weeks or months of planning", "Under 15 minutes (commit to live)", (225, 29, 72), (16, 185, 129)),
            ("Change Failure Rate", "30% - 50% high defect rate", "< 5% (DORA Elite benchmark)", (225, 29, 72), (16, 185, 129)),
            ("Mean Time to Recovery", "Hours or days of panic debugging", "< 60 seconds (automated rollback)", (225, 29, 72), (16, 185, 129)),
            ("Application Downtime", "Planned 2:00 AM outages", "100% Zero-downtime releases", (225, 29, 72), (16, 185, 129)),
            ("Rollback Process", "Unzipping backups & manual SQL", "1-Click or automated metric trigger", (225, 29, 72), (16, 185, 129)),
            ("Audit Trail & Compliance", "Lost in emails & chat threads", "Full Git commit history & logs", (225, 29, 72), (16, 185, 129)),
            ("Engineering Culture", "Stress, fatigue & fear of release", "Confidence, velocity & innovation", (225, 29, 72), (16, 185, 129))
        ],
        "footer": "Automated deployment frees engineers from manual drudgery and empowers high-velocity software delivery."
    }
]

# =========================================================================
# DRAWING ROUTINES FOR ALL 10 SLIDES
# =========================================================================

for cfg in slides:
    print(f"Generating Deployment Slide {cfg['id']}: {cfg['title']}...")
    img, d = draw_base_card(cfg["title"], cfg["category"], cfg["color"])

    draw_type = cfg["draw"]

    # 1. FLOW 5 (Slide 1 & Slide 4)
    if draw_type == "flow_5":
        steps = cfg["steps"]
        num = len(steps)
        gap = 26
        avail_w = W - 100 - (num - 1) * gap
        box_w = int(avail_w / num)
        box_h = 490
        start_x = 50
        y = 190

        for idx, (head, sub1, sub2, col) in enumerate(steps):
            bx = start_x + idx * (box_w + gap)
            # Shadow & container
            d.rounded_rectangle([(bx + 4, y + 4), (bx + box_w + 4, y + box_h + 4)], radius=20, fill=(226, 232, 240))
            d.rounded_rectangle([(bx, y), (bx + box_w, y + box_h)], radius=20, fill=(255, 255, 255), outline=col, width=4)

            # Header pill
            d.rounded_rectangle([(bx, y), (bx + box_w, y + 80)], radius=18, fill=col)
            d.rectangle([(bx, y + 50), (bx + box_w, y + 80)], fill=col)
            d.text((bx + 16, y + 26), head, fill=(255, 255, 255), font=font_head)

            # Detail Box 1
            d.rounded_rectangle([(bx + 14, y + 105), (bx + box_w - 14, y + 215)], radius=14, fill=(248, 250, 252), outline=(203, 213, 225), width=2)
            d.text((bx + 24, y + 120), "PROCESS:", fill=(100, 116, 139), font=font_badge)
            d.text((bx + 24, y + 155), sub1, fill=(15, 23, 42), font=font_sub)

            # Detail Box 2
            d.rounded_rectangle([(bx + 14, y + 235), (bx + box_w - 14, y + 345)], radius=14, fill=(248, 250, 252), outline=(203, 213, 225), width=2)
            d.text((bx + 24, y + 250), "ARTIFACT / TARGET:", fill=(100, 116, 139), font=font_badge)
            d.text((bx + 24, y + 285), sub2, fill=(30, 41, 59), font=font_sub)

            # Status Badge
            d.rounded_rectangle([(bx + 14, y + 370), (bx + box_w - 14, y + 460)], radius=14, fill=(236, 253, 245), outline=(16, 185, 129), width=2)
            d.text((bx + 30, y + 400), "VERIFIED [OK]", fill=(5, 150, 105), font=font_head)

            # Flow arrow
            if idx < num - 1:
                ax = bx + box_w + 4
                ay = y + 230
                d.line([(ax, ay), (ax + gap - 10, ay)], fill=col, width=6)
                d.polygon([(ax + gap - 10, ay - 12), (ax + gap - 1, ay), (ax + gap - 10, ay + 12)], fill=col)

    # 2. GRID 8 (Slide 2: Manual 8 Steps)
    elif draw_type == "grid_8":
        items = cfg["items"]
        cols = 4
        rows = 2
        card_w = (W - 100 - (cols - 1) * 20) // cols
        card_h = 240
        y_start = 180

        for idx, (head, desc, col) in enumerate(items):
            r = idx // cols
            c = idx % cols
            bx = 50 + c * (card_w + 20)
            by = y_start + r * (card_h + 20)

            # Shadow + card
            d.rounded_rectangle([(bx + 3, by + 3), (bx + card_w + 3, by + card_h + 3)], radius=16, fill=(226, 232, 240))
            d.rounded_rectangle([(bx, by), (bx + card_w, by + card_h)], radius=16, fill=(255, 255, 255), outline=col, width=3)

            # Step title pill
            d.rounded_rectangle([(bx, by), (bx + card_w, by + 55)], radius=14, fill=col)
            d.rectangle([(bx, by + 35), (bx + card_w, by + 55)], fill=col)
            d.text((bx + 16, by + 16), head, fill=(255, 255, 255), font=font_head)

            # Description wrapped
            draw_wrapped_text(d, desc, bx + 16, by + 75, card_w - 32, font_body, (30, 41, 59), line_spacing=6)

            # Danger badge
            d.rounded_rectangle([(bx + 16, by + card_h - 48), (bx + card_w - 16, by + card_h - 14)], radius=8, fill=(254, 242, 242), outline=(239, 68, 68), width=1)
            d.text((bx + 26, by + card_h - 40), "! HIGH HUMAN RISK", fill=(185, 28, 28), font=font_mono)

    # 3. CARDS 4 (Slide 3: Failure Modes)
    elif draw_type == "cards_4":
        cards = cfg["cards"]
        card_w = (W - 100 - 30) // 2
        card_h = 240
        y_start = 180

        for idx, (head, desc, col) in enumerate(cards):
            r = idx // 2
            c = idx % 2
            bx = 50 + c * (card_w + 30)
            by = y_start + r * (card_h + 30)

            # Shadow + card
            d.rounded_rectangle([(bx + 4, by + 4), (bx + card_w + 4, by + card_h + 4)], radius=20, fill=(226, 232, 240))
            d.rounded_rectangle([(bx, by), (bx + card_w, by + card_h)], radius=20, fill=(254, 242, 242), outline=col, width=3)

            # Header pill
            d.rounded_rectangle([(bx, by), (bx + card_w, by + 65)], radius=18, fill=col)
            d.rectangle([(bx, by + 40), (bx + card_w, by + 65)], fill=col)
            d.text((bx + 24, by + 18), head, fill=(255, 255, 255), font=font_head)

            # Body description
            draw_wrapped_text(d, desc, bx + 24, by + 85, card_w - 48, font_body_bold, (127, 29, 29), line_spacing=8)

            # Bottom impact warning
            d.rounded_rectangle([(bx + 24, by + card_h - 46), (bx + card_w - 24, by + card_h - 14)], radius=10, fill=(254, 226, 226), outline=(225, 29, 72), width=1)
            d.text((bx + 34, by + card_h - 38), "IMPACT: Production Outage / Revenue Loss / Hours of MTTR", fill=(159, 18, 57), font=font_mono)

    # 4. SPLIT 2 (Slide 5, Slide 6, Slide 8)
    elif draw_type == "split_2":
        card_w = (W - 130) // 2
        card_h = 510
        y = 180

        # Left Card
        d.rounded_rectangle([(54, y + 4), (54 + card_w, y + card_h + 4)], radius=22, fill=(226, 232, 240))
        d.rounded_rectangle([(50, y), (50 + card_w, y + card_h)], radius=22, fill=(255, 255, 255), outline=cfg["left_color"], width=4)

        # Left Header
        d.rounded_rectangle([(50, y), (50 + card_w, y + 85)], radius=20, fill=cfg["left_color"])
        d.rectangle([(50, y + 55), (50 + card_w, y + 85)], fill=cfg["left_color"])
        d.text((70, y + 25), cfg["left_title"], fill=(255, 255, 255), font=font_head)

        # Left Sub-badge
        d.rounded_rectangle([(70, y + 100), (50 + card_w - 20, y + 138)], radius=10, fill=(241, 245, 249), outline=(203, 213, 225), width=2)
        d.text((85, y + 110), cfg["left_badge"], fill=cfg["left_color"], font=font_badge)

        # Left Items
        item_y = y + 155
        for item in cfg["left_items"]:
            d.rounded_rectangle([(70, item_y), (50 + card_w - 20, item_y + 58)], radius=12, fill=(248, 250, 252), outline=(226, 232, 240), width=2)
            d.text((85, item_y + 17), item, fill=(30, 41, 59), font=font_body_bold)
            item_y += 68

        # Right Card
        rx = 50 + card_w + 30
        d.rounded_rectangle([(rx + 4, y + 4), (rx + card_w + 4, y + card_h + 4)], radius=22, fill=(226, 232, 240))
        d.rounded_rectangle([(rx, y), (rx + card_w, y + card_h)], radius=22, fill=(255, 255, 255), outline=cfg["right_color"], width=4)

        # Right Header
        d.rounded_rectangle([(rx, y), (rx + card_w, y + 85)], radius=20, fill=cfg["right_color"])
        d.rectangle([(rx, y + 55), (rx + card_w, y + 85)], fill=cfg["right_color"])
        d.text((rx + 20, y + 25), cfg["right_title"], fill=(255, 255, 255), font=font_head)

        # Right Sub-badge
        d.rounded_rectangle([(rx + 20, y + 100), (rx + card_w - 20, y + 138)], radius=10, fill=(241, 245, 249), outline=(203, 213, 225), width=2)
        d.text((rx + 35, y + 110), cfg["right_badge"], fill=cfg["right_color"], font=font_badge)

        # Right Items
        item_y = y + 155
        for item in cfg["right_items"]:
            d.rounded_rectangle([(rx + 20, item_y), (rx + card_w - 20, item_y + 58)], radius=12, fill=(248, 250, 252), outline=(226, 232, 240), width=2)
            d.text((rx + 35, item_y + 17), item, fill=(30, 41, 59), font=font_body_bold)
            item_y += 68

    # 5. PILLARS 3 (Slide 7 & Slide 9)
    elif draw_type == "pillars_3":
        pillars = cfg["pillars"]
        num = len(pillars)
        gap = 26
        avail_w = W - 100 - (num - 1) * gap
        box_w = int(avail_w / num)
        box_h = 510
        y = 180

        for idx, (head, sub, bullets, col) in enumerate(pillars):
            bx = 50 + idx * (box_w + gap)

            # Shadow + card
            d.rounded_rectangle([(bx + 4, y + 4), (bx + box_w + 4, y + box_h + 4)], radius=22, fill=(226, 232, 240))
            d.rounded_rectangle([(bx, y), (bx + box_w, y + box_h)], radius=22, fill=(255, 255, 255), outline=col, width=4)

            # Header pill
            d.rounded_rectangle([(bx, y), (bx + box_w, y + 85)], radius=20, fill=col)
            d.rectangle([(bx, y + 55), (bx + box_w, y + 85)], fill=col)
            d.text((bx + 18, y + 25), head, fill=(255, 255, 255), font=font_head)

            # Sub-pill
            d.rounded_rectangle([(bx + 16, y + 100), (bx + box_w - 16, y + 140)], radius=10, fill=(241, 245, 249), outline=(203, 213, 225), width=2)
            d.text((bx + 26, y + 110), sub, fill=col, font=font_badge)

            # Bullet boxes
            item_y = y + 155
            for bullet in bullets:
                d.rounded_rectangle([(bx + 16, item_y), (bx + box_w - 16, item_y + 58)], radius=12, fill=(248, 250, 252), outline=(226, 232, 240), width=2)
                d.text((bx + 26, item_y + 17), bullet, fill=(30, 41, 59), font=font_body_bold)
                item_y += 68

    # 6. MATRIX 8 (Slide 10: Comparison Table)
    elif draw_type == "matrix_8":
        rows = cfg["rows"]
        y_start = 180
        row_h = 56
        gap = 8

        # Table Header
        hx = 50
        hy = y_start
        d.rounded_rectangle([(hx, hy), (hx + 380, hy + 48)], radius=12, fill=(30, 41, 59))
        d.text((hx + 24, hy + 12), "EVALUATION METRIC", fill=(255, 255, 255), font=font_head)

        d.rounded_rectangle([(hx + 400, hy), (hx + 920, hy + 48)], radius=12, fill=(225, 29, 72))
        d.text((hx + 424, hy + 12), "[OLD WAY] MANUAL DEPLOYMENT", fill=(255, 255, 255), font=font_head)

        d.rounded_rectangle([(hx + 940, hy), (W - 50, hy + 48)], radius=12, fill=(16, 185, 129))
        d.text((hx + 964, hy + 12), "[MODERN] AUTOMATED CI/CD DEPLOY", fill=(255, 255, 255), font=font_head)

        # Table Rows
        curr_y = hy + 60
        for dim, manual_val, auto_val, col_m, col_a in rows:
            # Dimension column
            d.rounded_rectangle([(hx, curr_y), (hx + 380, curr_y + row_h)], radius=10, fill=(241, 245, 249), outline=(203, 213, 225), width=2)
            d.text((hx + 20, curr_y + 15), dim, fill=(15, 23, 42), font=font_body_bold)

            # Manual column
            d.rounded_rectangle([(hx + 400, curr_y), (hx + 920, curr_y + row_h)], radius=10, fill=(254, 242, 242), outline=(254, 202, 202), width=2)
            d.text((hx + 420, curr_y + 15), manual_val, fill=(159, 18, 57), font=font_body_bold)

            # Automated column
            d.rounded_rectangle([(hx + 940, curr_y), (W - 50, curr_y + row_h)], radius=10, fill=(240, 253, 244), outline=(187, 247, 208), width=2)
            d.text((hx + 960, curr_y + 15), auto_val, fill=(6, 95, 70), font=font_body_bold)

            curr_y += row_h + gap

    # Bottom Footer Pill
    draw_footer_badge(d, cfg["footer"], color=cfg["color"])

    # Save final high-res PNG image
    out_file = os.path.join(OUTPUT_DIR, f"slide_{cfg['id']}.png")
    img.save(out_file, "PNG", quality=95)
    print(f"Saved: {out_file}")

print("All 10 Deployment slide diagram images generated successfully!")

