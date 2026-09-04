# Agent-memory baseline: scope and host access understood

The learner correctly distinguishes thread-scoped state from information that should survive across runs. He places a current tool result in ReAct loop state and a stable programming-language preference in an auxiliary long-term store, and he understands that the host or harness must give the model access to stored information. Future teaching should start beyond those basics and sharpen two boundaries: thread-scoped memory may still be durable, and persisted history is not necessarily the exact context sent on every inference.
