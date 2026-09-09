const systemLab = document.querySelector("[data-system-lab]");

if (systemLab) {
  const feedback = systemLab.querySelector("[data-system-feedback]");
  const answers = { foundation: "foundation", component: "component", pattern: "pattern", governance: "governance" };
  const explanations = {
    foundation: "Right. A named semantic colour rule is a shared foundation: it should stay stable even when several components use it.",
    component: "Right. A button is a reusable UI part; its states and accessibility behavior belong with the component.",
    pattern: "Right. A confirmation flow combines components to solve a recurring user task, including what happens after the action.",
    governance: "Right. Deciding when a new variant earns its place is governance: a system needs an evidence-based change rule, not just files."
  };

  systemLab.querySelectorAll("[data-system-choice]").forEach((button) => {
    button.addEventListener("click", () => {
      const question = button.closest("[data-system-question]");
      const answer = question.dataset.systemQuestion;
      question.querySelectorAll("[data-system-choice]").forEach((choice) => choice.setAttribute("aria-pressed", String(choice === button)));
      const correct = button.dataset.systemChoice === answers[answer];
      feedback.className = `feedback ${correct ? "good" : "warn"}`;
      feedback.textContent = correct ? explanations[answer] : "Look for the level where this decision prevents a repeated kind of inconsistency. It is not always a component.";
    });
  });
}
