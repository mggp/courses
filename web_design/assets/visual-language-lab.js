const visualLanguageLab = document.querySelector("[data-visual-language-lab]");

if (visualLanguageLab) {
  const feedback = visualLanguageLab.querySelector("[data-language-feedback]");
  const required = new Set(["type", "geometry", "surface"]);
  const selected = new Set();

  visualLanguageLab.querySelectorAll("[data-language-rule]").forEach((button) => {
    button.addEventListener("click", () => {
      const rule = button.dataset.languageRule;
      const isSelected = selected.has(rule);
      button.setAttribute("aria-pressed", String(!isSelected));

      if (isSelected) selected.delete(rule);
      else selected.add(rule);

      const correctCount = [...selected].filter((item) => required.has(item)).length;
      const hasDistractor = selected.has("copy");

      if (hasDistractor) {
        feedback.className = "feedback warn";
        feedback.textContent = "The wording is shared, so it does not distinguish the visual languages. Look for a repeatable visual decision instead.";
      } else if (correctCount === required.size) {
        feedback.className = "feedback good";
        feedback.textContent = "Exactly. The type treatment, control geometry, and surface/color strategy form a compact visual-language brief. The information hierarchy and task can stay constant.";
      } else {
        feedback.className = "feedback";
        feedback.textContent = `${correctCount} of 3 evidence rules selected. Compare the headings, the call-to-action shapes, and the page surfaces—not the product copy.`;
      }
    });
  });
}
