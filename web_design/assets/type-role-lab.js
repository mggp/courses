const typeCard = document.querySelector("[data-type-card]");
const typeControls = [...document.querySelectorAll("[data-type-control]")];
const typeFeedback = document.querySelector("[data-type-feedback]");
const typeCheck = document.querySelector("[data-type-check]");
const typeReset = document.querySelector("[data-type-reset]");

const typeValues = () => Object.fromEntries(
  typeControls.map((control) => [control.dataset.typeControl, Number(control.value)])
);

const applyTypeValue = (control) => {
  const value = Number(control.value);
  const unit = control.dataset.unit || "";
  typeCard.style.setProperty(control.dataset.property, `${value}${unit}`);
  control.closest(".control").querySelector("output").value = `${value}${control.dataset.outputUnit || unit}`;
};

const assessTypeRoles = () => {
  const { taskSize, taskWeight, supportSize, supportLeading } = typeValues();
  const sizeRatio = taskSize / supportSize;

  if (sizeRatio < 1.45 && taskWeight - 400 < 200) {
    return {
      className: "feedback warn",
      text: "The instruction and explanation still have similar typographic weight. The screen has no clear textual entry point."
    };
  }

  if (sizeRatio > 2.25) {
    return {
      className: "feedback warn",
      text: "The instruction has become a display headline. It dominates the small task more than its role requires."
    };
  }

  if (supportSize < 14 || supportLeading < 1.4) {
    return {
      className: "feedback warn",
      text: "The explanation is quieter, but readability paid the price. Hierarchy should not depend on cramped or tiny body text."
    };
  }

  return {
    className: "feedback good",
    text: "The roles now separate cleanly. The instruction opens the task, the control text stays functional, and the explanation reads as supporting copy."
  };
};

typeControls.forEach((control) => {
  control.addEventListener("input", () => {
    applyTypeValue(control);
    typeFeedback.className = "feedback";
    typeFeedback.textContent = "Now compare roles, not individual numbers. Which text begins the task, and which text supports it?";
  });
});

typeCheck.addEventListener("click", () => {
  const result = assessTypeRoles();
  typeFeedback.className = result.className;
  typeFeedback.textContent = result.text;
});

typeReset.addEventListener("click", () => {
  typeControls.forEach((control) => {
    control.value = control.defaultValue;
    applyTypeValue(control);
  });
  typeFeedback.className = "feedback";
  typeFeedback.textContent = "The instruction and explanation are close in size, weight, and density. Assign each one a job before changing values.";
});
