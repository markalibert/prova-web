const canvasLogradouros = document.getElementById("graficoLogradouros");

if (canvasLogradouros) {
    const labels = JSON.parse(
        document.getElementById("logradouros-labels").textContent
    );

    const dados = JSON.parse(
        document.getElementById("logradouros-data").textContent
    );

    const areaGrafico = document.querySelector(
        ".grafico-logradouros-area"
    );

    const areaScroll = canvasLogradouros.closest(
        ".grafico-scroll"
    );

    const altura = Math.max(
        500,
        labels.length * 32
    );

    areaGrafico.style.height = `${altura}px`;

    const graficoLogradouros = new Chart(canvasLogradouros, {
        type: "bar",

        data: {
            labels: labels,

            datasets: [
                {
                    label: "Logradouros",

                    data: dados,

                    minBarLength: 10,

                    barPercentage: 0.75,
                    categoryPercentage: 0.9,

                    borderWidth: 1
                }
            ]
        },

        options: {
            indexAxis: "y",

            responsive: true,
            maintainAspectRatio: false,

            interaction: {
                mode: "nearest",
                intersect: true
            },

            plugins: {
                legend: {
                    display: true
                },

                tooltip: {
                    callbacks: {
                        title: function (items) {
                            return items[0].label;
                        },

                        label: function (context) {
                            return `Logradouros: ${context.raw}`;
                        }
                    }
                }
            },

            scales: {
                x: {
                    beginAtZero: true
                },

                y: {
                    ticks: {
                        autoSkip: false
                    }
                }
            }
        }
    });

    areaScroll.addEventListener("scroll", function () {
        graficoLogradouros.setActiveElements([]);

        if (graficoLogradouros.tooltip) {
            graficoLogradouros.tooltip.setActiveElements([]);
        }

        graficoLogradouros.update("none");
    });
}