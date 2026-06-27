# OpenCode Sub-Agents Collection

A comprehensive collection of specialized sub-agents for [OpenCode](https://opencode.ai), converted from the Claude Code agents collection. Designed to enhance development workflows through domain-specific expertise and intelligent task delegation.

## What are OpenCode Agents?

Agents are specialized AI assistants in OpenCode that can be configured for specific tasks and workflows. They allow you to create targeted tools with custom prompts, models, and tool access. Learn more in the [official documentation](https://opencode.ai/docs/agents/).

## Installation

### Per-Project Setup
Copy the agent `.md` files to your project's OpenCode agents directory:

```bash
# Create the agents directory in your project
mkdir -p .opencode/agents/

# Copy all agent files
cp *.md .opencode/agents/
```

### Global Setup
Copy the agent `.md` files to make them available across all projects:

```bash
# Copy to global OpenCode agents directory
cp *.md ~/.config/opencode/agents/
```

### Alternative: JSON Configuration
You can also configure agents via `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "code-reviewer": {
      "description": "Reviews code for best practices and potential issues",
      "mode": "subagent",
      "tools": {
        "write": true,
        "edit": true,
        "bash": true
      }
    }
  }
}
```

## Agent Categories

### 🏗️ Architecture & Design
| Agent | Description |
|-------|-------------|
| [backend-architect](./backend-architect.md) | Scalable API architectures, authentication systems, database schemas |
| [frontend-specialist](./frontend-specialist.md) | Modern React applications, component architecture, accessibility |
| [fullstack-developer](./fullstack-developer.md) | End-to-end feature implementation |
| [iac-expert](./iac-expert.md) | Infrastructure as Code and cloud resources |
| [ui-ux-designer](./ui-ux-designer.md) | Stunning user interfaces with modern design |

### 🧪 Testing & Quality Assurance
| Agent | Description |
|-------|-------------|
| [test-architect](./test-architect.md) | Test strategies and quality assurance planning |
| [unit-test-generator](./unit-test-generator.md) | Component-level tests with edge cases |
| [e2e-test-automator](./e2e-test-automator.md) | End-to-end user journey testing |
| [integration-test-builder](./integration-test-builder.md) | API and service interaction testing |

### 🔒 Security & Compliance
| Agent | Description |
|-------|-------------|
| [security-auditor](./security-auditor.md) | OWASP compliance and vulnerability assessments |
| [code-reviewer](./code-reviewer.md) | Code quality and best practices enforcement |
| [auth-architect](./auth-architect.md) | Authentication and authorization systems |

### ⚡ Performance & Monitoring
| Agent | Description |
|-------|-------------|
| [performance-profiler](./performance-profiler.md) | Performance bottleneck identification |
| [monitoring-architect](./monitoring-architect.md) | System observability and alerting |
| [caching-strategist](./caching-strategist.md) | Caching strategies and optimization |

### 🚀 DevOps & Deployment
| Agent | Description |
|-------|-------------|
| [cicd-engineer](./cicd-engineer.md) | CI/CD pipelines and deployment management |
| [docker-specialist](./docker-specialist.md) | Container optimization and orchestration |
| [config-expert](./config-expert.md) | Environment configuration and secrets |
| [serverless-specialist](./serverless-specialist.md) | Serverless architecture and deployment |

### 🛠️ Development & Maintenance
| Agent | Description |
|-------|-------------|
| [database-engineer](./database-engineer.md) | Database schema design and query optimization |
| [refactoring-expert](./refactoring-expert.md) | Technical debt reduction and design patterns |
| [error-detective](./error-detective.md) | Bug analysis and root cause identification |
| [dependency-manager](./dependency-manager.md) | Safe dependency updates |
| [mindful-dev](./mindful-dev.md) | Thoughtful development with educational focus |
| [migration-specialist](./migration-specialist.md) | Schema and data migrations |
| [monorepo-engineer](./monorepo-engineer.md) | Monorepo management and tooling |

### 🌐 API & Communication
| Agent | Description |
|-------|-------------|
| [api-designer](./api-designer.md) | API design and specification |
| [graphql-specialist](./graphql-specialist.md) | GraphQL schema design and optimization |
| [websocket-architect](./websocket-architect.md) | Real-time communication architecture |
| [queue-architect](./queue-architect.md) | Message queue design and patterns |

### 📚 Documentation & Release
| Agent | Description |
|-------|-------------|
| [tech-writer](./tech-writer.md) | Technical documentation and user guides |
| [release-compiler](./release-compiler.md) | Release notes and changelogs |
| [code-commentator](./code-commentator.md) | Inline documentation |

### 🎯 Specialized
| Agent | Description |
|-------|-------------|
| [project-orchestrator](./project-orchestrator.md) | Multi-agent workflow coordination |
| [accessibility-auditor](./accessibility-auditor.md) | WCAG compliance and accessibility |
| [i18n-specialist](./i18n-specialist.md) | Internationalization and localization |
| [seo-optimizer](./seo-optimizer.md) | Search engine optimization |
| [schema-validator](./schema-validator.md) | Schema validation and data contracts |
| [git-strategist](./git-strategist.md) | Git workflows and branching strategies |
| [cli-developer](./cli-developer.md) | CLI tool development |

## Usage

### Invoke via @ mention
```
@code-reviewer Review this authentication flow for vulnerabilities
@backend-architect Design the API structure for user management
@test-architect Create a testing strategy for this feature
```

### Switch between agents
Use **Tab** to cycle through primary agents during a session.

### Sub-agent delegation
Sub-agents are automatically called by primary agents for specialized tasks, or you can invoke them manually with `@` mentions.

## OpenCode Agent Format

Each agent uses OpenCode's markdown agent format:

```markdown
---
description: What this agent does and when to use it
mode: subagent
tools:
  write: true/false
  edit: true/false
  bash: true/false
---

Agent system prompt and instructions here...
```

### Configuration Options
- **description**: Brief description of the agent's purpose
- **mode**: `primary` (main agents) or `subagent` (specialized helpers)
- **tools.write**: Enable/disable file writing
- **tools.edit**: Enable/disable file editing
- **tools.bash**: Enable/disable bash command execution
- **model**: Override the default model (e.g., `anthropic/claude-sonnet-4-20250514`)
- **temperature**: Control response randomness (0.0-1.0)

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

