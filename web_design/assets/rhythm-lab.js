const lab = document.querySelector("[data-rhythm-lab]");

if (lab) {
  const releaseWindow = lab.querySelector("[data-release-window]");
  const measureButton = lab.querySelector("[data-show-measures]");
  const repairButton = lab.querySelector("[data-repair-rhythm]");
  const observationFeedback = lab.querySelector("[data-observation-feedback]");
  const meaningFeedback = lab.querySelector("[data-meaning-feedback]");

  const choose = (group, selected) => {
    lab.querySelectorAll(`[data-${group}]`).forEach((button) => {
      button.setAttribute("aria-pressed", String(button === selected));
    });
  };

  measureButton.addEventListener("click", () => {
    const visible = releaseWindow.classList.toggle("show-measures");
    measureButton.textContent = visible ? "Hide gap measurements" : "Show gap measurements";
  });

  lab.querySelectorAll("[data-observation]").forEach((button) => {
    button.addEventListener("click", () => {
      choose("observation", button);
      const correct = button.dataset.observation === "summary-gap";
      observationFeedback.className = `feedback ${correct ? "good" : "warn"}`;
      observationFeedback.textContent = correct
        ? "Yes. The same title-to-summary relationship uses 8px twice and 28px once."
        : "That feature repeats consistently. Compare the same relationship across all three entries.";
    });
  });

  lab.querySelectorAll("[data-meaning]").forEach((button) => {
    button.addEventListener("click", () => {
      choose("meaning", button);
      const correct = button.dataset.meaning === "unsupported";
      meaningFeedback.className = `feedback ${correct ? "good" : "warn"}`;
      meaningFeedback.textContent = correct
        ? "Correct. The content role did not change, so the spacing change communicates nothing useful."
        : "Look for a corresponding change in content role. None appears in the final entry.";
      repairButton.disabled = !correct;
    });
  });

  repairButton.addEventListener("click", () => {
    const brokenEntry = lab.querySelector(".release-entry.is-break");
    brokenEntry.classList.remove("is-break");
    brokenEntry.querySelector(".gap-measure").textContent = "8px title to summary";
    repairButton.textContent = "Rhythm repaired";
    repairButton.disabled = true;
  });
}
