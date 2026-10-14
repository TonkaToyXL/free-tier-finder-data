# Free Tier Finder data

Verified free tiers, promos and startup credits for AI and developer tools. This is the source data for [freetierfinder.com](https://freetierfinder.com).

![Last checked](https://img.shields.io/badge/last%20checked-2026--10--14-blue) ![Tools](https://img.shields.io/badge/tools-135-informational) ![Promos](https://img.shields.io/badge/promos-23-informational) ![License: CC BY 4.0](https://img.shields.io/badge/data%20license-CC%20BY%204.0-lightgrey)

- Site: https://freetierfinder.com
- Machine-readable summary: https://freetierfinder.com/llms.txt

## Files

| File | Contents |
| --- | --- |
| `data/tools.json`, `data/tools.csv` | 135 tools with active free tiers |
| `data/promos.json`, `data/promos.csv` | 23 promos, credits and startup programs |
| `data/dropped.json` | Entries removed after their free tier ended or could not be confirmed |
| `scripts/export.py` | Regenerates the data files, this README and the changelog |

### Fields

| Field | Meaning |
| --- | --- |
| `name` | Tool or offer name |
| `category` | Tool category, or offer type for promos |
| `what_you_get` | What the free tier or offer includes |
| `how_to_get_it` | How to claim it |
| `requirements` | Eligibility or account requirements |
| `catch` | Main limitation |
| `no_card_status` | Whether a payment card is required, as stated by the vendor |
| `official_source_url` | Vendor page the facts were taken from |
| `date_checked` | Date the facts were last checked (YYYY-MM-DD) |
| `page_url` | Entry page on freetierfinder.com |

## Methodology

- Every entry is verified on the vendor's official pricing, documentation or announcement page. Third-party sources are not used.
- Each entry records the source URL and the date it was checked.
- Where the vendor does not state a fact (for example, whether a card is required), the field says so instead of guessing.
- Entries are removed when the free tier or offer is no longer active. Removed entries are listed in `data/dropped.json`.
- Source URLs are official vendor URLs only. No affiliate or referral links are included.

## Tools by category

### AI Agents

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Aider](https://freetierfinder.com/tool/aider) | Terminal coding agent that maps your codebase, auto-commits to git, and works with cloud or local LLMs. | Not stated on pricing page | 2026-10-14 |
| [Botpress](https://freetierfinder.com/tool/botpress) | 3 AI agents, 3 seats, 100 conversations, Help Center, community support. | Not stated on pricing page | 2026-10-14 |
| [Cline](https://freetierfinder.com/tool/cline) | The open-source Cline VS Code extension and CLI, MCP Marketplace, community support. | Not stated on pricing page | 2026-10-14 |
| [CrewAI](https://freetierfinder.com/tool/crewai) | Studio visual editor and AI copilot, GitHub integration, templates, export as MCP server, 50 workflow executions a month. | Not stated on pricing page | 2026-10-14 |
| [Cursor](https://freetierfinder.com/tool/cursor) | Cursor Agent with limited AI usage, limited agent requests and limited chat requests. | Not stated on pricing page | 2026-10-14 |
| [Dify](https://freetierfinder.com/tool/dify) | 200 message credits to try models from OpenAI, Anthropic, Gemini, xAI and Tongyi, then switch to your own API key; 5 apps. | Not stated on pricing page | 2026-10-14 |
| [Flowise](https://freetierfinder.com/tool/flowise) | 2 flows and assistants, 100 predictions a month, 5MB storage, evaluations and metrics, embedded chatbot. | Not stated on pricing page | 2026-10-14 |
| [Hark](https://freetierfinder.com/tool/hark) | All Hark Pro features, no ads; the free usage amount is not published. | Not stated on pricing page | 2026-10-14 |
| [Kilo Code](https://freetierfinder.com/tool/kilo-code) | Open-source agentic coding assistant and code completion; works with any AI model. | Not stated on pricing page | 2026-10-14 |
| [Langflow](https://freetierfinder.com/tool/langflow) | Drag-and-drop agent and flow builder with Python under the hood; deploy flows as APIs. | Not stated on pricing page | 2026-10-14 |
| [OpenHands](https://freetierfinder.com/tool/openhands) | Local open-source OpenHands agent (web GUI, terminal UI, CLI), plus free hosted cloud access with API, Jira and Slack integrations. | Not stated on pricing page | 2026-10-14 |
| [Rival.io](https://freetierfinder.com/tool/rival-io) | A $0 Personal Workspace with unlimited DeepSeek 4 Flash (one concurrent connection) and a $1 one-time run balance. | No (stated on pricing page) | 2026-10-14 |
| [Roomote](https://freetierfinder.com/tool/roomote) | The same Roomote app as Cloud, self-hosted, all features, no license needed under 10 users. | Not stated on pricing page | 2026-10-14 |

### AI APIs

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Cloudflare Workers AI](https://freetierfinder.com/tool/cloudflare-workers-ai) | 10,000 Neurons per day at no charge. | Not stated on pricing page | 2026-10-14 |
| [Cohere](https://freetierfinder.com/tool/cohere) | Free API calls with a Trial API key. | Not stated on pricing page | 2026-10-14 |
| [Google AI Studio](https://freetierfinder.com/tool/google-ai-studio) | Free input and output tokens for some Gemini models plus Google AI Studio access. | Not stated on pricing page | 2026-10-14 |
| [Groq](https://freetierfinder.com/tool/groq) | Free API plan with per-model rate limits (for example 10 requests a minute, 100 a day on some models). | Not stated on pricing page | 2026-10-14 |
| [Hugging Face](https://freetierfinder.com/tool/hugging-face) | Hub hosting and Spaces on free CPU Basic (2 vCPU, 16 GB) and ZeroGPU hardware. | Not stated on pricing page | 2026-10-14 |
| [LM Studio](https://freetierfinder.com/tool/lm-studio) | LM Studio desktop app to run open models locally. | Not stated on pricing page | 2026-10-14 |
| [Mistral La Plateforme](https://freetierfinder.com/tool/mistral-la-plateforme) | Not stated by vendor | Not stated on pricing page | 2026-10-14 |
| [NVIDIA NIM](https://freetierfinder.com/tool/nvidia-nim) | Free NIM API endpoints for prototyping, plus self-hosting NIM on up to 16 GPUs for development. | Not stated on pricing page | 2026-10-14 |
| [Ollama](https://freetierfinder.com/tool/ollama) | Run models locally plus starter cloud usage credits. | Not stated on pricing page | 2026-10-14 |
| [OpenRouter](https://freetierfinder.com/tool/openrouter) | 25+ free models from 4 free providers via chat and API, with activity logs. | Not stated on pricing page | 2026-10-14 |

### AI Audio

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [AssemblyAI](https://freetierfinder.com/tool/assemblyai) | $50 in free credits on signup for speech-to-text and other APIs. | No (stated on pricing page) | 2026-10-14 |
| [Cartesia](https://freetierfinder.com/tool/cartesia) | 20K credits a month for text to speech and speech to text (about 27 minutes of Sonic-3.6 audio), plus $1 a month of prepaid voice-agent usage. | Not stated on pricing page | 2026-10-14 |
| [ElevenLabs](https://freetierfinder.com/tool/elevenlabs) | 10,000 credits a month for text to speech, speech to text, sound effects and more; 3 Studio projects. | Not stated on pricing page | 2026-10-14 |
| [Onepin](https://freetierfinder.com/tool/onepin) | 1,000 one-time credits, about 15 minutes of validated audio. | No (stated on pricing page) | 2026-10-14 |
| [Suno](https://freetierfinder.com/tool/suno) | 50 credits a day on free models, standard features, upload up to 8 minutes of audio. | Not stated on pricing page | 2026-10-14 |

### AI Chat

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [ChatGPT](https://freetierfinder.com/tool/chatgpt) | Unlimited text chats with GPT-6 (subject to abuse guardrails); limited uploads, image creation, voice, deep research and Codex. | Not stated on pricing page | 2026-10-14 |
| [Claude](https://freetierfinder.com/tool/claude) | Claude chat on web, desktop and mobile with web search, file creation, code execution, memory, connectors, Artifacts, and Claude Design, Slides and Docs. | No (stated on pricing page) | 2026-10-14 |
| [Google Gemini](https://freetierfinder.com/tool/google-gemini) | Gemini app with the Flash-Lite model, image generation and editing, Deep Research, Gemini Live, Canvas, Gems, limited Google Flow access and 15 GB of storage. | Not stated on pricing page | 2026-10-14 |
| [Microsoft Copilot](https://freetierfinder.com/tool/microsoft-copilot) | Copilot on web, desktop and mobile to research, create content and generate images, plus Word, Excel and PowerPoint free on the web. | Not stated on pricing page | 2026-10-14 |
| [Mistral Le Chat](https://freetierfinder.com/tool/mistral-le-chat) | Mistral's assistant (called Vibe on the pricing page) on web and mobile with limited messages, web searches and coding sessions, basic image generation and editing, and 100+ connectors. | Not stated on pricing page | 2026-10-14 |

### AI Coding

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Bolt.new](https://freetierfinder.com/tool/bolt-new) | Public and private projects, 300K tokens a day up to 1M a month, hosting, unlimited databases. | Not stated on pricing page | 2026-10-14 |
| [Gemini CLI](https://freetierfinder.com/tool/gemini-cli) | 1,000 requests per user per day when logged in with a Google account. | Not stated on pricing page | 2026-10-14 |
| [GitHub Copilot](https://freetierfinder.com/tool/github-copilot) | Entry-level models, 2,000 code completions a month, and limited chat and agent usage (CLI and agent mode supported). | No (stated on pricing page) | 2026-10-14 |
| [Google Antigravity](https://freetierfinder.com/tool/google-antigravity) | Access to a variety of agent models, unlimited Tab completions and Command requests. | Not stated on pricing page | 2026-10-14 |
| [Lovable](https://freetierfinder.com/tool/lovable) | 5 build credits a day (up to 30 a month), 20 Cloud credits a month, and 4 in-app AI credits to try. | No (stated on pricing page) | 2026-10-14 |
| [v0](https://freetierfinder.com/tool/v0) | Free v0 access, deploy to Vercel, Design Mode and GitHub sync. | Not stated on pricing page | 2026-10-14 |
| [Windsurf](https://freetierfinder.com/tool/windsurf) | Light agent quota, limited model availability, unlimited inline edits and Tab completions. | Not stated on pricing page | 2026-10-14 |

### AI Image

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Ideogram](https://freetierfinder.com/tool/ideogram) | Weekly slow credits for eligible accounts, 1 running or queued generation. | Not stated on pricing page | 2026-10-14 |
| [Krea](https://freetierfinder.com/tool/krea) | 100 compute units a day. | Not stated on pricing page | 2026-10-14 |
| [Leonardo.ai](https://freetierfinder.com/tool/leonardo-ai) | 150 fast tokens a day for image and video generation, 1 personal collection. | Not stated on pricing page | 2026-10-14 |
| [Microsoft Designer](https://freetierfinder.com/tool/microsoft-designer) | Not stated by vendor | Not stated on pricing page | 2026-10-14 |
| [Playground](https://freetierfinder.com/tool/playground) | Up to 10 images every 3 hours, 3 monthly generations on premium models, commercial use license. | Not stated on pricing page | 2026-10-14 |

### AI Research

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Consensus](https://freetierfinder.com/tool/consensus) | Not stated by vendor | Not stated on pricing page | 2026-10-14 |
| [Elicit](https://freetierfinder.com/tool/elicit) | Unlimited search over 138M+ papers, unlimited summaries and chat with papers, limited Research Agent use. | Not stated on pricing page | 2026-10-14 |

### AI Search

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Exa](https://freetierfinder.com/tool/exa) | $10 in free credits every month plus a $10 onboarding bonus, access to all endpoints, MCP server and 50+ integrations. | No (stated on pricing page) | 2026-10-14 |
| [Perplexity](https://freetierfinder.com/tool/perplexity) | AI answers with inline citations, plus a few advanced searches a day on a single default model. | Not stated on pricing page | 2026-10-14 |
| [Tavily](https://freetierfinder.com/tool/tavily) | 1,000 API credits a month. | No (stated on pricing page) | 2026-10-14 |

### AI Video

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [HeyGen](https://freetierfinder.com/tool/heygen) | 3 videos a month up to 1 minute each, Avatar IV, 500+ stock avatars, 1 custom avatar. | No (stated on pricing page) | 2026-10-14 |
| [Luma Dream Machine](https://freetierfinder.com/tool/luma-dream-machine) | Not stated by vendor | Not stated on pricing page | 2026-10-14 |
| [Pika](https://freetierfinder.com/tool/pika) | All models, no watermark; generation is via credit packs only. | Not stated on pricing page | 2026-10-14 |
| [Runway](https://freetierfinder.com/tool/runway) | 125 one-time credits, a selection of generative models, 5 GB asset storage. | No (stated on pricing page) | 2026-10-14 |

### Analytics

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Google Analytics](https://freetierfinder.com/tool/google-analytics) | Google Analytics tools free of charge. | Not stated on pricing page | 2026-10-14 |
| [Hotjar](https://freetierfinder.com/tool/hotjar) | 200k monthly sessions, 1 project, replays, heatmaps, funnels, basic surveys. | Not stated on pricing page | 2026-10-14 |
| [Microsoft Clarity](https://freetierfinder.com/tool/microsoft-clarity) | Session recordings, heatmaps, AI summaries and AI chat, free forever. | Not stated on pricing page | 2026-10-14 |
| [Mixpanel](https://freetierfinder.com/tool/mixpanel) | Up to 1M events a month, 10K session replays, unlimited seats. | No (stated on pricing page) | 2026-10-14 |
| [Plausible](https://freetierfinder.com/tool/plausible) | Plausible Community Edition: free, self-hosted, AGPL-licensed analytics. | No (stated on pricing page) | 2026-10-14 |

### Automation

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [IFTTT](https://freetierfinder.com/tool/ifttt) | 2 Applets, unlimited Applet runs, standard speeds, mobile app. | Not stated on pricing page | 2026-10-14 |
| [Make](https://freetierfinder.com/tool/make) | 1,000 credits a month, no-code visual workflow builder, 3,500+ apps, routers and filters, 1 MB data storage and 1 data store. | Not stated on pricing page | 2026-10-14 |
| [n8n](https://freetierfinder.com/tool/n8n) | Self-hosted n8n; hosted n8n Cloud offers a 14-day free trial with 800 Assistant credits. | No (stated on pricing page) | 2026-10-14 |
| [Zapier](https://freetierfinder.com/tool/zapier) | Zaps, Tables and Forms, with 100 tasks a month. | No (stated on pricing page) | 2026-10-14 |

### Commerce

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Gumroad](https://freetierfinder.com/tool/gumroad) | No monthly fee; Gumroad acts as merchant of record and handles sales tax. | Not stated on pricing page | 2026-10-14 |
| [Lemon Squeezy](https://freetierfinder.com/tool/lemon-squeezy) | No monthly charge for ecommerce features; merchant of record. | No (stated on pricing page) | 2026-10-14 |
| [Stripe](https://freetierfinder.com/tool/stripe) | No setup or monthly fees. | Not stated on pricing page | 2026-10-14 |

### Database

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Firebase](https://freetierfinder.com/tool/firebase) | Spark plan with no-cost usage limits across Firestore, Auth, Hosting and more. | No (stated on pricing page) | 2026-10-14 |
| [MongoDB Atlas](https://freetierfinder.com/tool/mongodb-atlas) | Free forever cluster with 512 MB storage, shared RAM and vCPU. | Not stated on pricing page | 2026-10-14 |
| [Neon](https://freetierfinder.com/tool/neon) | 100 projects, 100 CU-hours a month per project, 1 GB storage per project, 5 GB object storage. | No (stated on pricing page) | 2026-10-14 |
| [Pinecone](https://freetierfinder.com/tool/pinecone) | Starter plan with database, inference and assistant for small apps. | Not stated on pricing page | 2026-10-14 |
| [Supabase](https://freetierfinder.com/tool/supabase) | Unlimited API requests, 50,000 MAU, 500 MB database, 5 GB egress, 1 GB file storage. | Not stated on pricing page | 2026-10-14 |
| [Turso](https://freetierfinder.com/tool/turso) | 100 databases, 5 GB storage, 500M rows read and 10M rows written a month, 3 GB syncs. | No (stated on pricing page) | 2026-10-14 |
| [Upstash](https://freetierfinder.com/tool/upstash) | 1 free Redis database: 250 MB data, 10 GB bandwidth and 500K commands a month. | Not stated on pricing page | 2026-10-14 |

### Design

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Adobe Express](https://freetierfinder.com/tool/adobe-express) | 100,000+ templates, 1M+ Adobe Stock assets, 4,000+ fonts, standard photo, video and document editing, 5 GB storage and free daily AI generations. | No (stated on pricing page) | 2026-10-14 |
| [Canva](https://freetierfinder.com/tool/canva) | Not stated by vendor | Not stated on pricing page | 2026-10-14 |
| [Figma](https://freetierfinder.com/tool/figma) | Unlimited drafts, UI kits and templates, 150 AI credits a day up to 500 a month. | Not stated on pricing page | 2026-10-14 |
| [Napkin](https://freetierfinder.com/tool/napkin) | 500 AI credits a week (about 1 credit per word). | Not stated on pricing page | 2026-10-14 |
| [Photopea](https://freetierfinder.com/tool/photopea) | Full browser photo editor that runs locally, no uploads. | Not stated on pricing page | 2026-10-14 |
| [Remove.bg](https://freetierfinder.com/tool/remove-bg) | Not stated by vendor | Not stated on pricing page | 2026-10-14 |

### Dev Hosting

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Cloudflare Workers](https://freetierfinder.com/tool/cloudflare-workers) | Limited usage of Workers, Pages Functions, Workers KV and Hyperdrive. | Not stated on pricing page | 2026-10-14 |
| [GitHub](https://freetierfinder.com/tool/github) | Unlimited public and private repositories, 2,000 CI/CD minutes a month (free for public repos). | Not stated on pricing page | 2026-10-14 |
| [GitHub Pages](https://freetierfinder.com/tool/github-pages) | Static hosting from a GitHub repo; sites up to 1 GB with a 100 GB/month soft bandwidth limit. | Not stated on pricing page | 2026-10-14 |
| [GitLab](https://freetierfinder.com/tool/gitlab) | GitLab.com Free for personal projects and open source, 5 users per top-level group. | No (stated on pricing page) | 2026-10-14 |
| [Netlify](https://freetierfinder.com/tool/netlify) | Deploys, deploy previews, custom domains with SSL, functions, database, blob storage, CDN; 300 credits a month. | Not stated on pricing page | 2026-10-14 |
| [Vercel](https://freetierfinder.com/tool/vercel) | Hobby: deploy from Git with CI/CD, CDN, firewall, DDoS mitigation and fluid compute. | Not stated on pricing page | 2026-10-14 |

### Dev Tools

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Clerk](https://freetierfinder.com/tool/clerk) | Unlimited apps, 50,000 MRU per app, up to 3 dashboard seats. | No (stated on pricing page) | 2026-10-14 |
| [Docker](https://freetierfinder.com/tool/docker) | Docker Desktop, Engine with Kubernetes, Docker Hub, Scout and Debug for 1 user. | Not stated on pricing page | 2026-10-14 |
| [Firecrawl](https://freetierfinder.com/tool/firecrawl) | 1,000 credits a month (500 searches or 1,000 pages), 2 concurrent requests. | No (stated on pricing page) | 2026-10-14 |
| [Langfuse](https://freetierfinder.com/tool/langfuse) | All platform features with limits, 50k units a month, 2 users. | No (stated on pricing page) | 2026-10-14 |
| [Postman](https://freetierfinder.com/tool/postman) | Postman API platform with 50 AI credits a month. | Not stated on pricing page | 2026-10-14 |
| [Sentry](https://freetierfinder.com/tool/sentry) | Error monitoring and tracing, email alerts, 10 custom dashboards. | Not stated on pricing page | 2026-10-14 |
| [Warp](https://freetierfinder.com/tool/warp) | Warp's modern terminal and Agent CLI; use Warp's AI or bring your own. | Not stated on pricing page | 2026-10-14 |

### Email

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [beehiiv](https://freetierfinder.com/tool/beehiiv) | Up to 2,500 subscribers, 1 team seat, newsletter, website and podcast. | No (stated on pricing page) | 2026-10-14 |
| [Brevo](https://freetierfinder.com/tool/brevo) | Up to 300 emails a day. | No (stated on pricing page) | 2026-10-14 |
| [Kit (ConvertKit)](https://freetierfinder.com/tool/kit-convertkit) | Up to 10,000 subscribers, unlimited landing pages, forms and broadcasts. | No (stated on pricing page) | 2026-10-14 |
| [Mailchimp](https://freetierfinder.com/tool/mailchimp) | Mailchimp offers a basic Free plan. | Not stated on pricing page | 2026-10-14 |
| [Postmark](https://freetierfinder.com/tool/postmark) | 100 emails a month to test the integration. | No (stated on pricing page) | 2026-10-14 |
| [Resend](https://freetierfinder.com/tool/resend) | 3,000 emails a month, 3 domains, ticket support. | Not stated on pricing page | 2026-10-14 |

### Forms

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Jotform](https://freetierfinder.com/tool/jotform) | Starter plan, free with storage and submission limits. | Not stated on pricing page | 2026-10-14 |
| [Tally](https://freetierfinder.com/tool/tally) | Unlimited forms and submissions, payments, signatures and file uploads. | Not stated on pricing page | 2026-10-14 |

### Meetings

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Discord](https://freetierfinder.com/tool/discord) | Not stated by vendor | Not stated on pricing page | 2026-10-14 |
| [Loom](https://freetierfinder.com/tool/loom) | 25 videos per person, 5-minute recordings, transcription in 50+ languages, up to 50 members. | Not stated on pricing page | 2026-10-14 |
| [Slack](https://freetierfinder.com/tool/slack) | 90 days of message history, up to 10 apps. | Not stated on pricing page | 2026-10-14 |
| [Zoom](https://freetierfinder.com/tool/zoom) | Meetings up to 40 minutes with 100 participants, 3 AI summaries and 20 AI queries a month, local recording. | Not stated on pricing page | 2026-10-14 |

### Productivity

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Airtable](https://freetierfinder.com/tool/airtable) | Unlimited bases; all users are free on the Free plan. | Not stated on pricing page | 2026-10-14 |
| [Asana](https://freetierfinder.com/tool/asana) | Unlimited tasks and projects with list, board and calendar views. | Not stated on pricing page | 2026-10-14 |
| [Cal.com](https://freetierfinder.com/tool/cal-com) | 1 user, unlimited event types and calendars, email and SMS notifications, 100+ integrations. | Not stated on pricing page | 2026-10-14 |
| [Calendly](https://freetierfinder.com/tool/calendly) | One event type, one calendar connection, one-on-one scheduling, booking page. | Not stated on pricing page | 2026-10-14 |
| [Fireflies.ai](https://freetierfinder.com/tool/fireflies-ai) | Unlimited transcription in 100+ languages, real-time notes and live transcriptions, meeting search, limited AI summaries and 20 AI credits; works with Zoom, Google Meet and Teams. | Not stated on pricing page | 2026-10-14 |
| [Linear](https://freetierfinder.com/tool/linear) | Unlimited members, 2 teams, 250 issues, Linear Agent. | Not stated on pricing page | 2026-10-14 |
| [Miro](https://freetierfinder.com/tool/miro) | 3 editable boards and 7,000+ templates. | Not stated on pricing page | 2026-10-14 |
| [Notion](https://freetierfinder.com/tool/notion) | Personal workspace with forms, sites, Notion Calendar and a trial of Notion AI. | Not stated on pricing page | 2026-10-14 |
| [Obsidian](https://freetierfinder.com/tool/obsidian) | The full Obsidian app with no limits. | Not stated on pricing page | 2026-10-14 |
| [Otter.ai](https://freetierfinder.com/tool/otter-ai) | 300 transcription minutes a month, live transcription, 3 lifetime file imports. | Not stated on pricing page | 2026-10-14 |
| [Raycast](https://freetierfinder.com/tool/raycast) | All built-in extensions and public community extensions, for personal or organizational use. | Not stated on pricing page | 2026-10-14 |
| [Rill Browser](https://freetierfinder.com/tool/rill-browser) | The Rill AI browser, free while in beta. | Not stated on pricing page | 2026-10-14 |
| [tl;dv](https://freetierfinder.com/tool/tl-dv) | Unlimited recordings, viewers, storage and transcription in 30+ languages; 10 meetings with AI notes and 10 Ask AI queries. | No (stated on pricing page) | 2026-10-14 |
| [Todoist](https://freetierfinder.com/tool/todoist) | 5 personal projects, Smart Quick Add, task reminders. | Not stated on pricing page | 2026-10-14 |
| [Trello](https://freetierfinder.com/tool/trello) | Up to 10 boards per Workspace, 10 collaborators, unlimited cards and Power-Ups, 10 MB per file. | Not stated on pricing page | 2026-10-14 |

### Social

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Buffer](https://freetierfinder.com/tool/buffer) | Up to 3 channels, 10 scheduled posts per channel, 100 ideas, AI Assistant, 1 user. | Not stated on pricing page | 2026-10-14 |
| [Linktree](https://freetierfinder.com/tool/linktree) | Unlimited basic links, email and phone sign-ups. | Not stated on pricing page | 2026-10-14 |

### Storage

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Dropbox](https://freetierfinder.com/tool/dropbox) | 2 GB to store and share files. | Not stated on pricing page | 2026-10-14 |
| [Google Drive](https://freetierfinder.com/tool/google-drive) | Up to 15 GB of storage shared across Google services. | Not stated on pricing page | 2026-10-14 |
| [Mega](https://freetierfinder.com/tool/mega) | Free plan with storage and limited transfer. | Not stated on pricing page | 2026-10-14 |

### Video

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [CapCut](https://freetierfinder.com/tool/capcut) | Online and desktop photo and video editor with AI tools. | No (stated on pricing page) | 2026-10-14 |
| [Clipchamp](https://freetierfinder.com/tool/clipchamp) | Free video editor with AI editing, recorders, free stock assets and filters. | No (stated on pricing page) | 2026-10-14 |
| [Descript](https://freetierfinder.com/tool/descript) | 60 media minutes a month with transcription in 25 languages and text-based editing. | Not stated on pricing page | 2026-10-14 |
| [Kapwing](https://freetierfinder.com/tool/kapwing) | 10 credits, unlimited exports up to 4 minutes at 720p, 5 GB storage. | Not stated on pricing page | 2026-10-14 |

### Websites

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Framer](https://freetierfinder.com/tool/framer) | 500 AI credits to try, a Framer domain, 1 GB bandwidth. | Not stated on pricing page | 2026-10-14 |
| [Webflow](https://freetierfinder.com/tool/webflow) | Webflow.io domain, 2 static pages, limited CMS, 1 GB bandwidth, 50 form submissions. | Not stated on pricing page | 2026-10-14 |
| [Wix](https://freetierfinder.com/tool/wix) | Build a site for free. | No (stated on pricing page) | 2026-10-14 |
| [WordPress.com](https://freetierfinder.com/tool/wordpress-com) | Free WordPress.com plan with managed hosting. | No (stated on pricing page) | 2026-10-14 |

### Writing

| Tool | Free tier | Card required | Checked |
| --- | --- | --- | --- |
| [Copy.ai](https://freetierfinder.com/tool/copy-ai) | Not stated by vendor | Not stated on pricing page | 2026-10-14 |
| [Grammarly](https://freetierfinder.com/tool/grammarly) | Spelling and grammar checks, tone detection, 100 AI prompts. | Not stated on pricing page | 2026-10-14 |
| [QuillBot](https://freetierfinder.com/tool/quillbot) | Paraphrase up to 100 words in 2 modes (Standard and Fluency), basic grammar fixes, humanize up to 100 words, summaries up to 1,200 words, limited AI Detector and AI chat. | Not stated on pricing page | 2026-10-14 |

### Promos and startup credits

| Offer | Type | Expires | Checked |
| --- | --- | --- | --- |
| [AWS Activate: Up to $200,000 in credits; the Founders tier is up to $5,000](https://freetierfinder.com/promo/aws-activate) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [AWS Free Tier: Up to $200 in AWS credits for new accounts](https://freetierfinder.com/promo/aws-free-tier) | One-time credits | Credits usable up to 6 months after account creation | 2026-10-14 |
| [Cloudflare for Startups: Up to $350,000 in credits; the entry tier is $10,000](https://freetierfinder.com/promo/cloudflare-for-startups) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [Cloudflare Workers AI: 10,000 Neurons a day of AI inference](https://freetierfinder.com/promo/cloudflare-workers-ai) | Generous free tier | Ongoing | 2026-10-14 |
| [Datadog for Startups: A year of Datadog, up to $100,000 in credits](https://freetierfinder.com/promo/datadog-for-startups) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [Deepgram: $200 in free speech API credit](https://freetierfinder.com/promo/deepgram) | One-time credits | No end date stated | 2026-10-14 |
| [ElevenLabs: 10,000 free voice credits every month](https://freetierfinder.com/promo/elevenlabs) | Generous free tier | Ongoing | 2026-10-14 |
| [ElevenLabs Startup Grants: 33,000,000 characters (ElevenLabs says "$5,500+ in value", about 680 hours of Agents)](https://freetierfinder.com/promo/elevenlabs-startup-grants) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [Gemini CLI: 1,000 coding-agent requests a day](https://freetierfinder.com/promo/gemini-cli) | Generous free tier | Ongoing | 2026-10-14 |
| [Google AI Pro via Jio: Up to 18 months of Google AI Pro free for Jio users in India](https://freetierfinder.com/promo/google-ai-pro-via-jio) | Carrier bundle | No end date stated | 2026-10-14 |
| [Google for Startups Cloud: $2,000 for pre-funded startups; $200,000–$350,000 for Seed to Series A](https://freetierfinder.com/promo/google-for-startups-cloud) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [Google Vids: Free AI video generation for any Google account](https://freetierfinder.com/promo/google-vids) | New free tier | No end date stated | 2026-10-14 |
| [Kit (ConvertKit): A free newsletter plan for up to 10,000 subscribers](https://freetierfinder.com/promo/kit-convertkit) | Generous free tier | Ongoing | 2026-10-14 |
| [Microsoft for Startups: Up to $150,000 in credits, plus AI models and developer tools](https://freetierfinder.com/promo/microsoft-for-startups) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [MongoDB for Startups: Atlas credits (the amount isn't shown on the page)](https://freetierfinder.com/promo/mongodb-for-startups) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [Notion for Startups: Business plan free for up to 6 months (Notion says "save $12,000")](https://freetierfinder.com/promo/notion-for-startups) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [OpenCode: Free models on OpenCode Console](https://freetierfinder.com/promo/opencode) | Limited-time free models | Limited time; no end date stated | 2026-10-14 |
| [PostHog for Startups: $50,000 in PostHog credits for 12 months, plus $12,000 in partner perks](https://freetierfinder.com/promo/posthog-for-startups) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [Runable for Startups: $5,000 in credits](https://freetierfinder.com/promo/runable-for-startups) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [Runway: 125 one-time free credits for AI video](https://freetierfinder.com/promo/runway) | One-time credits | No end date stated | 2026-10-14 |
| [Stripe Atlas: $2,500 in Stripe credits plus $50,000+ in partner discounts](https://freetierfinder.com/promo/stripe-atlas) | Startup credits | Ongoing program; terms can change | 2026-10-14 |
| [Vercel AI Gateway: Free Nemotron 3.5 Lightning on AI Gateway](https://freetierfinder.com/promo/vercel-ai-gateway) | Limited-time free model | No end date stated | 2026-10-14 |
| [Vercel for Startups: Up to $30,000 in Flexible Commitment Amount, plus Enterprise-tier access](https://freetierfinder.com/promo/vercel-for-startups) | Startup credits | Ongoing program; terms can change | 2026-10-14 |

## Report an outdated entry

Open an issue with the [Report outdated entry](../../issues/new?template=report-outdated.md) template and include a link to the vendor's official page. To propose a new tool, use [Suggest a tool](../../issues/new?template=suggest-tool.md).

## License

The data in `data/` is licensed under [CC BY 4.0](LICENSE). Attribute "Free Tier Finder (https://freetierfinder.com)". Scripts in `scripts/` are MIT licensed.

## Citation

See [CITATION.cff](CITATION.cff).
