# Content Pipeline Agent

An intelligent content creation pipeline built with CrewAI that automatically generates, evaluates, and iteratively improves content for blogs, tweets, and LinkedIn posts.

## Overview

This project uses AI agents to create high-quality content through a multi-stage pipeline:
1. **Research** - Gathers relevant information about the topic
2. **Content Generation** - Creates optimized content based on research
3. **Quality Assessment** - Evaluates content using specialized scoring systems
4. **Iterative Improvement** - Automatically refines content until it meets quality thresholds

## Features

- 🎯 **Multi-format Support**: Generate blog posts, tweets, and LinkedIn posts
- 🔍 **Automated Research**: Web search integration for topic research
- 📊 **Quality Scoring**: 
  - SEO scoring for blog posts (0-10 scale)
  - Virality scoring for social media content (0-10 scale)
- 🔄 **Iterative Refinement**: Automatically improves content until score ≥ 7
- 🤖 **AI-Powered**: Uses OpenAI's o4-mini model for content generation

## Architecture

The project uses CrewAI Flow to orchestrate a multi-agent workflow:

### Main Components

- **ContentPipelineFlow** (`main.py`): Main orchestration flow that manages the entire pipeline
- **SeoCrew** (`seo_crew.py`): Specialized crew for SEO evaluation of blog posts
- **ViralityCrew** (`virality_crew.py`): Specialized crew for virality assessment of social media content
- **Web Search Tool** (`tools.py`): Firecrawl API integration for web research

### Workflow

**For Blog Posts:**
```
Start → Research → Generate Blog → Check SEO → [Score ≥ 7?] → Finalize
                                          ↓ No
                                     Remake Blog
```

**For Tweets & LinkedIn Posts:**
```
Start → Research → Generate Content → Check Virality → [Score ≥ 7?] → Finalize
                                          ↓ No
                                     Remake Content
```

## Installation

### Prerequisites

- Python >= 3.13
- UV package manager (recommended) or pip

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd content-pipeline-agent
```

2. Install dependencies:
```bash
uv sync
# or
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```env
FIRECRAWL_API_KEY=your_api_key_here
FIRECRAWL_API_URL=your_api_url_here
```

## Usage

### Basic Example

```python
from main import ContentPipelineFlow

flow = ContentPipelineFlow()

result = flow.kickoff(
    inputs={
        "content_type": "blog",  # or "tweet" or "linkedin"
        "topic": "AI Dog Training",
    }
)
```

### Content Types

- **`"blog"`**: Generates SEO-optimized blog posts with title, subtitle, and sections
- **`"tweet"`**: Creates viral tweets with content and hashtags
- **`"linkedin"`**: Produces LinkedIn posts with hook, content, and call-to-action

### Output Format

The pipeline returns structured content based on the content type:

**Blog Post:**
```python
BlogPost(
    title: str,
    subtitle: str,
    sections: List[str]
)
```

**Tweet:**
```python
Tweet(
    content: str,
    hashtags: str
)
```

**LinkedIn Post:**
```python
LinkedInPost(
    hook: str,
    content: str,
    call_to_action: str
)
```

## Project Structure

```
content-pipeline-agent/
├── main.py              # Main flow orchestration
├── seo_crew.py          # SEO evaluation crew
├── virality_crew.py     # Virality assessment crew
├── tools.py             # Web search tool (Firecrawl)
├── pyproject.toml       # Project dependencies
└── README.md            # This file
```

## How It Works

### 1. Initialization
- Validates content type (`blog`, `tweet`, or `linkedin`)
- Sets maximum length constraints based on content type
- Validates topic input

### 2. Research Phase
- Uses a research agent with web search capabilities
- Gathers relevant information about the topic
- Stores research results for content generation

### 3. Content Generation
- Routes to appropriate content generator based on type
- Uses LLM (o4-mini) with structured output format
- Generates initial content or improves existing content

### 4. Quality Assessment
- **Blog posts**: Evaluated by SEO specialist for:
  - Keyword optimization
  - Title effectiveness
  - Content structure
  - Readability
  - Search intent alignment

- **Social media**: Evaluated by virality expert for:
  - Hook strength
  - Emotional resonance
  - Shareability
  - Call-to-action effectiveness
  - Platform-specific optimization

### 5. Iterative Improvement
- If score < 7, content is automatically regenerated with feedback
- Process repeats until score ≥ 7 or maximum iterations reached
- Final content is returned upon passing quality threshold

## Configuration

### Content Length Limits
- Tweets: 150 characters
- Blog posts: 800 words
- LinkedIn posts: 500 words

### Quality Threshold
- Minimum score: 7/10
- Content below threshold is automatically improved

## Dependencies

- `crewai[tools]>=0.152.0` - AI agent framework
- `firecrawl-py==2.16.3` - Web scraping and search
- `python-dotenv>=1.1.1` - Environment variable management
- `pydantic` - Data validation (via CrewAI)

## Development

### Running the Pipeline

```bash
python main.py
```

### Visualizing the Flow

Uncomment the `flow.plot()` line in `main.py` to visualize the workflow graph.

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

