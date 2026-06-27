import os
import re
import subprocess
import requests

def get_added_agents():
    try:
        # Get list of added files in the last commit
        result = subprocess.run(
            ["git", "diff", "--diff-filter=A", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        files = result.stdout.strip().split("\n")
    except subprocess.CalledProcessError:
        # Fallback for initial commit or if HEAD~1 doesn't exist
        print("Fallback to checking all markdown files in the commit...")
        result = subprocess.run(
            ["git", "show", "--name-only", "--pretty=format:", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        files = result.stdout.strip().split("\n")

    agents = []
    for file in files:
        if file.endswith(".md") and file not in ["README.md", "orchestrator.md", "project-orchestrator.md"]:
            if os.path.exists(file):
                agents.append(file)
    return agents

def parse_agent(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Parse YAML frontmatter
    description = "A new specialized agent"
    match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        for line in frontmatter.split("\n"):
            if line.startswith("description:"):
                description = line.replace("description:", "").strip()
                break
    
    name = os.path.basename(filepath).replace(".md", "").replace("-", " ").title()
    return name, description

def post_to_linkedin(agent_name, description):
    access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    author_urn = os.environ.get("LINKEDIN_URN")
    
    if not access_token or not author_urn:
        print("Missing LINKEDIN_ACCESS_TOKEN or LINKEDIN_URN environment variables.")
        return False
        
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    
    commentary = (
        f"🤖 New Agent Added to OpenCode Agents!\n\n"
        f"Meet the {agent_name} Agent:\n"
        f"\"{description}\"\n\n"
        f"Check out the full repository of 41+ specialized OpenCode agents here:\n"
        f"👉 https://github.com/mouyox21/opencode-agents"
    )
    
    payload = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": commentary
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code in [200, 201]:
        print(f"Successfully posted to LinkedIn for agent: {agent_name}")
        return True
    else:
        print(f"Failed to post to LinkedIn. Status code: {response.status_code}")
        print(response.text)
        return False

def main():
    added_agents = get_added_agents()
    if not added_agents:
        print("No new agent files added in this commit.")
        return

    for agent_file in added_agents:
        name, desc = parse_agent(agent_file)
        print(f"Detected new agent: {name}")
        post_to_linkedin(name, desc)

if __name__ == "__main__":
    main()
