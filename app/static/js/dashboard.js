document.addEventListener("DOMContentLoaded", () => {
    // Fetch data for the charts (mock data used here, replace with API calls as needed)
    const fetchData = async () => {
        return {
            subscriberGrowth: [50, 100, 150, 200, 250, 300, 350],
            activeLoans: [20, 30, 25, 40, 50, 60],
            documentDistribution: {
                labels: ["Books", "Magazines", "Journals", "DVDs"],
                data: [40, 20, 15, 25],
            },
        };
    };

    fetchData().then((data) => {
        // Subscriber Growth Chart
        const subscriberGrowthCtx = document
            .getElementById("subscriberGrowthChart")
            .getContext("2d");
        new Chart(subscriberGrowthCtx, {
            type: "line",
            data: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                datasets: [
                    {
                        label: "Subscribers",
                        data: data.subscriberGrowth,
                        borderColor: "rgb(75, 192, 192)",
                        tension: 0.3,
                        fill: true,
                        backgroundColor: "rgba(75, 192, 192, 0.2)",
                    },
                ],
            },
        });

        // Active Loans Chart
        const activeLoansCtx = document
            .getElementById("activeLoansChart")
            .getContext("2d");
        new Chart(activeLoansCtx, {
            type: "bar",
            data: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                datasets: [
                    {
                        label: "Active Loans",
                        data: data.activeLoans,
                        backgroundColor: "rgb(255, 99, 132)",
                    },
                ],
            },
        });

        // Document Distribution Chart
        const documentDistributionCtx = document
            .getElementById("documentDistributionChart")
            .getContext("2d");
        new Chart(documentDistributionCtx, {
            type: "doughnut",
            data: {
                labels: data.documentDistribution.labels,
                datasets: [
                    {
                        label: "Document Distribution",
                        data: data.documentDistribution.data,
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
    });
});
