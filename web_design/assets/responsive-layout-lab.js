const responsiveFrame = document.querySelector("[data-responsive-frame]");
const responsiveLayout = document.querySelector("[data-responsive-layout]");
const widthControl = document.querySelector("[data-preview-width]");
const breakpointControl = document.querySelector("[data-layout-breakpoint]");
const layoutFeedback = document.querySelector("[data-layout-feedback]");
const layoutCheck = document.querySelector("[data-layout-check]");
const layoutReset = document.querySelector("[data-layout-reset]");
const layoutState = document.querySelector("[data-layout-state]");

const outputFor = (control) => control.closest(".control").querySelector("output");

const updateLayout = () => {
  const availableWidth = Number(widthControl.value);
  const breakpoint = Number(breakpointControl.value);
  const stacked = availableWidth <= breakpoint;

  responsiveFrame.style.setProperty("--preview-width", `${availableWidth}px`);
  responsiveLayout.classList.toggle("is-stacked", stacked);
  outputFor(widthControl).value = `${availableWidth}px`;
  outputFor(breakpointControl).value = `${breakpoint}px`;
  layoutState.textContent = `${availableWidth}px available · ${stacked ? "stacked" : "two columns"}`;
};

const assessBreakpoint = () => {
  const breakpoint = Number(breakpointControl.value);

  if (breakpoint < 500) {
    return {
      className: "feedback warn",
      text: "The switch happens after the layout budget has already failed. There is a width range where both columns are present but the secondary region is crushed."
    };
  }

  if (breakpoint > 540) {
    return {
      className: "feedback warn",
      text: "The layout is safe, but it stacks before the two regions run out of room. Move the switch closer to the content's actual minimum."
    };
  }

  return {
    className: "feedback good",
    text: "The breakpoint follows the content budget. Below it, source order becomes the reading order. Above it, both regions have enough room to work side by side."
  };
};

[widthControl, breakpointControl].forEach((control) => {
  control.addEventListener("input", () => {
    updateLayout();
    layoutFeedback.className = "feedback";
    layoutFeedback.textContent = "Sweep through the widths around the switch. Look for cramped text, awkward wrapping, and lost visual priority.";
  });
});

layoutCheck.addEventListener("click", () => {
  const result = assessBreakpoint();
  layoutFeedback.className = result.className;
  layoutFeedback.textContent = result.text;
});

layoutReset.addEventListener("click", () => {
  widthControl.value = widthControl.defaultValue;
  breakpointControl.value = breakpointControl.defaultValue;
  updateLayout();
  layoutFeedback.className = "feedback";
  layoutFeedback.textContent = "The 420px breakpoint is borrowed from a device chart. At 480px available width, this composition still forces two cramped columns.";
});

updateLayout();
