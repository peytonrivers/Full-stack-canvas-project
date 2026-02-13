const params = new URLSearchParams(window.location.search);
const targetCourse = params.get("query");
const currentGrade = params.get("grade");



// ===== REVEAL =====
const revealObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.08 }
);

// Observe anything already on the page
document.querySelectorAll(".reveal").forEach(el => revealObserver.observe(el));


// ===== API =====
const fastApi = "http://127.0.0.1:8000";

function formatDueDate(dueValue) {
  if (!dueValue) return "—";

  // Handles ISO strings like "2025-09-10T23:59:00Z" or "2025-09-10"
  const d = new Date(dueValue);

  // If parsing fails, just show dash
  if (isNaN(d.getTime())) return "—";

  return d.toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric"
  });
}

async function assignmentsGrades() {
  const assignmentsFastApi = `${fastApi}/assignments_with_grades`;
  const response = await fetch(assignmentsFastApi);
  const data = await response.json();

  const assignmentsContainer = document.querySelector(".assignments");
  if (!assignmentsContainer) return;

  assignmentsContainer.innerHTML = "";

  for (let i = 0; i < data.length; i++) {
    const name = data[i]["Course Name"];

    const assignmentName = data[i]["Assignment Name"];
    const pointsPossible = data[i]["Points Possible"];
    const percent = data[i]["Percent"];

    // ✅ grab due date (supports multiple possible key names)
    const dueAt =
      data[i]["Due At"] ??
      data[i]["Due Date"] ??
      data[i]["due_at"] ??
      data[i]["due_date"] ??
      null;

    if (name === targetCourse) {
      const box = makeBoxes({
        assignmentName,
        pointsPossible,
        percent,
        dueAt
      });

      assignmentsContainer.appendChild(box);
      revealObserver.observe(box);
    }
  }
}



