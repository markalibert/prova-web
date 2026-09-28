const canvas = document.getElementById("graficoCidades");

if (canvas) {

    const labels = JSON.parse(
        document.getElementById("grafico-cidades-labels").textContent
    );

    const dados = JSON.parse(
        document.getElementById("grafico-cidades-data").textContent
    );

    const areaGrafico = document.querySelector(".grafico-area");

    const areaScroll = canvas.closest(".grafico-scroll");


    // Altura dinâmica de acordo com a quantidade de cidades
    const altura = Math.max(
        500,
        labels.length * 32
    );

    areaGrafico.style.height = `${altura}px`;


    const grafico = new Chart(canvas, {

        type: "bar",

        data: {

            labels: labels,

            datasets: [

                {
                    label: "Registros",

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

                            return `Registros: ${context.raw}`;

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


    // Limpa o tooltip durante a rolagem

    areaScroll.addEventListener("scroll", function () {

        grafico.setActiveElements([]);

        if (grafico.tooltip) {

            grafico.tooltip.setActiveElements([]);

        }

        grafico.update("none");

    });

}