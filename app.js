// OpenCode Showcase Page interactive logic
document.addEventListener("DOMContentLoaded", () => {
    // Check if AGENTS_DATA exists (loaded from agents-data.js)
    if (typeof AGENTS_DATA === 'undefined') {
        console.error("AGENTS_DATA is not defined. Make sure agents-data.js is loaded first.");
        return;
    }

    // Categories static catalog mapping
    const CATEGORIES = [
        { id: "01-core-development", name: "Core Development", icon: "🏗️" },
        { id: "02-language-specialists", name: "Language Specialists", icon: "💻" },
        { id: "03-infrastructure", name: "Infrastructure", icon: "☁️" },
        { id: "04-quality-security", name: "Quality & Security", icon: "🛡️" },
        { id: "05-data-ai", name: "Data & AI", icon: "🧠" },
        { id: "06-developer-experience", name: "Developer Experience", icon: "🛠️" },
        { id: "07-specialized-domains", name: "Specialized Domains", icon: "🎯" },
        { id: "08-business-product", name: "Business & Product", icon: "💼" },
        { id: "09-meta-orchestration", name: "Meta & Orchestration", icon: "🔄" },
        { id: "10-research-analysis", name: "Research & Analysis", icon: "🔬" }
    ];

    // State Variables
    let currentFilters = {
        search: "",
        category: null,
        tools: {
            write: false,
            edit: false,
            bash: false
        },
        sortBy: "name-asc"
    };

    // DOM Elements Cache
    const searchInput = document.getElementById("search-input");
    const clearSearchBtn = document.getElementById("clear-search");
    const categoryContainer = document.getElementById("category-filter-container");
    const toolWriteCheckbox = document.getElementById("tool-write");
    const toolEditCheckbox = document.getElementById("tool-edit");
    const toolBashCheckbox = document.getElementById("tool-bash");
    const resetFiltersBtn = document.getElementById("reset-filters");
    const emptyResetBtn = document.getElementById("empty-reset-btn");
    const sortSelect = document.getElementById("sort-select");
    
    const agentGrid = document.getElementById("agent-grid");
    const resultsCountBadge = document.getElementById("results-count");
    const emptyState = document.getElementById("empty-state");

    // Stats Elements
    const statTotalAgents = document.getElementById("stat-total-agents");
    const statCategories = document.getElementById("stat-categories");
    const statPrimary = document.getElementById("stat-primary");
    const statBashAgents = document.getElementById("stat-bash-agents");

    // Modal Elements
    const agentModal = document.getElementById("agent-modal");
    const modalCloseBtn = document.getElementById("modal-close");
    const modalCloseFooterBtn = document.getElementById("modal-close-footer");
    const modalCategoryIcon = document.getElementById("modal-category-icon");
    const modalAgentName = document.getElementById("modal-agent-name");
    const modalAgentCategory = document.getElementById("modal-agent-category");
    const modalAgentMode = document.getElementById("modal-agent-mode");
    const modalAgentDescription = document.getElementById("modal-agent-description");
    const modalToolsContainer = document.getElementById("modal-tools-container");
    
    const modalRawBtn = document.getElementById("modal-raw-btn");
    
    // Code tabs elements
    const tabButtons = document.querySelectorAll(".tab-btn");
    const codePromptText = document.getElementById("code-prompt-text");
    const codeYamlText = document.getElementById("code-yaml-text");
    const codeJsonText = document.getElementById("code-json-text");
    
    // Copy buttons
    const copyPromptBtn = document.getElementById("copy-prompt-btn");
    const copyYamlBtn = document.getElementById("copy-yaml-btn");
    const copyJsonBtn = document.getElementById("copy-json-btn");

    // Initialize Page Stats
    function initStats() {
        statTotalAgents.textContent = AGENTS_DATA.length;
        statCategories.textContent = CATEGORIES.length;
        
        const primaryCount = AGENTS_DATA.filter(a => a.mode === "primary").length;
        statPrimary.textContent = primaryCount;
        
        const bashCount = AGENTS_DATA.filter(a => a.tools && a.tools.bash === true).length;
        statBashAgents.textContent = bashCount;
    }

    // Render category sidebar filter buttons
    function renderCategoryFilters() {
        categoryContainer.innerHTML = "";
        
        // Add "All Categories" count button
        const allBtn = document.createElement("button");
        allBtn.className = "category-btn active";
        allBtn.dataset.catId = "all";
        allBtn.innerHTML = `
            <span class="category-btn-left">
                <span class="category-icon">📁</span>
                <span>All Agents</span>
            </span>
            <span class="category-count">${AGENTS_DATA.length}</span>
        `;
        allBtn.addEventListener("click", () => selectCategory(null));
        categoryContainer.appendChild(allBtn);

        // Individual category buttons
        CATEGORIES.forEach(cat => {
            const count = AGENTS_DATA.filter(a => a.category === cat.id).length;
            const btn = document.createElement("button");
            btn.className = "category-btn";
            btn.dataset.catId = cat.id;
            btn.innerHTML = `
                <span class="category-btn-left">
                    <span class="category-icon">${cat.icon}</span>
                    <span>${cat.name}</span>
                </span>
                <span class="category-count">${count}</span>
            `;
            btn.addEventListener("click", () => selectCategory(cat.id));
            categoryContainer.appendChild(btn);
        });
    }

    // Category selection update logic
    function selectCategory(catId) {
        currentFilters.category = catId;
        
        // Update active class in DOM
        const buttons = categoryContainer.querySelectorAll(".category-btn");
        buttons.forEach(btn => {
            if (btn.dataset.catId === (catId || "all")) {
                btn.classList.add("active");
            } else {
                btn.classList.remove("active");
            }
        });
        
        applyFilters();
    }

    // Generate Agent Card Element
    function createAgentCard(agent) {
        const card = document.createElement("div");
        card.className = "agent-card";
        card.dataset.agentId = agent.id;
        
        // Category representation
        const isOrchestrator = agent.category === "orchestrator";
        const catBadge = `<span class="badge ${isOrchestrator ? 'badge-primary' : 'badge-category'}">${agent.categoryName}</span>`;
        const modeBadge = `<span class="badge badge-mode">${agent.mode}</span>`;
        
        // Tool representation
        const writeTag = agent.tools && agent.tools.write ? '<span class="tool-tag enabled">write</span>' : '<span class="tool-tag disabled">write</span>';
        const editTag = agent.tools && agent.tools.edit ? '<span class="tool-tag enabled">edit</span>' : '<span class="tool-tag disabled">edit</span>';
        const bashTag = agent.tools && agent.tools.bash ? '<span class="tool-tag enabled">bash</span>' : '<span class="tool-tag disabled">bash</span>';

        card.innerHTML = `
            <div class="card-header">
                <div class="card-meta-tags">
                    ${catBadge}
                    ${modeBadge}
                </div>
                <h3 class="card-title">${agent.name}</h3>
                <p class="card-desc">${agent.description || 'No description provided.'}</p>
            </div>
            <div class="card-footer">
                <div class="card-tools">
                    ${writeTag}
                    ${editTag}
                    ${bashTag}
                </div>
                <button class="card-action-btn">
                    Details <i data-lucide="arrow-right"></i>
                </button>
            </div>
        `;

        // Click to open details
        card.addEventListener("click", (e) => {
            openAgentModal(agent);
        });

        return card;
    }

    // Modal Controls
    function openAgentModal(agent) {
        modalCategoryIcon.textContent = agent.categoryIcon || "🤖";
        modalAgentName.textContent = agent.name;
        modalAgentCategory.textContent = agent.categoryName;
        modalAgentMode.textContent = agent.mode;
        
        // Mode styling
        if (agent.mode === "primary") {
            modalAgentCategory.className = "badge badge-primary";
        } else {
            modalAgentCategory.className = "badge badge-category";
        }

        modalAgentDescription.textContent = agent.description || "No execution rules specified.";
        
        // Setup Toolsbadges
        modalToolsContainer.innerHTML = "";
        const toolsToCheck = ['write', 'edit', 'bash'];
        toolsToCheck.forEach(tool => {
            const isEnabled = agent.tools && agent.tools[tool] === true;
            const toolItem = document.createElement("div");
            toolItem.className = `modal-tool-item ${isEnabled ? 'enabled' : 'disabled'}`;
            
            const iconName = isEnabled ? 'check-circle' : 'minus-circle';
            toolItem.innerHTML = `
                <i data-lucide="${iconName}"></i>
                <code>tools.${tool}: ${isEnabled}</code>
            `;
            modalToolsContainer.appendChild(toolItem);
        });

        // Setup Raw Link
        // Format path correctly
        const normalizedPath = agent.path.replace('./', '');
        modalRawBtn.href = `https://github.com/mouyox21/opencode-agents/blob/master/${normalizedPath}`;

        // Setup Code Text values
        codePromptText.textContent = agent.prompt;
        
        // Generate YAML
        const yamlFront = `---\ndescription: "${agent.description.replace(/"/g, '\\"')}"\nmode: ${agent.mode}\ntools:\n  write: ${agent.tools.write || false}\n  edit: ${agent.tools.edit || false}\n  bash: ${agent.tools.bash || false}\n---`;
        codeYamlText.textContent = yamlFront;

        // Generate JSON
        const jsonSchema = JSON.stringify({
            id: agent.id,
            name: agent.name,
            description: agent.description,
            mode: agent.mode,
            tools: agent.tools
        }, null, 2);
        codeJsonText.textContent = jsonSchema;

        // Re-initialize Lucide Icons for dynamic content
        lucide.createIcons();

        // Default tab selection reset to Prompt
        switchTab("prompt-tab");

        // Display Modal
        agentModal.style.display = "flex";
        document.body.style.overflow = "hidden"; // Disable background scrolling
    }

    function closeAgentModal() {
        agentModal.style.display = "none";
        document.body.style.overflow = ""; // Enable background scrolling
    }

    // Modal tab selector handler
    function switchTab(tabId) {
        tabButtons.forEach(btn => {
            if (btn.dataset.tab === tabId) {
                btn.classList.add("active");
            } else {
                btn.classList.remove("active");
            }
        });

        const tabContents = document.querySelectorAll(".tab-content");
        tabContents.forEach(tab => {
            if (tab.id === tabId) {
                tab.classList.add("active");
            } else {
                tab.classList.remove("active");
            }
        });
    }

    // Filter Logic core execution
    function applyFilters() {
        let filtered = AGENTS_DATA.filter(agent => {
            // 1. Search Query Filter
            if (currentFilters.search) {
                const searchLower = currentFilters.search.toLowerCase();
                const matchesName = agent.name.toLowerCase().includes(searchLower);
                const matchesDesc = (agent.description || "").toLowerCase().includes(searchLower);
                const matchesId = agent.id.toLowerCase().includes(searchLower);
                const matchesPrompt = (agent.prompt || "").toLowerCase().includes(searchLower);
                
                if (!matchesName && !matchesDesc && !matchesId && !matchesPrompt) {
                    return false;
                }
            }

            // 2. Category Filter
            if (currentFilters.category && agent.category !== currentFilters.category) {
                return false;
            }

            // 3. Tool Permissions Checkboxes
            if (currentFilters.tools.write && (!agent.tools || agent.tools.write !== true)) {
                return false;
            }
            if (currentFilters.tools.edit && (!agent.tools || agent.tools.edit !== true)) {
                return false;
            }
            if (currentFilters.tools.bash && (!agent.tools || agent.tools.bash !== true)) {
                return false;
            }

            return true;
        });

        // 4. Sort results
        if (currentFilters.sortBy === "name-asc") {
            filtered.sort((a, b) => a.name.localeCompare(b.name));
        } else if (currentFilters.sortBy === "name-desc") {
            filtered.sort((a, b) => b.name.localeCompare(a.name));
        } else if (currentFilters.sortBy === "category") {
            filtered.sort((a, b) => a.categoryName.localeCompare(b.categoryName) || a.name.localeCompare(b.name));
        }

        // Render Results
        renderGrid(filtered);
    }

    // Render Grid Elements
    function renderGrid(agentsList) {
        agentGrid.innerHTML = "";
        resultsCountBadge.textContent = agentsList.length;

        if (agentsList.length === 0) {
            emptyState.style.display = "flex";
            agentGrid.style.display = "none";
        } else {
            emptyState.style.display = "none";
            agentGrid.style.display = "grid";
            
            agentsList.forEach(agent => {
                const card = createAgentCard(agent);
                agentGrid.appendChild(card);
            });
        }

        // Apply Lucide icons for generated elements
        lucide.createIcons();
    }

    // Toast Notifications helper
    function showToast(message) {
        const toastContainer = document.getElementById("toast-container");
        const toast = document.createElement("div");
        toast.className = "toast";
        toast.innerHTML = `
            <i data-lucide="check-circle"></i>
            <span>${message}</span>
        `;
        toastContainer.appendChild(toast);
        lucide.createIcons();

        // Remove toast after animation
        setTimeout(() => {
            toast.style.animation = "fadeOut 0.3s forwards";
            setTimeout(() => {
                toast.remove();
            }, 300);
        }, 2500);
    }

    // Clipboard Copy Helper
    function handleCopy(text, buttonEl, successMsg) {
        navigator.clipboard.writeText(text).then(() => {
            buttonEl.classList.add("copied");
            const originalHTML = buttonEl.innerHTML;
            buttonEl.innerHTML = `<i data-lucide="check"></i> Copied!`;
            lucide.createIcons();
            
            showToast(successMsg);

            setTimeout(() => {
                buttonEl.classList.remove("copied");
                buttonEl.innerHTML = originalHTML;
                lucide.createIcons();
            }, 2000);
        }).catch(err => {
            console.error("Failed to copy to clipboard", err);
            showToast("Failed to copy content.");
        });
    }

    // Reset Filters action
    function resetFilters() {
        searchInput.value = "";
        clearSearchBtn.style.display = "none";
        toolWriteCheckbox.checked = false;
        toolEditCheckbox.checked = false;
        toolBashCheckbox.checked = false;
        sortSelect.value = "name-asc";
        
        currentFilters = {
            search: "",
            category: null,
            tools: {
                write: false,
                edit: false,
                bash: false
            },
            sortBy: "name-asc"
        };

        selectCategory(null);
    }

    // Event Listeners setup
    
    // Search inputs
    searchInput.addEventListener("input", (e) => {
        currentFilters.search = e.target.value.trim();
        if (e.target.value) {
            clearSearchBtn.style.display = "flex";
        } else {
            clearSearchBtn.style.display = "none";
        }
        applyFilters();
    });

    clearSearchBtn.addEventListener("click", () => {
        searchInput.value = "";
        clearSearchBtn.style.display = "none";
        currentFilters.search = "";
        applyFilters();
    });

    // Checkboxes
    toolWriteCheckbox.addEventListener("change", (e) => {
        currentFilters.tools.write = e.target.checked;
        applyFilters();
    });

    toolEditCheckbox.addEventListener("change", (e) => {
        currentFilters.tools.edit = e.target.checked;
        applyFilters();
    });

    toolBashCheckbox.addEventListener("change", (e) => {
        currentFilters.tools.bash = e.target.checked;
        applyFilters();
    });

    // Sort Selection
    sortSelect.addEventListener("change", (e) => {
        currentFilters.sortBy = e.target.value;
        applyFilters();
    });

    // Reset buttons
    resetFiltersBtn.addEventListener("click", resetFilters);
    emptyResetBtn.addEventListener("click", resetFilters);

    // Modal Close Actions
    modalCloseBtn.addEventListener("click", closeAgentModal);
    modalCloseFooterBtn.addEventListener("click", closeAgentModal);
    
    // Close modal by clicking outside overlay
    agentModal.addEventListener("click", (e) => {
        if (e.target === agentModal) {
            closeAgentModal();
        }
    });

    // Close modal on ESC key
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && agentModal.style.display === "flex") {
            closeAgentModal();
        }
    });

    // Tab buttons event attachment
    tabButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            switchTab(btn.dataset.tab);
        });
    });

    // Copy actions
    copyPromptBtn.addEventListener("click", () => {
        handleCopy(codePromptText.textContent, copyPromptBtn, "Agent prompt copied to clipboard!");
    });

    copyYamlBtn.addEventListener("click", () => {
        handleCopy(codeYamlText.textContent, copyYamlBtn, "YAML configuration copied to clipboard!");
    });

    copyJsonBtn.addEventListener("click", () => {
        handleCopy(codeJsonText.textContent, copyJsonBtn, "JSON configuration schema copied!");
    });

    // Initialize application layout elements
    initStats();
    renderCategoryFilters();
    applyFilters();
});
