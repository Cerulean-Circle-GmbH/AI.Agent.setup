# Research Agent Setup

A Cursor-integrated research agent that implements the WODA methodology (What, Overview, Details, Actions) for structured research projects.

## Overview

This research agent automatically creates organized research structures for any question, following a systematic approach to information gathering and analysis.

## Features

- **WODA Methodology**: Structured research following What, Overview, Details, Actions framework
- **Automatic File Generation**: Creates organized folder structures for each research topic
- **Task Management**: Generates comprehensive research task lists
- **Progress Tracking**: Maintains status updates throughout the research process
- **Answer Synthesis**: Creates comprehensive final answers with structured documentation
- **ONCE Kernel Documentation**: Comprehensive documentation of the incredibly small interoperating system that boots everything
- **Cross-Reference Agent**: Automatic cross-referencing and backlinking between related documents

## Project Structure

```
AI.Agent.setup/
├── src/
│   └── index.js              # Main research agent server
├── research/                 # Generated research folders
├── package.json              # Node.js dependencies
├── .cursorrules             # Cursor IDE integration rules
├── README.md               # This file
└── research.agent.md       # Original agent specification
```

## Installation

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Start the Research Agent**:
   ```bash
   npm start
   ```

3. **Development Mode**:
   ```bash
   npm run dev
   ```

## API Endpoints

### Create New Research
```bash
POST /research
Content-Type: application/json

{
  "question": "Your research question here"
}
```

### Get Research Status
```bash
GET /research/:topicName
```

### Update Research
```bash
PUT /research/:topicName
Content-Type: application/json

{
  "updates": {
    "what.md": "Updated content...",
    "overview.md": "Updated content..."
  }
}
```

### Create Final Answer
```bash
POST /research/:topicName/answer
Content-Type: application/json

{
  "answer": {
    "question": "Original question",
    "summary": "Brief summary",
    "details": "Detailed answer",
    "actions": "Recommended actions",
    "references": "Sources and references"
  }
}
```

### List All Research
```bash
GET /research
```

### Health Check
```bash
GET /health
```

## WODA Methodology

### What
- Define the topic and scope
- Identify core concepts
- Establish boundaries

### Overview
- Document current knowledge
- Identify research gaps
- Plan investigation approach

### Details
- Collect research findings
- Document technical details
- Gather references and sources

### Actions
- Derive actionable insights
- Create implementation steps
- Plan next actions

## Research File Structure

For each research topic, the agent creates:

```
research/
└── topic-name/
    ├── topic-name.md          # Main topic file with question
    ├── research-tasks.md      # Comprehensive task list
    ├── what.md               # WODA: What
    ├── overview.md           # WODA: Overview  
    ├── details.md            # WODA: Details
    ├── actions.md            # WODA: Actions
    └── answer.md             # Final comprehensive answer
```

## Cursor Integration

The `.cursorrules` file configures Cursor IDE to:
- Recognize research questions
- Automatically create research structures
- Follow WODA methodology
- Maintain organized documentation

## Usage Example

1. **Ask a Research Question**:
   ```
   "Can Cursor automate backend agent creation?"
   ```

2. **Agent Creates Structure**:
   - Generates topic name: `cursor-automate-backend-agent-creation`
   - Creates research folder with WODA files
   - Generates research task list

3. **Research Process**:
   - Fill in WODA framework files
   - Collect information and references
   - Update progress regularly

4. **Final Answer**:
   - Synthesize findings into answer.md
   - Update main topic file with links
   - Mark research as completed

## Development

### Adding New Features
- Extend the `ResearchAgent` class in `src/index.js`
- Add new API endpoints as needed
- Update `.cursorrules` for new behaviors

