# Claude Certified Developer: Ep 09 | How AI Agents Actually Use MCP | Full Course

**URL:** https://www.youtube.com/watch?v=M3zvzzwzZSY
**Added:** 2026-08-29
**Relevance:** ⭐⭐⭐⭐ (4/5)
**Model:** `azure/gpt-5`
**Channel:** Peace Of Code

## Key Takeaways
- **🔧 Focus** — Move from mock PRs to real data using MCP with two patterns—connect to external MCP servers and build a standalone MCP server.…
- **🧩 Key clarification** — Prior “custom tools” built with the SDK were actually in-process MCP servers (SDK format).
- **🌐 MCP server access formats** — STDIO, HTTP, SSE, SDK.

## Apply to ArchonOS
- Reconcile the fleet's MCP lifecycle paths (in-process SDK vs STDIO vs HTTP) and document which ArchonOS tools use which — `references/tubeonai-prompt-output-shapes.md` already shows the operational cost when MCP server output shapes drift.

## TubeOnAI Summary
> - 🔧 Focus: Move from mock PRs to real data using MCP with two patterns—connect to external MCP servers and build a standalone MCP server. – Existing mock flow remains via a feature toggle to safely test concepts without network variability. - 🧩 Key clarification: Prior “custom tools” built with the SDK were actually in-process MCP servers (SDK format). – The function to create them (e.g., create SDK MCP server) runs a server inside the Python process. - 🌐 MCP server access formats: STDIO, HTTP, SSE, SDK. – STDIO uses command + env/args and streams JSON-RPC over stdin/stdout; HTTP uses standard endpoints and headers; SSE is legacy streaming; SDK runs in-process. - 🛠️ GitHub MCP server: Use the official remote endpoint api.githubcopilot.com/mcp (not github.com). – Configure in .mcp.json with type HTTP, headers (including Authorization), and toolset (e.g., pullRequests). - 🔐 Authentication: Use a fine-grained, read-only GitHub PAT scoped to the minimum needed (e.g., PR read on a single repo). – Reference the token via env var expansion (e.g., $GITHUB_PAT) rather than hardcoding. - ⚠️ Known issue: Header env-var expansion in HTTP configurations may fail on some setups, sending the lite…

## Tags
`#MCP` `#agents` `#tool-use` `#failure-modes`
