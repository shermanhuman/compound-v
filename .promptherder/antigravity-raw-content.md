# Antigravity Documentation & Blog — Full Content Dump

Fetched 44 pages


======================================================================
## BLOG: introducing-google-antigravity
URL: https://antigravity.google/blog/introducing-google-antigravity
======================================================================
---
slug: introducing-google-antigravity
categories:
  - Product
author: The Antigravity Team
authorTitle: 
date: 2025-11-18T18:19:47.807Z
title: Introducing Google Antigravity, a New Era in AI-Assisted Software Development
articleImage: blog/blog-introducing-google-antigravity.png
---

Every advancement in model intelligence for coding has encouraged us to rethink how development should be done. The Integrated Development Environment (IDE) of today is a far cry from the IDE of just a few years ago. Gemini 3, our most intelligent model, represents a step-change for agentic coding, and requires us to think about what the next step-change of an IDE should be. 

Today, we are introducing Google Antigravity, our new agentic development platform. While the core is a familiar AI-powered IDE experience with the best of Google’s models, Antigravity is evolving the IDE towards an agent-first future with browser control capabilities, asynchronous interaction patterns, and an agent-first product form factor that together, enable agents to autonomously plan and execute complex, end-to-end software tasks.

## Why We Built Antigravity
We want Antigravity to be the home base for software development in the era of agents. Our vision is to ultimately enable anyone with an idea to experience liftoff and build that idea into reality. From today, Google Antigravity is available in public preview at no charge, with generous rate limits on Gemini 3 Pro usage. 

With models like Gemini 3, we have started hitting the point in agentic intelligence where models are capable of running for longer periods of time without intervention across multiple surfaces. Not yet for days at a time without intervention, but we’re getting closer to a world where we interface with agents at higher abstractions over individual prompts and tool calls. In this world, the product surface that enables communication between the agent and user should look and feel different - and Antigravity is our answer to this.

## Core Tenets
Antigravity is our first product that brings four key tenets of collaborative development together: trust, autonomy, feedback, and self-improvement.

### Trust
Most products today live in one of two extremes: either they show the user every single action and tool call the agent has made or they only show the final code change with no context on how the agent got there, and with no easy way to verify the work. Neither engenders user trust in the work that the agent undertook. Antigravity provides context on agentic work at a more natural task-level abstraction, with the necessary and sufficient set of artifacts and verification results, for the user to gain that trust. There is a concerted emphasis for the agent to thoroughly think through verification of its work, not just the work itself.

In a conversation with an agent in Antigravity, the user sees tool calls grouped within tasks, monitoring high level summaries and progress along that task. As the agent works, it produces Artifacts, tangible deliverables in formats that are easier for users to validate than raw tool calls, such as task lists, implementation plans, walkthroughs, screenshots, and browser recordings.  Agents in Antigravity use Artifacts to communicate to the user that it understands what it is doing and that it is thoroughly verifying its work.

