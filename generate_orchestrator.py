# -*- coding: utf-8 -*-
import os
import re

# Resolve directories relative to this script
target_dir = os.path.dirname(os.path.abspath(__file__))

categories = [
    { "id": "01-core-development", "name": "🏗️ Core Development" },
    { "id": "02-language-specialists", "name": "💻 Language Specialists" },
    { "id": "03-infrastructure", "name": "☁️ Infrastructure" },
    { "id": "04-quality-security", "name": "🛡️ Quality & Security" },
    { "id": "05-data-ai", "name": "🧠 Data & AI" },
    { "id": "06-developer-experience", "name": "🛠️ Developer Experience" },
    { "id": "07-specialized-domains", "name": "🎯 Specialized Domains" },
    { "id": "08-business-product", "name": "💼 Business & Product" },
    { "id": "09-meta-orchestration", "name": "🔄 Meta & Orchestration" },
    { "id": "10-research-analysis", "name": "🔬 Research & Analysis" }
]

def get_agent_description(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""
    
    # Strip BOM and trim whitespace
    content_clean = content.lstrip('\ufeff').strip()
    if content_clean.startswith("---"):
        parts = content_clean.split("---", 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1].strip()
            # Process line-by-line
            for line in frontmatter_text.splitlines():
                line_stripped = line.strip()
                if line_stripped.startswith("description:"):
                    desc_val = line_stripped[len("description:"):].strip()
                    if desc_val.startswith('"') and desc_val.endswith('"'):
                        desc_val = desc_val[1:-1].replace('\\"', '"')
                    elif desc_val.startswith("'") and desc_val.endswith("'"):
                        desc_val = desc_val[1:-1].replace("\\'", "'")
                    return desc_val
    return ""

def split_description(desc):
    if not desc:
        return "Specialized sub-agent.", "Specialized sub-agent."
    
    # Check for "MUST BE USED" (case insensitive)
    idx = desc.lower().find("must be used")
    if idx != -1:
        part1 = desc[:idx].strip()
        part2 = desc[idx:].strip()
        # Clean up any trailing punctuation from part 1
        if part1.endswith(".") or part1.endswith(";"):
            part1 = part1[:-1].strip()
        return part1, part2
    else:
        return desc, desc

team_section = []
total_agents_count = 0

for cat in categories:
    cat_dir = os.path.join(target_dir, cat["id"])
    if not os.path.exists(cat_dir):
        continue
    
    files = [f for f in os.listdir(cat_dir) if f.endswith(".md") and f != "README.md"]
    files.sort()
    
    if not files:
        continue
    
    team_section.append(f"### {cat['name']}")
    team_section.append("")
    team_section.append("| Agent | Expertise | When to invoke |")
    team_section.append("|-------|-----------|----------------|")
    
    for filename in files:
        file_path = os.path.join(cat_dir, filename)
        desc = get_agent_description(file_path)
        exp, invoke = split_description(desc)
        
        # Escape pipe symbol in description if any, to avoid breaking markdown table
        exp_clean = exp.replace("|", "\\|")
        invoke_clean = invoke.replace("|", "\\|")
        
        base_name = os.path.splitext(filename)[0]
        team_section.append(f"| **{base_name}** | {exp_clean} | {invoke_clean} |")
        total_agents_count += 1
        
    team_section.append("")

# Load existing orchestrator.md
orchestrator_path = os.path.join(target_dir, "orchestrator.md")
with open(orchestrator_path, "r", encoding="utf-8") as f:
    orch_content = f.read()

# Replace the Agent Team section
# It starts at ## Your 112-Agent Team (or ## Your \d+-Agent Team) and ends at ## Orchestration Process
pattern = re.compile(r"## Your \d+-Agent Team\r?\n.*?\r?\n## Orchestration Process", re.DOTALL)
team_text = "\n".join(team_section)
replacement = f"## Your {total_agents_count}-Agent Team\n\n{team_text}\n## Orchestration Process"

new_orch_content = re.sub(pattern, replacement, orch_content)

# Update counts in orchestrator.md
# 1. Frontmatter description count: "coordinating all 112 specialized sub-agents" -> "coordinating all 258 specialized sub-agents"
new_orch_content = re.sub(r"coordinating all \d+ specialized sub-agents", f"coordinating all {total_agents_count} specialized sub-agents", new_orch_content)

# 2. Body count: "coordinates a team of 112 specialized sub-agents" -> "coordinates a team of 258 specialized sub-agents"
new_orch_content = re.sub(r"coordinates a team of \d+ specialized sub-agents", f"coordinates a team of {total_agents_count} specialized sub-agents", new_orch_content)

with open(orchestrator_path, "w", encoding="utf-8") as f:
    f.write(new_orch_content)

print(f"SUCCESS: Generated orchestrator.md with {total_agents_count} sub-agents.")