// ===== BOX BUILDER =====
function makeBoxes({ assignmentName, pointsPossible, percent, dueAt }) {
  // OUTER BOX
  const assignmentsBox = document.createElement("div");
  assignmentsBox.classList.add("assignments-box", "reveal");

  // TOP
  const assignmentsBoxTop = document.createElement("div");
  assignmentsBoxTop.classList.add("assignments-box-top");

  assignmentsBox.appendChild(assignmentsBoxTop);

  const assignmentsBoxTopTop = document.createElement("div");
  assignmentsBoxTopTop.classList.add("assignments-box-top-top");

  assignmentsBoxTop.appendChild(assignmentsBoxTopTop);

  const assignmentsBoxTopTopLeft = document.createElement("div");
  assignmentsBoxTopTopLeft.classList.add("assignments-box-top-top-left");

  const statusBadge = document.createElement("div");
  statusBadge.classList.add("status-badge");

  const svgBadge = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svgBadge.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svgBadge.setAttribute("height", "16px");
  svgBadge.setAttribute("viewBox", "0 -960 960 960");
  svgBadge.setAttribute("width", "16px");
  svgBadge.setAttribute("fill", "currentColor");

  const pathBadge = document.createElementNS("http://www.w3.org/2000/svg", "path");
  pathBadge.setAttribute("d", "M320-440h320v-80H320v80Zm0 120h320v-80H320v80Zm0 120h200v-80H320v80ZM240-80q-33 0-56.5-23.5T160-160v-640q0-33 23.5-56.5T240-880h320l240 240v480q0 33-23.5 56.5T720-80H240Zm280-520v-200H240v640h480v-440H520ZM240-800v200-200 640-640Z");
  
  svgBadge.appendChild(pathBadge);

  const spanText = document.createElement("span");
  spanText.classList.add("status-text");
  if (percent == null || percent == undefined || percent == "") {
    spanText.textContent = "Not Graded";
  } else {
    spanText.textContent = "Graded";
  }

  statusBadge.appendChild(svgBadge);
  statusBadge.appendChild(spanText);
  
  assignmentsBoxTopTopLeft.appendChild(statusBadge);

  const assignmentsBoxTopTopRight = document.createElement("div");
  assignmentsBoxTopTopRight.classList.add("assignments-box-top-top-right");

  const gradePill = document.createElement("div");
  gradePill.classList.add("grade-pill");

  const gradeText = document.createElement("span");
  gradeText.classList.add("grade-text");
  if (percent == null || percent == undefined || percent == "") {
    gradeText.textContent = "--";
  } else {
    gradeText.textContent = percent + "%";
  }

  gradePill.appendChild(gradeText);

  assignmentsBoxTopTopRight.appendChild(gradePill);

  assignmentsBoxTopTop.appendChild(assignmentsBoxTopTopLeft);
  assignmentsBoxTopTop.appendChild(assignmentsBoxTopTopRight);

  const assignmentsBoxTopBottom = document.createElement("div");
  assignmentsBoxTopBottom.classList.add("assignments-box-top-bottom");

  const hgroupBoxTopBottom = document.createElement("hgroup");
  hgroupBoxTopBottom.textContent = assignmentName ?? "--";
  assignmentsBoxTopBottom.appendChild(hgroupBoxTopBottom);

  assignmentsBoxTop.appendChild(assignmentsBoxTopBottom);

  const assignmentsBoxBottom = document.createElement("div");
  assignmentsBoxBottom.classList.add("assignments-box-bottom");

  const assignmentsBoxBottomLeft = document.createElement("div");
  assignmentsBoxBottomLeft.classList.add("assignments-box-bottom-left");

  const svgBoxBottomLeft = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svgBoxBottomLeft.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svgBoxBottomLeft.setAttribute("height", "24px");
  svgBoxBottomLeft.setAttribute("viewBox", "0 -960 960 960");
  svgBoxBottomLeft.setAttribute("width", "24px");
  svgBoxBottomLeft.setAttribute("fill", "#1f1f1f");


  const pathBoxBottomLeft = document.createElementNS("http://www.w3.org/2000/svg", "path");
  pathBoxBottomLeft.setAttribute("d", "M200-80q-33 0-56.5-23.5T120-160v-560q0-33 23.5-56.5T200-800h40v-80h80v80h320v-80h80v80h40q33 0 56.5 23.5T840-720v560q0 33-23.5 56.5T760-80H200Zm0-80h560v-400H200v400Zm0-480h560v-80H200v80Zm0 0v-80 80Zm280 240q-17 0-28.5-11.5T440-440q0-17 11.5-28.5T480-480q17 0 28.5 11.5T520-440q0 17-11.5 28.5T480-400Zm-188.5-11.5Q280-423 280-440t11.5-28.5Q303-480 320-480t28.5 11.5Q360-457 360-440t-11.5 28.5Q337-400 320-400t-28.5-11.5ZM640-400q-17 0-28.5-11.5T600-440q0-17 11.5-28.5T640-480q17 0 28.5 11.5T680-440q0 17-11.5 28.5T640-400ZM480-240q-17 0-28.5-11.5T440-280q0-17 11.5-28.5T480-320q17 0 28.5 11.5T520-280q0 17-11.5 28.5T480-240Zm-188.5-11.5Q280-263 280-280t11.5-28.5Q303-320 320-320t28.5 11.5Q360-297 360-280t-11.5 28.5Q337-240 320-240t-28.5-11.5ZM640-240q-17 0-28.5-11.5T600-280q0-17 11.5-28.5T640-320q17 0 28.5 11.5T680-280q0 17-11.5 28.5T640-240Z");

  svgBoxBottomLeft.appendChild(pathBoxBottomLeft);

  const hgroupBoxBottomLeft = document.createElement("hgroup");
  hgroupBoxBottomLeft.textContent = formatDueDate(dueAt);

  assignmentsBoxBottomLeft.append(svgBoxBottomLeft);
  assignmentsBoxBottomLeft.append(hgroupBoxBottomLeft);

  const assignmentsBoxBottomRight = document.createElement("div");
  assignmentsBoxBottomRight.classList.add("assignments-box-bottom-right");

  const hgroupBoxBottomRight = document.createElement("hgroup");
  hgroupBoxBottomRight.textContent = pointsPossible !== null && pointsPossible !== undefined ? `${pointsPossible}pts` : "--pts";
  assignmentsBoxBottomRight.appendChild(hgroupBoxBottomRight);

  assignmentsBoxBottom.appendChild(assignmentsBoxBottomLeft);
  assignmentsBoxBottom.appendChild(assignmentsBoxBottomRight);
  
  assignmentsBox.appendChild(assignmentsBoxBottom);


  return assignmentsBox;
}

document.querySelector(".the-title").textContent = targetCourse

// RUN

async function totalAssignments() {
  const assignmentsFastApi = `${fastApi}/assignments_with_grades`;
  const response = await fetch(assignmentsFastApi);
  const data = await response.json();

  let totalAssignments = 0;

  for (let i=0; i<data.length; i++) {
    if (data[i]["Course Name"] === targetCourse) {
      totalAssignments ++;
    }
  }

  document.querySelector("#total-assignments span").textContent = totalAssignments;
}

document.querySelector("#current-grade span").textContent = currentGrade + "%";

assignmentsGrades();

totalAssignments();



const searchBox = document.querySelector('input[type="search"]');



searchBox.addEventListener("input", () => {
  const userInput = searchBox.value.trim().toLowerCase();

  // IMPORTANT: re-grab the cards each time (handles dynamic rendering)
  const textBoxes = document.querySelectorAll(".assignments-box");

  textBoxes.forEach(box => {
    const titleElement = box.querySelector(".assignments-box-top-bottom hgroup");
    const assignmentName = (titleElement?.textContent || "").toLowerCase();

    box.style.display = assignmentName.includes(userInput) ? "" : "none";
  });
});
