# OpenCode Sub-Agents Collection

A comprehensive collection of 259 specialized agents (258 sub-agents + 1 orchestrator) for [OpenCode](https://opencode.ai), converted from the Claude Code agents collection. Designed to enhance development workflows through domain-specific expertise and intelligent task delegation.

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

### 🏗️ Core Development (`01-core-development`)

| Agent | Description |
|-------|-------------|
| [api-designer](./01-core-development/api-designer.md) | Use this agent when designing new APIs, creating API specifications, or refactoring existing API architecture for scalability and developer experience. Invoke when you need REST/GraphQL endpoint design, OpenAPI documentation, authentication patterns, or API versioning strategies. |
| [api-mock-specialist](./01-core-development/api-mock-specialist.md) | USE PROACTIVELY for creating mock API servers, establishing front-end mock contexts, and seeding mock data. MUST BE USED when mocking REST/GraphQL endpoints for development or testing, configuring Mock Service Worker (MSW), or simulating network behaviors. |
| [architect](./01-core-development/architect.md) | Software architecture specialist for system design, scalability, and technical decision-making. Use PROACTIVELY when planning new features, refactoring large systems, or making architectural decisions. |
| [asset-optimizer](./01-core-development/asset-optimizer.md) | USE PROACTIVELY for optimizing frontend bundle sizes, static assets, and resource deliveries. MUST BE USED when configuring bundler settings (Vite, Webpack, Rollup), debugging build performance bottlenecks, implementing code splitting, and analyzing bundle maps. |
| [auth-architect](./01-core-development/auth-architect.md) | Specialized sub-agent. |
| [backend-architect](./01-core-development/backend-architect.md) | Specialized sub-agent. |
| [backend-developer](./01-core-development/backend-developer.md) | Use this agent when building server-side APIs, microservices, and backend systems that require robust architecture, scalability planning, and production-ready implementation. |
| [caching-strategist](./01-core-development/caching-strategist.md) | Specialized sub-agent. |
| [code-architect](./01-core-development/code-architect.md) | Designs feature architectures by analyzing existing codebase patterns and conventions, then providing implementation blueprints with concrete files, interfaces, data flow, and build order. |
| [database-engineer](./01-core-development/database-engineer.md) | Specialized sub-agent. |
| [design-bridge](./01-core-development/design-bridge.md) | Use this agent when you need to translate a DESIGN.md from the VoltAgent/awesome-design-md repository into polished Claude Code instructions for building user interfaces that faithfully match the chosen brand. Invoke this agent whenever a developer or designer asks to replicate the look and feel of an existing product or website. |
| [electron-pro](./01-core-development/electron-pro.md) | Use this agent when building Electron desktop applications that require native OS integration, cross-platform distribution, security hardening, and performance optimization. Use electron-pro for complete desktop app development from architecture to signed, distributable installers. |
| [frontend-developer](./01-core-development/frontend-developer.md) | Use when building complete frontend applications across React, Vue, and Angular frameworks requiring multi-framework expertise and full-stack integration. |
| [frontend-specialist](./01-core-development/frontend-specialist.md) | Specialized sub-agent. |
| [fullstack-developer](./01-core-development/fullstack-developer.md) | Use this agent when you need to build complete features spanning database, API, and frontend layers together as a cohesive unit. |
| [graphql-architect](./01-core-development/graphql-architect.md) | Use this agent when designing or evolving GraphQL schemas across microservices, implementing federation architectures, or optimizing query performance in distributed graphs. |
| [graphql-specialist](./01-core-development/graphql-specialist.md) | Specialized sub-agent. |
| [microservices-architect](./01-core-development/microservices-architect.md) | Use when designing distributed system architecture, decomposing monolithic applications into independent microservices, or establishing communication patterns between services at scale. |
| [migration-specialist](./01-core-development/migration-specialist.md) | Specialized sub-agent. |
| [mobile-developer](./01-core-development/mobile-developer.md) | Use this agent when building cross-platform mobile applications requiring native performance optimization, platform-specific features, and offline-first architecture. Use for React Native and Flutter projects where code sharing must exceed 80% while maintaining iOS and Android native excellence. |
| [performance-optimizer](./01-core-development/performance-optimizer.md) | Performance analysis and optimization specialist. Use PROACTIVELY for identifying bottlenecks, optimizing slow code, reducing bundle sizes, and improving runtime performance. Profiling, memory leaks, render optimization, and algorithmic improvements. |
| [planner](./01-core-development/planner.md) | Expert planning specialist for complex features and refactoring. Use PROACTIVELY when users request feature implementation, architectural changes, or complex refactoring. Automatically activated for planning tasks. |
| [spec-miner](./01-core-development/spec-miner.md) | Extracts behavioral specs from existing codebases for OpenSpec. Produces flat Requirement and Invariant blocks with structured metadata (entities, enforced, id, test anchors). Outputs openspec/specs/<capability>/spec.md. Fully self-bootstrapping — no dependency on codebase-onboarding. Use when onboarding a brownfield project to spec-driven development. |
| [state-management-architect](./01-core-development/state-management-architect.md) | USE PROACTIVELY for designing frontend state management architectures, configuring global stores, and optimizing state reactivity patterns. MUST BE USED when designing complex application state flows, setting up caching strategies for frontend stores, resolving reactivity leaks, or planning store architectures (Pinia, Redux, Zustand, Recoil). |
| [ui-designer](./01-core-development/ui-designer.md) | Use this agent when designing visual interfaces, creating design systems, building component libraries, or refining user-facing aesthetics requiring expert visual design, interaction patterns, and accessibility considerations. |
| [ui-ux-designer](./01-core-development/ui-ux-designer.md) | Specialized sub-agent. |
| [websocket-architect](./01-core-development/websocket-architect.md) | Specialized sub-agent. |
| [websocket-engineer](./01-core-development/websocket-engineer.md) | Use this agent when implementing real-time bidirectional communication features using WebSockets, Socket.IO, or similar technologies at scale. |

### 💻 Language Specialists (`02-language-specialists`)

| Agent | Description |
|-------|-------------|
| [angular-architect](./02-language-specialists/angular-architect.md) | Use when architecting enterprise Angular 15+ applications with complex state management, optimizing RxJS patterns, designing micro-frontend systems, or solving performance and scalability challenges in large codebases. |
| [build-error-resolver](./02-language-specialists/build-error-resolver.md) | Build and TypeScript error resolution specialist. Use PROACTIVELY when build fails or type errors occur. Fixes build/type errors only with minimal diffs, no architectural edits. Focuses on getting the build green quickly. |
| [cpp-build-resolver](./02-language-specialists/cpp-build-resolver.md) | C++ build, CMake, and compilation error resolution specialist. Fixes build errors, linker issues, and template errors with minimal changes. Use when C++ builds fail. |
| [cpp-pro](./02-language-specialists/cpp-pro.md) | Use this agent when building high-performance C++ systems requiring modern C++20/23 features, template metaprogramming, or zero-overhead abstractions for systems programming, embedded systems, or performance-critical applications. |
| [cpp-reviewer](./02-language-specialists/cpp-reviewer.md) | Expert C++ code reviewer specializing in memory safety, modern C++ idioms, concurrency, and performance. Use for all C++ code changes. MUST BE USED for C++ projects. |
| [csharp-developer](./02-language-specialists/csharp-developer.md) | Use this agent when building ASP.NET Core web APIs, cloud-native .NET solutions, or modern C# applications requiring async patterns, dependency injection, Entity Framework optimization, and clean architecture. |
| [csharp-reviewer](./02-language-specialists/csharp-reviewer.md) | Expert C# code reviewer specializing in .NET conventions, async patterns, security, nullable reference types, and performance. Use for all C# code changes. MUST BE USED for C# projects. |
| [dart-build-resolver](./02-language-specialists/dart-build-resolver.md) | Dart/Flutter build, analysis, and dependency error resolution specialist. Fixes `dart analyze` errors, Flutter compilation failures, pub dependency conflicts, and build_runner issues with minimal, surgical changes. Use when Dart/Flutter builds fail. |
| [database-reviewer](./02-language-specialists/database-reviewer.md) | PostgreSQL database specialist for query optimization, schema design, security, and performance. Use PROACTIVELY when writing SQL, creating migrations, designing schemas, or troubleshooting database performance. Incorporates Supabase best practices. |
| [django-build-resolver](./02-language-specialists/django-build-resolver.md) | Django/Python build, migration, and dependency error resolution specialist. Fixes pip/Poetry errors, migration conflicts, import errors, Django configuration issues, and collectstatic failures with minimal changes. Use when Django setup or startup fails. |
| [django-developer](./02-language-specialists/django-developer.md) | Use when building Django 4+ web applications, REST APIs, or modernizing existing Django projects with async views and enterprise patterns. |
| [django-reviewer](./02-language-specialists/django-reviewer.md) | Expert Django code reviewer specializing in ORM correctness, DRF patterns, migration safety, security misconfigurations, and production-grade Django practices. Use for all Django code changes. MUST BE USED for Django projects. |
| [dotnet-core-expert](./02-language-specialists/dotnet-core-expert.md) | Use when building .NET Core applications requiring cloud-native architecture, high-performance microservices, modern C# patterns, or cross-platform deployment with minimal APIs and advanced ASP.NET Core features. |
| [dotnet-framework-4.8-expert](./02-language-specialists/dotnet-framework-4.8-expert.md) | Use this agent when working on legacy .NET Framework 4.8 enterprise applications that require maintenance, modernization, or integration with Windows-based infrastructure. |
| [elixir-expert](./02-language-specialists/elixir-expert.md) | Use this agent when you need to build fault-tolerant, concurrent systems leveraging OTP patterns, GenServer architectures, and Phoenix framework for real-time applications. |
| [expo-react-native-expert](./02-language-specialists/expo-react-native-expert.md) | Use when building mobile applications with Expo and React Native that require native module integration, navigation setup, performant animations, push notifications, OTA updates, or App Store/Play Store deployment. |
| [fastapi-developer](./02-language-specialists/fastapi-developer.md) | Use when building modern async Python APIs with FastAPI, implementing Pydantic v2 validation, dependency injection patterns, or deploying high-performance ASGI applications. |
| [fastapi-reviewer](./02-language-specialists/fastapi-reviewer.md) | Reviews FastAPI applications for async correctness, dependency injection, Pydantic schemas, security, OpenAPI quality, testing, and production readiness. |
| [flutter-expert](./02-language-specialists/flutter-expert.md) | Use when building cross-platform mobile applications with Flutter 3+ that require custom UI implementation, complex state management, native platform integrations, or performance optimization across iOS/Android/Web. |
| [flutter-reviewer](./02-language-specialists/flutter-reviewer.md) | Flutter and Dart code reviewer. Reviews Flutter code for widget best practices, state management patterns, Dart idioms, performance pitfalls, accessibility, and clean architecture violations. Library-agnostic — works with any state management solution and tooling. |
| [fsharp-reviewer](./02-language-specialists/fsharp-reviewer.md) | Expert F# code reviewer specializing in functional idioms, type safety, pattern matching, computation expressions, and performance. Use for all F# code changes. MUST BE USED for F# projects. |
| [go-build-resolver](./02-language-specialists/go-build-resolver.md) | Go build, vet, and compilation error resolution specialist. Fixes build errors, go vet issues, and linter warnings with minimal changes. Use when Go builds fail. |
| [go-reviewer](./02-language-specialists/go-reviewer.md) | Expert Go code reviewer specializing in idiomatic Go, concurrency patterns, error handling, and performance. Use for all Go code changes. MUST BE USED for Go projects. |
| [golang-pro](./02-language-specialists/golang-pro.md) | Use when building Go applications requiring concurrent programming, high-performance systems, microservices, or cloud-native architectures where idiomatic patterns, error handling excellence, and efficiency are critical. |
| [harmonyos-app-resolver](./02-language-specialists/harmonyos-app-resolver.md) | HarmonyOS application development expert specializing in ArkTS and ArkUI. Reviews code for V2 state management compliance, Navigation routing patterns, API usage, and performance best practices. Use for HarmonyOS/OpenHarmony projects. |
| [java-architect](./02-language-specialists/java-architect.md) | Use this agent when designing enterprise Java architectures, migrating Spring Boot applications, or establishing microservices patterns for scalable cloud-native systems. |
| [java-build-resolver](./02-language-specialists/java-build-resolver.md) | Java/Maven/Gradle build, compilation, and dependency error resolution specialist. Automatically detects Spring Boot or Quarkus and applies framework-specific fixes. Fixes build errors, Java compiler errors, and Maven/Gradle issues with minimal changes. Use when Java builds fail. |
| [java-reviewer](./02-language-specialists/java-reviewer.md) | Expert Java code reviewer for Spring Boot and Quarkus projects. Automatically detects the framework and applies the appropriate review rules. Covers layered architecture, JPA/Panache, MongoDB, security, and concurrency. MUST BE USED for all Java code changes. |
| [javascript-pro](./02-language-specialists/javascript-pro.md) | Use this agent when you need to build, optimize, or refactor modern JavaScript code for browser, Node.js, or full-stack applications requiring ES2023+ features, async patterns, or performance-critical implementations. |
| [kotlin-build-resolver](./02-language-specialists/kotlin-build-resolver.md) | Kotlin/Gradle build, compilation, and dependency error resolution specialist. Fixes build errors, Kotlin compiler errors, and Gradle issues with minimal changes. Use when Kotlin builds fail. |
| [kotlin-reviewer](./02-language-specialists/kotlin-reviewer.md) | Kotlin and Android/KMP code reviewer. Reviews Kotlin code for idiomatic patterns, coroutine safety, Compose best practices, clean architecture violations, and common Android pitfalls. |
| [kotlin-specialist](./02-language-specialists/kotlin-specialist.md) | Use when building Kotlin applications requiring advanced coroutine patterns, multiplatform code sharing, or Android/server-side development with functional programming principles. |
| [laravel-specialist](./02-language-specialists/laravel-specialist.md) | Use when building Laravel 10+ applications, architecting Eloquent models with complex relationships, implementing queue systems for async processing, or optimizing API performance. |
| [nextjs-developer](./02-language-specialists/nextjs-developer.md) | Use this agent when building production Next.js 14+ applications that require full-stack development with App Router, server components, and advanced performance optimization. Invoke when you need to architect or implement complete Next.js applications, optimize Core Web Vitals, implement server actions and mutations, or deploy SEO-optimized applications. |
| [node-specialist](./02-language-specialists/node-specialist.md) | Use this agent when you need to build, optimize, or debug Node.js backend applications, APIs, CLIs, or microservices requiring deep ecosystem knowledge and server-side JavaScript expertise. |
| [php-pro](./02-language-specialists/php-pro.md) | Use this agent when working with PHP 8.3+ projects that require strict typing, modern language features, and enterprise framework expertise (Laravel or Symfony). Use when building scalable applications, optimizing performance, or requiring async/Fiber patterns. |
| [php-reviewer](./02-language-specialists/php-reviewer.md) | Expert PHP code reviewer specializing in PSR-12 compliance, PHP type system, Eloquent ORM patterns, security, and performance. Use for all PHP code changes. MUST BE USED for PHP projects. |
| [powershell-5.1-expert](./02-language-specialists/powershell-5.1-expert.md) | Use when automating Windows infrastructure tasks requiring PowerShell 5.1 scripts with RSAT modules for Active Directory, DNS, DHCP, GPO management, or when building safe, enterprise-grade automation workflows in legacy .NET Framework environments. |
| [powershell-7-expert](./02-language-specialists/powershell-7-expert.md) | Use when building cross-platform cloud automation scripts, Azure infrastructure orchestration, or CI/CD pipelines requiring PowerShell 7+ with modern .NET interop, idempotent operations, and enterprise-grade error handling. |
| [python-pro](./02-language-specialists/python-pro.md) | Use this agent when you need to build type-safe, production-ready Python code for web APIs, system utilities, or complex applications requiring modern async patterns and extensive type coverage. |
| [python-reviewer](./02-language-specialists/python-reviewer.md) | Expert Python code reviewer specializing in PEP 8 compliance, Pythonic idioms, type hints, security, and performance. Use for all Python code changes. MUST BE USED for Python projects. |
| [rails-expert](./02-language-specialists/rails-expert.md) | Use when building or modernizing Rails applications requiring API development, Hotwire reactivity, real-time features, background job processing, deployment automation, or Rails-idiomatic patterns for maximum productivity. Version-aware: adapts to Rails 7.x and 8.x projects. |
| [react-build-resolver](./02-language-specialists/react-build-resolver.md) | Diagnose and fix React build failures across Vite, webpack, Next.js, CRA, Parcel, esbuild, and Bun. Handles JSX/TSX compile errors, hydration mismatches, server/client component boundary failures, missing types, and bundler-specific configuration issues with minimal, surgical changes. MUST BE USED when a React build fails. |
| [react-reviewer](./02-language-specialists/react-reviewer.md) | Expert React/JSX code reviewer specializing in hook correctness, render performance, server/client component boundaries, accessibility, and React-specific security. Use for any change touching .tsx/.jsx files or React component logic. MUST BE USED for React projects. |
| [react-specialist](./02-language-specialists/react-specialist.md) | Use when optimizing existing React applications for performance, implementing advanced React 18+ features, or solving complex state management and architectural challenges within React codebases. |
| [rust-build-resolver](./02-language-specialists/rust-build-resolver.md) | Rust build, compilation, and dependency error resolution specialist. Fixes cargo build errors, borrow checker issues, and Cargo.toml problems with minimal changes. Use when Rust builds fail. |
| [rust-engineer](./02-language-specialists/rust-engineer.md) | Use when building Rust systems where memory safety, ownership patterns, zero-cost abstractions, and performance optimization are critical for systems programming, embedded development, async applications, or high-performance services. |
| [rust-reviewer](./02-language-specialists/rust-reviewer.md) | Expert Rust code reviewer specializing in ownership, lifetimes, error handling, unsafe usage, and idiomatic patterns. Use for all Rust code changes. MUST BE USED for Rust projects. |
| [spring-boot-engineer](./02-language-specialists/spring-boot-engineer.md) | Use this agent when building enterprise Spring Boot 3+ applications requiring microservices architecture, cloud-native deployment, or reactive programming patterns. |
| [sql-pro](./02-language-specialists/sql-pro.md) | Use this agent when you need to optimize complex SQL queries, design efficient database schemas, or solve performance issues across PostgreSQL, MySQL, SQL Server, and Oracle requiring advanced query optimization, index strategies, or data warehouse patterns. |
| [swift-build-resolver](./02-language-specialists/swift-build-resolver.md) | Swift/Xcode build, compilation, and dependency error resolution specialist. Fixes swift build errors, Xcode build failures, SPM dependency issues, and code signing problems with minimal changes. Use when Swift builds fail. |
| [swift-expert](./02-language-specialists/swift-expert.md) | Use this agent when building native iOS, macOS, or server-side Swift applications requiring advanced concurrency patterns, protocol-oriented architecture, and Swift-specific optimizations. Invoke for SwiftUI modernization, async/await implementation, actor-based state management, or memory safety concerns. |
| [swift-reviewer](./02-language-specialists/swift-reviewer.md) | Expert Swift code reviewer specializing in protocol-oriented design, value semantics, ARC memory management, Swift Concurrency, and idiomatic patterns. Use for all Swift code changes. MUST BE USED for Swift projects. |
| [symfony-specialist](./02-language-specialists/symfony-specialist.md) | Use when building Symfony 6+/7+/8+ applications, architecting Doctrine ORM entities with complex relationships, implementing Messenger component for async processing, or optimizing API Platform performance. |
| [typescript-pro](./02-language-specialists/typescript-pro.md) | Use when implementing TypeScript code requiring advanced type system patterns, complex generics, type-level programming, or end-to-end type safety across full-stack applications. |
| [typescript-reviewer](./02-language-specialists/typescript-reviewer.md) | Expert TypeScript/JavaScript code reviewer specializing in type safety, async correctness, Node/web security, and idiomatic patterns. Use for all TypeScript and JavaScript code changes. MUST BE USED for TypeScript/JavaScript projects. |
| [vue-expert](./02-language-specialists/vue-expert.md) | Use this agent when building Vue 3 applications that require Composition API mastery, reactivity optimization, or Nuxt 3 development with enterprise-scale performance concerns. |
| [vue-reviewer](./02-language-specialists/vue-reviewer.md) | Expert Vue.js code reviewer specializing in Composition API correctness, reactivity pitfalls, component architecture, template security, and Vue-specific performance. Use for any change touching .vue, .ts/.js files with Vue imports, or Vue ecosystem code (Pinia, Vue Router, Nuxt). MUST BE USED for Vue projects. |

### ☁️ Infrastructure (`03-infrastructure`)

| Agent | Description |
|-------|-------------|
| [azure-infra-engineer](./03-infrastructure/azure-infra-engineer.md) | Use when designing, deploying, or managing Azure infrastructure with focus on network architecture, Entra ID integration, PowerShell automation, and Bicep IaC. |
| [cicd-engineer](./03-infrastructure/cicd-engineer.md) | Specialized sub-agent. |
| [cloud-architect](./03-infrastructure/cloud-architect.md) | Use this agent when you need to design, evaluate, or optimize cloud infrastructure architecture at scale. Invoke when designing multi-cloud strategies, planning cloud migrations, implementing disaster recovery, optimizing cloud costs, or ensuring security/compliance across cloud platforms. |
| [config-expert](./03-infrastructure/config-expert.md) | Specialized sub-agent. |
| [database-administrator](./03-infrastructure/database-administrator.md) | Use this agent when optimizing database performance, implementing high-availability architectures, setting up disaster recovery, or managing database infrastructure for production systems. |
| [deployment-engineer](./03-infrastructure/deployment-engineer.md) | Use this agent when designing, building, or optimizing CI/CD pipelines and deployment automation strategies. |
| [devops-engineer](./03-infrastructure/devops-engineer.md) | Use this agent when building or optimizing infrastructure automation, CI/CD pipelines, containerization strategies, and deployment workflows to accelerate software delivery while maintaining reliability and security. |
| [devops-incident-responder](./03-infrastructure/devops-incident-responder.md) | Use when actively responding to production incidents, diagnosing critical service failures, or conducting incident postmortems to implement permanent fixes and preventative measures. |
| [docker-expert](./03-infrastructure/docker-expert.md) | Use this agent when you need to build, optimize, or secure Docker container images and orchestration for production environments. |
| [docker-specialist](./03-infrastructure/docker-specialist.md) | Specialized sub-agent. |
| [homelab-architect](./03-infrastructure/homelab-architect.md) | Designs home and small-lab network plans from hardware inventory, goals, and operator experience level, with safe staged changes and rollback guidance. |
| [iac-expert](./03-infrastructure/iac-expert.md) | Specialized sub-agent. |
| [incident-responder](./03-infrastructure/incident-responder.md) | Use this agent when an active security breach, service outage, or operational incident requires immediate response, evidence preservation, and coordinated recovery. |
| [kubernetes-specialist](./03-infrastructure/kubernetes-specialist.md) | Use this agent when you need to design, deploy, configure, or troubleshoot Kubernetes clusters and workloads in production environments. |
| [monitoring-architect](./03-infrastructure/monitoring-architect.md) | Specialized sub-agent. |
| [network-architect](./03-infrastructure/network-architect.md) | Designs enterprise or multi-site network architecture from requirements, using existing network skills for focused routing, validation, automation, and troubleshooting detail. |
| [network-engineer](./03-infrastructure/network-engineer.md) | Use this agent when designing, optimizing, or troubleshooting cloud and hybrid network infrastructures, or when addressing network security, performance, or reliability challenges. |
| [network-troubleshooter](./03-infrastructure/network-troubleshooter.md) | Diagnoses network connectivity, routing, DNS, interface, and policy symptoms with a read-only OSI-layer workflow and evidence-backed root cause summary. |
| [observability-analyst](./03-infrastructure/observability-analyst.md) | USE PROACTIVELY for designing logging structures, configuring telemetry, and tracing requests. MUST BE USED when standardizing log formats (Pino, Winston), setting up OpenTelemetry, instrumenting microservices, or building observability Dashboards. |
| [platform-engineer](./03-infrastructure/platform-engineer.md) | Use when building or improving internal developer platforms (IDPs), designing self-service infrastructure, or optimizing developer workflows to reduce friction and accelerate delivery. The platform-engineer agent specializes in designing platform architecture, implementing golden paths, and maximizing developer self-service capabilities. |
| [queue-architect](./03-infrastructure/queue-architect.md) | Specialized sub-agent. |
| [security-engineer](./03-infrastructure/security-engineer.md) | Use this agent when implementing comprehensive security solutions across infrastructure, building automated security controls into CI/CD pipelines, or establishing compliance and vulnerability management programs. Invoke for threat modeling, zero-trust architecture design, security automation implementation, and shifting security left into development workflows. |
| [serverless-specialist](./03-infrastructure/serverless-specialist.md) | Specialized sub-agent. |
| [sre-engineer](./03-infrastructure/sre-engineer.md) | Use this agent when you need to establish or improve system reliability through SLO definition, error budget management, and automation. Invoke when implementing SLI/SLO frameworks, reducing operational toil, designing fault-tolerant systems, conducting chaos engineering, or optimizing incident response processes. |
| [terraform-engineer](./03-infrastructure/terraform-engineer.md) | Use when building, refactoring, or scaling infrastructure as code using Terraform with focus on multi-cloud deployments, module architecture, and enterprise-grade state management. |
| [terragrunt-expert](./03-infrastructure/terragrunt-expert.md) | Expert Terragrunt specialist mastering infrastructure orchestration, DRY configurations, and multi-environment deployments. Masters stacks, units, dependency management, and scalable IaC patterns with focus on code reuse, maintainability, and enterprise-grade infrastructure automation. |
| [windows-infra-admin](./03-infrastructure/windows-infra-admin.md) | Use when managing Windows Server infrastructure, Active Directory, DNS, DHCP, and Group Policy configurations, especially for enterprise-scale deployments requiring safe automation and compliance validation. |

### 🛡️ Quality & Security (`04-quality-security`)

| Agent | Description |
|-------|-------------|
| [a11y-architect](./04-quality-security/a11y-architect.md) | Accessibility Architect specializing in WCAG 2.2 compliance for Web and Native platforms. Use PROACTIVELY when designing UI components, establishing design systems, or auditing code for inclusive user experiences. |
| [accessibility-auditor](./04-quality-security/accessibility-auditor.md) | Specialized sub-agent. |
| [accessibility-tester](./04-quality-security/accessibility-tester.md) | Use this agent when you need comprehensive accessibility testing, WCAG compliance verification, or assessment of assistive technology support. |
| [ad-security-reviewer](./04-quality-security/ad-security-reviewer.md) | Use this agent when you need to audit Active Directory security posture, evaluate privilege escalation risks, review identity delegation patterns, or assess authentication protocol hardening. |
| [ai-writing-auditor](./04-quality-security/ai-writing-auditor.md) | Use this agent when you need to audit content for AI writing patterns and rewrite text to remove them. |
| [architect-reviewer](./04-quality-security/architect-reviewer.md) | Use this agent when you need to evaluate system design decisions, architectural patterns, and technology choices at the macro level. |
| [chaos-engineer](./04-quality-security/chaos-engineer.md) | Use this agent when you need to design and execute controlled failure experiments, validate system resilience before incidents occur, or conduct game day exercises to test your team's incident response capabilities. |
| [code-reviewer](./04-quality-security/code-reviewer.md) | Use this agent when you need to conduct comprehensive code reviews focusing on code quality, security vulnerabilities, and best practices. |
| [compliance-auditor](./04-quality-security/compliance-auditor.md) | Use this agent when you need to achieve regulatory compliance, implement compliance controls, or prepare for audits across frameworks like GDPR, HIPAA, PCI DSS, SOC 2, and ISO standards. |
| [debugger](./04-quality-security/debugger.md) | Use this agent when you need to diagnose and fix bugs, identify root causes of failures, or analyze error logs and stack traces to resolve issues. |
| [e2e-runner](./04-quality-security/e2e-runner.md) | End-to-end testing specialist using Vercel Agent Browser (preferred) with Playwright fallback. Use PROACTIVELY for generating, maintaining, and running E2E tests. Manages test journeys, quarantines flaky tests, uploads artifacts (screenshots, videos, traces), and ensures critical user flows work. |
| [e2e-test-automator](./04-quality-security/e2e-test-automator.md) | Specialized sub-agent. |
| [error-detective](./04-quality-security/error-detective.md) | Use this agent when you need to diagnose why errors are occurring in your system, correlate errors across services, identify root causes, and prevent future failures. |
| [gdpr-ccpa-compliance](./04-quality-security/gdpr-ccpa-compliance.md) | Use when the user needs to understand GDPR or CCPA compliance, review data practices, or assess privacy requirements. Triggers on: 'GDPR', 'CCPA', 'privacy compliance', 'data privacy', 'right to deletion', 'consent', 'data subject rights', 'California privacy'. |
| [integration-test-builder](./04-quality-security/integration-test-builder.md) | Specialized sub-agent. |
| [network-config-reviewer](./04-quality-security/network-config-reviewer.md) | Reviews router and switch configurations for security, correctness, stale references, risky change-window commands, and missing operational guardrails. |
| [penetration-tester](./04-quality-security/penetration-tester.md) | Use this agent when you need to conduct authorized security penetration tests to identify real vulnerabilities through active exploitation and validation. Use penetration-tester for offensive security testing, vulnerability exploitation, and hands-on risk demonstration. |
| [performance-engineer](./04-quality-security/performance-engineer.md) | Use this agent when you need to identify and eliminate performance bottlenecks in applications, databases, or infrastructure systems, and when baseline performance metrics need improvement. |
| [performance-profiler](./04-quality-security/performance-profiler.md) | Specialized sub-agent. |
| [powershell-security-hardening](./04-quality-security/powershell-security-hardening.md) | Use this agent when you need to harden PowerShell automation, secure remoting configuration, enforce least-privilege design, or align scripts with enterprise security baselines and compliance frameworks. |
| [pr-test-analyzer](./04-quality-security/pr-test-analyzer.md) | Review pull request test coverage quality and completeness, with emphasis on behavioral coverage and real bug prevention. |
| [privacy-compliance-agent](./04-quality-security/privacy-compliance-agent.md) | USE PROACTIVELY for auditing privacy regulations (GDPR, CCPA) compliance, reviewing PII handling, and verifying consent workflows. MUST BE USED when planning personal data management, configuring data deletion routines, or auditing cookies and tracking systems. |
| [qa-expert](./04-quality-security/qa-expert.md) | Use this agent when you need comprehensive quality assurance strategy, test planning across the entire development cycle, or quality metrics analysis to improve overall software quality. |
| [schema-validator](./04-quality-security/schema-validator.md) | Specialized sub-agent. |
| [security-auditor](./04-quality-security/security-auditor.md) | Use this agent when conducting comprehensive security audits, compliance assessments, or risk evaluations across systems, infrastructure, and processes. Invoke when you need systematic vulnerability analysis, compliance gap identification, or evidence-based security findings. |
| [security-reviewer](./04-quality-security/security-reviewer.md) | Security vulnerability detection and remediation specialist. Use PROACTIVELY after writing code that handles user input, authentication, API endpoints, or sensitive data. Flags secrets, SSRF, injection, unsafe crypto, and OWASP Top 10 vulnerabilities. |
| [silent-failure-hunter](./04-quality-security/silent-failure-hunter.md) | Review code for silent failures, swallowed errors, bad fallbacks, and missing error propagation. |
| [tdd-guide](./04-quality-security/tdd-guide.md) | Test-Driven Development specialist enforcing write-tests-first methodology. Use PROACTIVELY when writing new features, fixing bugs, or refactoring code. Ensures 80%+ test coverage. |
| [test-architect](./04-quality-security/test-architect.md) | Specialized sub-agent. |
| [test-automator](./04-quality-security/test-automator.md) | Use this agent when you need to build, implement, or enhance automated test frameworks, create test scripts, or integrate testing into CI/CD pipelines. |
| [ui-ux-tester](./04-quality-security/ui-ux-tester.md) | Use this agent when you need exhaustive UI and UX functionality testing driven by documented user flows, with browser or desktop interaction tooling and structured defect reporting. |
| [unit-test-generator](./04-quality-security/unit-test-generator.md) | Specialized sub-agent. |

### 🧠 Data & AI (`05-data-ai`)

| Agent | Description |
|-------|-------------|
| [ai-engineer](./05-data-ai/ai-engineer.md) | Use this agent when architecting, implementing, or optimizing end-to-end AI systems—from model selection and training pipelines to production deployment and monitoring. |
| [data-analyst](./05-data-ai/data-analyst.md) | Use when you need to extract insights from business data, create dashboards and reports, or perform statistical analysis to support decision-making. |
| [data-engineer](./05-data-ai/data-engineer.md) | Use this agent when you need to design, build, or optimize data pipelines, ETL/ELT processes, and data infrastructure. Invoke when designing data platforms, implementing pipeline orchestration, handling data quality issues, or optimizing data processing costs. |
| [data-scientist](./05-data-ai/data-scientist.md) | Use this agent when you need to analyze data patterns, build predictive models, or extract statistical insights from datasets. Invoke this agent for exploratory analysis, hypothesis testing, machine learning model development, and translating findings into business recommendations. |
| [database-optimizer](./05-data-ai/database-optimizer.md) | Use this agent when you need to analyze slow queries, optimize database performance across multiple systems, or implement indexing strategies to improve query execution. |
| [gan-evaluator](./05-data-ai/gan-evaluator.md) | GAN Harness — Evaluator agent. Tests the live running application via Playwright, scores against rubric, and provides actionable feedback to the Generator. |
| [gan-generator](./05-data-ai/gan-generator.md) | GAN Harness — Generator agent. Implements features according to the spec, reads evaluator feedback, and iterates until quality threshold is met. |
| [gan-planner](./05-data-ai/gan-planner.md) | GAN Harness — Planner agent. Expands a one-line prompt into a full product specification with features, sprints, evaluation criteria, and design direction. |
| [llm-architect](./05-data-ai/llm-architect.md) | Use when designing LLM systems for production, implementing fine-tuning or RAG architectures, optimizing inference serving infrastructure, or managing multi-model deployments. |
| [machine-learning-engineer](./05-data-ai/machine-learning-engineer.md) | Use this agent when you need to deploy, optimize, or serve machine learning models at scale in production environments. |
| [ml-engineer](./05-data-ai/ml-engineer.md) | Use this agent when building production ML systems requiring model training pipelines, model serving infrastructure, performance optimization, and automated retraining. |
| [mle-reviewer](./05-data-ai/mle-reviewer.md) | Production machine-learning engineering reviewer for data contracts, feature pipelines, training reproducibility, offline/online evaluation, model serving, monitoring, and rollback. Use when ML, MLOps, model training, inference, feature store, or evaluation code changes. |
| [mlops-engineer](./05-data-ai/mlops-engineer.md) | Use this agent when you need to design and implement ML infrastructure, set up CI/CD for machine learning models, establish model versioning systems, or optimize ML platforms for reliability and automation. Invoke this agent to build production-grade experiment tracking, implement automated training pipelines, configure GPU resource orchestration, and establish operational monitoring for ML systems. |
| [nlp-engineer](./05-data-ai/nlp-engineer.md) | Use when building production NLP systems, implementing text processing pipelines, developing language models, or solving domain-specific NLP tasks like named entity recognition, sentiment analysis, or machine translation. |
| [postgres-pro](./05-data-ai/postgres-pro.md) | Use when you need to optimize PostgreSQL performance, design high-availability replication, or troubleshoot database issues at scale. Invoke this agent for query optimization, configuration tuning, replication setup, backup strategies, and mastering advanced PostgreSQL features for enterprise deployments. |
| [prompt-engineer](./05-data-ai/prompt-engineer.md) | Use this agent when you need to design, optimize, test, or evaluate prompts for large language models in production systems. |
| [pytorch-build-resolver](./05-data-ai/pytorch-build-resolver.md) | PyTorch runtime, CUDA, and training error resolution specialist. Fixes tensor shape mismatches, device errors, gradient issues, DataLoader problems, and mixed precision failures with minimal changes. Use when PyTorch training or inference crashes. |
| [reinforcement-learning-engineer](./05-data-ai/reinforcement-learning-engineer.md) | Use when designing RL environments, training agents with reward optimization, implementing policy gradient methods, or deploying decision-making systems for robotics, gaming, and autonomous operations. |

### 🛠️ Developer Experience (`06-developer-experience`)

| Agent | Description |
|-------|-------------|
| [build-engineer](./06-developer-experience/build-engineer.md) | Use this agent when you need to optimize build performance, reduce compilation times, or scale build systems across growing teams. |
| [cli-developer](./06-developer-experience/cli-developer.md) | Use this agent when building command-line tools and terminal applications that require intuitive command design, cross-platform compatibility, and optimized developer experience. |
| [code-commentator](./06-developer-experience/code-commentator.md) | Specialized sub-agent. |
| [code-explorer](./06-developer-experience/code-explorer.md) | Deeply analyzes existing codebase features by tracing execution paths, mapping architecture layers, and documenting dependencies to inform new development. |
| [code-simplifier](./06-developer-experience/code-simplifier.md) | Simplifies and refines code for clarity, consistency, and maintainability while preserving behavior. Focus on recently modified code unless instructed otherwise. |
| [comment-analyzer](./06-developer-experience/comment-analyzer.md) | Analyze code comments for accuracy, completeness, maintainability, and comment rot risk. |
| [dependency-manager](./06-developer-experience/dependency-manager.md) | Use this agent when you need to audit dependencies for vulnerabilities, resolve version conflicts, optimize bundle sizes, or implement automated dependency updates. |
| [doc-updater](./06-developer-experience/doc-updater.md) | Documentation and codemap specialist. Use PROACTIVELY for updating codemaps and documentation. Runs /update-codemaps and /update-docs, generates docs/CODEMAPS/*, updates READMEs and guides. |
| [docs-lookup](./06-developer-experience/docs-lookup.md) | When the user asks how to use a library, framework, or API or needs up-to-date code examples, use Context7 MCP to fetch current documentation and return answers with examples. Invoke for docs/API/setup questions. |
| [documentation-engineer](./06-developer-experience/documentation-engineer.md) | Use this agent when you need to create, architect, or overhaul comprehensive documentation systems including API docs, tutorials, guides, and developer-friendly content that keeps pace with code changes. |
| [dx-optimizer](./06-developer-experience/dx-optimizer.md) | Use this agent when optimizing the complete developer workflow including build times, feedback loops, testing efficiency, and developer satisfaction metrics across the entire development environment. |
| [git-strategist](./06-developer-experience/git-strategist.md) | Specialized sub-agent. |
| [git-workflow-manager](./06-developer-experience/git-workflow-manager.md) | Use this agent when you need to design, establish, or optimize Git workflows, branching strategies, and merge management for a project or team. |
| [harness-optimizer](./06-developer-experience/harness-optimizer.md) | Analyze and improve the local agent harness configuration for reliability, cost, and throughput. |
| [legacy-modernizer](./06-developer-experience/legacy-modernizer.md) | Use this agent when modernizing legacy systems that need incremental migration strategies, technical debt reduction, and risk mitigation while maintaining business continuity. |
| [mcp-developer](./06-developer-experience/mcp-developer.md) | Use this agent when you need to build, debug, or optimize Model Context Protocol (MCP) servers and clients that connect AI systems to external tools and data sources. |
| [mindful-dev](./06-developer-experience/mindful-dev.md) | Specialized sub-agent. |
| [monorepo-engineer](./06-developer-experience/monorepo-engineer.md) | Specialized sub-agent. |
| [opensource-forker](./06-developer-experience/opensource-forker.md) | Fork any project for open-sourcing. Copies files, strips secrets and credentials (20+ patterns), replaces internal references with placeholders, generates .env.example, and cleans git history. First stage of the opensource-pipeline skill. |
| [opensource-packager](./06-developer-experience/opensource-packager.md) | Generate complete open-source packaging for a sanitized project. Produces CLAUDE.md, setup.sh, README.md, LICENSE, CONTRIBUTING.md, and GitHub issue templates. Makes any repo immediately usable with Claude Code. Third stage of the opensource-pipeline skill. |
| [opensource-sanitizer](./06-developer-experience/opensource-sanitizer.md) | Verify an open-source fork is fully sanitized before release. Scans for leaked secrets, PII, internal references, and dangerous files using 20+ regex patterns. Generates a PASS/FAIL/PASS-WITH-WARNINGS report. Second stage of the opensource-pipeline skill. Use PROACTIVELY before any public release. |
| [powershell-module-architect](./06-developer-experience/powershell-module-architect.md) | Use this agent when architecting and refactoring PowerShell modules, designing profile systems, or creating cross-version compatible automation libraries. Invoke it for module design reviews, profile optimization, packaging reusable code, and standardizing function structure across teams. |
| [powershell-ui-architect](./06-developer-experience/powershell-ui-architect.md) | Use when designing or building desktop graphical interfaces (WinForms, WPF, Metro-style dashboards) or terminal user interfaces (TUIs) for PowerShell automation tools that need clean separation between UI and business logic. |
| [readme-generator](./06-developer-experience/readme-generator.md) | Use this agent when you need a maintainer-ready README built from exact repository reality, with deep codebase scanning, zero hallucination, and optional git commit/push only when explicitly requested. |
| [refactor-cleaner](./06-developer-experience/refactor-cleaner.md) | Dead code cleanup and consolidation specialist. Use PROACTIVELY for removing unused code, duplicates, and refactoring. Runs analysis tools (knip, depcheck, ts-prune) to identify dead code and safely removes it. |
| [refactoring-expert](./06-developer-experience/refactoring-expert.md) | Specialized sub-agent. |
| [refactoring-specialist](./06-developer-experience/refactoring-specialist.md) | Use when you need to transform poorly structured, complex, or duplicated code into clean, maintainable systems while preserving all existing behavior. |
| [slack-expert](./06-developer-experience/slack-expert.md) | Use this agent when developing Slack applications, implementing Slack API integrations, or reviewing Slack bot code for security and best practices. |
| [tooling-engineer](./06-developer-experience/tooling-engineer.md) | Use this agent when you need to build or enhance developer tools including CLIs, code generators, build tools, and IDE extensions. |
| [type-design-analyzer](./06-developer-experience/type-design-analyzer.md) | Analyze type design for encapsulation, invariant expression, usefulness, and enforcement. |
| [visual-asset-generator](./06-developer-experience/visual-asset-generator.md) | Use this agent when you need to generate production-ready visual assets for a project — app icons, favicons, OG images, logos, wordmarks, or social media images. Invokes the prompt-to-asset MCP server to route generation requests across 30+ image models. |

### 🎯 Specialized Domains (`07-specialized-domains`)

| Agent | Description |
|-------|-------------|
| [api-documenter](./07-specialized-domains/api-documenter.md) | Use this agent when creating or improving API documentation, writing OpenAPI specifications, building interactive documentation portals, or generating code examples for APIs. |
| [blockchain-developer](./07-specialized-domains/blockchain-developer.md) | Use this agent when building smart contracts, DApps, and blockchain protocols that require expertise in Solidity, gas optimization, security auditing, and Web3 integration. |
| [embedded-systems](./07-specialized-domains/embedded-systems.md) | Use when developing firmware for resource-constrained microcontrollers, implementing RTOS-based applications, or optimizing real-time systems where hardware constraints, latency guarantees, and reliability are critical. |
| [fintech-engineer](./07-specialized-domains/fintech-engineer.md) | Use when building payment systems, financial integrations, or compliance-heavy financial applications that require secure transaction processing, regulatory adherence, and high transaction accuracy. |
| [game-developer](./07-specialized-domains/game-developer.md) | Use this agent when implementing game systems, optimizing graphics rendering, building multiplayer networking, or developing gameplay mechanics for games targeting specific platforms. |
| [healthcare-admin](./07-specialized-domains/healthcare-admin.md) | Use when working on healthcare administration tasks including revenue cycle management, HIPAA/compliance auditing, medical coding (ICD-10, CPT, DRGs), CMS cost reports, payer contract analysis, quality improvement, clinical operations, health IT/interoperability, population health, and pharmacy benefits. |
| [healthcare-reviewer](./07-specialized-domains/healthcare-reviewer.md) | Reviews healthcare application code for clinical safety, CDSS accuracy, PHI compliance, and medical data integrity. Specialized for EMR/EHR, clinical decision support, and health information systems. |
| [hipaa-compliance](./07-specialized-domains/hipaa-compliance.md) | Use when the user is building a healthcare product and needs to understand HIPAA compliance. Triggers on: 'HIPAA', 'protected health information', 'PHI', 'healthcare compliance', 'covered entity', 'business associate', 'BAA', 'HITECH', 'health data'. |
| [i18n-specialist](./07-specialized-domains/i18n-specialist.md) | Specialized sub-agent. |
| [iot-engineer](./07-specialized-domains/iot-engineer.md) | Use when designing and deploying IoT solutions requiring expertise in device management, edge computing, cloud integration, and handling challenges like massive device scale, complex connectivity scenarios, or real-time data pipelines. |
| [m365-admin](./07-specialized-domains/m365-admin.md) | Use when automating Microsoft 365 administrative tasks including Exchange Online mailbox provisioning, Teams collaboration management, SharePoint site configuration, license lifecycle management, and Graph API-driven identity automation. |
| [mobile-app-developer](./07-specialized-domains/mobile-app-developer.md) | Use this agent when developing iOS and Android mobile applications with focus on native or cross-platform implementation, performance optimization, and platform-specific user experience. |
| [payment-integration](./07-specialized-domains/payment-integration.md) | Use this agent when implementing payment systems, integrating payment gateways, or handling financial transactions that require PCI compliance, fraud prevention, and secure transaction processing. |
| [quant-analyst](./07-specialized-domains/quant-analyst.md) | Use this agent when you need to develop quantitative trading strategies, build financial models with rigorous mathematical foundations, or conduct advanced risk analytics for derivatives and portfolios. Invoke this agent for statistical arbitrage strategy development, backtesting with historical validation, derivatives pricing models, and portfolio risk assessment. |
| [risk-manager](./07-specialized-domains/risk-manager.md) | Use this agent when you need to identify, quantify, and mitigate enterprise-level risks across financial, operational, regulatory, and strategic domains. Invoke this agent when you need to assess risk exposure, design control frameworks, validate risk models, or ensure regulatory compliance. |
| [seo-optimizer](./07-specialized-domains/seo-optimizer.md) | Specialized sub-agent. |
| [seo-specialist](./07-specialized-domains/seo-specialist.md) | Use this agent when you need comprehensive SEO optimization encompassing technical audits, keyword strategy, content optimization, and search rankings improvement. |

### 💼 Business & Product (`08-business-product`)

| Agent | Description |
|-------|-------------|
| [assumption-mapping](./08-business-product/assumption-mapping.md) | Use when the user needs to identify and prioritize risky assumptions in a product idea, feature, or strategy. Triggers on: 'assumptions', 'what could go wrong', 'validate', 'riskiest assumption', 'de-risk', 'assumption map'. |
| [backlog-grooming](./08-business-product/backlog-grooming.md) | Use when the user needs to groom, refine, or clean up a product backlog. Triggers on: 'groom backlog', 'backlog refinement', 'backlog grooming', 'clean up backlog', 'refine stories', 'sprint refinement', 'backlog management'. |
| [business-analyst](./08-business-product/business-analyst.md) | Use when analyzing business processes, gathering requirements from stakeholders, or identifying process improvement opportunities to drive operational efficiency and measurable business value. |
| [chief-of-staff](./08-business-product/chief-of-staff.md) | Personal communication chief of staff that triages email, Slack, LINE, and Messenger. Classifies messages into 4 tiers (skip/info_only/meeting_info/action_required), generates draft replies, and enforces post-send follow-through via hooks. Use when managing multi-channel communication workflows. |
| [content-marketer](./08-business-product/content-marketer.md) | Use this agent when you need to develop comprehensive content strategies, create SEO-optimized marketing content, or execute multi-channel content campaigns to drive engagement and conversions. Invoke this agent for content planning, content creation, audience analysis, and measuring content ROI. |
| [content-quality-editor](./08-business-product/content-quality-editor.md) | Use this agent before publishing any AI-generated content — blog posts, READMEs, release notes, commit messages, PR descriptions, documentation, or social posts. Strips AI writing patterns using unslop, then performs a final quality pass. |
| [customer-success-manager](./08-business-product/customer-success-manager.md) | Use this agent when you need to assess customer health, develop retention strategies, identify upsell opportunities, or maximize customer lifetime value. Invoke this agent for account health analysis, churn prevention, product adoption optimization, and customer success planning. |
| [growth-loops](./08-business-product/growth-loops.md) | Use when the user wants to design a growth loop, understand PLG mechanics, or build sustainable acquisition. Triggers on: 'growth loop', 'flywheel', 'viral loop', 'PLG growth', 'product-led growth', 'growth mechanics', 'how do we grow', 'word of mouth'. |
| [legal-advisor](./08-business-product/legal-advisor.md) | Use this agent when you need to draft contracts, review compliance requirements, develop IP protection strategies, or assess legal risks for technology businesses. |
| [license-engineer](./08-business-product/license-engineer.md) | Use this agent when architecting, implementing, or optimizing end-to-end legal licensing systems—from OSI standard selection and dependency compliance pipelines to proprietary deployment and risk monitoring. |
| [marketing-agent](./08-business-product/marketing-agent.md) | Marketing strategist and copywriter for campaign planning, audience research, positioning, copy creation, and content review. Covers landing pages, email sequences, social posts, ad copy, short-form video scripts, and content calendars. Use when the user wants to plan or execute a product launch or marketing campaign. |
| [product-manager](./08-business-product/product-manager.md) | Use this agent when you need to make product strategy decisions, prioritize features, or define roadmap plans based on user needs and business goals. |
| [project-manager](./08-business-product/project-manager.md) | Use this agent when you need to establish project plans, track execution progress, manage risks, control budget/schedule, and coordinate stakeholders across complex initiatives. |
| [release-compiler](./08-business-product/release-compiler.md) | Specialized sub-agent. |
| [sales-engineer](./08-business-product/sales-engineer.md) | Use this agent when you need to conduct technical pre-sales activities including solution architecture, proof-of-concept development, and technical demonstrations for complex sales deals. |
| [scrum-master](./08-business-product/scrum-master.md) | Use when teams need facilitation, process optimization, velocity improvement, or agile ceremony management—especially for sprint planning, retrospectives, impediment removal, and scaling agile practices across multiple teams. |
| [tech-writer](./08-business-product/tech-writer.md) | Specialized sub-agent. |
| [technical-writer](./08-business-product/technical-writer.md) | Use this agent when you need to create, improve, or maintain technical documentation including API references, user guides, SDK documentation, and getting-started guides. |
| [ux-researcher](./08-business-product/ux-researcher.md) | Use this agent when you need to conduct user research, analyze user behavior, or generate actionable insights to validate design decisions and uncover user needs. Invoke when you need usability testing, user interviews, survey design, analytics interpretation, persona development, or competitive research to inform product strategy. |
| [wordpress-master](./08-business-product/wordpress-master.md) | Use this agent when you need to architect, optimize, or troubleshoot WordPress implementations ranging from custom theme/plugin development to enterprise-scale multisite platforms. Invoke this agent for performance optimization, security hardening, headless WordPress APIs, WooCommerce solutions, and scaling WordPress to handle millions of visitors. |
| [workflow-dmn-engineer](./08-business-product/workflow-dmn-engineer.md) | USE PROACTIVELY for modeling, implementing, and debugging business rules (DMN) and workflow processes (BPMN). MUST BE USED when configuring decision tables, setting up Flowable/Camunda process definitions, mapping BPMN service tasks, and designing stateful workflows. |

### 🔄 Meta & Orchestration (`09-meta-orchestration`)

| Agent | Description |
|-------|-------------|
| [agent-evaluator](./09-meta-orchestration/agent-evaluator.md) | Evaluates agent output against 5-axis quality rubric (accuracy, completeness, clarity, actionability, conciseness). Use after any non-trivial task when the user wants a quality assessment, or when the agent-self-evaluation skill is active. Produces structured scorecard with evidence and improvement suggestions. |
| [agent-installer](./09-meta-orchestration/agent-installer.md) | Use this agent when the user wants to discover, browse, or install Claude Code agents from the awesome-claude-code-subagents repository. |
| [agent-organizer](./09-meta-orchestration/agent-organizer.md) | Use when assembling and optimizing multi-agent teams to execute complex projects that require careful task decomposition, agent capability matching, and workflow coordination. |
| [codebase-orchestrator](./09-meta-orchestration/codebase-orchestrator.md) | Use this agent when you need repository-wide refactor governance with explicit approval loops, weighted risk prioritization, diff previews, and deterministic fallback strategies. |
| [context-manager](./09-meta-orchestration/context-manager.md) | Use for managing shared state, information retrieval, and data synchronization when multiple agents need coordinated access to context and metadata. |
| [conversation-analyzer](./09-meta-orchestration/conversation-analyzer.md) | Use this agent when analyzing conversation transcripts to find behaviors worth preventing with hooks. Triggered by /hookify without arguments. |
| [error-coordinator](./09-meta-orchestration/error-coordinator.md) | Use this agent when distributed system errors occur and need coordinated handling across multiple components, or when you need to implement comprehensive error recovery strategies with automated failure detection and cascade prevention. |
| [it-ops-orchestrator](./09-meta-orchestration/it-ops-orchestrator.md) | Use for orchestrating complex IT operations tasks that span multiple domains (PowerShell automation, .NET development, infrastructure management, Azure, M365) by intelligently routing work to specialized agents. |
| [knowledge-synthesizer](./09-meta-orchestration/knowledge-synthesizer.md) | Use when you need to extract actionable patterns from agent interactions, synthesize insights across multiple workflows, and enable organizational learning from collective experience. |
| [loop-operator](./09-meta-orchestration/loop-operator.md) | Operate autonomous agent loops, monitor progress, and intervene safely when loops stall. |
| [multi-agent-coordinator](./09-meta-orchestration/multi-agent-coordinator.md) | Use when coordinating multiple concurrent agents that need to communicate, share state, synchronize work, and handle distributed failures across a system. |
| [performance-monitor](./09-meta-orchestration/performance-monitor.md) | Use when establishing observability infrastructure to track system metrics, detect performance anomalies, and optimize resource usage across multi-agent environments. |
| [project-orchestrator](./09-meta-orchestration/project-orchestrator.md) | Specialized sub-agent. |
| [task-distributor](./09-meta-orchestration/task-distributor.md) | Use when distributing tasks across multiple agents or workers, managing queues, and balancing workloads to maximize throughput while respecting priorities and deadlines. |
| [workflow-orchestrator](./09-meta-orchestration/workflow-orchestrator.md) | Use this agent when you need to design, implement, or optimize complex business process workflows with multiple states, error handling, and transaction management. |

### 🔬 Research & Analysis (`10-research-analysis`)

| Agent | Description |
|-------|-------------|
| [ab-test-analysis](./10-research-analysis/ab-test-analysis.md) | Use when the user wants to analyze A/B test results, interpret p-values, determine statistical significance, or make a ship/no-ship decision. Triggers on: 'analyze A/B test', 'p-value', 'statistical significance', 'confidence interval', 'ship or no ship', 'test results', 'did it work'. |
| [cohort-analysis](./10-research-analysis/cohort-analysis.md) | Use when the user wants to analyze retention, cohort behavior, engagement trends, or understand how different user groups perform over time. Triggers on: 'cohort analysis', 'retention analysis', 'user retention', 'cohort retention', 'week 1 retention', 'retention curve'. |
| [competitive-analyst](./10-research-analysis/competitive-analyst.md) | Use when you need to analyze direct and indirect competitors, benchmark against market leaders, or develop strategies to strengthen competitive positioning and market advantage. |
| [data-researcher](./10-research-analysis/data-researcher.md) | Use this agent when you need to discover, collect, and validate data from multiple sources to fuel analysis and decision-making. Invoke this agent for identifying data sources, gathering raw datasets, performing quality checks, and preparing data for downstream analysis or modeling. |
| [first-principles-thinking](./10-research-analysis/first-principles-thinking.md) | Use when the user wants to challenge assumptions, break down a complex problem from scratch, or approach something with first principles reasoning. Triggers on: 'first principles', 'challenge assumptions', 'why do we do it this way', 'rethink', 'from scratch', 'fundamental truths'. |
| [market-researcher](./10-research-analysis/market-researcher.md) | Use this agent when you need to analyze markets, understand consumer behavior, assess competitive landscapes, and size opportunities to inform business strategy and market entry decisions. |
| [project-idea-validator](./10-research-analysis/project-idea-validator.md) | Use this agent when you need an idea pressure-tested with brutal honesty, competitor teardown, market validation, and clear go/no-go guidance before building. |
| [research-analyst](./10-research-analysis/research-analyst.md) | Use this agent when you need comprehensive research across multiple sources with synthesis of findings into actionable insights, trend identification, and detailed reporting. |
| [scientific-literature-researcher](./10-research-analysis/scientific-literature-researcher.md) | Use when you need to search scientific literature and retrieve structured experimental data from published studies. Invoke this agent when the task requires evidence-grounded answers from full-text research papers, including methods, results, sample sizes, and quality scores. |
| [search-specialist](./10-research-analysis/search-specialist.md) | Use when you need to find specific information across multiple sources using advanced search strategies, query optimization, and targeted information retrieval. Invoke this agent when the priority is locating precise, relevant results efficiently rather than analyzing or synthesizing content. |
| [trend-analyst](./10-research-analysis/trend-analyst.md) | Use when analyzing emerging patterns, predicting industry shifts, or developing future scenarios to inform strategic planning and competitive positioning. |

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

