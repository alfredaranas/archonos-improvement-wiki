# Skills vs MCP vs RAG vs Memory: What AI Agents Need to Know

**URL:** https://youtube.com/watch?v=X4FVEEegCbk
**Added:** 2026-09-05
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- **🧭 Problematyczne podejście** — wrzucanie całego kontekstu do modelu często jest nieefektywne i prowadzi do błądzenia lub fałszywych ścieżek rozumowania.…
- **✅ Zasada praktyczna** — używaj RAG dla wiedzy spisanej przez ludzi, pamięci dla doświadczeń agenta, skills dla powtarzalnych procedur, a MCP gdy agent musi odpytać zewnętrzne systemy.…

## Apply to ArchonOS
- Cross-cutting reference: useful framing for future architecture discussions
- Save for FOCUS-card context when planning cross-archon changes

## TubeOnAI Summary
> 🧭 Problematyczne podejście: wrzucanie całego kontekstu do modelu często jest nieefektywne i prowadzi do błądzenia lub fałszywych ścieżek rozumowania.  
  – Skutek: brak specyficznej wiedzy o konkretnej aplikacji i nadmiar informacji.

⚙️ Skills (umiejętności agenta) to zdefiniowane procedury z instrukcjami i opcjonalnym kodem, używane przez agenta tylko gdy zadanie tego wymaga.  
  – Zakres: dostarczają kroków i kryteriów decyzji (np. gdy eskalować), lecz nie łączą się same z zewnętrznymi źródłami danych.

🔗 MCP (Model Context Protocol) łączy agenta z zewnętrznymi systemami przez standardowy interfejs host/server, umożliwiając dostęp do logów i metryk.  
  – Funkcja: pozwala agentowi na wykonanie zapytań do narzędzi i dashboardów bez osadzania własnego kodu dostępu.

📚 RAG (Retrieval-Augmented Generation) przywołuje relewantne, wcześniej zapisane dokumenty przez wyszukiwanie semantyczne i wstrzykuje je do okna kontekstu.  
  – Źródło wiedzy: dokumenty przygotowane i umieszczone w wektorowej bazie danych przez ludzi.

🧠 Pamięć agenta to doświadczenia i zapisy wygenerowane przez samego agenta z poprzednich interakcji, wykorzystywane przy przyszłych problemach.  
  – Różnica od RAG: pochodzi z doświadczenia agenta, nie z uprzednio wprowadzonych dokumentów.

✅ Zasada praktyczna: używaj RAG dla wiedzy spisanej przez ludzi, pamięci dla doświadczeń agenta, skills dla powtarzalnych procedur, a MCP gdy agent musi odpytać zewnętrzne systemy.

## Tags
#general #general #memory #mcp
