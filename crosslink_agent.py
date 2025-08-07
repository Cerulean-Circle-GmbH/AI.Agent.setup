#!/usr/bin/env python3
"""
Cross-Linking Agent for Markdown Files
=====================================

Automatically generates cross-references and backlinks for markdown files
in research directories following WODA methodology.

Features:
- Automatic topic detection and cross-referencing
- Backlink generation between related files
- WODA structure linking
- Topic navigation enhancement
- Bi-directional relationship mapping
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class MarkdownFile:
    """Represents a markdown file with metadata."""
    path: Path
    title: str
    content: str
    headers: List[str]
    links: List[str]
    topics: Set[str]
    woda_type: str = None  # what, overview, details, actions, answer
    
class CrossLinkAgent:
    """Agent for automatic cross-linking of markdown files."""
    
    def __init__(self, research_dir: str = "research"):
        self.research_dir = Path(research_dir)
        self.files: Dict[str, MarkdownFile] = {}
        self.topic_map: Dict[str, Set[str]] = defaultdict(set)
        self.backlinks: Dict[str, Set[str]] = defaultdict(set)
        self.woda_structure = ["what", "overview", "details", "actions", "answer"]
        
    def scan_markdown_files(self) -> None:
        """Scan all markdown files in research directory."""
        print(f"🔍 Scanning markdown files in {self.research_dir}")
        
        for md_file in self.research_dir.rglob("*.md"):
            if md_file.is_file():
                self.process_file(md_file)
                
        print(f"📄 Found {len(self.files)} markdown files")
    
    def process_file(self, file_path: Path) -> None:
        """Process a single markdown file and extract metadata."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title (first header or filename)
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file_path.stem
            
            # Extract headers
            headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
            
            # Extract existing links
            links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
            
            # Extract topics/keywords
            topics = self.extract_topics(content, title)
            
            # Detect WODA type
            woda_type = self.detect_woda_type(file_path, content)
            
            md_file = MarkdownFile(
                path=file_path,
                title=title,
                content=content,
                headers=headers,
                links=links,
                topics=topics,
                woda_type=woda_type
            )
            
            relative_path = str(file_path.relative_to(self.research_dir))
            self.files[relative_path] = md_file
            
            # Build topic map
            for topic in topics:
                self.topic_map[topic.lower()].add(relative_path)
                
        except Exception as e:
            print(f"⚠️  Error processing {file_path}: {e}")
    
    def extract_topics(self, content: str, title: str) -> Set[str]:
        """Extract topics and keywords from content."""
        topics = set()
        
        # Add title words
        title_words = re.findall(r'\b[A-Z][a-z]+\b', title)
        topics.update(title_words)
        
        # Extract from headers
        headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
        for header in headers:
            header_words = re.findall(r'\b[A-Z][a-z]+\b', header)
            topics.update(header_words)
        
        # Extract capitalized terms (likely important concepts)
        concept_words = re.findall(r'\b[A-Z][a-z]{3,}\b', content)
        topics.update(concept_words)
        
        # Extract code/technical terms
        tech_terms = re.findall(r'`([^`]+)`', content)
        topics.update([term for term in tech_terms if len(term) > 2])
        
        # Filter out common words
        common_words = {'The', 'This', 'That', 'When', 'Where', 'What', 'How', 'Why', 'Research', 'File', 'Document'}
        topics = {t for t in topics if t not in common_words and len(t) > 2}
        
        return topics
    
    def detect_woda_type(self, file_path: Path, content: str) -> str:
        """Detect WODA methodology type from filename or content."""
        filename = file_path.stem.lower()
        
        # Direct filename matches
        for woda_type in self.woda_structure:
            if woda_type in filename:
                return woda_type
        
        # Pattern matches
        if 'overview' in filename or 'research-tasks' in filename:
            return 'overview'
        elif re.search(r'\d+_topic\.md$', str(file_path)):
            return 'what'
        elif 'answer' in filename:
            return 'answer'
        elif 'action' in filename:
            return 'actions'
        elif 'detail' in filename:
            return 'details'
            
        return None
    
    def generate_cross_references(self) -> None:
        """Generate cross-references between related files."""
        print("🔗 Generating cross-references...")
        
        for file_path, md_file in self.files.items():
            related_files = self.find_related_files(file_path, md_file)
            
            for related_path, relationship_type in related_files:
                self.backlinks[related_path].add(file_path)
    
    def find_related_files(self, file_path: str, md_file: MarkdownFile) -> List[Tuple[str, str]]:
        """Find files related to the current file."""
        related = []
        current_dir = str(Path(file_path).parent)
        
        # Find files in same research topic directory
        for other_path, other_file in self.files.items():
            if other_path == file_path:
                continue
                
            other_dir = str(Path(other_path).parent)
            
            # Same research topic
            if current_dir == other_dir:
                related.append((other_path, "same_topic"))
            
            # Topic overlap
            topic_overlap = md_file.topics.intersection(other_file.topics)
            if len(topic_overlap) >= 2:  # Significant overlap
                related.append((other_path, "topic_overlap"))
        
        return related
    
    def generate_navigation_section(self, file_path: str, md_file: MarkdownFile) -> str:
        """Generate navigation section for a file."""
        current_dir = Path(file_path).parent
        navigation_lines = []
        
        # Back navigation to parent topic
        topic_file = current_dir / "0_topic.md"
        overview_file = current_dir / "overview.md"
        
        back_links = []
        if topic_file.exists() and str(topic_file.relative_to(self.research_dir)) in self.files:
            back_links.append("[Topic](./0_topic.md)")
        if overview_file.exists() and str(overview_file.relative_to(self.research_dir)) in self.files:
            back_links.append("[Overview](./overview.md)")
        
        if back_links:
            navigation_lines.append(f"**🔙 Back to**: {' | '.join(back_links)}")
            navigation_lines.append("")
        
        return "\n".join(navigation_lines)
    
    def generate_related_section(self, file_path: str) -> str:
        """Generate related files section."""
        if file_path not in self.backlinks or not self.backlinks[file_path]:
            return ""
        
        lines = ["## Related Files", ""]
        
        for related_path in sorted(self.backlinks[file_path]):
            related_file = self.files[related_path]
            rel_path = os.path.relpath(related_file.path, Path(file_path).parent)
            lines.append(f"- **[{related_file.title}]({rel_path})**")
        
        lines.append("")
        return "\n".join(lines)
    
    def generate_backlinks_section(self, file_path: str) -> str:
        """Generate backlinks section showing files that reference this one."""
        backlink_files = []
        
        for other_path, other_file in self.files.items():
            if other_path == file_path:
                continue
            
            # Check if other file links to this one
            for link_text, link_url in other_file.links:
                if self.normalize_link_path(link_url, other_path) == file_path:
                    backlink_files.append((other_path, other_file, link_text))
        
        if not backlink_files:
            return ""
        
        lines = ["## Referenced By", ""]
        
        for ref_path, ref_file, link_text in backlink_files:
            rel_path = os.path.relpath(ref_file.path, Path(file_path).parent)
            lines.append(f"- **[{ref_file.title}]({rel_path})** - {link_text}")
        
        lines.append("")
        return "\n".join(lines)
    
    def normalize_link_path(self, link_url: str, from_file: str) -> str:
        """Normalize a link URL to a file path relative to research directory."""
        if link_url.startswith('http'):
            return None
        
        # Remove anchors
        link_url = link_url.split('#')[0]
        
        if link_url.startswith('./'):
            # Relative to current directory
            current_dir = Path(from_file).parent
            target_path = (current_dir / link_url[2:]).resolve()
        elif link_url.startswith('../'):
            # Relative to parent directory
            current_dir = Path(from_file).parent
            target_path = (current_dir / link_url).resolve()
        else:
            # Assume relative to current directory
            current_dir = Path(from_file).parent
            target_path = (current_dir / link_url).resolve()
        
        try:
            return str(target_path.relative_to(self.research_dir.resolve()))
        except ValueError:
            return None
    
    def update_file_with_crosslinks(self, file_path: str, md_file: MarkdownFile) -> str:
        """Update file content with cross-links and navigation."""
        content = md_file.content
        
        # Check if file already has navigation
        if "**🔙 Back to**" in content:
            # Update existing navigation
            lines = content.split('\n')
            new_lines = []
            skip_old_nav = False
            
            for line in lines:
                if line.startswith("**🔙 Back to**"):
                    # Replace old navigation
                    nav_section = self.generate_navigation_section(file_path, md_file)
                    if nav_section:
                        new_lines.extend(nav_section.split('\n'))
                    skip_old_nav = True
                elif skip_old_nav and line.strip() == "":
                    skip_old_nav = False
                    if new_lines and new_lines[-1] != "":
                        new_lines.append("")
                elif not skip_old_nav:
                    new_lines.append(line)
            
            content = '\n'.join(new_lines)
        else:
            # Add navigation at the top
            nav_section = self.generate_navigation_section(file_path, md_file)
            if nav_section:
                content = nav_section + content
        
        # Add related files section before end
        related_section = self.generate_related_section(file_path)
        backlinks_section = self.generate_backlinks_section(file_path)
        
        if related_section or backlinks_section:
            # Add sections before any existing footer
            if "---" in content:
                parts = content.rsplit("---", 1)
                if len(parts) == 2:
                    content = parts[0] + related_section + backlinks_section + "---" + parts[1]
                else:
                    content = content + "\n" + related_section + backlinks_section
            else:
                content = content + "\n" + related_section + backlinks_section
        
        return content
    
    def apply_crosslinks(self, dry_run: bool = False) -> None:
        """Apply cross-links to all files."""
        print(f"✍️  {'Previewing' if dry_run else 'Applying'} cross-links...")
        
        for file_path, md_file in self.files.items():
            updated_content = self.update_file_with_crosslinks(file_path, md_file)
            
            if updated_content != md_file.content:
                if dry_run:
                    print(f"📝 Would update: {file_path}")
                else:
                    try:
                        with open(md_file.path, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        print(f"✅ Updated: {file_path}")
                    except Exception as e:
                        print(f"❌ Error updating {file_path}: {e}")
            else:
                if not dry_run:
                    print(f"⏭️  No changes needed: {file_path}")
    
    def generate_report(self) -> str:
        """Generate a cross-linking report."""
        report = ["# Cross-Linking Report", ""]
        
        report.append(f"## Summary")
        report.append(f"- **Files processed**: {len(self.files)}")
        report.append(f"- **Topics identified**: {len(self.topic_map)}")
        report.append(f"- **Cross-references**: {sum(len(refs) for refs in self.backlinks.values())}")
        report.append("")
        
        # Topic distribution
        report.append("## Topic Distribution")
        for topic, files in sorted(self.topic_map.items()):
            if len(files) > 1:  # Only show topics with multiple files
                report.append(f"- **{topic}**: {len(files)} files")
        report.append("")
        
        # WODA structure analysis
        report.append("## WODA Structure")
        woda_count = defaultdict(int)
        for md_file in self.files.values():
            if md_file.woda_type:
                woda_count[md_file.woda_type] += 1
        
        for woda_type in self.woda_structure:
            count = woda_count.get(woda_type, 0)
            report.append(f"- **{woda_type.title()}**: {count} files")
        report.append("")
        
        return "\n".join(report)
    
    def run(self, dry_run: bool = False, generate_report: bool = False) -> None:
        """Run the complete cross-linking process."""
        print("🚀 Starting Cross-Link Agent")
        
        # Step 1: Scan files
        self.scan_markdown_files()
        
        # Step 2: Generate cross-references
        self.generate_cross_references()
        
        # Step 3: Apply changes
        self.apply_crosslinks(dry_run=dry_run)
        
        # Step 4: Generate report if requested
        if generate_report:
            report = self.generate_report()
            report_path = self.research_dir / "crosslink_report.md"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"📊 Report generated: {report_path}")
        
        print("✅ Cross-linking complete!")

def main():
    parser = argparse.ArgumentParser(description="Cross-Linking Agent for Markdown Files")
    parser.add_argument("--research-dir", default="research", help="Research directory path")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--report", action="store_true", help="Generate cross-linking report")
    parser.add_argument("--file", help="Process single file (for new file integration)")
    
    args = parser.parse_args()
    
    agent = CrossLinkAgent(args.research_dir)
    
    if args.file:
        # Process single file (for automation integration)
        file_path = Path(args.file)
        if file_path.exists() and file_path.suffix == '.md':
            agent.scan_markdown_files()  # Scan all files for context
            agent.generate_cross_references()
            
            # Update just the target file
            rel_path = str(file_path.relative_to(agent.research_dir))
            if rel_path in agent.files:
                md_file = agent.files[rel_path]
                updated_content = agent.update_file_with_crosslinks(rel_path, md_file)
                
                if updated_content != md_file.content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"✅ Updated cross-links for: {file_path}")
                else:
                    print(f"⏭️  No cross-link updates needed for: {file_path}")
    else:
        # Process all files
        agent.run(dry_run=args.dry_run, generate_report=args.report)

if __name__ == "__main__":
    main()