### Testing
```bash
npm test
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Follow the WODA methodology
2. Maintain clear documentation
3. Test thoroughly before submitting
4. Update README for new features

### Handover & Recovery (The Dory Problem)

Roles: User = TRON (QA; Mission Commander), Assistant = Scrum Master (Cursor; Facilitator/Implementer)

Trigger phrase: “recover from readme.md”

When invoked, perform these steps in order to fully restore working context and proceed safely:

- Identity-first gates
  - Apply the checklist from `IDENTITY_INTEGRATION_GUIDE.md` to all actions (Foundation First, User Sovereignty, Permanence, Privacy, Universal Access, Biblical Alignment).

- Repository and branch
  - Ensure branch is `dev/tron-gpt5` (current GPT-5 iteration) or `dev/tron` (baseline), and submodules are initialized and up to date.
  - Commands:
    ```bash
    git checkout dev/tron-gpt5 || git checkout dev/tron || true
    git submodule update --init --recursive --progress
    ```

- Read core context (this file first)
  - `README.md` (this file) and `PROJECT_SUMMARY.md`
  - TRON governance: `TRON_ACCOUNTABILITY_LOG.md`, `MISSION_CRITICAL_PROJECT_MANAGEMENT.md`
  - Identity anchor: `IDENTITY_INTEGRATION_GUIDE.md`, `research/web4x-identity-foundation.md`

- GROK learning context (for teaching method and memory constraints)
  - `research/grok-learning-context.md`
  - `research/grok-teaching-research-analysis.md`
  - `research/content-sharing-framework.md`

- Web4x canonical references (submodules)
  - Wiki pages in `research/web4x-codingWeb4-wiki/`:
    - `Web-4.x-Home.md`, `Why-4.0.md`, `Web-4.x-Ecosystem.md`, `Web-4.x-Curriculum.md`

- Project management cadence (Scrum/PMO)
  - `research/web4articles/README.md` (Plain Simple Scrum, “less scrum flavor”)
  - `research/web4articles/wiki/Ontology.md` (SCRUM/PMO term definitions)
  - `research/web4articles/scrum.pmo/roles/*/process.md` (role duties)
  - `research/web4articles/scrum.pmo/sprints/sprint-0/planning.md` (initial plan)

- TRACE ON discipline (TRON oversight)
  - For each major decision, record TRON source, context, implementation, verification, and accountability. Append to `TRON_ACCOUNTABILITY_LOG.md` as needed.

- WODA pipeline
  - For any new question, generate a research topic (API via `src/index.js` or Python via `research_agent.py`), then fill What/Overview/Details/Actions and synthesize `answer.md`.

- Cross-linking
  - Generate or refresh cross-links and reports:
    ```bash
    python3 crosslink_agent.py --research-dir research --report
    ```

- Health check / API (optional)
  - Start the API server for endpoints `/health`, `/research`:
    ```bash
    npm install
    npm start
    ```

- Recovery summary (optional but recommended)
  - Create or append `recovery.md` with: timestamp, branch, submodule status, docs read, pending actions, risks, and next steps.

Execution rule: Non-destructive steps may be executed autonomously. Any destructive action (delete/move) requires explicit TRON confirmation. Always verify outcomes and document results.

## Related Files

- **[Research Agent Project Summary](PROJECT_SUMMARY.md)**
- **[Research Agent Setup](SETUP.md)**
- **[Research Agent Definition](research.agent.md)**
- **[Actions](research/can-cursor-automate-the-creation/actions.md)**
- **[Can Cursor Automate The Creation](research/can-cursor-automate-the-creation/can-cursor-automate-the-creation.md)**
- **[Details](research/can-cursor-automate-the-creation/details.md)**
- **[Overview](research/can-cursor-automate-the-creation/overview.md)**
- **[Research Tasks for: Can Cursor automate the creation of a backend agent like you?](research/can-cursor-automate-the-creation/research-tasks.md)**
- **[What](research/can-cursor-automate-the-creation/what.md)**
- **[Cursor Background Agents Research](research/cursor-background-agents/0_topic.md)**
- **[What: Cursor Background Agents](research/cursor-background-agents/1_what.md)**
- **[Cursor Background Agents: Comprehensive Analysis](research/cursor-background-agents/2_answer.md)**
- **[Access & Control: Cursor Background Agents](research/cursor-background-agents/access-control.md)**
- **[Actions: Cursor Background Agents Implementation Guide](research/cursor-background-agents/actions.md)**
- **[Implementation Guide: Cursor Background Agents](research/cursor-background-agents/implementation-guide.md)**
- **[Operational Considerations: Cursor Background Agents](research/cursor-background-agents/operational-considerations.md)**
- **[Overview: Cursor Background Agents Research Hub](research/cursor-background-agents/overview.md)**
- **[Research Tasks: Cursor Background Agents](research/cursor-background-agents/research-tasks.md)**
- **[Security & Privacy: Cursor Background Agents](research/cursor-background-agents/security-privacy.md)**
- **[Technical Architecture: Cursor Background Agents](research/cursor-background-agents/technical-architecture.md)**
