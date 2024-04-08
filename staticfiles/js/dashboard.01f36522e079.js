document.addEventListener('DOMContentLoaded', function() {
  const profileTab = document.getElementById('profile-tab');
  const settingsTab = document.getElementById('settings-tab');
  const logoutTab = document.getElementById('logout-tab');
  const mainContent = document.getElementById('main-content');
  
  profileTab.addEventListener('click', function(event) {
    event.preventDefault();
    mainContent.innerHTML = '<h2>Profile Page</h2><p>This is your profile page content.</p>';
  });
  
  settingsTab.addEventListener('click', function(event) {
    event.preventDefault();
    mainContent.innerHTML = '<h2>Settings Page</h2><p>This is your settings page content.</p>';
  });
});

new Chart("myChart1", {
  type: "bar",
  data: {
    labels: xArray,
    datasets: [{
      backgroundColor: barColors,
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
      borderRadius: 5, // Set border radius for the bars
      data: yArray
    }]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: "World Wine Production 2018"
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true,
          fontColor: '#333',
          fontSize: 12,
          padding: 10, // Add padding between ticks and axis line
          // Example of additional styling options:
          // fontStyle: 'bold',
          // suggestedMin: 0, // Set suggested minimum value for the axis
          // suggestedMax: 100, // Set suggested maximum value for the axis
          // stepSize: 10, // Set step size for ticks
          // callback: function(value, index, values) {
          //   return '$' + value; // Customize tick labels with a callback function
          // }
        },
        gridLines: {
          color: '#ccc', // Color of grid lines
          zeroLineColor: '#ccc', // Color of grid lines at zero value
          drawBorder: false, // Hide the axis border
        }
      }],
      xAxes: [{
        ticks: {
          fontColor: '#333',
          fontSize: 12,
          padding: 10, // Add padding between ticks and axis line
        },
        gridLines: {
          color: '#ccc', // Color of grid lines
          zeroLineColor: '#ccc', // Color of grid lines at zero value
          drawBorder: false, // Hide the axis border
        }
      }]
    }
  }
});

new Chart("myChart2", {
  type: "bar",
  data: {
    labels: xArray,
    datasets: [{
      backgroundColor: barColors,
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
      borderRadius: 5, // Set border radius for the bars
      data: yArray
    }]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: "World Wine Production 2018"
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true,
          fontColor: '#333',
          fontSize: 12,
          padding: 10, // Add padding between ticks and axis line
          // Example of additional styling options:
          // fontStyle: 'bold',
          // suggestedMin: 0, // Set suggested minimum value for the axis
          // suggestedMax: 100, // Set suggested maximum value for the axis
          // stepSize: 10, // Set step size for ticks
          // callback: function(value, index, values) {
          //   return '$' + value; // Customize tick labels with a callback function
          // }
        },
        gridLines: {
          color: '#ccc', // Color of grid lines
          zeroLineColor: '#ccc', // Color of grid lines at zero value
          drawBorder: false, // Hide the axis border
        }
      }],
      xAxes: [{
        ticks: {
          fontColor: '#333',
          fontSize: 12,
          padding: 10, // Add padding between ticks and axis line
        },
        gridLines: {
          color: '#ccc', // Color of grid lines
          zeroLineColor: '#ccc', // Color of grid lines at zero value
          drawBorder: false, // Hide the axis border
        }
      }]
    }
  }
});

new Chart("myChart3", {
  type: "bar",
  data: {
    labels: xArray,
    datasets: [{
      backgroundColor: barColors,
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
      borderRadius: 5, // Set border radius for the bars
      data: yArray
    }]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: "World Wine Production 2018"
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true,
          fontColor: '#333',
          fontSize: 12,
          padding: 10, // Add padding between ticks and axis line
          // Example of additional styling options:
          // fontStyle: 'bold',
          // suggestedMin: 0, // Set suggested minimum value for the axis
          // suggestedMax: 100, // Set suggested maximum value for the axis
          // stepSize: 10, // Set step size for ticks
          // callback: function(value, index, values) {
          //   return '$' + value; // Customize tick labels with a callback function
          // }
        },
        gridLines: {
          color: '#ccc', // Color of grid lines
          zeroLineColor: '#ccc', // Color of grid lines at zero value
          drawBorder: false, // Hide the axis border
        }
      }],
      xAxes: [{
        ticks: {
          fontColor: '#333',
          fontSize: 12,
          padding: 10, // Add padding between ticks and axis line
        },
        gridLines: {
          color: '#ccc', // Color of grid lines
          zeroLineColor: '#ccc', // Color of grid lines at zero value
          drawBorder: false, // Hide the axis border
        }
      }]
    }
  }
});

new Chart("myChart4", {
  type: "bar",
  data: {
    labels: xArray,
    datasets: [{
      backgroundColor: barColors,
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
      borderRadius: 5, // Set border radius for the bars
      data: yArray
    }]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: "World Wine Production 2018"
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true,
          fontColor: '#333',
          fontSize: 12,
          padding: 10, // Add padding between ticks and axis line
          // Example of additional styling options:
          // fontStyle: 'bold',
          // suggestedMin: 0, // Set suggested minimum value for the axis
          // suggestedMax: 100, // Set suggested maximum value for the axis
          // stepSize: 10, // Set step size for ticks
          // callback: function(value, index, values) {
          //   return '$' + value; // Customize tick labels with a callback function
          // }
        },
        gridLines: {
          color: '#ccc', // Color of grid lines
          zeroLineColor: '#ccc', // Color of grid lines at zero value
          drawBorder: false, // Hide the axis border
        }
      }],
      xAxes: [{
        ticks: {
          fontColor: '#333',
          fontSize: 12,
          padding: 10, // Add padding between ticks and axis line
        },
        gridLines: {
          color: '#ccc', // Color of grid lines
          zeroLineColor: '#ccc', // Color of grid lines at zero value
          drawBorder: false, // Hide the axis border
        }
      }]
    }
  }
});