{{video: https://www.youtube.com/embed/6QeVnO709r0?si=Wdrd2haIwDE1MMSe, blog/introducing-antigravity-1.jpg, View the Agent's task list, review the implementation plan post-research and pre-implementation, or scan the walkthrough at completion.}}

### Autonomy
Today, the most intuitive product form factor is working synchronously with an agent embedded within a surface (an editor, browser, terminal, etc). That is why Antigravity’s primary “Editor view” is a state-of-the-art AI-powered IDE experience, with Tab completions, in-line Commands, and a fully functioning agent in the side panel. 

That being said, we are transitioning to an era, with models like Gemini 3, when agents can operate across all of these surfaces simultaneously and autonomously: 

{{video: https://www.youtube.com/embed/HRH4kUlMeAM?si=Wdrd2haIwDE1MMSe, blog/introducing-antigravity-2.jpg, Autonomously, an Antigravity Agent writes code for a new frontend feature, uses the terminal to launch localhost, and actuates the browser to test that the new feature works.}}

We also believe agents deserve a form factor that exposes this autonomy optimally and allows users to interact with them more asynchronously. So, in addition to the IDE-like Editor surface,  we are introducing an agent-first Manager surface, which flips the paradigm of agents being embedded within surfaces to one where the surfaces are embedded into the agent. You can think of it like a mission control for spawning, orchestrating, and observing multiple agents across multiple workspaces in parallel. 

{{video: https://www.youtube.com/embed/JG28VZRHRe0?si=Wdrd2haIwDE1MMSe, blog/introducing-antigravity-3.jpg, User spawned an Agent to do background research in a different workspace while focusing on a more involved task in the foreground, using the Inbox and side panel in the Agent Manager to be notified of progress.}}

We decided not to try to squeeze both the asynchronous Manager experience and the synchronous Editor experience into a single window, rather optimizing for instantaneous handoffs between the Manager and Editor. Antigravity is designed to be forward-looking, intuitively bringing development to the asynchronous era as models like Gemini continue to rapidly get smarter. 

### Feedback
A core failing of a remote-only form factor is the inability to iterate easily with the agent. Agentic intelligence has indeed improved significantly, but it is still not perfect. An agent being able to complete 80% of the work should be useful, but if there is no easy way to provide feedback, then it becomes more work than benefit to resolve the remaining 20%. User feedback allows us to not treat an agent as a black-or-white system that either is perfect or unhelpful. Antigravity is starting with local operation, allowing intuitive async user feedback across every surface and Artifact, whether it be Google-doc-style comments on text Artifacts or select-and-comment feedback on screenshots. This feedback will be automatically incorporated into the agent’s execution without requiring you to stop the agent’s process. 

{{video: https://www.youtube.com/embed/WpjiSzypOkY?si=Wdrd2haIwDE1MMSe, blog/introducing-antigravity-4.jpg, An example of feedback on textual Artifacts such as an implementation plan and an example of feedback on a visual Artifact such as a screenshot taken by the Agent.}}

### Self-improvement
Antigravity treats learning as a core primitive, with agent actions both retrieving from and contributing to a knowledge base. This knowledge management allows the agent to learn from past work. This could be important explicit information such as useful snippets of code or derived architecture, but could also be more abstract, such as the series of steps taken to successfully complete a particular subtask.

{{video: https://www.youtube.com/embed/tB7flTt8A1E?si=Wdrd2haIwDE1MMSe, blog/introducing-antigravity-5.jpg, Agent learning from work and feedback to generate and leverage knowledge items, viewable from the Agent Manager.}}

## Try Antigravity Today
We believe Antigravity’s product form factor represents the next fundamental step function in agent-assisted development. Thus, our goal is to channel it into the best product offering possible for end users. In today’s public preview:

- Google Antigravity for individuals at no charge 
- Compatibility with MacOS, Linux, and Windows
- Access to Google’s Gemini 3, Anthropic’s Claude Sonnet 4.5 models, and OpenAI’s GPT-OSS within the agent, offering developers model optionality [^rate-limits]

Learn more about the features of Antigravity in [our docs](/docs) and read more about how Antigravity can assist you by browsing various [use cases](/use-cases). We will have new features dropping frequently, so keep up-to-date with this blog and socials at [X](https://x.com/antigravity), [LinkedIn](https://linkedin.com/company/google-antigravity), and [YouTube](https://youtube.com/@GoogleAntigravity).

Experience liftoff in 3… 2… 1…

{{button: Download Antigravity, /download}}

[^rate-limits]: [1] We will be providing access to models to the degree we have capacity, with rate limits to prevent abuse and that are refreshed every five hours. Under the hood, the rate limits are correlated with the amount of work done by the agent, which can differ from prompt to prompt. Thus, you may get many more prompts if your tasks are more straightforward and the agent can complete the work quickly, and the opposite is also true. Our modeling suggests that a very small fraction of power users will ever hit the per-five-hour rate limit, so our hope is that this is something that you won’t have to worry about, and you feel unrestrained in your usage of Antigravity.


======================================================================
## BLOG: nano-banana-pro-in-google-antigravity
URL: https://antigravity.google/blog/nano-banana-pro-in-google-antigravity
======================================================================
---
slug: nano-banana-pro
categories:
  - Product
author: The Antigravity Team
authorTitle: 
date: 2025-11-20T18:19:47.807Z
title: Nano Banana Pro in Google Antigravity
articleImage: blog/blog-nano-banana-pro-wide.png
---

[Nano Banana Pro](https://blog.google/technology/ai/nano-banana-pro) (Gemini 3 Pro Image) is rolling out now to Google Antigravity. This higher-fidelity model built on Gemini 3 Pro, is an advancement across multiple axes over the original Nano Banana, particularly in text rendering and collateral generation, while maintaining strengths in edit-to-edit consistency.

In Google Antigravity, the Agent has the ability to decide when to use an image generation model when it deems appropriate. This often manifests in developer workflows such as:

- Generating a UI mockup for a new frontend, allowing the user to provide precise visual feedback to iterate on the design before asking the Agent to continue and generate the code. The improved text rendering and edit consistency with Nano Banana Pro makes this even more rich and robust.
- Generating an easy to understand system or architecture diagram to explain existing code or knowledge. Nano Banana Pro’s text rendering and collateral generation shines for this use case.
- Generating highly relevant image assets for use within websites or other visual applications, as opposed to scouring through stock photo assets for a meaningful fit.

{{video: https://www.youtube.com/embed/FB6HO7CZHWw?si=Wdrd2haIwDE1MMSe, blog/blog-nano-banana-pro-wide.png, Generating and iterating on a UI mockup with Nano Banana Pro.}}

Nano Banana Pro is rolling out incrementally to Google Antigravity users. Agents will still leverage the original Nano Banana for image generation steps if the user is yet to receive access to Nano Banana Pro.

{{button: Download Antigravity, /download}}


======================================================================
## BLOG: gemini-3-flash-in-google-antigravity
URL: https://antigravity.google/blog/gemini-3-flash-in-google-antigravity
======================================================================
---
slug: gemini-3-flash-in-google-antigravity
categories:
  - Product
author: The Antigravity Team
authorTitle: 
date: 2025-12-17T18:19:47.807Z
title: Gemini 3 Flash in Google Antigravity, agentic coding at the speed of thought
articleImage: blog/blog-gemini-3-flash-wide.png
---

Over the past few weeks, Google Antigravity has started to change how we think about development.  Building with a more capable agent is moving us from simple code completion to an era where agents autonomously plan, execute, and debug end-to-end across the editor, terminal and browser tackling more complex, long-running tasks. Today, we are accelerating that shift by bringing [Gemini 3 Flash](https://blog.google/products/gemini/gemini-3-flash) directly into your workflow in Google Antigravity.

Building on the momentum of [Gemini 3 Pro](https://blog.google/products/gemini/gemini-3/), which delivered state-of-the-art performance across complex reasoning and multimodal understanding, Gemini 3 Flash offers frontier intelligence built for speed at a fraction of the cost.

For the best synchronous agent-first IDE workflow, intelligence needs to be fast. The friction of waiting for an agent to "think" or plan a complex multi-step workflow for many tasks can break your flow state. Gemini 3 Flash in Antigravity is the answer to that friction — enabling you to build at the speed of thought, accelerating your creativity even farther.

## The Antigravity Experience

For developers using Google Antigravity, Gemini 3 Flash offers a distinct advantage: it balances Pro-grade coding performance with the low latency required for a human-in-the-loop agentic experience. Gemini 3 Flash has even better coding and agent capabilities over previous versions, enabling rapid, iterative development, outperforming 3 Pro's agentic coding skill (78% on SWE-bench Verified) but operating faster for quick iterations.

While directing agents to control the browser, manage the terminal, or scaffold entire features—Gemini 3 Flash ensures those agents keep up with your thought process, making the collaboration feel even more fluid.

{{video: https://www.youtube.com/embed/oCFqZ0Ri6gg?si=Wdrd2haIwDE1MMSe, blog/blog-gemini-3-flash-wide.png, Gemini 3 Flash side-by-side with Gemini 3 Pro.}}

With Gemini 3 Flash, you describe a change, and the agent much more rapidly formulates a plan, writes code, uses the browser, generates artifacts, performs verification, and everything you have come to expect from Antigravity. The reduced latency tightens the feedback loop, allowing you to iterate, correct, and refine faster than ever before.

## Build and Scale with Confidence

While benchmarks confirm that [Gemini 3 Flash rivals the coding capabilities](https://blog.google/technology/developers/build-with-gemini-3-flash/) of larger models, the real metric that matters here is flow. It allows the autonomous planning and execution features of Antigravity to feel like a natural extension of your own thought process.

Agentic workflows often involve multiple steps of reasoning, planning, and execution. Running these loops on larger models can become costly and slow, especially for simpler tasks, but by bringing Gemini 3 Flash into Google Antigravity, we are giving developers the ability to run sophisticated, multi-step agent loops efficiently. You get the benefits of a model that can handle long-horizon tasks and complex refactors, but with the efficiency profile that makes it practical for everyday, heavy usage.

## Get Started

The era of agentic development is evolving. Experience more intelligent, faster collaboration at scale with Gemini 3 Flash now available in preview in Google Antigravity.

{{button: Download Antigravity, /download}}


======================================================================
## BLOG: gemini-3-1-pro-in-google-antigravity
URL: https://antigravity.google/blog/gemini-3-1-pro-in-google-antigravity
======================================================================
---
slug: gemini-3-1-pro-in-google-antigravity
categories:
  - Product
author: The Antigravity Team
authorTitle: 
date: 2026-02-19T18:19:47.807Z
title: Gemini 3.1 Pro, Building with Advanced Intelligence in Google Antigravity
articleImage: blog/blog-gemini-3-1-pro-wide.png
---

Since we first introduced Google Antigravity, our mission has been to move beyond simple code completion and toward an era of agent-first development. Today, we’re taking a step forward by bringing [Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro) directly into your Antigravity workflow.

Expanding on the Gemini 3 series, 3.1 Pro marks a significant advancement in fundamental reasoning. As a smarter and more adept baseline for intricate problem-solving, 3.1 Pro is built for scenarios where basic responses fall short. It's strong in complex tasks, like workflows that require the model to think through the optimal path for a solution.

## Advanced Reasoning for Complex Workflows

Whether you are refactoring a legacy authentication module or building immersive and interactive data visualizations, Gemini 3.1 Pro works intelligently and efficiently,  thinking more deeply to solve an even wider range of coding problems. 

In Antigravity, this translated intelligence means the agents are more capable of:

- Robust planning: Mapping out a complete architectural plan before touching a single line of code.
- Code-based animation: Generate website-ready animated SVGs from a text prompt built to scale in pure code rather than pixels. 
- Navigating long-horizon tasks across entire codebases while maintaining perfect context.
- Dynamic visualization: Turning high-level concepts into interactive UI components and dynamic data visualizations that improve your user experience.

## Building Real-World Applications

The upgraded reasoning in 3.1 Pro translates directly to higher productivity for developers. To showcase this, we asked Gemini 3.1 Pro to navigate an intricate database migration. It generated a comprehensive risk assessment where it proactively addresses potential data loss by architecting a Local-First sync engine and a robust conflict resolution strategy. This ensures the application remains resilient and user data stays protected throughout the transition:

{{video: https://www.youtube.com/embed/g9XJgXsYkws?si=Wdrd2haIwDE1MMSe, blog/blog-gemini-3-1-pro-wide.png, Gemini 3.1 Pro performing a database migration.}}

We can also see how Gemini 3.1 Pro uses advanced reasoning to transform dense research into functional code. By ingesting complex PDFs directly into Antigravity, the agent translates high-level theory into an interactive Local-First simulation. It successfully architects a CRDT-backed network, complete with real-time sync and connection toggling, bridging the gap between academic papers full of high-level theory and a debugged, interactive web application in a single long-horizon task:

{{video: https://www.youtube.com/embed/xwzcK37kZkM?si=Wdrd2haIwDE1MMSe, blog/blog-gemini-3-1-pro-wide.png, Gemini 3.1 Pro transforming dense research into functional code.}}

## Get Started Today

Gemini 3.1 Pro is now available in the latest version of Google Antigravity.

In addition to Google Antigravity users, Gemini 3.1 Pro is rolling out globally starting today via the Gemini API in [Google AI Studio](https://aistudio.google.com), [Vertex AI](https://cloud.google.com/vertex-ai), [Gemini CLI](https://geminicli.com), and [Android Studio](https://developer.android.com/studio) for developers. 

Experience these new capabilities by selecting Gemini 3.1 Pro in Antigravity:

{{button: Download Antigravity, /download}}


======================================================================
## DOC: [home] home
URL: https://antigravity.google/docs/home
======================================================================
---
slug: home
section: Home
title: Home
path:
  - Home
---

# Google Antigravity

Google Antigravity is an agentic development platform, evolving the IDE into the agent-first era. Antigravity enables developers to operate at a higher, task-oriented level managing agents across workspaces, while retaining a familiar AI IDE experience at its core. Antigravity extracts agents into their own surface and provides them the tools needed to autonomously operate across the editor, terminal, and browser emphasizing verification and higher-level communication via tasks and artifacts. This capability enables agents to plan and execute more complex, end-to-end software tasks, elevating all aspects of development, from building features, UI iteration, and fixing bugs to research and generating reports.

<FeatureBlocks>
name: Main Features
blocks:
- link: /
  icon: automatic_cluster
  title: AI-powered IDE
  description: An AI-powered IDE with all of the AI features that developers have come to rely on such as Agent, Tab, and Command.
- link: /
  icon: automatic_cluster
  title: Asynchronous Agents
  description: Asynchronous, local agents that can work in parallel on all of your workspaces.
- link: /
  icon: automatic_cluster
  title: Agent Manager
  description: New Agent Manager view for an agent-first experience built around planning mode, the conversation UI, and artifact review.
- link: /
  icon: automatic_cluster
  title: Multi-window
  description: A multi-window product with an Editor, Manager, and Browser.
- link: /
  icon: automatic_cluster
  title: Browser Agent
  description: Agent that can actuate the browser for you and to accomplish dev tasks like dashboard reads, SCM actions, UI testing, etc. in the Browser.
</FeatureBlocks>

## Core Surfaces

<IconCardGroup>
- link: /
  icon: automatic_cluster
  title: Editor
  description: A fully-functional AI-powered IDE that maps to a single workspace.
- link: /
  icon: automatic_cluster
  title: Browser
  description: Browser-use agent capabilities to read & actuate on more surfaces beyond just the IDE.
- link: /
  icon: automatic_cluster
  title: Agent Manager
  description: An orchestration “no code” view to start and view tasks in a minimalist product focused on the conversation and artifacts.
</IconCardGroup>

## Key Terms

- **Agent**: The primary AI modality within Antigravity. While the user can work tightly with an Agent within the Editor, they can also have multiple agents working across multiple codebases, orchestrated and monitored through the Agent Manager.
- **Tab & Command**: The other AI modalities within Antigravity, specifically within the text editor part of the editor surface. Tab is a more powerful “autocomplete” and Command is an inline instructive modality. From past experience, these do not get nearly as much use as the Agent.
- **Artifacts**: We define an artifact as anything that the agent creates to allow it to get its work done or communicate its accomplishments to the human user. These include rich markdown files, diff views, architecture diagrams, images, browser recordings, etc.


======================================================================
## DOC: [home] get-started
URL: https://antigravity.google/docs/get-started
======================================================================
---
slug: get-started
section: Home
title: Getting Started
path:
  - Home
  - Getting Started
---

# Getting Started

## Download

Please visit [antigravity.google/download](https://antigravity.google/download) to download Google Antigravity.

<b>Available platforms and minimum versions:</b>
- **macOS**: macOS versions with Apple security update support. This is typically the current and two previous versions. Min Version 12 (Monterey), X86 is not supported
- **Windows**: Windows 10 (64 bit)
- **Linux**: glibc >= 2.28, glibcxx >= 3.4.25 (e.g. Ubuntu 20. Debian 10, Fedora 36, RHEL 8)

The application will prompt when updates are available:

![Update Available](assets/image/docs/restart-to-update.png)

## Basic Navigation

The Agent Manager can be opened from the Editor via the button on the top bar or via keyboard shortcut `Cmd + E`:

![Editor Open Agent Manager](assets/image/docs/editor-open-agent-manager.png)

Similarly, from the Agent Manager, the Editor can be opened from any workspace via the “Focus Editor” option in the workspace’s drop down. When focused on a workspace, the Editor can be opened from any of the “Open Editor” buttons, or via the keyboard shortcut `Cmd + E`.

![Agent Manager Open Editor](assets/image/docs/agent-manager-open-editor.png)


======================================================================
## DOC: [home] firebase-studio-migration
URL: https://antigravity.google/docs/firebase-studio-migration
======================================================================
---
title: Firebase Studio Migration
slug: firebase-studio-migration
path:
  - Home
  - Firebase Studio Migration
---

# Firebase Studio Migration

Antigravity is Google's next-generation, agent-first platform. It’s designed to be the primary home for high-velocity, autonomous development workflows. Instead of relying on just a cloud-based web editor, Antigravity brings the power of AI right into your local development environment.

## Why Antigravity?

Antigravity offers significant enhancements over the web-based Code view in Firebase Studio:

- **Local environment control**: Antigravity runs locally on your machine, which means you have full control over your filesystem, versions, and terminal.
- **True agentic development**: Move beyond basic code completion. Antigravity provides agentic development workflows that can autonomously format, test, and implement entire tasks across your codebase.
- **Seamless Firebase support**: You can still easily deploy your projects to Firebase, communicate with Firebase services via the Firebase CLI, and test your functions locally as you always have.

## Learn how to navigate Antigravity

To help you settle in, here is where you can find your favorite Firebase Studio features in Antigravity:

<IconCardGroup>
- link: /docs/editor
  icon: code
  title: Cloud IDE Code view
  description: Enjoy the familiar interface of VS Code, but supercharged with AI and running locally on your hardware.
- link: /docs/agent
  icon: auto_awesome
  title: Agentic chat
  description: The AI chat you used in Firebase Studio is now natively integrated into your IDE, capable of taking autonomous actions across your local files.
- link: /docs/tools
  icon: rocket_launch
  title: App Hosting deployments
  description: You can continue to deploy and manage your App Hosting URLs seamlessly using the Firebase CLI or built-in IDE integrations.
- link: /docs/browser
  icon: important_devices
  title: Browser-based emulators
  description: Run the Firebase Local Emulator Suite directly on your machine for faster, offline testing.
</IconCardGroup>

## Migrate your Firebase Studio project to Antigravity

Antigravity is a local, agent-first IDE that brings the power of AI into your local development environment.

### Prerequisites

Ensure you have the following installed locally and fully up-to-date:

- [Google Antigravity IDE](https://antigravity.google/download)
- [Node.js](https://nodejs.org/en) (version 20 or higher)
- [Firebase CLI](https://firebase.google.com/docs/cli) (version 15.10.0 or higher)

### Step 1: Export and initialize your app

**Option 1: Automated migration**

This workflow uses the Antigravity agent to autonomously handle project transformation.

1. In Firebase Studio, click the **Move now** button at the top of your workspace.
2. Follow the export method based on the window that appears:
   - If you see a **Zip and Download** button, click it.
   - Otherwise, open the command palette (`Cmd` + `Shift` + `P` on Mac or `Ctrl` + `Shift` + `P` on ChromeOS, Windows, or Linux) and run the **Firebase Studio: Zip & Download** command.
3. Extract the folder locally and open it in Antigravity.
4. In the Agent pane within Antigravity, enter the following prompt. To optimize your workflow and conserve tokens, we recommend selecting the **Gemini Flash** model. It’s designed for speed and efficiency in high-volume transformation tasks like file conversion.

```
@fbs-to-agy-export
```

   The Antigravity agent will then begin project migration, requesting your assistance along the way. Follow the agent’s guidance to complete the migration process. If you encounter any errors, prompt the agent to try again.

<Announcement>
icon: info
color: "#f5f5f5"
iconColor: "#4285f4"
text: "If the download window doesn’t appear, check your browser’s address bar for a pop-up blocker icon and ensure pop-ups are allowed."
</Announcement>

**Option 2: Manual export**

If you prefer to manage the migration yourself without using AI tokens, you can use the Firebase CLI to manually export your project. This method is direct and does not require agent interaction.

Open your terminal and run the following command, replacing `<path>` with the file path to your extracted project folder or the original `.zip` file:

```bash
npx firebase-tools@latest studio:export <path>
```

<Announcement>
icon: warning
color: "#fff8e1"
iconColor: "#f9ab00"
text: "The <code>studio:export</code> command is currently optimized for Next.js, Flutter, and Angular workspaces. While you can use this command for other workspace types, the migration may not be fully successful. We’re actively working to improve the migration flow."
</Announcement>

### Step 2: Preview your app

Once you have extracted your project and opened it within Antigravity, you can view your application locally:

1. In Antigravity, navigate to the **Run and Debug** menu located in the left sidebar.
2. Click the play button to start your local development server.
3. Follow the instructions in the terminal to preview your app.

<Announcement>
icon: lightbulb
color: "#f5f5f5"
iconColor: "#4285f4"
text: "To refine your app or troubleshoot issues, simply chat with the agent using natural language. If the agent pane is hidden, click the Toggle Agent icon at the top of the window to reopen it."
</Announcement>

### Step 3: Publish your app

Antigravity uses agent skills to publish your app using Firebase best practices.

1. In the chat panel, enter the following prompt: simply instruct the agent:

```
Publish my app
```

2. When prompted to run `firebase deploy`, choose **Yes**. The agent will publish to your existing URL if you’ve previously published to App Hosting. If this is your first time publishing to App Hosting, the agent will walk you through the process.
3. For future updates, simply instruct the agent to `publish my app` in the Antigravity chat panel.

## Continue your work

There are several ways you can continue your development in Antigravity.

- **Running workflows:** In Antigravity, you can seamlessly execute workflows and continue your work with the model by typing `@workflows <workflow_name>` into the agentic chat panel.
- **App Hosting deployments:** You can seamlessly deploy your apps directly through the agent using agent skills, or by using the platform-agnostic Firebase CLI and GitHub.
- **Troubleshooting:** If you experience deployment issues, try re-authenticating with the Firebase CLI or verifying your project secrets.

Thank you for being part of the Firebase Studio journey. Your prototypes and feedback have directly shaped Google's AI tools, and we can’t wait to see what you build next in Antigravity!

## Need help?

File any migration bugs in our [GitHub Issues](https://github.com/firebase/firebase-tools/issues).


======================================================================
## DOC: [agent] agent
URL: https://antigravity.google/docs/agent
======================================================================
---
slug: agent
section: Agent
title: Agent
path:
  - Agent
---

# Agent

The Agent is the main AI functionality within Google Antigravity. It is a multi-step reasoning system powered by a frontier LLM that can reason over your existing code, use a wide range of tools (including the browser), and communicate with the user through tasks, artifacts, and more.

## Core Components

- Reasoning model
- Tools
- Artifacts
- Knowledge

## Customizations

- Agent Modes / Settings
- MCP
- Rules / Workflows

You can spin up multiple Agent conversations, including in parallel. Deleting an Agent conversation via “Right Click > Delete Conversation” in the Agent Manager or by clicking the trash icon in the Editor’s Agent panel.


======================================================================
## DOC: [agent] models
URL: https://antigravity.google/docs/models
======================================================================
---
slug: models
section: Agent
title: Models
path:
  - Agent
  - Models
---

# Models

## Reasoning Model

For the core reasoning model, Antigravity offers leading frontier models from the Google Vertex Model Garden:

- Gemini 3.1 Pro (high)
- Gemini 3.1 Pro (low)
- Gemini 3 Flash
- Claude Sonnet 4.6 (thinking)
- Claude Opus 4.6 (thinking)
- GPT-OSS-120b

Users can select which reasoning model they want to use within the model selector drop down under the conversation prompt box:

![Model Selector Drop Down](/assets/image/docs/model-selector.png)

The choice of reasoning model is sticky between user messages within a conversation, so if you change the reasoning model while the Agent is running, it will continue to use the previously selected reasoning model until it has completed its steps for that user turn (or until the user cancels the current execution).

Learn more about reasoning model rate limits in [our plans page](/docs/plans).

## Additional Models

Antigravity uses a number of other models for various parts of the stack that are not customizable:

- **Nano Banana Pro 2**: Used by the generative image tool when the Agent wants to produce a UI mockup, needs images to populate a web page or application, generate system or architecture diagrams, or other generative image tasks.
- **Gemini 2.5 Pro UI Checkpoint**: Used by the [browser subagent](/docs/browser-subagent) to actuate the browser, such as clicking, scrolling, or filling in input.
- **Gemini 2.5 Flash**: Used in the background for checkpointing and context summarization.
- **Gemini 2.5 Flash Lite**: Used by the codebase semantic search tool.


======================================================================
## DOC: [agent] agent-modes-settings
URL: https://antigravity.google/docs/agent-modes-settings
======================================================================
---
slug: agent-modes-settings
section: Agent
title: Agent Modes / Settings
path:
  - Agent
  - Agent Modes / Settings
---

# Agent Modes / Settings

## Conversation-Level

When starting a new Agent conversation, users can choose between multiple modes:

- Planning: Agent can plan before executing tasks. Use for deep research, complex tasks, or collaborative work. In this mode, the Agent organizes its work in [task groups](/docs/task-groups), produces [Artifacts](/docs/artifacts), and takes other steps to thoroughly research, think through, and plan its work for optimal quality.
- Fast: Agent will execute tasks directly. Use for simple tasks that can be completed faster, such as renaming variables, kicking off a few bash commands, or other smaller, localized tasks. This is helpful for when speed is an important factor, and the task is simple enough that there is low worry of worse quality.

## Overall Settings

Settings across every Agent conversation can be found in the “Agent” tab of the Settings pane. Some of the major ones include:

### Artifact Review Policy

These are the possible options for Artifact Review Policy:
- Always Proceed: Agent never asks for review
- Request Review: Agent always asks for review

When Agent decides to request review from the user for implementation plans, this policy determines what the agent does. When set to “Request Review”, the agent will always terminate after notifying, allowing the user to spend time reviewing the plan and adding comments to augment proposed changes. 

![Settings Review Policy Proceed](assets/image/docs/agent/settings-review-policy-proceed.png)

If you do not need to manually review Agent’s plan before making changes, set this to “Always Proceed”, in which case every time the agent decides to request review from the user, it will then immediately continue with executing the plan. 

![Settings Review Policy Manual](assets/image/docs/agent/settings-review-policy-manual.png)

### Terminal Command Auto Execution

For the terminal command generation tool:

- Request Review: Never auto-execute terminal commands (except those in a configurable Allow list)
- Always Proceed: Agent never asks for review (except those in a configurable Deny list)

### Agent Non-Workspace File Access

Allow Agent to view and edit files outside of the current workspace. By default, the Agent only has access to the files in the workspace and in the application’s root folder `~/.antigravity/`, which contains [Artifacts](docs/artifacts), [Knowledge Items](docs/knowledge), and other Antigravity-specific data.

Use with caution, as this could expose local secret or sensitive data to the Agent.


======================================================================
## DOC: [agent] permissions
URL: https://antigravity.google/docs/permissions
======================================================================
---
slug: agent-permissions
section: Agent
title: Agent Permissions
path:
  - Agent
---

# Agent Permissions

Antigravity uses a unified permission system to control what actions the Agent can perform on your behalf. Every action is represented as a **permission resource** that can be placed into one of three lists:

-   **Allow**: The action is auto-approved without prompting.
-   **Deny**: The action is blocked immediately.
-   **Ask**: The Agent pauses and asks for your approval before proceeding.

## Resource String Format

Every entry in the Allow, Deny, or Ask list follows the format:

```
action(target)
```

Where `action` is one of the supported action types and `target` is a pattern describing what the permission covers.

### Supported Actions

| Action | Target Format | Matching |
| :--- | :--- | :--- |
| `command` | `command(prefix)` or `command(*)` | Matches commands by prefix. `command(git)` matches `git add`, `git commit`, etc. |
| `read_file` | `read_file(/path)` | Matches the file or everything under the directory. Paths must be literal and absolute. Globs (`*.go`), regex, and `~` are not supported. |
| `write_file` | `write_file(/path)` | Same as `read_file`. Also implicitly covers `read_file` for the same path. |
| `read_url` | `read_url(domain)` or `read_url(*)` | Matches the domain and all subdomains. Does not match URL paths. |
| `mcp` | `mcp(server/tool)`, `mcp(server/*)`, or `mcp(*)` | Matches by exact server name. `server/*` covers all tools on that server. |

### Examples

**Allow list** — these actions run without prompting:

```text
command(git)                       # Any git command
command(npm run build)             # Build commands
read_file(/home/user/project)      # Read anything in the project
write_file(/home/user/project/src) # Edit files under src/
read_url(example.com)              # Fetch any public page
mcp(workspace/*)                   # All workspace tools
```

**Deny list** — these actions are always blocked:

```text
command(rm)                        # No rm commands
command(sudo)                      # No sudo
write_file(/home/user/.ssh)        # No writes to .ssh
```

**Ask list** — the Agent pauses and asks before proceeding:

```text
command(*)                         # Prompt for every command
mcp(*)                             # Prompt for every MCP tool call
```


======================================================================
## DOC: [agent] rules-workflows
URL: https://antigravity.google/docs/rules-workflows
======================================================================
---
slug: rules-workflows
section: Agent
title: Rules / Workflows
path:
  - Agent
  - Rules / Workflows
---

# Rules

Rules are manually defined constraints for the Agent to follow, at both the local and global levels. Rules allow users to guide the agent to follow behaviors particular to their own use cases and style.

To get started with Rules:
1. Open the Customizations panel via the "..." dropdown at the top of the editor's agent panel.
2. Navigate to the Rules panel.
3. Click **+ Global** to create new Global Rules, or **+ Workspace** to create new Workspace-specific rules.

A Rule itself is simply a Markdown file, where you can input the constraints to guide the Agent to your tasks, stack, and style.

Rules files are limited to 12,000 characters each.

## Global Rules

Global rules live in ~/.gemini/GEMINI.md and are applied across all workspaces.

## Workspace Rules

Workspace rules live in the .agents/rules folder of your workspace or git root.

At the rule level you can define how a rule should be activated:

- Manual: The rule is manually activated via at mention in Agent’s input box.
- Always On: The rule is always applied.
- Model Decision: Based on a natural language description of the rule, the model decides whether to apply the rule.
- Glob: Based on the glob pattern you define (e.g., *.js, src/**/*.ts), the rule will be applied to all files that match the pattern.

Note: Antigravity now defaults to .agents/rules, but still maintains backward support for .agent/rules. 

## @ Mentions

You can reference other files using @filename in a Rules file. If filename is a relative path, it will be interpreted relative to the location of the Rules file. If filename is an absolute path, it will be resolved as a true absolute path, otherwise it will be resolved relative to the repository. For example, @/path/to/file.md will first attempt to be resolved to /path/to/file.md, and if that file does not exist, it will be resolved to workspace/path/to/file.md.

# Workflows

Workflows enable you to define a series of steps to guide the Agent through a repetitive set of tasks, such as deploying a service or responding to PR comments. These Workflows are saved as markdown files, allowing you to have an easy repeatable way to run key processes. Once saved, Workflows can be invoked in Agent via a slash command with the format /workflow-name.

While Rules provide models with guidance by providing persistent, reusable context at the prompt level, Workflows provide a structured sequence of steps or prompts at the trajectory level, guiding the model through a series of interconnected tasks or actions.

To create a workflow:

1. Open the Customizations panel via the "..." dropdown at the top of the editor's agent panel.
2. Navigate to the Workflows panel.
3. Click the **+ Global** button to create a new global workflow that can be accessed across all your workspaces, or click the **+ Workspace** button to create a workflow specific to your current workspace.

To execute a workflow, simply invoke it in Agent using the /workflow-name command. You can call other Workflows from within a workflow! For example, /workflow-1 can include instructions like “Call /workflow-2” and “Call /workflow-3”. Upon invocation, Agent sequentially processes each step defined in the workflow, performing actions or generating responses as specified.

Workflows are saved as markdown files and contain a title, a description and a series of steps with specific instructions for Agent to follow. Workflow files are limited to 12,000 characters each.

## Agent-Generated Workflows

You can also ask Agent to generate Workflows for you! This works particularly well after manually working with Agent through a series of steps since it can use the conversation history to create the Workflow.


======================================================================
## DOC: [agent] skills
URL: https://antigravity.google/docs/skills
======================================================================
---
title: Skills
slug: skills
path: ['Agent', 'Skills']
---

# Agent Skills

Skills are an [open standard](https://agentskills.io/home) for extending agent capabilities. A skill is a folder containing a `SKILL.md` file with instructions that the agent can follow when working on specific tasks.

## What are skills?

Skills are reusable packages of knowledge that extend what the agent can do. Each skill contains:

- **Instructions** for how to approach a specific type of task  
- **Best practices** and conventions to follow  
- **Optional scripts and resources** the agent can use

When you start a conversation, the agent sees a list of available skills with their names and descriptions. If a skill looks relevant to your task, the agent reads the full instructions and follows them.

## Where skills live

Antigravity supports two types of skills:

| Location | Scope |
| :---- | :---- |
| `<workspace-root>/.agents/skills/<skill-folder>/` | Workspace-specific |
| `~/.gemini/antigravity/skills/<skill-folder>/` | Global (all workspaces) |

**Workspace skills** are great for project-specific workflows, like your team's deployment process or testing conventions.

**Global skills** work across all your projects. Use these for personal utilities or general-purpose tools you want everywhere.

Note: Antigravity now defaults to .agents/skills, but still maintains backward support for .agent/skills. 

## Creating a skill

To create a skill:

1. Create a folder for your skill in one of the skill directories  
2. Add a `SKILL.md` file inside that folder

```
.agents/skills/
└─── my-skill/
    └─── SKILL.md
```

Every skill needs a `SKILL.md` file with YAML frontmatter at the top:

```
---
name: my-skill
description: Helps with a specific task. Use when you need to do X or Y.
---

# My Skill

Detailed instructions for the agent go here.

## When to use this skill

- Use this when...
- This is helpful for...

## How to use it

Step-by-step guidance, conventions, and patterns the agent should follow.
```

### Frontmatter fields

| Field | Required | Description |
| :---- | :---- | :---- |
| `name` | No | A unique identifier for the skill (lowercase, hyphens for spaces). Defaults to the folder name if not provided. |
| `description` | Yes | A clear description of what the skill does and when to use it. This is what the agent sees when deciding whether to apply the skill. |

Tip: Write your description in third person and include keywords that help the agent recognize when the skill is relevant. For example: "Generates unit tests for Python code using pytest conventions."

## Skill folder structure

While `SKILL.md` is the only required file, you can include additional resources:

```
.agents/skills/my-skill/
├─── SKILL.md       # Main instructions (required)
├─── scripts/       # Helper scripts (optional)
├─── examples/      # Reference implementations (optional)
└─── resources/     # Templates and other assets (optional)
```

The agent can read these files when following your skill's instructions.

## How the agent uses skills

Skills follow a **progressive disclosure** pattern:

1. **Discovery**: When a conversation starts, the agent sees a list of available skills with their names and descriptions  
2. **Activation**: If a skill looks relevant to your task, the agent reads the full `SKILL.md` content  
3. **Execution**: The agent follows the skill's instructions while working on your task

You don't need to explicitly tell the agent to use a skill—it decides based on context. However, you can mention a skill by name if you want to ensure it's used.

## Best practices

### Keep skills focused

Each skill should do one thing well. Instead of a "do everything" skill, create separate skills for distinct tasks.

### Write clear descriptions

The description is how the agent decides whether to use your skill. Make it specific about what the skill does and when it's useful.

### Use scripts as black boxes

If your skill includes scripts, encourage the agent to run them with `--help` first rather than reading the entire source code. This keeps the agent's context focused on the task.

### Include decision trees

For complex skills, add a section that helps the agent choose the right approach based on the situation.

## Example: A code review skill

Here's a simple skill that helps the agent review code:

```
---
name: code-review
description: Reviews code changes for bugs, style issues, and best practices. Use when reviewing PRs or checking code quality.
---

# Code Review Skill

When reviewing code, follow these steps:

## Review checklist

1. **Correctness**: Does the code do what it's supposed to?
2. **Edge cases**: Are error conditions handled?
3. **Style**: Does it follow project conventions?
4. **Performance**: Are there obvious inefficiencies?

## How to provide feedback

- Be specific about what needs to change
- Explain why, not just what
- Suggest alternatives when possible
```



======================================================================
## DOC: [agent] task-groups
URL: https://antigravity.google/docs/task-groups
======================================================================
---
slug: task-groups
section: Agent
title: Task Groups
path:
  - Agent
  - Task Groups
---

# Task Groups

When Agent is in planning mode, large and complex tasks  are handled with Task Groups, which break down these problems into smaller, more approachable units of work. Oftentimes, Agent will work on multiple parts of the greater task at the same time, and task sections are how these changes are presented to the user. Here is an example task group.

![Task Group](assets/image/docs/agent/task-group.png)

The top component of the task group specifies the overarching goal of this task as well as summarizes the changes made within this unit of work. There is also a section of edited files for quick user audit of changes: click on the file pill and you will view the current state of the changed files.

![Task Group Clicked Pill](assets/image/docs/agent/task-group-clicked-pill.png)

Within a task group, Agent identifies subtasks that help modularize necessary changes, and all work done by the Agent is viewable within these progress update sections. By default, the details in each subtask are not directly exposed to the user, but if you are interested, there is a toggle that will expand on the exact steps that Agent made.

![Task Group Expanded](assets/image/docs/agent/task-group-expanded.png)

Sometimes, there are pending steps, such as browser setup or terminal commands requiring approval, that are created inside these progress updates. In this case, instead of expanding all of the updates, Agent provides a special section at the end of the task group where you can review these pending steps accordingly.

![Task Group Pending](assets/image/docs/agent/task-group-pending.png)


======================================================================
## DOC: [agent] browser-subagent
URL: https://antigravity.google/docs/browser-subagent
======================================================================
---
slug: browser-subagent
section: Agent
title: Browser Subagent
path:
  - Agent
  - Browser Subagent
---

# Browser Subagent

When the agent wants to interact with the browser, it invokes a browser subagent to handle the task at hand. The browser subagent runs a model specialized to operate on the pages that are open within the Antigravity-managed browser, which is different from the model you selected for the main agent.

This subagent has access to a variety of tools that are necessary to control your browser, including clicking, scrolling, typing, reading console logs, and more. It can also read your open pages through DOM capture, screenshots, or markdown parsing, as well as taking videos.

While the agent is controlling a page, it will show an overlay on the page with a blue border and a small panel with short descriptions of the actions being taken. When this is shown, you will not be allowed to interact with the page to ensure it doesn’t get confused by your actions.

The browser subagent can act on tabs that are not focused, so you are free to open other tabs and use them uninterrupted as it works.



======================================================================
## DOC: [agent] strict-mode
URL: https://antigravity.google/docs/strict-mode
======================================================================
---
slug: strict-mode
section: Agent
title: Strict Mode
path:
  - Agent
  - Strict Mode
---

# Strict Mode

Strict mode provides enhanced security controls for the Agent, allowing you to restrict its access to external resources and sensitive operations. When strict mode is enabled, several security measures are enforced to protect your environment.

## Features

### Browser URL Allowlist/Denylist

In strict mode, the Agent's ability to interact with external websites is governed by the browser's Allowlist and Denylist. This applies to:
- **External Markdown Images**: The Agent will only render images from URLs that are allowed.
- **Read URL Tool**: The Read URL tool will only auto-execute for allowed URLs.

### Terminal, Browser, and Artifact Review Policies

Strict mode enforces the following behavior for terminal, browser, and artifact interactions:
- **Terminal Auto Execution**: Set to "Request Review". The Agent will always prompt for permission before executing any terminal command. The terminal allowlist is ignored when strict mode is enabled.
- **Browser Javascript Execution**: Set to "Request Review". The Agent will always prompt for permission before executing Javascript in the browser.
- **Artifact Review**: Set to "Request Review". The Agent will always prompt for confirmation before acting on plans laid out in artifacts.

### File System Access

Strict mode restricts the Agent's access to the file system to ensure it only interacts with authorized files:
- **Respect .gitignore**: The Agent will respect `.gitignore` rules, preventing it from accessing ignored files.
- **Workspace Isolation**: Access to files outside the workspace is disabled. The Agent can only view and edit files within the designated workspace.


======================================================================
## DOC: [agent] sandbox-mode
URL: https://antigravity.google/docs/sandbox-mode
======================================================================
---
slug: sandbox-mode
section: Agent
title: Sandboxing Terminal Commands
path:
  - Agent
  - Sandboxing
---

# Sandboxing Terminal Commands

Sandboxing provides kernel-level isolation for terminal commands executed by the Agent. When enabled, commands run in a restricted environment with limited file system and network access, protecting your system from unintended modifications.

Sandboxing is currently disabled by default, but this may change in future releases. It is supported on macOS and Linux. On macOS, it leverages Seatbelt (`sandbox-exec`), Apple's kernel-level sandboxing mechanism. On Linux, it uses `nsjail` for process isolation.

## Enabling Sandboxing

You can enable or disable sandboxing in Antigravity User Settings. Toggle "Enable Terminal Sandboxing" to turn sandboxing on or off. When enabled, you can also control network access separately using the "Sandbox Allow Network" toggle.

![Sandbox settings toggles](/assets/image/docs/sandbox-settings-toggle.png)

## Restrictions

When sandboxing is enabled, the Agent's terminal commands are subject to the following restrictions:

- **File System**: Commands can only write to your designated workspace directory and essential system locations. This prevents the Agent from accidentally deleting or modifying files outside your project.

  ![File system operation blocked by sandbox](/assets/image/docs/sandbox-filesystem-denied.png)

- **Network Access**: Network connectivity can be independently controlled. Use the "Sandbox Network Access" toggle in Antigravity User Settings to allow or deny network access while maintaining file system restrictions.

Here's an example of a command being blocked due to network restrictions:

![Sandbox network denial example](/assets/image/docs/sandbox-network-denied.png)

## Handling Sandbox Violations

If a command fails due to sandbox restrictions, you'll see a message indicating the failure may be sandbox-related. To resolve this, you can:

- **Disable Sandbox Permanently**: Turn off sandboxing entirely in Antigravity User Settings.
- **Bypass for a Single Command**: When using "Request Review" mode, you can choose to run an individual command with or without sandbox restrictions.

In "Request Review" mode, you'll see a "Bypass Sandbox" option when prompted to run a command:

![Bypass Sandbox option in Request Review mode](/assets/image/docs/sandbox-bypass-option.png)

## Interaction with Strict Mode

When strict mode is enabled, sandboxing is automatically activated with network access denied. This ensures maximum protection when operating in a strict environment.

![Sandbox settings in strict mode](/assets/image/docs/sandbox-secure-mode-settings.png)


======================================================================
## DOC: [tools] mcp
URL: https://antigravity.google/docs/mcp
======================================================================
---
slug: mcp
section: Tools
title: MCP
path:
  - Tools
  - MCP
---

# Antigravity Editor: MCP Integration

Antigravity supports the Model Context Protocol (MCP), a standard that allows the editor to securely connect to your local tools, databases, and external services. This integration provides the AI with real-time context beyond just the files open in your editor.

## What is MCP?

MCP acts as a bridge between Antigravity and your broader development environment. Instead of manually pasting context (like database schemas or logs) into the editor, MCP allows Antigravity to fetch this information directly when needed.

## Core Features

### 1. Context Resources

The AI can read data from connected MCP servers to inform its suggestions.

**Example:** When writing a SQL query, Antigravity can inspect your live Neon or Supabase schema to suggest correct table and column names.

**Example:** When debugging, the editor can pull in recent build logs from Netlify or Heroku.

### 2. Custom Tools

MCP enables Antigravity to execute specific, safe actions defined by your connected servers.

**Example:** "Create a Linear issue for this TODO."

**Example:** "Search Notion or GitHub for authentication patterns."

## How to Connect

Connections are managed directly through the built-in MCP Store.

1. **Access the Store:** Open the MCP Store panel within the "..." dropdown at the top of the editor's side panel.
2. **Browse & Install:** Select any of the supported servers from the list and click Install.
3. **Authenticate:** Follow the on-screen prompts to securely link your accounts (where applicable).

Once installed, resources and tools from the server are automatically available to the editor.

## Connecting Custom MCP Servers

To connect to a custom MCP server:

1. Open the MCP store via the "..." dropdown at the top of the editor's agent panel.
2. Click on "Manage MCP Servers"
3. Click on "View raw config"
4. Modify the mcp_config.json with your custom MCP server configuration.

The configuration file is located at `~/.gemini/antigravity/mcp_config.json`.

### Configuration Structure

The configuration file has a single `mcpServers` object where you define each server you want to connect to.

```json
{
  "mcpServers": {
    "serverName": {
      "command": "path/to/executable",
      "args": ["--arg1", "value1"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

### Configuration Properties

Each server entry supports the following properties:

**Transport (one required):**

- **`command`** (string): Path to the executable for stdio transport.
- **`serverUrl`** (string): URL for remote servers for Streamable HTTP transport.

**Optional:**

- **`args`** (string[]): Command-line arguments for stdio transport.
- **`env`** (object): Environment variables for the stdio server process.
- **`cwd`** (string): Working directory for stdio servers.
- **`headers`** (object): Custom HTTP headers for remote servers.
- **`authProviderType`** (string): Authentication provider. Supports `"google_credentials"` for ADC.
- **`oauth`** (object): OAuth client credentials (`clientId`, `clientSecret`).
- **`disabled`** (boolean): Temporarily disable a server without removing its configuration.
- **`disabledTools`** (string[]): Tool names to not provide to the model.

## Authentication

### Google Credentials

Set `authProviderType` to `"google_credentials"` to use Google Application Default Credentials (ADC).

```json
{
  "mcpServers": {
    "my-gcp-service": {
      "serverUrl": "https://example.googleapis.com/mcp/",
      "authProviderType": "google_credentials"
    }
  }
}
```

This requires Application Default Credentials to be configured. To set them up, run:

```bash
gcloud auth application-default login
```

### OAuth

Antigravity can automatically handle OAuth for servers that support dynamic client registration (DCR). For these servers, no additional configuration is needed:

```json
{
  "mcpServers": {
    "oauth-server": {
      "serverUrl": "https://api.example.com/mcp/"
    }
  }
}
```

If the server does not support dynamic client registration, you can provide your client credentials manually:

```json
{
  "mcpServers": {
    "oauth-server": {
      "serverUrl": "https://api.example.com/mcp/",
      "oauth": {
        "clientId": "your-client-id",
        "clientSecret": "your-client-secret"
      }
    }
  }
}
```

If you provided client credentials manually, ensure the following is registered as a redirect URI in your OAuth provider:

```
https://antigravity.google/oauth-callback
```

When connecting to an OAuth-enabled server:

1. Open **Agent Settings** with `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux).
2. Navigate to the **Customizations** tab and click the **Authenticate** button next to the server.

![Click Authenticate](assets/image/docs/tools/mcp-oauth-authenticate.png)

3. Complete authentication in your browser and copy the authorization code.

![Copy authorization code](assets/image/docs/tools/mcp-oauth-copy-code.png)

4. Paste the code back into the settings panel and click **Submit**.

![Paste auth code](assets/image/docs/tools/mcp-oauth-paste-code.png)

Once authenticated, the server will reconnect automatically.

![Authenticated server](assets/image/docs/tools/mcp-oauth-authenticated.png)

Access tokens are stored in `~/.gemini/antigravity/mcp_oauth_tokens.json`. Expired tokens are refreshed automatically, and invalid tokens are removed.

### Custom Headers

For servers that require custom HTTP headers (e.g. API keys or bearer tokens), add them to the `headers` object. For example:

```json
{
  "mcpServers": {
    "my-remote-server": {
      "serverUrl": "https://api.example.com/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

## Supported Servers

The MCP Store currently features integrations for:

- Airweave
- Arize
- AlloyDB for PostgreSQL
- Atlassian
- BigQuery
- Chrome DevTools
- ClickHouse
- Cloud SQL for PostgreSQL
- Cloud SQL for MySQL
- Cloud SQL for SQL Server
- Dart
- Dataplex
- Figma Dev Mode MCP
- Firebase
- GitHub
- Harness
- Heroku
- Linear
- Locofy
- Looker
- MCP Toolbox for Databases
- MongoDB
- Neon
- Netlify
- Notion
- PayPal
- Perplexity Ask
- Pinecone
- Postman
- Prisma
- Redis
- Sequential Thinking
- SonarQube
- Spanner
- Stripe
- Supabase


======================================================================
## DOC: [artifacts] artifacts
URL: https://antigravity.google/docs/artifacts
======================================================================
---
slug: artifacts
section: Artifacts
title: Artifacts
path:
  - Artifacts
---

# Artifacts

We define an Artifact as anything that the agent creates to allow it to get its work done or communicate its work and thinking to the human user. These include rich markdown files, diff views, architecture diagrams, images, browser recordings, code diffs, etc. As Agents become more autonomous and can run for longer and longer periods, Artifacts allow for the Agent to asynchronously communicate its work to the user, as opposed to requiring the user to carefully monitor every Agent step synchronously.

Artifacts are produced while the Agent is in [Planning mode](/docs/agent-modes-settings), and appear in both the [Agent Manager](/docs/agent-manager) and [Editor](/docs/editor) views, though the former is optimized for displaying, organizing, and managing Artifacts.

Feedback is another key concept with Artifacts. Depending on the user settings, the Agent may ask for review on intermediate Artifacts to receive confirmation that it has made progress in its thinking or implementation that aligns with the user’s intent and goal. The user is able to provide feedback on the Artifact to provide guidance to steer the Agent in the proper direction. The UI/UX of feedback differs from Artifact type to Artifact type.


======================================================================
## DOC: [artifacts] task-list
URL: https://antigravity.google/docs/task-list
======================================================================
---
slug: task-list
section: Artifacts
title: Task List
path:
  - Artifacts
  - Task List
---

# Task List

A task list is an artifact that the agent uses to approach complex tasks and monitor progress on various action items. You can find a live snapshot of what the agent is doing in this artifact, which is constructed as a markdown list of items related to research, implementation, verification, and more. This type of artifact is generally used by the agent to keep on track with the user’s overarching goal; typically, you do not need to directly interact with this artifact.

![Task List](assets/image/docs/artifacts/artifact-task.png)


======================================================================
## DOC: [artifacts] implementation-plan
URL: https://antigravity.google/docs/implementation-plan
======================================================================
---
slug: implementation-plan
section: Artifacts
title: Implementation Plan
path:
  - Artifacts
  - Implementation Plan
---

# Implementation Plan

Agent utilizes the implementation plan artifact to architect changes within your codebase to accomplish a task. These plans contain technical details on what revisions are necessary and are meant to be reviewed by the user. Below is an example plan generated by the agent.

![Artifact Implementation Plan](assets/image/docs/artifacts/artifact-implementation-plan.png)

Unless you have you artifact review policy set to “Always Proceed” [link to docs on this setting], Agent will typically request your review on the implementation plan before making the changes needed to complete your task. You can click either the in-conversation or artifact header “Proceed” button to instantly continue with Agent’s plan.

![Artifact Implementation Plan Proceed](assets/image/docs/artifacts/artifact-implementation-plan-proceed.png)

Oftentimes, Agent will create a plan that is slightly different from what you exactly want. Antigravity supports commenting on these artifacts so you can provide feedback to Agent for any reason, whether it be to decrease scope of changes, use a different tech stack, or correct any Agent discrepancies.

![Artifact Implementation Plan Comments](assets/image/docs/artifacts/artifact-implementation-plan-comments.png)
 
Once you have left comments on the implementation plan, you can still use the “Proceed” to continue with Agent’s plan; alternatively, you can also toggle the “Review” button in the artifact header, where you can examine all comments and leave a message as feedback instead of directly proceeding, if needed.

![Artifact Implementation Plan Submit Comments](assets/image/docs/artifacts/artifact-implementation-plan-submit-comments.png)

Once you have proceeded or left a review, Agent will continue its work, either iterating on the implementation plan and re-requesting your review or beginning with its work!

![Artifact Implementation Plan Proceeded](assets/image/docs/artifacts/artifact-implementation-plan-proceeded.png)


======================================================================
## DOC: [artifacts] walkthrough
URL: https://antigravity.google/docs/walkthrough
======================================================================
---
slug: walkthrough
section: Artifacts
title: Walkthrough
path:
  - Artifacts
  - Walkthrough
---

# Walkthrough

Agent creates walkthrough artifacts when it has completed task implementation; this type of artifact includes a concise summary of the changes that have been made to remind the user of what has happened in the active conversation. This is a great way to get up to speed with the state of your codebase after Agent has made its changes in case you were not strictly following it the whole time.

![Walkthrough](assets/image/docs/artifacts/artifact-walkthrough.png)

For browser tasks, walkthroughs often contain screenshots and screen recordings of what Agent has built or created in the browser!

![Walkthrough with Image](assets/image/docs/artifacts/artifact-walkthrough-image.png)


======================================================================
## DOC: [artifacts] screenshots
URL: https://antigravity.google/docs/screenshots
======================================================================
---
slug: screenshots
section: Artifacts
title: Screenshots
path:
  - Artifacts
  - Screenshots
---

# Screenshots

The browser subagent can take screenshots of open pages or elements on pages when it would like your review of the state of the page. This is surfaced as a tool to the agent, and you can also prompt the agent to take a screenshot of a page.

![Browser Screenshot Capture Tool](assets/image/docs/artifacts/browser-screenshot-capture.png)

All screenshots are saved as image artifacts and can be commented on to give feedback to the agent.

![Browser Screenshot Artifact](assets/image/docs/artifacts/browser-screenshot-artifact.png)


======================================================================
## DOC: [artifacts] browser-recordings
URL: https://antigravity.google/docs/browser-recordings
======================================================================
---
slug: browser-recordings
section: Artifacts
title: Browser Recordings
path:
  - Artifacts
  - Browser Recordings
---

# Browser Recordings

Every time the browser subagent actuates on the Browser, it may choose to generate a recording of the agent’s actions for your review. You can view this playback, if it is available, at the bottom of the Browser step UI.

![Browser Recording Capture Tool](assets/image/docs/artifacts/browser-recording-capture.png)

All browser recordings are also saved as a recording artifact for your review. This view loops through the browser agent’s actions.

![Browser Recording Artifact](assets/image/docs/artifacts/browser-recording-artifact.png)


======================================================================
## DOC: [artifacts] knowledge
URL: https://antigravity.google/docs/knowledge
======================================================================
---
slug: knowledge
section: Artifacts
title: Knowledge
path:
  - Artifacts
  - Knowledge
---

# Knowledge

Knowledge Items are Antigravity's persistent memory system that automatically captures and organizes important insights, patterns, and solutions from your coding sessions. They help you build upon previous work across conversations.

## What is a Knowledge Item?

A Knowledge Item is a collection of related information on a specific topic. Each Knowledge Item contains a title and summary describing what it covers, and a collection of artifacts providing information on the topic. Possible examples of artifacts include automatically generated documentation, code examples, or persistent memories of user instructions. 

## How are Knowledge Items Generated?

As you interact with the agent, Antigravity automatically analyzes and extracts information from your conversation and uses that information to create new KIs or update existing KIs. 

## Viewing Knowledge Items

You can view your Knowledge Items in the Antigravity **Agent Manager**.

![Knowledge View](assets/image/docs/artifacts/knowledge-view.png)

## How are Knowledge Items used by the Agent?

The summaries of all your Knowledge Items are available to the agent, which uses them to inform its responses. When the agent identifies a Knowledge Item that is relevant to the conversation, it will automatically study the artifacts in that Knowledge Item and use the applicable information.


======================================================================
## DOC: [editor] editor
URL: https://antigravity.google/docs/editor
======================================================================
---
slug: editor
section: Editor
title: Editor
path:
  - Editor
---

# Editor

The primary entry point to Antigravity is our Editor, a surface based upon the VS Code codebase but full of rich AI-enabled features designed to improve your code-writing experience. 

Much of this editor is designed to feel the same as prior experiences you may have had. You can open files up, tab through them, edit them directly, get suggestions with [Tab](docs/tab), and work with an agent on [smaller](docs/command) or [larger tasks](docs/agent-side-panel). When you’re done, you can review your changes and interface with your preferred [source control](docs/review-changes-editor). You can also still download extensions from the Open VSX marketplace to augment your experience, through further syntax highlighting, source control integrations, or other additions. 

![Editor Screenshot](assets/image/docs/editor/editor.png)

======================================================================
## DOC: [editor] tab
URL: https://antigravity.google/docs/tab
======================================================================
---
slug: tab
section: Editor
title: Tab
path:
  - Editor
  - Tab
---

# Antigravity Editor: Tab & Navigation

This guide covers the core navigation and completion tools: **Supercomplete**, **Tab-to-Jump**, and **Tab-to-Import**.

## Supercomplete

Supercomplete provides code suggestions in a region near your current cursor position.

![Supercomplete](assets/image/docs/editor/supercomplete.png)

### How it Works

- **File-Wide Suggestions**: Suggestions can modify code throughout the document, handling tasks like changing variable names or updating separate function definitions simultaneously.
- **Accepting**: Press `Tab` to accept the changes.

## Tab-to-Jump

Tab-to-Jump is a fluid navigation tool that suggests the next logical place in your document to move your cursor to.

![Tab-to-Jump](assets/image/docs/editor/tab_to_jump.png)

### How it Works

- A "Tab to jump" icon will appear offering to move your cursor to where your next logical edit will be. Pressing `Tab` instantly moves your cursor to that location.
- **Accepting**: Press `Tab` to accept the jump.

## Tab-to-Import

Tab-to-Import handles missing dependencies without breaking your flow.

![Tab-to-Import](assets/image/docs/editor/tab_to_import.png)

### How it Works

- **Detection**: If you type a class or function that isn't imported, Antigravity suggests the import.
- **Action**: Press `Tab` to complete the word and instantly add the import statement to the top of the file.

## Settings

In your settings, you can customize the behavior of these features:
- **Enable/Disable Features**: You can individually turn off Autocomplete, Tab-to-Jump, Supercomplete, or Tab-to-Import.
- **Tab Speed**: Controls the responsiveness of suggestions.
  - `Slow`: Waits for more context before suggesting.
  - `Default`: Offers a balanced pace.
  - `Fast`: Provides rapid-fire suggestions.
- **Highlight Inserted Text**: When enabled, text inserted via Tab is highlighted to track changes easily.
- **Clipboard Context**: When enabled, Antigravity uses the contents of your clipboard to improve completion accuracy.
- **Allow Gitignored Files**: Enables Tab features (suggestions and jumping) within files listed in your `.gitignore` file. Tab will only ignore gitignored files if git is installed.


======================================================================
## DOC: [editor] command
URL: https://antigravity.google/docs/command
======================================================================
---
slug: command
section: Editor
title: Command
path:
  - Editor
  - Command
---

# Antigravity Editor: Command

The **Command** feature brings the power of natural language directly into your workflow, allowing you to request specific inline completions or terminal commands on the fly.

## How it Works
1. **Trigger**: Press `Command + I` (Mac) or `Ctrl + I` (Windows/Linux).
2. **Prompt**: A text input box will appear at your current cursor position.
3. **Instruction**: Type your request in natural language (e.g., "Create a function to sort this list" or "Add error handling to this block").
4. **Execution**: Antigravity generates the code or command directly inline for you to review and accept.

## Where to Use It

### In the Editor

![Command in Editor](assets/image/docs/editor/command_editor.png)

Use Command to generate boilerplate code, refactor complex functions, or write documentation without breaking your coding flow.

* _Example_: "Create a React component for a login form."

### In the Terminal

![Command in Terminal](assets/image/docs/editor/command_terminal.png)

Use Command within the integrated Antigravity terminal to generate complex shell commands without needing to memorize syntax.

* _Example_: "Find all processes listening on port 3000 and kill them."


======================================================================
## DOC: [editor] agent-side-panel
URL: https://antigravity.google/docs/agent-side-panel
======================================================================
---
slug: agent-side-panel
section: Editor
title: Agent Side Panel
path:
  - Editor
  - Agent Side Panel
---

# Agent Side Panel

Use the panel on the right side of the editor to work directly with the agent. You can spin up new conversations, attach images, switch [agent modes](docs/agent-modes-settings), and select between [different models](docs/models). 

![Editor Agent Panel](assets/image/docs/editor/editor_agent_panel.png)

As your conversation progresses, you’ll be able to keep track of open file changes, running terminal processes, and artifacts in the bottom toolbar above the input.

![Editor Agent Panel](assets/image/docs/editor/agent_panel_toolbar.png)


======================================================================
## DOC: [editor] review-changes-editor
URL: https://antigravity.google/docs/review-changes-editor
======================================================================
---
slug: review-changes-editor
section: Editor
title: Review Changes + Source Control
path:
  - Editor
  - Review Changes + Source Control
---

# Review Changes + Source Control

Once the agent has begun writing code within a conversation, you’ll see a `Review Changes` section within the Agent panel’s [bottom toolbar](docs/agent-side-panel). Clicking it will open up a pane within your editor where you can scroll through all of the changes you and your agent made within the conversation. 

![Editor Review Changes](assets/image/docs/editor/review_changes_editor.png)

Just like with artifacts, you can comment on any of the file diffs to communicate with the agent.

![Editor Source Control](assets/image/docs/editor/source_control_editor.png)



======================================================================
## DOC: [agent-manager] agent-manager
URL: https://antigravity.google/docs/agent-manager
======================================================================
---
slug: agent-manager
section: Agent Manager
title: Agent Manager
path:
  - Agent Manager
---

# Agent Manager

We've built out the Agent Manager, to provide a higher level view into the work Antigravity agents are doing under your guidance. Here, you can work across multiple workspaces, oversee dozens of agents simultaneously, and interact with your codebase primarily through the agent, rather than through writing code directly. As agents and models continue to get better, we believe that this birds-eye view will be the primary entry point to all of your work. We expect to move it to be central to the Antigravity experience soon.

At any point, you can toggle between the Agent Manager and the editor by hitting CMD+E (Mac) or CTRL+E (Windows), or through the Open Editor & Open Agent Manager buttons at the top right of the menu bar. You can also manage your editor windows through the manager, either hiding, focusing, or closing them.

![Agent Manager Editor](assets/image/docs/agent_manager_editor.png)


======================================================================
## DOC: [agent-manager] workspaces
URL: https://antigravity.google/docs/workspaces
======================================================================
---
slug: workspaces
section: Agent Manager
title: Workspaces
path:
  - Agent Manager
  - Workspaces
---

# Workspaces

In the Agent Manager, you can work across multiple workspaces simultaneously. In order to open a new workspace, just select the button in the left sidebar and select a starting folder. At any point, you can switch between conversations across workspaces through the left sidebar.

![Switch Workspaces](../../../assets/image/docs/workspaces/switch_workspace.png)

To start a new conversation within a workspace, either select the desired workspace from the Start Conversation tab or hit the Plus button next to the workspace name in the sidebar.

![Start Conversation Within Workspace](../../../assets/image/docs/workspaces/start_within_workspace.png)


======================================================================
## DOC: [agent-manager] playground
URL: https://antigravity.google/docs/playground
======================================================================
---
slug: playground
section: Agent Manager
title: Playground
path:
  - Agent Manager
  - Workspaces
  - Playground
---

# Playground

Playgrounds are independent workspaces that allow you to start a conversation and explore ideas instantly, without the overhead of setting up a new workspace.

## Creating a Playground

From the Start Conversation page, you can quickly send a message to a new playground by clicking the Use Playground button below the input box.

![Playground Button](../../../assets/image/docs/playground/playground_button.png)

From here, you can send a message as you would normally.

![Playground Send Message](../../../assets/image/docs/playground/playground_send.png)

## Persisting Your Work

If you want to keep the work you've done in a playground, you can move its contents into a dedicated workspace in a folder of your choosing. This action preserves your conversation history and any files created during your session, allowing you to continue exploring with multiple conversations.

![Playground Persist](../../../assets/image/docs/playground/playground_persist.png)

Clicking on the move button in the top bar will pop up the following modal:

![Playground Move Modal](../../../assets/image/docs/playground/playground_move.png)


======================================================================
## DOC: [agent-manager] inbox
URL: https://antigravity.google/docs/inbox
======================================================================
---
slug: inbox
section: Agent Manager
title: Inbox
path:
  - Agent Manager
  - Workspaces
  - Inbox
---

# Inbox

The inbox is your one stop shop to track all of your conversations in one place. From the inbox you can see if any of your conversations are awaiting your approval to run terminal commands, use the browser, or build out an implementation plan.

![Inbox Overview](../../../assets/image/docs/inbox/basic_inbox.png)

You can use the search bar and the pending switch to search for conversations by folder or by title to make sure your inbox is always focused on what is most relevant to you.

Selecting a conversation from the inbox will jump directly to the conversation, where you can continue where you left off.

![Continue Conversation](../../../assets/image/docs/inbox/continue_conversation.png)


======================================================================
## DOC: [agent-manager] conversation-view
URL: https://antigravity.google/docs/conversation-view
======================================================================
---
slug: conversation-view
section: Agent Manager
title: Conversation View
path:
  - Agent Manager
  - Conversation View
---

# Conversation View

The [Agent Panel](/docs/agent-side-panel) takes center stage in the agent manager. As the agent makes progress, you'll be able to follow along with what it's doing. To toggle off this follow-along mode, simply hit the `Following` button at the top right of the conversation.

![Follow Along Manager](assets/image/docs/follow_along_manager.png)


======================================================================
## DOC: [agent-manager] browser-subagent-view
URL: https://antigravity.google/docs/browser-subagent-view
======================================================================
---
slug: browser-subagent-view
section: Agent Manager
title: Browser Subagent View
path:
  - Agent Manager
  - Conversation View
  - Browser Subagent View
---

# Browser Subagent View

## Overview

The Manager has a dedicated side panel that allows you to expand and inspect the Agent’s work for a task.

![Browser Subagent View](assets/image/docs/browser-subagent-view.png)

In the regular manager conversation view (left half of the image), the browser subagent’s work is hidden.
Clicking the expand button (shown in red box) will bring up the subagent view (right half of the image). Updates to the Agent’s work will be streamed into this view, so you can follow along and interact with steps as required (e.g. confirm/deny actions).

## What’s in the side panel

- All subagent actions (clicking, scrolling, navigating, etc.)
- Visual feedback showing exactly where clicks happened
- Screenshots captured at each step

## Visual Inspection Feature

Tool calls that produce actions in the browser, like clicks, include a button (shown in blue box) which opens a screenshot of the browser at that exact moment and a red dot showing what interaction the agent has done in the browser.



======================================================================
## DOC: [agent-manager] panes
URL: https://antigravity.google/docs/panes
======================================================================
---
slug: panes
section: Agent Manager
title: Panes
path:
  - Agent Manager
  - Conversation View
  - Panes
---

# Panes

You can open files, [artifacts](/docs/artifacts), knowledge items, and other content directly within the manager in panes that persist per-conversation. In order to open up a pane, simply open up the quick picker (by hitting CMD+P on Mac or CTRL+P on Windows/Linux) and select a resource. You can also hit the "+" from within a conversation's header.

![Manager New Tab](assets/image/docs/agent-manager/manager_new_tab.png)

![Manager File Picker](assets/image/docs/agent-manager/manager_file_picker.png)

These panes are resizable, splittable, and drag-and-droppable. You should configure them around as makes sense for your workflow.

![Manager Split Pane](assets/image/docs/agent-manager/manager_split_pane.png)

If you use CMD+Click or CMD+Enter (Mac) or CTRL+Click / CTRL+Enter (non-Mac), the contents will open in a new pane, rather than replacing the currently open pane.



======================================================================
## DOC: [agent-manager] review-changes-manager
URL: https://antigravity.google/docs/review-changes-manager
======================================================================
---
slug: review-changes-manager
section: Agent Manager
title: Review Changes + Source Control
path:
  - Agent Manager
  - Conversation View
  - Review Changes + Source Control
---

# Review Changes + Source Control

Just as in the [editor](/docs/review-changes-editor), you can easily review the work you and your agent have collaborated on from within the manager.

Once you enter a conversation, you can toggle the Review Changes pane through the button at the top right to open up a pane where you can scroll through and comment on any file diffs made as a part of the conversation.

![Review Changes Manager](assets/image/docs/review_changes_manager.png)

You can similarly toggle to the Source Control tab within the Review Changes pane to see changed files, stage or unstage them, and commit them upstream.

![Manager Source Control](assets/image/docs/manager_source_control.png)


======================================================================
## DOC: [agent-manager] changes-sidebar
URL: https://antigravity.google/docs/changes-sidebar
======================================================================
---
slug: changes-sidebar
section: Agent Manager
title: Changes Sidebar
path:
  - Agent Manager
  - Conversation View
  - Changes Sidebar
---

# Changes Sidebar

Similar to the toolbar at the bottom of the editor's [Agent Panel](docs/agent-side-panel), the Changes Sidebar in the manager offers a quick way to see what [artifacts](docs/artifacts) the agent has created and what files it has modified within a conversation.

Clicking on any of the listed resources will open its contents within a pane. The icons on each resource indicate whether there are new changes to a resource since your last review.

![Aux Sidebar](assets/image/docs/aux-sidebar.png)


======================================================================
## DOC: [browser] allowlist-denylist
URL: https://antigravity.google/docs/allowlist-denylist
======================================================================
---
slug: allowlist-denylist
section: Browser
title: Allowlist / Denylist
path:
  - Browser
  - Allowlist / Denylist
---

# Allowlist / Denylist

The browser uses a two-layer security system to control which URLs can be accessed:
- **Denylist** - Deny dangerous/malicious URLs
- **Allowlist** - Explicitly allow trusted URLs

## How It Works

### Denylist
The denylist is maintained and enforced using the Google Superroots’s BadUrlsChecker service (See documentation).
When the browser attempts to navigate to a URL, the hostname is checked against the server-side denylist via RPC.

**NOTE:** If the server is unavailable, access is denied by default.

### Allowlist

The allowlist is a local text file that you can edit to explicitly trust specific URLs.

![Allowlist](assets/image/docs/browser-allowlist.png)

The allowlist is initialized with just localhost, and can be edited at anytime.

When the browser attempts to navigate to a non-allowlisted URL, it will prompt you with an “always allow” button, which if clicked will add the URL to the allowlist and enable the browser to open and interact with the web page. An example situation is shown below:

![Always Allow](assets/image/docs/always-allow-url.png)

You can also add/remove URLS from the allowlist manually. However, the denylist always takes precedence: you cannot allowlist a URL that appears on the denylist.


======================================================================
## DOC: [browser] separate-chrome-profile
URL: https://antigravity.google/docs/separate-chrome-profile
======================================================================
---
slug: separate-chrome-profile
section: Browser
title: Separate Chrome Profile
path:
  - Browser
  - Separate Chrome Profile
---

# Separate Chrome Profile

To isolate the browser from your general browsing, it operates on a [separate Chrome profile](https://support.google.com/chrome/answer/2364824).

Since Chrome profiles are isolated, this will not share any of the cookies or sign-in information from your normal browsing profile. However, all sign-ins will be persisted such that anytime you open the browser in the future, all your accounts will still be there. 

If you had your normal Chrome open while launching this profile, it will show up as a separate dock icon and be considered a separate application. If Chrome was not open beforehand, this application will look the same as your default profile. To return to the default profile, you must quit the application and relaunch Chrome.

If you would like to change the location where your browser profile will be created, you can modify the following setting in the browser section.

![Browser Profile](../../../assets/image/docs/browser/browser-profile.png)


======================================================================
## DOC: [plans] plans
URL: https://antigravity.google/docs/plans
======================================================================
---
slug: plans
section: Plans
title: Plans
path:
  - Plans
---

# Plans

At this moment, Google Antigravity is available with [terms](https://antigravity.google/terms) to individual accounts derived from Google's terms of service, and in preview (pre-general availability) to teams derived from Section 5 of the General Service Terms in Google Cloud's enterprise terms of service.

Rate limits and model availability differs based on usage of [Google AI](https://one.google.com/about/google-ai-plans/) plans.

## Baseline Quota

All plans receive a baseline of:

* Use of Gemini 3 Pro, Gemini 3 Flash, and other offered Vertex Model Garden models as the core agent model
* Unlimited Tab completions
* Unlimited Command requests
* Access to all product features, such as the Agent Manager and Browser integration

Users on Google AI Ultra receive:

* The highest, most generous quota, refreshed every five hours
* Highest weekly rate limits

Users on Google AI Pro receive:

* High, generous quota, refreshed every five hours until weekly limit reached
* Higher weekly rate limit

Users not on AI Pro and Ultra plans receive:

* Meaningful quota, refreshed weekly
* Weekly rate limit

The baseline rate limits are primarily determined to the degree we have capacity, and exist to prevent abuse. Under the hood, the rate limits are correlated with the amount of work done by the agent, which can differ from prompt to prompt. Thus, you may get many more prompts if your tasks are more straightforward and the agent can complete the work quickly, and the opposite is also true.

## Overages

Users on Google AI Pro or Ultra plans also have the ability to utilize their plan-included AI credits for additional overage usage above the baseline provided quota, and can [purchase additional AI credits](http://one.google.com/ai/credits) if desired. AI credits are consumed at Vertex API pricing.

Usage of credits once the baseline quota is exhausted for any particular model is controlled by the "AI Credit Overages" user setting, which can be set to the following:

* Never: Never use AI credits automatically, wait until the baseline quota refreshes before using this model further
* Always: Always use AI credits when the baseline quota is exhausted (will switch back automatically to using the baseline quota once the refresh hits)

Baseline quota usage across models can be viewed in the settings page.

## Other

There is currently no support for:

* Bring-your-own-key or bring-your-own-endpoint for additional rate limits
* Organizational tiers in general availability, or via contract


======================================================================
## DOC: [settings] settings
URL: https://antigravity.google/docs/settings
======================================================================
---
slug: settings
section: Settings
title: Settings
path:
  - Settings
---

# Settings

You can configure your Antigravity settings across Agent, Browser, Editor, and more via:

* Keyboard shortcut in any surface: `Cmd + ,`
* From the Settings tab or gear icon in the Agent Manager
* From "Settings > Open Antigravity User Settings" in the Editor

## Data Collection Settings

The "Enable Telemetry" setting can be found in the Settings panel under the "Account" section. When toggled on, Antigravity collects interactions for use in evaluating, developing, and improving Antigravity and models that support Antigravity.

======================================================================
## DOC: [faq] faq
URL: https://antigravity.google/docs/faq
======================================================================
---
slug: faq
section: FAQ
title: FAQ
path:
  - FAQ
---

# FAQ

## Why can I not authenticate into Google Antigravity?

Google Antigravity is currently available for personal Google accounts in approved geographies. Please try using an @gmail.com email address if having challenges with Workspace Google accounts.

## Why is my age unverified?

At the moment, Antigravity is unavailable to under-18 users. If you do meet the minimum age requirement, you may [verify your age](https://myaccount.google.com/age-verification) to continue using Antigravity.

## What is Google Antigravity’s geographical availability?
Google Antigravity is available in the following countries and territories. If you're not in one of these countries or territories, you will be unable to use Google Antigravity at this time:

**Important**: Please check the country listed on the [Google Terms of Service](https://policies.google.com/terms) page. If this is the wrong country, you may [submit a request](https://policies.google.com/country-association-form) to change your associated region.

Americas
- American Samoa
- Anguilla
- Antigua and Barbuda
- Argentina
- Aruba
- The Bahamas
- Barbados
- Belize
- Bermuda
- Bolivia
- Brazil
- British Virgin Islands
- Canada
- Caribbean Netherlands
- Cayman Islands
- Chile
- Colombia
- Costa Rica
- Curaçao
- Dominica
- Dominican Republic
- Ecuador
- El Salvador
- Falkland Islands (Islas Malvinas)
- Greenland
- Grenada
- Guatemala
- Guyana
- Haiti
- Honduras
- Jamaica
- Mexico
- Montserrat
- Nicaragua
- Panama
- Paraguay
- Peru
- Puerto Rico
- Saint Barthélemy
- Saint Kitts and Nevis
- Saint Lucia
- Saint Pierre and Miquelon
- Saint Vincent and the Grenadines
- South Georgia and the South Sandwich Islands
- Suriname
- Trinidad and Tobago
- Turks and Caicos Islands
- United States
- Uruguay
- U.S. Virgin Islands
- Venezuela

Europe
- Albania
- Armenia
- Austria
- Azerbaijan
- Belgium
- Bosnia and Herzegovina
- Bulgaria
- Croatia
- Cyprus
- Czech Republic
- Denmark
- Estonia
- Faroe Islands
- Finland
- France
- Georgia
- Germany
- Gibraltar
- Greece
- Guernsey
- Hungary
- Iceland
- Ireland
- Isle of Man
- Italy
- Jersey
- Kosovo
- Latvia
- Liechtenstein
- Lithuania
- Luxembourg
- Malta
- Montenegro
- Netherlands
- North Macedonia
- Norway
- Poland
- Portugal
- Romania
- Serbia
- Slovakia
- Slovenia
- Spain
- Sweden
- Switzerland
- Ukrainian territories other than Crimea, the so-called Donetsk People's Republic ("DNR"), and the so-called Luhansk People's Republic ("LNR")
- United Kingdom

Africa
- Algeria
- Angola
- Benin
- Botswana
- Burkina Faso
- Burundi
- Cabo Verde
- Cameroon
- Central African Republic
- Chad
- Comoros
- Côte d'Ivoire
- Democratic Republic of the Congo
- Djibouti
- Egypt
- Equatorial Guinea
- Eritrea
- Eswatini
- Ethiopia
- Gabon
- The Gambia
- Ghana
- Guinea
- Guinea-Bissau
- Kenya
- Lesotho
- Liberia
- Libya
- Madagascar
- Malawi
- Mali
- Mauritania
- Mauritius
- Morocco
- Mozambique
- Namibia
- Niger
- Nigeria
- Republic of the Congo
- Rwanda
- Saint Helena, Ascension and Tristan da Cunha
- São Tomé and Príncipe
- Senegal
- Seychelles
- Sierra Leone
- Somalia
- South Africa
- South Sudan
- Sudan
- Tanzania
- Togo
- Tunisia
- Uganda
- Western Sahara
- Zambia
- Zimbabwe

Asia
- Bahrain
- Bangladesh
- Bhutan
- British Indian Ocean Territory
- Brunei
- Cambodia
- Christmas Island
- Cocos (Keeling) Islands
- India
- Indonesia
- Iraq
- Israel
- Japan
- Jordan
- Kazakhstan
- Kuwait
- Kyrgyzstan
- Laos
- Lebanon
- Malaysia
- Maldives
- Mongolia
- Nepal
- Oman
- Pakistan
- Palestine
- Philippines
- Qatar
- Saudi Arabia
- Singapore
- South Korea
- Sri Lanka
- Taiwan
- Tajikistan
- Thailand
- Timor-Leste
- Türkiye
- Turkmenistan
- United Arab Emirates
- Uzbekistan
- Vietnam
- Yemen

Oceania
- Australia
- Cook Islands
- Fiji
- Guam
- Heard Island and McDonald Islands
- Kiribati
- Marshall Islands
- Micronesia
- Nauru
- New Caledonia
- New Zealand
- Niue
- Norfolk Island
- Northern Mariana Islands
- Palau
- Papua New Guinea
- Pitcairn Islands
- Samoa
- Solomon Islands
- Tokelau
- Tonga
- Tuvalu
- United States Minor Outlying Islands
- Vanuatu
- Wallis and Futuna

Antarctica
- Antarctica

## Why am I ineligible for a Google One AI plan?

The following regions do not currently have access to Google One AI plans:

- Antarctica
- Brunei
- Caribbean Netherlands
- Curaçao
- Democratic Republic of the Congo
- Eswatini
- Falkland Islands (Islas Malvinas)
- Faroe Islands
- Greenland
- Guernsey
- Heard Island and McDonald Islands
- Isle of Man
- Jersey
- Kosovo
- Montenegro
- New Caledonia
- Pitcairn Islands
- Republic of the Congo
- Saint Barthélemy
- Saint Helena, Ascension and Tristan da Cunha
- Saint Kitts and Nevis
- Saint Vincent and the Grenadines
- São Tomé and Príncipe
- South Georgia and the South Sandwich Islands
- South Sudan
- Sudan
- The Gambia
- Türkiye
- United States Minor Outlying Islands
- U.S. Virgin Islands
- Wallis and Futuna


## What is Google Antigravity’s stance on data collection?
Please refer to the [Terms of Service](/terms). You may opt out of data collection at any point from the Settings panel.

## How do I sign in with a GCP project?

This sign-in option is only available to invited teams, and we are not currently taking requests.

## How do I get support?
Check out the communities on our [Support page](/support).

## What are the model rate limits?
Please see more details in the docs on [Plans](/docs/plans).

## Why can’t I use third party software (e.g. Claude Code, OpenClaw, OpenCode) with my Antigravity login?

Using third party software, tools, or services to access Antigravity is a violation of our [Terms of Service](/terms), and severely degrades the experience for legitimate product users. Such actions may be grounds for suspension or termination of your account. If you would like to use a third party coding agent with Gemini, we recommend using a Vertex or AI Studio API key.

## Does Google Antigravity currently support worktrees?
Not at the moment.

## What happens when my computer goes to sleep?
If an agent is running, Antigravity will prevent your computer from sleeping.

