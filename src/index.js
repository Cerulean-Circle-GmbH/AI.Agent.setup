const express = require('express');
const cors = require('cors');
const fs = require('fs-extra');
const path = require('path');
const { marked } = require('marked');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Research Agent Class implementing WODA methodology
class ResearchAgent {
  constructor() {
    this.researchDir = path.join(__dirname, '../research');
    this.ensureResearchDir();
  }

  ensureResearchDir() {
    fs.ensureDirSync(this.researchDir);
  }

  // Generate topic name from question (max 5 words)
  generateTopicName(question) {
    const words = question.toLowerCase()
      .replace(/[^\w\s]/g, '')
      .split(' ')
      .filter(word => word.length > 2)
      .slice(0, 5);
    return words.join('-');
  }

  // Create research folder structure
  async createResearchStructure(topicName, question) {
    const topicDir = path.join(this.researchDir, topicName);
    await fs.ensureDir(topicDir);

    // Create main topic file
    const topicFile = path.join(topicDir, `${topicName}.md`);
    await fs.writeFile(topicFile, `# ${topicName}\n\n**Question**: ${question}\n\n**Status**: Research in progress`);

    // Create research tasks file
    const tasksFile = path.join(topicDir, 'research-tasks.md');
    const tasks = this.generateResearchTasks(question);
    await fs.writeFile(tasksFile, tasks);

    // Create WODA structure files
    const wodafiles = {
      'what.md': this.createWhatFile(question),
      'overview.md': this.createOverviewFile(question),
      'details.md': this.createDetailsFile(question),
      'actions.md': this.createActionsFile(question)
    };

    for (const [filename, content] of Object.entries(wodafiles)) {
      await fs.writeFile(path.join(topicDir, filename), content);
    }

    return topicDir;
  }

  generateResearchTasks(question) {
    return `# Research Tasks for: ${question}

## Task List

### Phase 1: Understanding
- [ ] Define the core concepts and terminology
- [ ] Identify key stakeholders and use cases
- [ ] Map out the problem space

### Phase 2: Investigation
- [ ] Research current solutions and approaches
- [ ] Analyze technical requirements and constraints
- [ ] Identify relevant tools and technologies

### Phase 3: Analysis
- [ ] Evaluate findings against WODA framework
- [ ] Synthesize information into actionable insights
- [ ] Identify gaps and areas for further research

### Phase 4: Documentation
- [ ] Create comprehensive answer document
- [ ] Structure findings according to WODA principles
- [ ] Update question with structured links

## Notes
- Follow WODA methodology: What, Overview, Details, Actions
- Collect relevant images, documents, and references
- Maintain clear documentation structure
- Update progress regularly`;
  }

  createWhatFile(question) {
    return `# What

## Topic Definition
**Research Question**: ${question}

## Core Concepts
- [To be filled during research]

## Scope and Boundaries
- [To be defined]

## Key Questions
1. What is the main topic?
2. What are the essential components?
3. What are the primary use cases?

## Status: Research in Progress`;
  }

  createOverviewFile(question) {
    return `# Overview

## What We Know
- [To be filled during research]

## What We Need to Research
- [To be identified]

## Current Understanding
- [To be developed]

## Knowledge Gaps
- [To be identified]

## Status: Research in Progress`;
  }

  createDetailsFile(question) {
    return `# Details

## Research Findings
- [To be filled during research]

## Technical Details
- [To be documented]

## Implementation Considerations
- [To be analyzed]

## References and Sources
- [To be collected]

## Status: Research in Progress`;
  }

  createActionsFile(question) {
    return `# Actions

## Recommended Actions
- [To be derived from research]

## Implementation Steps
- [To be defined]

## Next Steps
- [To be planned]

## Priority Actions
- [To be identified]

## Status: Research in Progress`;
  }

  // Process research request
  async processResearchRequest(question) {
    const topicName = this.generateTopicName(question);
    const topicDir = await this.createResearchStructure(topicName, question);
    
    return {
      topicName,
      topicDir,
      question,
      status: 'Research structure created',
      files: await this.listResearchFiles(topicDir)
    };
  }

  async listResearchFiles(topicDir) {
    const files = await fs.readdir(topicDir);
    return files.map(file => ({
      name: file,
      path: path.join(topicDir, file)
    }));
  }

  // Get research status
  async getResearchStatus(topicName) {
    const topicDir = path.join(this.researchDir, topicName);
    if (!await fs.pathExists(topicDir)) {
      return { error: 'Research topic not found' };
    }

    const files = await this.listResearchFiles(topicDir);
    const answerFile = files.find(f => f.name === 'answer.md');
    
    return {
      topicName,
      files,
      hasAnswer: !!answerFile,
      status: answerFile ? 'Completed' : 'In Progress'
    };
  }

  // Update research with findings
  async updateResearch(topicName, updates) {
    const topicDir = path.join(this.researchDir, topicName);
    if (!await fs.pathExists(topicDir)) {
      return { error: 'Research topic not found' };
    }

    for (const [filename, content] of Object.entries(updates)) {
      const filePath = path.join(topicDir, filename);
      await fs.writeFile(filePath, content);
    }

    return { status: 'Research updated successfully' };
  }

  // Create final answer
  async createAnswer(topicName, answer) {
    const topicDir = path.join(this.researchDir, topicName);
    const answerFile = path.join(topicDir, 'answer.md');
    
    const answerContent = `# Answer

## Research Question
${answer.question}

## Summary
${answer.summary}

## Detailed Answer
${answer.details}

## Actions
${answer.actions}

## References
${answer.references}

## Status: Completed`;
    
    await fs.writeFile(answerFile, answerContent);
    
    // Update main topic file with answer link
    const topicFile = path.join(topicDir, `${topicName}.md`);
    const topicContent = await fs.readFile(topicFile, 'utf8');
    const updatedContent = topicContent.replace(
      '**Status**: Research in progress',
      '**Status**: Completed\n\n**Answer**: [View Answer](./answer.md)'
    );
    await fs.writeFile(topicFile, updatedContent);

    return { status: 'Answer created successfully' };
  }
}

const researchAgent = new ResearchAgent();

// API Routes
app.post('/research', async (req, res) => {
  try {
    const { question } = req.body;
    if (!question) {
      return res.status(400).json({ error: 'Question is required' });
    }

    const result = await researchAgent.processResearchRequest(question);
    res.json(result);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.get('/research/:topicName', async (req, res) => {
  try {
    const { topicName } = req.params;
    const status = await researchAgent.getResearchStatus(topicName);
    res.json(status);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.put('/research/:topicName', async (req, res) => {
  try {
    const { topicName } = req.params;
    const { updates } = req.body;
    const result = await researchAgent.updateResearch(topicName, updates);
    res.json(result);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/research/:topicName/answer', async (req, res) => {
  try {
    const { topicName } = req.params;
    const { answer } = req.body;
    const result = await researchAgent.createAnswer(topicName, answer);
    res.json(result);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.get('/research', async (req, res) => {
  try {
    const researchDir = path.join(__dirname, '../research');
    const topics = await fs.readdir(researchDir);
    const researchList = await Promise.all(
      topics.map(async (topic) => {
        const status = await researchAgent.getResearchStatus(topic);
        return {
          topic,
          status: status.status,
          hasAnswer: status.hasAnswer
        };
      })
    );
    res.json(researchList);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'Research Agent is running', timestamp: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`Research Agent running on port ${PORT}`);
  console.log(`Health check: http://localhost:${PORT}/health`);
});
