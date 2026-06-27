# OpenCode Sub-Agents Collection

A comprehensive collection of 113 specialized agents (112 sub-agents + 1 orchestrator) for [OpenCode](https://opencode.ai), converted from the Claude Code agents collection. Designed to enhance development workflows through domain-specific expertise and intelligent task delegation.

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
| [backend-architect](./backend-architect.md) | USE PROACTIVELY for designing scalable API architectures, implementing authentication/authorization systems, creating database schemas, microservices design, and API documentation. MUST BE USED for backend architecture decisions, API design patterns, authentication flows, database modeling, and service integration planning. |
| [frontend-specialist](./frontend-specialist.md) | USE PROACTIVELY for creating UI components with shadcn/ui, implementing responsive designs with Tailwind CSS, ensuring WCAG accessibility compliance, optimizing frontend performance, and building modern React applications. MUST BE USED for component architecture, design system implementation, user interface design, and frontend performance optimization. |
| [fullstack-developer](./fullstack-developer.md) | USE PROACTIVELY for implementing complete features from UI to database, integrating frontend with backend, ensuring end-to-end functionality, and delivering working features across the full stack. MUST BE USED for full-stack feature implementation, frontend-backend integration, and cross-layer feature delivery. |
| [api-designer](./api-designer.md) | USE PROACTIVELY for REST and GraphQL API design, OpenAPI specification authoring, versioning strategy, and API contract definition. MUST BE USED for resource modeling, HTTP semantics enforcement, OpenAPI 3.1 spec generation, pagination design, error format standardization (RFC 7807), rate limiting, and client SDK generation. |
| [auth-architect](./auth-architect.md) | USE PROACTIVELY for designing authentication and authorization systems, implementing OAuth 2.0/OIDC flows, configuring MFA and passkeys, and architecting session management. MUST BE USED for auth strategy selection, RBAC/ABAC design, SSO integration, token lifecycle management, and security hardening of identity systems. |
| [ui-ux-designer](./ui-ux-designer.md) | USE PROACTIVELY for creating UI components with shadcn/ui, implementing responsive designs with Tailwind CSS, ensuring WCAG accessibility compliance, optimizing frontend performance, and building modern React applications. MUST BE USED for component architecture, design system implementation, user interface design, and frontend performance optimization. Creates stunning, unique, and modern user interfaces with exceptional visual design and seamless interactions. Ensures every project has a distinctive aesthetic while maintaining high design standards and accessibility compliance. |
| [iac-expert](./iac-expert.md) | Invoke for managing cloud resources as code, ensuring scalability, and implementing disaster recovery |
| [state-management-architect](./state-management-architect.md) | USE PROACTIVELY for designing frontend state management architectures, configuring global stores, and optimizing state reactivity patterns. MUST BE USED when designing complex application state flows, setting up caching strategies for frontend stores, resolving reactivity leaks, or planning store architectures (Pinia, Redux, Zustand, Recoil). |
| [a11y-architect](./a11y-architect.md) | Accessibility Architect specializing in WCAG 2.2 compliance for Web and Native platforms. Use PROACTIVELY when designing UI components, establishing design systems, or auditing code for inclusive user experiences. |
| [architect](./architect.md) | Software architecture specialist for system design, scalability, and technical decision-making. Use PROACTIVELY when planning new features, refactoring large systems, or making architectural decisions. |
| [chief-of-staff](./chief-of-staff.md) | Personal communication chief of staff that triages email, Slack, LINE, and Messenger. Classifies messages into 4 tiers (skip/info_only/meeting_info/action_required), generates draft replies, and enforces post-send follow-through via hooks. Use when managing multi-channel communication workflows. |
| [code-architect](./code-architect.md) | Designs feature architectures by analyzing existing codebase patterns and conventions, then providing implementation blueprints with concrete files, interfaces, data flow, and build order. |
| [homelab-architect](./homelab-architect.md) | Designs home and small-lab network plans from hardware inventory, goals, and operator experience level, with safe staged changes and rollback guidance. |
| [network-architect](./network-architect.md) | Designs enterprise or multi-site network architecture from requirements, using existing network skills for focused routing, validation, automation, and troubleshooting detail. |
| [planner](./planner.md) | Expert planning specialist for complex features and refactoring. Use PROACTIVELY when users request feature implementation, architectural changes, or complex refactoring. Automatically activated for planning tasks. |
| [spec-miner](./spec-miner.md) | Extracts behavioral specs from existing codebases for OpenSpec. Produces flat Requirement and Invariant blocks with structured metadata (entities, enforced, id, test anchors). Outputs openspec/specs/<capability>/spec.md. Fully self-bootstrapping — no dependency on codebase-onboarding. Use when onboarding a brownfield project to spec-driven development. |
| [project-orchestrator](./project-orchestrator.md) | USE PROACTIVELY for breaking down complex project specifications, orchestrating multi-agent workflows, and managing end-to-end feature delivery. MUST BE USED when receiving project briefs or specifications that require coordination across multiple specialized domains (frontend, backend, testing, security, etc.) |

### 🌐 API & Communication
| Agent | Description |
|-------|-------------|
| [graphql-specialist](./graphql-specialist.md) | USE PROACTIVELY for GraphQL schema design, resolver implementation, N+1 prevention with DataLoader, real-time subscriptions, federation architecture, and type-safe code generation. MUST BE USED for schema type system design, DataLoader batching, query complexity limiting, persisted queries, schema evolution, and Apollo Federation setup. |
| [websocket-architect](./websocket-architect.md) | USE PROACTIVELY for designing real-time communication architectures, implementing WebSocket and SSE connections, scaling with Redis pub/sub adapters, and building reconnection and state reconciliation logic. MUST BE USED for real-time feature design, protocol selection (WebSocket vs SSE), connection lifecycle management, horizontal scaling patterns, and real-time security controls. |
| [queue-architect](./queue-architect.md) | USE PROACTIVELY for designing message queue architectures, implementing event-driven patterns, configuring delivery guarantees, and building resilient async workflows. MUST BE USED for broker selection, topic/queue topology design, dead-letter queue configuration, saga/choreography patterns, and outbox pattern implementation. |
| [schema-validator](./schema-validator.md) | USE PROACTIVELY for implementing runtime type checking, input validation, API contract enforcement, schema-driven form validation, and type-safe data boundaries. MUST BE USED for validation strategy design, schema library creation, API request/response validation, form validation integration, and TypeScript type generation from schemas. |
| [workflow-dmn-engineer](./workflow-dmn-engineer.md) | USE PROACTIVELY for modeling, implementing, and debugging business rules (DMN) and workflow processes (BPMN). MUST BE USED when configuring decision tables, setting up Flowable/Camunda process definitions, mapping BPMN service tasks, and designing stateful workflows. |

### 🛠️ Development & Maintenance
| Agent | Description |
|-------|-------------|
| [database-engineer](./database-engineer.md) | USE PROACTIVELY for designing database schemas, optimizing queries, managing migrations, ensuring data integrity, and scaling database infrastructure. MUST BE USED for schema design, query performance optimization, migration planning, data modeling, ORM configuration, and database architecture decisions. |
| [caching-strategist](./caching-strategist.md) | USE PROACTIVELY for designing multi-layer cache architectures, implementing cache invalidation strategies, optimizing data access latency, and configuring CDN and HTTP caching. MUST BE USED for cache topology design, Redis integration, stampede prevention, TTL strategy planning, and cache hit rate optimization. |
| [refactoring-expert](./refactoring-expert.md) | Invoke for reducing technical debt, improving code maintainability, implementing design patterns, and simplifying complex code |
| [error-detective](./error-detective.md) | USE PROACTIVELY for analyzing and fixing bugs, identifying root causes, debugging complex errors, and improving error handling patterns. MUST BE USED for stack trace analysis, error pattern diagnosis, production incident investigation, systematic debugging, and error handling architecture. |
| [dependency-manager](./dependency-manager.md) | Invoke for updating dependencies safely, ensuring security, verifying compatibility, and minimizing package bloat |
| [migration-specialist](./migration-specialist.md) | Invoke for handling schema and data migrations, ensuring safe migrations, and maintaining data integrity |
| [mindful-dev](./mindful-dev.md) | MUST BE USED for any development task where educational value is important. Breaks down complex development tasks into digestible steps, explains the reasoning behind each decision, and provides learning insights. Use PROACTIVELY when users want to understand not just what to code, but why and how to approach problems systematically. |
| [config-expert](./config-expert.md) | Invoke for managing environment configurations, securing sensitive data, and ensuring consistency across environments |
| [serverless-specialist](./serverless-specialist.md) | USE PROACTIVELY for designing serverless architectures, implementing edge computing solutions, optimizing Lambda/Workers functions, building event-driven workflows, and configuring function orchestration. MUST BE USED for serverless platform selection, cold start optimization, workflow design (Step Functions/Inngest), function composition, and IaC deployment of serverless resources. |
| [cli-developer](./cli-developer.md) | USE PROACTIVELY for building CLI tools, implementing interactive terminal prompts, designing command structures, formatting terminal output, and configuring shell completions. MUST BE USED for CLI framework selection, argument parsing design, interactive workflow creation, output formatting (human + machine), and CLI distribution/packaging. |
| [monorepo-engineer](./monorepo-engineer.md) | USE PROACTIVELY for designing monorepo architectures, configuring build systems with Turborepo or Nx, managing pnpm workspaces, implementing shared packages, and optimizing CI with remote caching. MUST BE USED for monorepo setup, workspace structure design, package boundary enforcement, affected-only CI configuration, and polyrepo-to-monorepo migration. |
| [api-mock-specialist](./api-mock-specialist.md) | USE PROACTIVELY for creating mock API servers, establishing front-end mock contexts, and seeding mock data. MUST BE USED when mocking REST/GraphQL endpoints for development or testing, configuring Mock Service Worker (MSW), or simulating network behaviors. |
| [code-explorer](./code-explorer.md) | Deeply analyzes existing codebase features by tracing execution paths, mapping architecture layers, and documenting dependencies to inform new development. |
| [code-simplifier](./code-simplifier.md) | Simplifies and refines code for clarity, consistency, and maintainability while preserving behavior. Focus on recently modified code unless instructed otherwise. |
| [comment-analyzer](./comment-analyzer.md) | Analyze code comments for accuracy, completeness, maintainability, and comment rot risk. |
| [conversation-analyzer](./conversation-analyzer.md) | Use this agent when analyzing conversation transcripts to find behaviors worth preventing with hooks. Triggered by /hookify without arguments. |
| [loop-operator](./loop-operator.md) | Operate autonomous agent loops, monitor progress, and intervene safely when loops stall. |
| [refactor-cleaner](./refactor-cleaner.md) | Dead code cleanup and consolidation specialist. Use PROACTIVELY for removing unused code, duplicates, and refactoring. Runs analysis tools (knip, depcheck, ts-prune) to identify dead code and safely removes it. |
| [type-design-analyzer](./type-design-analyzer.md) | Analyze type design for encapsulation, invariant expression, usefulness, and enforcement. |
| [harness-optimizer](./harness-optimizer.md) | Analyze and improve the local agent harness configuration for reliability, cost, and throughput. |

### 🛠️ Build Error Resolvers
| Agent | Description |
|-------|-------------|
| [build-error-resolver](./build-error-resolver.md) | Build and TypeScript error resolution specialist. Use PROACTIVELY when build fails or type errors occur. Fixes build/type errors only with minimal diffs, no architectural edits. Focuses on getting the build green quickly. |
| [cpp-build-resolver](./cpp-build-resolver.md) | C++ build, CMake, and compilation error resolution specialist. Fixes build errors, linker issues, and template errors with minimal changes. Use when C++ builds fail. |
| [dart-build-resolver](./dart-build-resolver.md) | Dart/Flutter build, analysis, and dependency error resolution specialist. Fixes `dart analyze` errors, Flutter compilation failures, pub dependency conflicts, and build_runner issues with minimal, surgical changes. Use when Dart/Flutter builds fail. |
| [django-build-resolver](./django-build-resolver.md) | Django/Python build, migration, and dependency error resolution specialist. Fixes pip/Poetry errors, migration conflicts, import errors, Django configuration issues, and collectstatic failures with minimal changes. Use when Django setup or startup fails. |
| [go-build-resolver](./go-build-resolver.md) | Go build, vet, and compilation error resolution specialist. Fixes build errors, go vet issues, and linter warnings with minimal changes. Use when Go builds fail. |
| [harmonyos-app-resolver](./harmonyos-app-resolver.md) | HarmonyOS application development expert specializing in ArkTS and ArkUI. Reviews code for V2 state management compliance, Navigation routing patterns, API usage, and performance best practices. Use for HarmonyOS/OpenHarmony projects. |
| [java-build-resolver](./java-build-resolver.md) | Java/Maven/Gradle build, compilation, and dependency error resolution specialist. Automatically detects Spring Boot or Quarkus and applies framework-specific fixes. Fixes build errors, Java compiler errors, and Maven/Gradle issues with minimal changes. Use when Java builds fail. |
| [kotlin-build-resolver](./kotlin-build-resolver.md) | Kotlin/Gradle build, compilation, and dependency error resolution specialist. Fixes build errors, Kotlin compiler errors, and Gradle issues with minimal changes. Use when Kotlin builds fail. |
| [pytorch-build-resolver](./pytorch-build-resolver.md) | PyTorch runtime, CUDA, and training error resolution specialist. Fixes tensor shape mismatches, device errors, gradient issues, DataLoader problems, and mixed precision failures with minimal changes. Use when PyTorch training or inference crashes. |
| [react-build-resolver](./react-build-resolver.md) | Diagnose and fix React build failures across Vite, webpack, Next.js, CRA, Parcel, esbuild, and Bun. Handles JSX/TSX compile errors, hydration mismatches, server/client component boundary failures, missing types, and bundler-specific configuration issues with minimal, surgical changes. MUST BE USED when a React build fails. |
| [rust-build-resolver](./rust-build-resolver.md) | Rust build, compilation, and dependency error resolution specialist. Fixes cargo build errors, borrow checker issues, and Cargo.toml problems with minimal changes. Use when Rust builds fail. |
| [swift-build-resolver](./swift-build-resolver.md) | Swift/Xcode build, compilation, and dependency error resolution specialist. Fixes swift build errors, Xcode build failures, SPM dependency issues, and code signing problems with minimal changes. Use when Swift builds fail. |

### 🔍 Language & Framework Reviewers
| Agent | Description |
|-------|-------------|
| [cpp-reviewer](./cpp-reviewer.md) | Expert C++ code reviewer specializing in memory safety, modern C++ idioms, concurrency, and performance. Use for all C++ code changes. MUST BE USED for C++ projects. |
| [csharp-reviewer](./csharp-reviewer.md) | Expert C# code reviewer specializing in .NET conventions, async patterns, security, nullable reference types, and performance. Use for all C# code changes. MUST BE USED for C# projects. |
| [database-reviewer](./database-reviewer.md) | PostgreSQL database specialist for query optimization, schema design, security, and performance. Use PROACTIVELY when writing SQL, creating migrations, designing schemas, or troubleshooting database performance. Incorporates Supabase best practices. |
| [django-reviewer](./django-reviewer.md) | Expert Django code reviewer specializing in ORM correctness, DRF patterns, migration safety, security misconfigurations, and production-grade Django practices. Use for all Django code changes. MUST BE USED for Django projects. |
| [fastapi-reviewer](./fastapi-reviewer.md) | Reviews FastAPI applications for async correctness, dependency injection, Pydantic schemas, security, OpenAPI quality, testing, and production readiness. |
| [flutter-reviewer](./flutter-reviewer.md) | Flutter and Dart code reviewer. Reviews Flutter code for widget best practices, state management patterns, Dart idioms, performance pitfalls, accessibility, and clean architecture violations. Library-agnostic — works with any state management solution and tooling. |
| [fsharp-reviewer](./fsharp-reviewer.md) | Expert F# code reviewer specializing in functional idioms, type safety, pattern matching, computation expressions, and performance. Use for all F# code changes. MUST BE USED for F# projects. |
| [go-reviewer](./go-reviewer.md) | Expert Go code reviewer specializing in idiomatic Go, concurrency patterns, error handling, and performance. Use for all Go code changes. MUST BE USED for Go projects. |
| [healthcare-reviewer](./healthcare-reviewer.md) | Reviews healthcare application code for clinical safety, CDSS accuracy, PHI compliance, and medical data integrity. Specialized for EMR/EHR, clinical decision support, and health information systems. |
| [java-reviewer](./java-reviewer.md) | Expert Java code reviewer for Spring Boot and Quarkus projects. Automatically detects the framework and applies the appropriate review rules. Covers layered architecture, JPA/Panache, MongoDB, security, and concurrency. MUST BE USED for all Java code changes. |
| [kotlin-reviewer](./kotlin-reviewer.md) | Kotlin and Android/KMP code reviewer. Reviews Kotlin code for idiomatic patterns, coroutine safety, Compose best practices, clean architecture violations, and common Android pitfalls. |
| [php-reviewer](./php-reviewer.md) | Expert PHP code reviewer specializing in PSR-12 compliance, PHP type system, Eloquent ORM patterns, security, and performance. Use for all PHP code changes. MUST BE USED for PHP projects. |
| [python-reviewer](./python-reviewer.md) | Expert Python code reviewer specializing in PEP 8 compliance, Pythonic idioms, type hints, security, and performance. Use for all Python code changes. MUST BE USED for Python projects. |
| [react-reviewer](./react-reviewer.md) | Expert React/JSX code reviewer specializing in hook correctness, render performance, server/client component boundaries, accessibility, and React-specific security. Use for any change touching .tsx/.jsx files or React component logic. MUST BE USED for React projects. |
| [rust-reviewer](./rust-reviewer.md) | Expert Rust code reviewer specializing in ownership, lifetimes, error handling, unsafe usage, and idiomatic patterns. Use for all Rust code changes. MUST BE USED for Rust projects. |
| [swift-reviewer](./swift-reviewer.md) | Expert Swift code reviewer specializing in protocol-oriented design, value semantics, ARC memory management, Swift Concurrency, and idiomatic patterns. Use for all Swift code changes. MUST BE USED for Swift projects. |
| [typescript-reviewer](./typescript-reviewer.md) | Expert TypeScript/JavaScript code reviewer specializing in type safety, async correctness, Node/web security, and idiomatic patterns. Use for all TypeScript and JavaScript code changes. MUST BE USED for TypeScript/JavaScript projects. |
| [vue-reviewer](./vue-reviewer.md) | Expert Vue.js code reviewer specializing in Composition API correctness, reactivity pitfalls, component architecture, template security, and Vue-specific performance. Use for any change touching .vue, .ts/.js files with Vue imports, or Vue ecosystem code (Pinia, Vue Router, Nuxt). MUST BE USED for Vue projects. |

### 🧪 Testing & Quality Assurance
| Agent | Description |
|-------|-------------|
| [test-architect](./test-architect.md) | USE PROACTIVELY for designing comprehensive test strategies, defining coverage goals, creating test plans across all testing layers, and establishing testing standards. MUST BE USED for test strategy planning, coverage analysis, test automation architecture, and quality assurance planning. |
| [unit-test-generator](./unit-test-generator.md) | Invoke for creating comprehensive unit tests with edge cases, mocks, and high code coverage |
| [e2e-test-automator](./e2e-test-automator.md) | USE PROACTIVELY for creating end-to-end tests using Playwright for complete user journey testing, cross-browser validation, and critical path verification. MUST BE USED for user journey testing, cross-browser compatibility testing, visual regression testing, and accessibility testing automation. |
| [integration-test-builder](./integration-test-builder.md) | Invoke for building API tests, database tests, and service interaction tests |
| [code-reviewer](./code-reviewer.md) | Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code. MUST BE USED for all code changes. |
| [accessibility-auditor](./accessibility-auditor.md) | USE PROACTIVELY for auditing WCAG 2.1/2.2 compliance, implementing ARIA patterns, testing keyboard navigation, validating screen reader compatibility, and integrating automated accessibility testing. MUST BE USED for accessibility audits, ARIA implementation review, assistive technology testing, color contrast validation, and CI accessibility gates. |
| [pr-test-analyzer](./pr-test-analyzer.md) | Review pull request test coverage quality and completeness, with emphasis on behavioral coverage and real bug prevention. |
| [tdd-guide](./tdd-guide.md) | Test-Driven Development specialist enforcing write-tests-first methodology. Use PROACTIVELY when writing new features, fixing bugs, or refactoring code. Ensures 80%+ test coverage. |
| [e2e-runner](./e2e-runner.md) | End-to-end testing specialist using Vercel Agent Browser (preferred) with Playwright fallback. Use PROACTIVELY for generating, maintaining, and running E2E tests. Manages test journeys, quarantines flaky tests, uploads artifacts (screenshots, videos, traces), and ensures critical user flows work. |

### 🔒 Security & Compliance
| Agent | Description |
|-------|-------------|
| [security-auditor](./security-auditor.md) | USE PROACTIVELY for identifying security vulnerabilities, ensuring OWASP compliance, conducting security assessments, implementing security controls, and protecting sensitive data. MUST BE USED for security reviews, vulnerability assessments, compliance validation, and security architecture evaluation. |
| [privacy-compliance-agent](./privacy-compliance-agent.md) | USE PROACTIVELY for auditing privacy regulations (GDPR, CCPA) compliance, reviewing PII handling, and verifying consent workflows. MUST BE USED when planning personal data management, configuring data deletion routines, or auditing cookies and tracking systems. |
| [security-reviewer](./security-reviewer.md) | Security vulnerability detection and remediation specialist. Use PROACTIVELY after writing code that handles user input, authentication, API endpoints, or sensitive data. Flags secrets, SSRF, injection, unsafe crypto, and OWASP Top 10 vulnerabilities. |
| [network-config-reviewer](./network-config-reviewer.md) | Reviews router and switch configurations for security, correctness, stale references, risky change-window commands, and missing operational guardrails. |
| [network-troubleshooter](./network-troubleshooter.md) | Diagnoses network connectivity, routing, DNS, interface, and policy symptoms with a read-only OSI-layer workflow and evidence-backed root cause summary. |

### ⚡ Performance & Monitoring
| Agent | Description |
|-------|-------------|
| [performance-profiler](./performance-profiler.md) | Invoke for identifying performance bottlenecks, optimizing resource usage, and ensuring SLA compliance |
| [monitoring-architect](./monitoring-architect.md) | Invoke for ensuring system observability, creating actionable alerts, building dashboards, and enabling quick issue resolution |
| [seo-optimizer](./seo-optimizer.md) | USE PROACTIVELY for implementing technical SEO, structured data markup, Open Graph meta tags, XML sitemaps, and Core Web Vitals optimization in modern web applications. MUST BE USED for metadata strategy, JSON-LD structured data, search engine crawlability, social sharing previews, and SEO performance auditing. |
| [asset-optimizer](./asset-optimizer.md) | USE PROACTIVELY for optimizing frontend bundle sizes, static assets, and resource deliveries. MUST BE USED when configuring bundler settings (Vite, Webpack, Rollup), debugging build performance bottlenecks, implementing code splitting, and analyzing bundle maps. |
| [observability-analyst](./observability-analyst.md) | USE PROACTIVELY for designing logging structures, configuring telemetry, and tracing requests. MUST BE USED when standardizing log formats (Pino, Winston), setting up OpenTelemetry, instrumenting microservices, or building observability Dashboards. |
| [performance-optimizer](./performance-optimizer.md) | Performance analysis and optimization specialist. Use PROACTIVELY for identifying bottlenecks, optimizing slow code, reducing bundle sizes, and improving runtime performance. Profiling, memory leaks, render optimization, and algorithmic improvements. |

### 🚀 DevOps & Deployment
| Agent | Description |
|-------|-------------|
| [cicd-engineer](./cicd-engineer.md) | USE PROACTIVELY for creating CI/CD pipelines, automating builds and deployments, managing environments, and implementing deployment strategies. MUST BE USED for pipeline design, deployment automation, environment management, release orchestration, and build optimization across GitHub Actions, GitLab CI, and other platforms. |
| [docker-specialist](./docker-specialist.md) | Invoke for optimizing containerization, creating efficient Docker images, and implementing orchestration |
| [git-strategist](./git-strategist.md) | USE PROACTIVELY for designing branching strategies, implementing PR workflows, enforcing conventional commits, automating version management, and configuring release tagging. MUST BE USED for branching model selection, branch protection configuration, commit convention enforcement, merge strategy decisions, and release automation setup. |

### 🚀 Open Source Pipeline
| Agent | Description |
|-------|-------------|
| [opensource-forker](./opensource-forker.md) | Fork any project for open-sourcing. Copies files, strips secrets and credentials (20+ patterns), replaces internal references with placeholders, generates .env.example, and cleans git history. First stage of the opensource-pipeline skill. |
| [opensource-packager](./opensource-packager.md) | Generate complete open-source packaging for a sanitized project. Produces CLAUDE.md, setup.sh, README.md, LICENSE, CONTRIBUTING.md, and GitHub issue templates. Makes any repo immediately usable with Claude Code. Third stage of the opensource-pipeline skill. |
| [opensource-sanitizer](./opensource-sanitizer.md) | Verify an open-source fork is fully sanitized before release. Scans for leaked secrets, PII, internal references, and dangerous files using 20+ regex patterns. Generates a PASS/FAIL/PASS-WITH-WARNINGS report. Second stage of the opensource-pipeline skill. Use PROACTIVELY before any public release. |

### 📚 Documentation & Release
| Agent | Description |
|-------|-------------|
| [tech-writer](./tech-writer.md) | Invoke for creating comprehensive documentation, API docs, onboarding guides, and technical architecture documentation |
| [release-compiler](./release-compiler.md) | Invoke for creating release notes, documenting breaking changes, providing migration guides, and compiling changelogs |
| [code-commentator](./code-commentator.md) | Invoke for adding helpful inline documentation, explaining complex logic, and documenting APIs with proper comments |
| [doc-updater](./doc-updater.md) | Documentation and codemap specialist. Use PROACTIVELY for updating codemaps and documentation. Runs /update-codemaps and /update-docs, generates docs/CODEMAPS/*, updates READMEs and guides. |
| [docs-lookup](./docs-lookup.md) | When the user asks how to use a library, framework, or API or needs up-to-date code examples, use Context7 MCP to fetch current documentation and return answers with examples. Invoke for docs/API/setup questions. |

### 🤖 GAN & ML Specialists
| Agent | Description |
|-------|-------------|
| [agent-evaluator](./agent-evaluator.md) | Evaluates agent output against 5-axis quality rubric (accuracy, completeness, clarity, actionability, conciseness). Use after any non-trivial task when the user wants a quality assessment, or when the agent-self-evaluation skill is active. Produces structured scorecard with evidence and improvement suggestions. |
| [gan-evaluator](./gan-evaluator.md) | GAN Harness — Evaluator agent. Tests the live running application via Playwright, scores against rubric, and provides actionable feedback to the Generator. |
| [gan-generator](./gan-generator.md) | GAN Harness — Generator agent. Implements features according to the spec, reads evaluator feedback, and iterates until quality threshold is met. |
| [gan-planner](./gan-planner.md) | GAN Harness — Planner agent. Expands a one-line prompt into a full product specification with features, sprints, evaluation criteria, and design direction. |
| [mle-reviewer](./mle-reviewer.md) | Production machine-learning engineering reviewer for data contracts, feature pipelines, training reproducibility, offline/online evaluation, model serving, monitoring, and rollback. Use when ML, MLOps, model training, inference, feature store, or evaluation code changes. |

### 🎯 Specialized & Domain Specific
| Agent | Description |
|-------|-------------|
| [i18n-specialist](./i18n-specialist.md) | USE PROACTIVELY for implementing internationalization and localization, configuring locale routing, handling ICU MessageFormat for plurals and dates, supporting RTL layouts, and integrating translation management systems. MUST BE USED for i18n framework setup, translation key structure design, RTL implementation, locale detection/switching, and translation workflow configuration. |
| [marketing-agent](./marketing-agent.md) | Marketing strategist and copywriter for campaign planning, audience research, positioning, copy creation, and content review. Covers landing pages, email sequences, social posts, ad copy, short-form video scripts, and content calendars. Use when the user wants to plan or execute a product launch or marketing campaign. |
| [seo-specialist](./seo-specialist.md) | SEO specialist for technical SEO audits, on-page optimization, structured data, Core Web Vitals, and content/keyword mapping. Use for site audits, meta tag reviews, schema markup, sitemap and robots issues, and SEO remediation plans. |
| [silent-failure-hunter](./silent-failure-hunter.md) | Review code for silent failures, swallowed errors, bad fallbacks, and missing error propagation. |

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

