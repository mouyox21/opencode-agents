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

categories_section = []
total_agents_count = 0

for cat in categories:
    cat_dir = os.path.join(target_dir, cat["id"])
    if not os.path.exists(cat_dir):
        continue
    
    files = [f for f in os.listdir(cat_dir) if f.endswith(".md") and f != "README.md"]
    files.sort()
    
    if not files:
        continue
    
    categories_section.append(f"### {cat['name']} (`{cat['id']}`)")
    categories_section.append("")
    categories_section.append("| Agent | Description |")
    categories_section.append("|-------|-------------|")
    
    for filename in files:
        file_path = os.path.join(cat_dir, filename)
        desc = get_agent_description(file_path)
        if not desc:
            desc = "Specialized sub-agent."
        
        # Escape pipe symbol in description if any, to avoid breaking markdown table
        desc_clean = desc.replace("|", "\\|")
        
        base_name = os.path.splitext(filename)[0]
        rel_path = f"./{cat['id']}/{filename}"
        categories_section.append(f"| [{base_name}]({rel_path}) | {desc_clean} |")
        total_agents_count += 1
        
    categories_section.append("")

# Load existing README.md
readme_path = os.path.join(target_dir, "README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

# Replace the Agent Categories section
pattern = re.compile(r"## Agent Categories\r?\n.*?\r?\n## Usage", re.DOTALL)
categories_text = "\n".join(categories_section)
replacement = f"## Agent Categories\n\n{categories_text}\n## Usage"

new_readme_content = re.sub(pattern, replacement, readme_content)

# Update count in title
# e.g., "A comprehensive collection of 113 specialized agents (112 sub-agents + 1 orchestrator)"
title_pattern = re.compile(r"collection of \d+ specialized agents \(\d+ sub-agents \+ 1 orchestrator\)")
new_readme_content = re.sub(title_pattern, f"collection of {total_agents_count + 1} specialized agents ({total_agents_count} sub-agents + 1 orchestrator)", new_readme_content)

title_pattern_2 = re.compile(r"collection of \d+ specialized agents")
new_readme_content = re.sub(title_pattern_2, f"collection of {total_agents_count + 1} specialized agents", new_readme_content)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_readme_content)

print(f"SUCCESS: Generated README.md with {total_agents_count} categorized agents.")
