document.addEventListener("DOMContentLoaded", () => {
    async function fetchData(url) {
        try {
            const response = await fetch(url);
            return response.json();
        } catch (error) {
            console.error("Error fetching data:", error);
            return null;
        }
    }

    async function loadCharts() {
        // Fetch data from APIs
        const subscriberGrowth = await fetchData("/api/dashboard/subscriber-growth");
        const activeLoans = await fetchData("/api/dashboard/active-loans");
        const documentDistribution = await fetchData("/api/dashboard/document-distribution");

        // Subscriber Growth Chart
        if (subscriberGrowth) {
            const ctx = document.getElementById("subscriberGrowthChart").getContext("2d");
            new Chart(ctx, {
                type: "line",
                data: {
                    labels: subscriberGrowth.months,
                    datasets: [
                        {
                            label: "Subscribers",
                            data: subscriberGrowth.counts,
                            borderColor: "rgb(75, 192, 192)",
                            tension: 0.3,
                            fill: true,
                            backgroundColor: "rgba(75, 192, 192, 0.2)",
                        },
                    ],
                },
            });
        }

        // Active Loans Chart
        if (activeLoans) {
            const ctx = document.getElementById("activeLoansChart").getContext("2d");
            new Chart(ctx, {
                type: "bar",
                data: {
                    labels: activeLoans.months,
                    datasets: [
                        {
                            label: "Active Loans",
                            data: activeLoans.counts,
                            backgroundColor: "rgb(255, 99, 132)",
                        },
                    ],
                },
            });
        }

        // Document Distribution Chart
        if (documentDistribution) {
            const ctx = document.getElementById("documentDistributionChart").getContext("2d");
            new Chart(ctx, {
                type: "doughnut",
                data: {
                    labels: documentDistribution.labels,
                    datasets: [
                        {
                            label: "Document Distribution",
                            data: documentDistribution.counts,
                            backgroundColor: [
                                "rgb(255, 99, 132)",
                                "rgb(54, 162, 235)",
                                "rgb(255, 206, 86)",
                                "rgb(75, 192, 192)",
                            ],
                        },
                    ],
                },
            });
        }
    }

    loadCharts();
});
