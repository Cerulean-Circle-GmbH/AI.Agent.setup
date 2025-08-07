#!/usr/bin/env python3
"""
Research Agent - Python Implementation
Implements WODA methodology for structured research
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

class ResearchAgent:
    def __init__(self, research_dir: str = "research"):
        self.research_dir = Path(research_dir)
        self.research_dir.mkdir(exist_ok=True)
    
    def generate_topic_name(self, question: str) -> str:
        """Generate topic name from question (max 5 words)"""
        # Clean and split question into words
        words = re.sub(r'[^\w\s]', '', question.lower()).split()
        # Filter words longer than 2 characters and take first 5
        topic_words = [word for word in words if len(word) > 2][:5]
        return '-'.join(topic_words)
    
    def create_research_structure(self, topic_name: str, question: str) -> Path:
        """Create research folder structure with WODA files"""
        topic_dir = self.research_dir / topic_name
        topic_dir.mkdir(exist_ok=True)
        
        # Create main topic file
        topic_file = topic_dir / f"{topic_name}.md"
        topic_content = f"""# {topic_name.replace('-', ' ').title()}

**Question**: {question}

**Status**: Research in progress

**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        topic_file.write_text(topic_content)
        
        # Create research tasks file
        tasks_file = topic_dir / "research-tasks.md"
        tasks_content = self._generate_research_tasks(question)
        tasks_file.write_text(tasks_content)
        
        # Create WODA structure files
        wodafiles = {
            'what.md': self._create_what_file(question),
            'overview.md': self._create_overview_file(question),
            'details.md': self._create_details_file(question),
            'actions.md': self._create_actions_file(question)
        }
        
        for filename, content in wodafiles.items():
            (topic_dir / filename).write_text(content)
        
        return topic_dir
    
    def _generate_research_tasks(self, question: str) -> str:
        """Generate research task list"""
        return f"""# Research Tasks for: {question}

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
- Update progress regularly

**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    def _create_what_file(self, question: str) -> str:
        """Create What file for WODA methodology"""
        return f"""# What

## Topic Definition
**Research Question**: {question}

## Core Concepts
- [To be filled during research]

## Scope and Boundaries
- [To be defined]

## Key Questions
1. What is the main topic?
2. What are the essential components?
3. What are the primary use cases?

## Status: Research in Progress

**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    def _create_overview_file(self, question: str) -> str:
        """Create Overview file for WODA methodology"""
        return f"""# Overview

## What We Know
- [To be filled during research]

## What We Need to Research
- [To be identified]

## Current Understanding
- [To be developed]

## Knowledge Gaps
- [To be identified]

## Status: Research in Progress

**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    def _create_details_file(self, question: str) -> str:
        """Create Details file for WODA methodology"""
        return f"""# Details

## Research Findings
- [To be filled during research]

## Technical Details
- [To be documented]

## Implementation Considerations
- [To be analyzed]

## References and Sources
- [To be collected]

## Status: Research in Progress

**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    def _create_actions_file(self, question: str) -> str:
        """Create Actions file for WODA methodology"""
        return f"""# Actions

## Recommended Actions
- [To be derived from research]

## Implementation Steps
- [To be defined]

## Next Steps
- [To be planned]

## Priority Actions
- [To be identified]

## Status: Research in Progress

**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    def process_research_request(self, question: str) -> Dict:
        """Process a new research request"""
        topic_name = self.generate_topic_name(question)
        topic_dir = self.create_research_structure(topic_name, question)
        
        files = [f.name for f in topic_dir.iterdir() if f.is_file()]
        
        return {
            'topic_name': topic_name,
            'topic_dir': str(topic_dir),
            'question': question,
            'status': 'Research structure created',
            'files': files,
            'created_at': datetime.now().isoformat()
        }
    
    def get_research_status(self, topic_name: str) -> Dict:
        """Get status of a research topic"""
        topic_dir = self.research_dir / topic_name
        if not topic_dir.exists():
            return {'error': 'Research topic not found'}
        
        files = [f.name for f in topic_dir.iterdir() if f.is_file()]
        has_answer = 'answer.md' in files
        
        return {
            'topic_name': topic_name,
            'files': files,
            'has_answer': has_answer,
            'status': 'Completed' if has_answer else 'In Progress'
        }
    
    def update_research(self, topic_name: str, updates: Dict[str, str]) -> Dict:
        """Update research files with new content"""
        topic_dir = self.research_dir / topic_name
        if not topic_dir.exists():
            return {'error': 'Research topic not found'}
        
        for filename, content in updates.items():
            file_path = topic_dir / filename
            file_path.write_text(content)
        
        return {'status': 'Research updated successfully'}
    
    def create_answer(self, topic_name: str, answer: Dict) -> Dict:
        """Create final answer for research topic"""
        topic_dir = self.research_dir / topic_name
        answer_file = topic_dir / 'answer.md'
        
        answer_content = f"""# Answer

## Research Question
{answer.get('question', '')}

## Summary
{answer.get('summary', '')}

## Detailed Answer
{answer.get('details', '')}

## Actions
{answer.get('actions', '')}

## References
{answer.get('references', '')}

## Status: Completed

**Completed**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        answer_file.write_text(answer_content)
        
        # Update main topic file with answer link
        topic_file = topic_dir / f"{topic_name}.md"
        if topic_file.exists():
            content = topic_file.read_text()
            updated_content = content.replace(
                '**Status**: Research in progress',
                '**Status**: Completed\n\n**Answer**: [View Answer](./answer.md)'
            )
            topic_file.write_text(updated_content)
        
        return {'status': 'Answer created successfully'}
    
    def list_all_research(self) -> List[Dict]:
        """List all research topics"""
        topics = []
        for topic_dir in self.research_dir.iterdir():
            if topic_dir.is_dir():
                status = self.get_research_status(topic_dir.name)
                topics.append({
                    'topic': topic_dir.name,
                    'status': status.get('status', 'Unknown'),
                    'has_answer': status.get('has_answer', False)
                })
        return topics

def main():
    """Main function for testing the research agent"""
    agent = ResearchAgent()
    
    # Example usage
    question = "Can Cursor automate the creation of a backend agent like you?"
    print(f"🔍 Processing research request: {question}")
    
    result = agent.process_research_request(question)
    print(f"✅ Research created: {result['topic_name']}")
    print(f"📁 Files created: {', '.join(result['files'])}")
    
    # List all research
    all_research = agent.list_all_research()
    print(f"\n📋 All research topics: {len(all_research)}")
    for research in all_research:
        print(f"  - {research['topic']}: {research['status']}")

if __name__ == "__main__":
    main()
