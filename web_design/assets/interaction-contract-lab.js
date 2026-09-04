const lab = document.querySelector("[data-contract-lab]");

if (lab) {
  const editorView = lab.querySelector("[data-editor-view]");
  const pageView = lab.querySelector("[data-page-view]");
  const disclosure = lab.querySelector("[data-disclosure]");
  const panel = lab.querySelector("[data-advanced-panel]");
  const stageResult = lab.querySelector("[data-stage-result]");
  const tryButton = lab.querySelector("[data-try-behavior]");
  const repairButton = lab.querySelector("[data-apply-repair]");
  const backButton = lab.querySelector("[data-return-editor]");
  const predictionFeedback = lab.querySelector("[data-prediction-feedback]");
  const diagnosisFeedback = lab.querySelector("[data-diagnosis-feedback]");
  let repaired = false;

  const choose = (group, selected) => {
    lab.querySelectorAll(`[data-${group}]`).forEach((button) => {
      button.setAttribute("aria-pressed", String(button === selected));
    });
  };

  lab.querySelectorAll("[data-prediction]").forEach((button) => {
    button.addEventListener("click", () => {
      choose("prediction", button);
      const correct = button.dataset.prediction === "inline";
      predictionFeedback.className = `feedback ${correct ? "good" : "warn"}`;
      predictionFeedback.textContent = correct
        ? "Yes. The chevron and row treatment predict an inline disclosure. Now test whether the interface keeps that promise."
        : "Look at the chevron and the row's position inside the editor. What behavior have you seen that cue perform elsewhere?";
      tryButton.disabled = !correct;
    });
  });

  const useControl = () => {
    if (!repaired) {
      editorView.hidden = true;
      pageView.hidden = false;
      stageResult.textContent = "Actual result: the editor was replaced by another page.";
      repairButton.disabled = false;
      return;
    }

    const expanded = disclosure.getAttribute("aria-expanded") === "true";
    disclosure.setAttribute("aria-expanded", String(!expanded));
    panel.hidden = expanded;
    stageResult.textContent = expanded
      ? "Result: advanced controls collapsed in place."
      : "Result: advanced controls appeared in place.";
  };

  tryButton.addEventListener("click", useControl);
  disclosure.addEventListener("click", useControl);

  backButton.addEventListener("click", () => {
    pageView.hidden = true;
    editorView.hidden = false;
    stageResult.textContent = "You returned to the editor. The original cue still predicts the wrong transition.";
  });

  lab.querySelectorAll("[data-diagnosis]").forEach((button) => {
    button.addEventListener("click", () => {
      choose("diagnosis", button);
      const correct = button.dataset.diagnosis === "contract";
      diagnosisFeedback.className = `feedback ${correct ? "good" : "warn"}`;
      diagnosisFeedback.textContent = correct
        ? "Correct. The control looks like a disclosure but behaves like navigation."
        : "That may affect polish, but it does not explain the surprise. Compare the predicted transition with the actual one.";
    });
  });

  repairButton.addEventListener("click", () => {
    repaired = true;
    pageView.hidden = true;
    editorView.hidden = false;
    disclosure.setAttribute("aria-expanded", "false");
    panel.hidden = true;
    stageResult.textContent = "Repair applied. Activate Advanced publishing again.";
    repairButton.textContent = "Repair applied";
    repairButton.disabled = true;
  });
}
