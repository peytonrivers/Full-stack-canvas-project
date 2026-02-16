const revealElements = document.querySelectorAll('.reveal');

const revealObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target); // reveal once
      }
    });
  },
  {
    threshold: 0.08
  }
);

revealElements.forEach(el => revealObserver.observe(el));

const fastApi = "https://full-stack-canvas-project.onrender.com"

async function averageGradeCalculator () {
    const totalGradesApi = `${fastApi}/totalgrades`
    const response = await fetch(totalGradesApi);
    const data = await response.json();
    let total = 0;
    for (let i=0; i < data.length; i++) {
        total += data[i]["Total Grade"];
        console.log(data[i]["Course Name"]);
    }
    let average = total / 6;
    let roundedAverage = Number(average.toFixed(2));
    document.querySelector("#average").innerHTML = roundedAverage + "%";
}

async function assignmentsDisplay() {
    const totalGradesApi = `${fastApi}/totalgrades`
    const response = await fetch(totalGradesApi);
    const data = await response.json();
    for (let i=0; i < 6; i++) {
        let name = data[i]["Course Name"];
        let grade = data[i]["Total Grade"];
        document.querySelector(`#bar-percent${i + 1}`).style.width = grade + "%";
        document.querySelector(`#class${i + 1}`).innerHTML = name;
        document.querySelector(`#grade${i + 1}`).innerHTML = grade + "%";
        if (grade >= 90) {
            document.querySelector(`#letter${i + 1}`).innerHTML = 'A';
        } else if (grade >= 80) {
            document.querySelector(`#letter${i + 1}`).innerHTML = 'B';
        } else if (grade >= 70) {
            document.querySelector(`#letter${i + 1}`).innerHTML = 'C';
        } else if (grade >= 60) {
            document.querySelector(`#letter${i + 1}`).innerHTML = 'D';
        } else {
            document.querySelector(`#letter${i + 1}`).innerHTML = 'F';
        }
    }
}






"202580-Fall 2025-ITSC-1212_Combined"

"202580-Fall 2025-ITSC-1600-001-Computing Professionals"

"202580-Fall 2025-MATH-1241-004-Calculus I"

"202580-Fall 2025-WRDS-1103-048-Wrtng & Inqry Acdmc Ctx I & II"

"First-Year New Student Modules, College of Computing and Informatics - Summer II/Fall 2025"

averageGradeCalculator();
assignmentsDisplay();


async function historyEncode () {
  const parameterValue = "202580-Fall 2025-HIST-1575-008-American Democracy";

  const totalGradesApi = `${fastApi}/totalgrades`;
  const response = await fetch(totalGradesApi);
  const data = await response.json();
  for (let i=0; i<data.length; i++) {
    if (data[i]["Course Name"] === parameterValue) {
      parameterTotalGrade = data[i]["Total Grade"];
      break;
    }
  }

  const encodeName = encodeURIComponent(parameterValue);
  const encodeTotalGrade = encodeURIComponent(parameterTotalGrade);
  const baseURL = "assignments.html";
  const fullURL = `${baseURL}?query=${encodeName}&grade=${encodeTotalGrade}`;
  window.location.href = fullURL; 
}

async function computerScienceEncode () {
  const parameterValue = "202580-Fall 2025-ITSC-1212_Combined";

  const totalGradesApi = `${fastApi}/totalgrades`;
  const response = await fetch(totalGradesApi);
  const data = await response.json();
  for (let i=0; i<data.length; i++) {
    if (data[i]["Course Name"] === parameterValue) {
      parameterTotalGrade = data[i]["Total Grade"];
      break;
    }
  }

  const encodeName = encodeURIComponent(parameterValue);
  const encodeTotalGrade = encodeURIComponent(parameterTotalGrade);
  const baseURL = "assignments.html";
  const fullURL = `${baseURL}?query=${encodeName}&grade=${encodeTotalGrade}`;
  window.location.href = fullURL;
}



async function computingProfessionalsEncode () {
  const parameterValue = "202580-Fall 2025-ITSC-1600-001-Computing Professionals";

  const totalGradesApi = `${fastApi}/totalgrades`;
  const response = await fetch(totalGradesApi);
  const data = await response.json();
  for (let i=0; i<data.length; i++) {
    if (data[i]["Course Name"] === parameterValue) {
      parameterTotalGrade = data[i]["Total Grade"];
      break;
    }
  }

  const encodeName = encodeURIComponent(parameterValue);
  const encodeTotalGrade = encodeURIComponent(parameterTotalGrade);
  const baseURL = "assignments.html";
  const fullURL = `${baseURL}?query=${encodeName}&grade=${encodeTotalGrade}`;
  window.location = fullURL;
}

async function mathEncode () {
  const parameterValue = "202580-Fall 2025-MATH-1241-004-Calculus I";

  const totalGradesApi = `${fastApi}/totalgrades`;
  const response = await fetch(totalGradesApi);
  const data = await response.json();
  for (let i=0; i<data.length; i++) {
    if (data[i]["Course Name"] === parameterValue) {
      parameterTotalGrade = data[i]["Total Grade"];
      break;
    }
  }

  const encodeName = encodeURIComponent(parameterValue);
  const encodeTotalGrade = encodeURIComponent(parameterTotalGrade);
  const baseURL = "assignments.html";
  const fullURL = `${baseURL}?query=${encodeName}&grade=${encodeTotalGrade}`;
  window.location.href = fullURL;
}

async function englishEncode () {
  const parameterValue = "202580-Fall 2025-WRDS-1103-048-Wrtng & Inqry Acdmc Ctx I & II";

  const totalGradesApi = `${fastApi}/totalgrades`;
  const response = await fetch(totalGradesApi);
  const data = await response.json();
  for (let i=0; i<data.length; i++) {
    if (data[i]["Course Name"] === parameterValue) {
      parameterTotalGrade = data[i]["Total Grade"];
      break;
    }
  }

  const encodeName = encodeURIComponent(parameterValue);
  const encodeTotalGrade = encodeURIComponent(parameterTotalGrade);
  const baseURL = "assignments.html";
  const fullURL = `${baseURL}?query=${encodeName}&grade=${encodeTotalGrade}`;
  window.location.href = fullURL
}

async function cciEncode () {
  const parameterValue = "First-Year New Student Modules, College of Computing and Informatics - Summer II/Fall 2025";

  const totalGradesApi = `${fastApi}/totalgrades`;
  const response = await fetch(totalGradesApi);
  const data = await response.json();
  for (let i=0; i<data.length; i++) {
    if (data[i]["Course Name"] === parameterValue) {
      parameterTotalGrade = data[i]["Total Grade"];
      break;
    }
  }

  const encodeName = encodeURIComponent(parameterValue);
  const encodeTotalGrade = encodeURIComponent(parameterTotalGrade);
  const baseURL = "assignments.html";
  const fullURL = `${baseURL}?query=${encodeName}&grade=${encodeTotalGrade}`;
  window.location.href = fullURL;
}

document.querySelector("#history").addEventListener("click", historyEncode);

document.querySelector("#computer-science").addEventListener("click", computerScienceEncode);

document.querySelector("#computing-professionals").addEventListener("click", computingProfessionalsEncode);

document.querySelector("#math").addEventListener("click", mathEncode);

document.querySelector("#english").addEventListener("click", englishEncode);

document.querySelector("#cci").addEventList