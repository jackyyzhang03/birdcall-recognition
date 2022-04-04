const submitAudio = async () => {
  const audio = document.getElementById("audio").files[0];
  if (!audio) return;
  const data = new FormData();
  data.append("audio", audio);
  await setLoading();
  const response = await fetch("/", {
    method: "POST",
    body: data,
  });
  if (response.status == 200) {
    updateResults(await response.json());
  } else {
    updateResults([0]);
  }
};

const sleep = (ms) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};

const setLoading = async () => {
  const field = document.getElementById("prediction");
  const spinner = document.getElementById("spinner");
  field.className = "hidden";
  await sleep(600);
  spinner.style.opacity = 1;
};

const updateResults = (results) => {
  chart.data.datasets[0].data = results.probabilities;
  chart.update();

  const field = document.getElementById("prediction");
  const spinner = document.getElementById("spinner");
  spinner.style.opacity = 0;
  setTimeout(() => {
    field.innerText = "Prediction: " + results.prediction;
    field.className = results.prediction ? "visible" : "hidden";
  }, 600);
};

const selectFile = () => {
  const fileInput = document.getElementById("audio");
  fileInput.onchange = () => {
    const fileNameField = document.getElementById("file-name");
    fileNameField.value = fileInput.value.replace("C:\\fakepath\\", "");
    submitAudio();
  };
  fileInput.click();
};

const ctx = document.getElementById("chart");
const chart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: [
      "American Crow",
      "American Robin",
      "Barn Swallow",
      "Bewick's Wren",
      "Blue Jay",
      "Carolina Wren",
      "Northern Raven",
      "Common Yellowthroat",
      "House Sparrow",
      "House Wren",
      "Mallard",
      "Marsh Wren",
      "Northern Cardinal",
      "Northern Mockingbird",
      "Red Crossbill",
      "Red-winged Blackbird",
      "Song Sparrow",
      "Spotted Towhee",
      "Swainson's Thrush",
      "Western Meadowlark",
    ],
    datasets: [
      {
        axis: "x",
        data: [],
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    onResize: (chart, size) => {
      if (size.width <= 768) {
        chart.data.datasets[0].axis = "y";
        chart.options.indexAxis = "y";
        chart.options.scales = {
          x: {
            beginAtZero: true,
            max: 1,
            ticks: {
              format: {
                style: "percent",
              },
            },
          },
        };
      } else {
        chart.data.datasets[0].axis = "x";
        chart.options.indexAxis = "x";
        chart.options.scales = {
          y: {
            beginAtZero: true,
            max: 1,
            ticks: {
              format: {
                style: "percent",
              },
            },
          },
        };
      }
    },
    indexAxis: "x",
    responsive: true,
    maintainAspectRatio: false,
    animation: {
      duration: 1800,
      easing: "easeOutQuint",
    },
    plugins: {
      legend: {
        display: false,
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 1,
        ticks: {
          format: {
            style: "percent",
          },
        },
      },
    },
  },
});
