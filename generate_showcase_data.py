# -*- coding: utf-8 -*-
import os
import json
import re

# Resolve directories relative to this script
target_dir = os.path.dirname(os.path.abspath(__file__))

categories = [
    { "id": "01-core-development", "name": "Core Development", "icon": "🏗️" },
    { "id": "02-language-specialists", "name": "Language Specialists", "icon": "💻" },
    { "id": "03-infrastructure", "name": "Infrastructure", "icon": "☁️" },
    { "id": "04-quality-security", "name": "Quality & Security", "icon": "🛡️" },
    { "id": "05-data-ai", "name": "Data & AI", "icon": "🧠" },
    { "id": "06-developer-experience", "name": "Developer Experience", "icon": "🛠️" },
    { "id": "07-specialized-domains", "name": "Specialized Domains", "icon": "🎯" },
    { "id": "08-business-product", "name": "Business & Product", "icon": "💼" },
    { "id": "09-meta-orchestration", "name": "Meta & Orchestration", "icon": "🔄" },
    { "id": "10-research-analysis", "name": "Research & Analysis", "icon": "🔬" }
]

agents = []

def parse_agent_file(file_path, category_id, category_name, category_icon):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    # Strip BOM and trim whitespace
    content_clean = content.lstrip('\ufeff').strip()
    
    frontmatter_text = ""
    prompt_body = content_clean
    description = ""
    mode = "subagent"
    tools = {"write": False, "edit": False, "bash": False}
    
    if content_clean.startswith("---"):
        parts = content_clean.split("---", 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1].strip()
            prompt_body = parts[2].strip()
            
            # Robust frontmatter parsing
            lines = frontmatter_text.splitlines()
            in_tools_block = False
            
            for line in lines:
                line_stripped = line.strip()
                if not line_stripped:
                    continue
                
                # Check tools block entry
                if line_stripped.startswith("tools:"):
                    in_tools_block = True
                    continue
                
                if in_tools_block:
                    # If line has no indentation and starts a new key, we exited tools block
                    if not line.startswith(" ") and not line.startswith("\t"):
                        in_tools_block = False
                    else:
                        tool_match = re.match(r'^\s*(\w+):\s*(true|false)\s*$', line_stripped)
                        if tool_match:
                            tools[tool_match.group(1)] = tool_match.group(2) == 'true'
                            continue
                
                # Parse description
                if line_stripped.startswith("description:"):
                    desc_val = line_stripped[len("description:"):].strip()
                    if desc_val.startswith('"') and desc_val.endswith('"'):
                        desc_val = desc_val[1:-1].replace('\\"', '"')
                    elif desc_val.startswith("'") and desc_val.endswith("'"):
                        desc_val = desc_val[1:-1].replace("\\'", "'")
                    description = desc_val
                    continue
                
                # Parse mode
                if line_stripped.startswith("mode:"):
                    mode = line_stripped[len("mode:"):].strip()
                    continue
                
                # Parse flat tools
                if line_stripped.startswith("tools."):
                    tool_match = re.match(r'^tools\.(\w+):\s*(true|false)\s*$', line_stripped)
                    if tool_match:
                        tools[tool_match.group(1)] = tool_match.group(2) == 'true'

    # Get agent id and display name
    agent_id = os.path.splitext(os.path.basename(file_path))[0]
    display_name = agent_id.replace("-", " ").title()
    
    # Capitalize acronyms
    acronyms = ["Ui", "Ux", "Cli", "Mle", "Tdd", "Api", "Iac", "Ab", "Cicd", "Gdpr", "Seo", "Pr", "Gsf", "Dmn", "Bpmn", "Wcag", "Pii"]
    words = display_name.split()
    for i, w in enumerate(words):
        if w in ["Ui", "Ux", "Cli", "Mle", "Tdd", "Api", "Iac", "Ab", "Seo", "Pr", "Dmn", "Bpmn", "Pii"]:
            words[i] = w.upper()
        elif w == "Cicd":
            words[i] = "CI/CD"
        elif w == "Gdpr":
            words[i] = "GDPR"
        elif w == "Wcag":
            words[i] = "WCAG"
    display_name = " ".join(words)
    
    # Path relative to root of opencode agent/
    if category_id:
        rel_path = f"./{category_id}/{os.path.basename(file_path)}"
    else:
        rel_path = f"./{os.path.basename(file_path)}"
        
    return {
        "id": agent_id,
        "name": display_name,
        "category": category_id or "orchestrator",
        "categoryName": category_name or "Orchestrator",
        "categoryIcon": category_icon or "👑",
        "description": description,
        "mode": mode,
        "tools": tools,
        "path": rel_path,
        "prompt": prompt_body,
        "frontmatter": frontmatter_text
    }

# 1. Parse Orchestrator
orch_path = os.path.join(os.path.dirname(target_dir), "orchestrator.md")
# Wait, orchestrator.md is at the root of target_dir ("opencode agent/orchestrator.md")
orch_path = os.path.join(target_dir, "orchestrator.md")
if os.path.exists(orch_path):
    orch_data = parse_agent_file(orch_path, "", "", "")
    if orch_data:
        agents.append(orch_data)

# 2. Parse Sub-Agents
for cat in categories:
    cat_dir = os.path.join(target_dir, cat["id"])
    if not os.path.exists(cat_dir):
        continue
    
    files = [f for f in os.listdir(cat_dir) if f.endswith(".md") and f != "README.md"]
    files.sort()
    
    for filename in files:
        file_path = os.path.join(cat_dir, filename)
        agent_data = parse_agent_file(file_path, cat["id"], cat["name"], cat["icon"])
        if agent_data:
            agents.append(agent_data)

# Output javascript file
output_js_path = os.path.join(target_dir, "agents-data.js")
with open(output_js_path, "w", encoding="utf-8") as f:
    f.write("// Auto-generated data file for OpenCode agent landing page\n")
    f.write("const AGENTS_DATA = ")
    json.dump(agents, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print(f"SUCCESS: Generated {output_js_path} with {len(agents)} agents.")
