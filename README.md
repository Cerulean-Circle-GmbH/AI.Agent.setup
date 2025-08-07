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

## Related Files

- **[Research Agent Project Summary](PROJECT_SUMMARY.md)**
- **[Research Agent Setup Guide](SETUP.md)**
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
