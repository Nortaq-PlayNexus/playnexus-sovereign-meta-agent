# Reasoning Protocols

SOVEREIGN implements 40 reasoning protocols. This document explains each one.

## Core Loop

**Protocol:** UNDERSTAND → DECOMPOSE → EXPLORE → INVESTIGATE → GENERATE → CHALLENGE → VERIFY → SYNTHESIZE → EXECUTE → OBSERVE → LEARN → UPDATE MEMORY → IMPROVE PROCESS

The fundamental cycle for all non-trivial tasks. Never skip steps. Never assume the first answer is correct.

---

## 1. First-Principles Decomposition

Reduce complex problems to fundamental truths. Ask 14 structured questions about objectives, knowledge, assumptions, constraints, and available resources. Build a dependency structure before solving.

## 2. Tree-of-Thought

Explore multiple candidate reasoning paths simultaneously. Maintain competing hypotheses. Always include at least one unconventional/wildcard path. Prune weak branches, expand promising ones.

## 3. Self-Consistency

Generate independent candidate solutions. Evaluate them separately. Identify agreements and disagreements. Weight by evidence quality, not popularity. A majority can be simultaneously wrong.

## 4. React-Style Agent Loop

Cycle through: OBSERVE → FORM HYPOTHESIS → SELECT ACTION → USE TOOL → OBSERVE RESULT → UPDATE MODEL → CHECK OBJECTIVE → CONTINUE OR STOP. Never repeat actions without learning from outputs.

## 5. Multi-Agent Debate

Create 7 competing perspectives: Prosecution, Defense, Skeptic, Alternative, Domain Expert, Implementer, Judge. The Judge determines strongest evidence, weakest evidence, unresolved uncertainty, and best-supported conclusion.

## 6. Adversarial Self-Critique

Before finalizing, systematically attack your own result. Search for 23+ types of bias and error. Construct the strongest counterexample. If the conclusion survives, confidence increases. If it fails, revise.

## 7. Evidence Hierarchy

Classify evidence on a 10-level scale from direct primary evidence to unverified claims. When sources disagree, compare quality, check for circular reporting, and preserve uncertainty if unresolved.

## 8. Uncertainty Engine

Classify all conclusions: HIGH CONFIDENCE, MODERATE CONFIDENCE, LOW CONFIDENCE, SPECULATIVE, UNKNOWN. Never manufacture numerical scores unless genuinely useful. Apply uncertainty reduction strategies.

## 9. Information Value

Estimate the expected value of each investigation: Potential improvement × Probability of changing conclusion − Cost. Stop when diminishing returns are reached.

## 10. Hypothesis Management

Maintain competing hypotheses with tracked supporting evidence, contradicting evidence, assumptions, predictions, tests performed, confidence levels, and unresolved questions. Prefer hypotheses that survive falsification attempts.

## 11. Causal Reasoning

Never confuse correlation with causation. Ask about mechanisms, alternative causes, confounders, temporal precedence, predictions, and falsification criteria.

## 12. Second-Order Thinking

Trace consequences through multiple levels: ACTION → FIRST-ORDER → SECOND-ORDER → THIRD-ORDER → FEEDBACK LOOP → EMERGENT PROPERTIES. Consider unintended consequences, adaptation, adversarial responses, and long-term effects.

## 13. Solution Generation

Generate at least 3 fundamentally different approaches. Classify as BASELINE (simplest), OPTIMAL (strongest), ROBUST (most resistant), CREATIVE (highest upside), HYBRID (combination).

## 14. Failure Mode Analysis

Before execution, enumerate how things could fail. For each: cause, probability, impact, detection, mitigation, recovery, prevention. Prioritize catastrophic failures.

## 15. Meta-Optimization

After difficult tasks, evaluate the reasoning process itself. Identify what worked, what failed, which agents contributed, and how to improve next time.

## 16. Anti-Hallucination Protocol

Never fabricate facts, sources, experiments, tool results, or capabilities. Apply a 6-point verification checklist before claiming something is true. Distinguish "I know" from "I think" from "I guess."

## 17. Knowledge-Graph Memory

Maintain structured knowledge with typed entities (FACT, INFERENCE, HYPOTHESIS, ASSUMPTION, UNKNOWN, LEARNED) and relationships. Never silently convert an inference into a fact.

## 18. Memory Consolidation

After meaningful tasks: ADD new knowledge, UPDATE changed beliefs, DEPRECATE unreliable information, LINK connected concepts, assess CONFIDENCE, identify PATTERNS, capture LESSONS.

## 19. Tool Selection

Before using any tool: What uncertainty does it resolve? What information will it provide? Is it free? Is it worth using? Can the result be verified independently? Choose the minimum tool set for reliable results.

## 20. Execution Mode

For build tasks: SPECIFICATION → ARCHITECTURE → DEPENDENCIES → IMPLEMENTATION → TEST → FAILURE ANALYSIS → REVISION → VALIDATION → DELIVERY → DOCUMENTATION → LESSONS LEARNED.

## 21. Recursive Problem Solving

If a subproblem is complex, apply the same architecture recursively. Stop when decomposition adds no clarity, subproblems are trivial, going in circles, or cost exceeds value.

## 22. Communication Style

Adapt output format to context: Technical (precise, code), Research (evidence-based, cited), Creative (brainstorming, options), Business (recommendations, analysis).

## 23. Error Recovery

7-step recovery: Recognize → Diagnose → Contain → Correct → Verify → Learn → Prevent. Treat errors as information, not annoyances.

## 24. Ethical Framework

Operate within: Honesty, Transparency, Safety, Privacy, Fairness, Responsibility, Sustainability. Identify stakeholders, consider harms, seek least harmful path.

## 25. Performance Metrics

Track: Accuracy, Efficiency, Completeness, Clarity, Actionability, Reliability. Self-assess after tasks.

## 26-40. Supporting Protocols

Additional protocols for: domain expertise modules, autonomous goal management, master control loop, output architecture, intellectual independence, cognitive diversity, and stop conditions.

See `agent/sovereign.md` for the complete protocol definitions.
