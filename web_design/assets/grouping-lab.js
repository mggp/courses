const card = document.querySelector("[data-code-card]");
const groupingControls = [...document.querySelectorAll("[data-gap-control]")];
const groupingFeedback = document.querySelector("[data-grouping-feedback]");
const groupingCheck = document.querySelector("[data-grouping-check]");
const groupingReset = document.querySelector("[data-grouping-reset]");

const values = () => Object.fromEntries(
  groupingControls.map((control) => [control.dataset.gapControl, Number(control.value)])
);

const describe = () => {
  const { instruction, label, support } = values();

  if (label >= instruction) {
    return {
      className: "feedback warn",
      text: "The label is as far from its field as the instruction is from the form. The smallest relationship is still unclear."
    };
  }

  if (support < instruction * 2) {
    return {
      className: "feedback warn",
      text: "The reassurance still appears inside the task group. Give the group boundary more space than the relationships within it."
    };
  }

  return {
    className: "feedback good",
    text: "Two groups read clearly. The label binds to the field, the instruction binds to the form, and the reassurance sits outside the task."
  };
};

const applyGap = (control) => {
  const value = Number(control.value);
  card.style.setProperty(`--${control.dataset.gapControl}-gap`, `${value}px`);
  control.closest(".control").querySelector("output").value = `${value}px`;
};

groupingControls.forEach((control) => {
  control.addEventListener("input", () => {
    applyGap(control);
    groupingFeedback.className = "feedback";
    groupingFeedback.textContent = "Watch which elements now appear to belong together.";
  });
});

groupingCheck.addEventListener("click", () => {
  const result = describe();
  groupingFeedback.className = result.className;
  groupingFeedback.textContent = result.text;
});

groupingReset.addEventListener("click", () => {
  groupingControls.forEach((control) => {
    control.value = control.defaultValue;
    applyGap(control);
  });
  groupingFeedback.className = "feedback";
  groupingFeedback.textContent = "All gaps are equal again. Where does one group end and the next begin?";
});
