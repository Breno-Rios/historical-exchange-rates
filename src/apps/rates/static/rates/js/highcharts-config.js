
Highcharts.setOptions({
    chart: {
        style: {
            fontFamily: 'Roboto, sans-serif',
            fontSize: '16px',
            color: '#193b4f' 
        }
    },
    title: {
        style: { fontSize: '16px' }
    },
    xAxis: {
        labels: { style: { fontSize: '14px' } },
        title: { style: { fontSize: '16px' } }
    },
    yAxis: {
        labels: { style: { fontSize: '14px' } },
        title: { style: { fontSize: '16px' } }
    },
    legend: {
        itemStyle: { fontSize: '14px' }
    },
    tooltip: {
        style: { fontSize: '14px' }
    }
});
    
window.chart = Highcharts.chart('container', {
    title: { text: 'Dashboard Exchange Rates' },
    xAxis: { title: { text: 'Date' }, categories:  [] },
    yAxis: { type: 'logarithmic', title: { text: '' } },
    tooltip: { headerFormat: '<b>{series.name}</b><br />', pointFormat: '{point.y}' },
    series: [{ name: 'Rates', data: [], color: '#193b4f' }]
});

    
    
    // function updateChart(data) {
    //     if (!data || !data.length) {
    //         console.warn("No data received to update chart");
    //         chart.series[0].setData([]);
    //         chart.xAxis[0].setCategories([]);
    //         return;
    //     }
        
    //     const categories = data.map(d => d.date);
    //     const values = data.map(d => parseFloat(d.value) || 0);
    //     const currencyStr = '0'

        
    //     chart.xAxis[0].setCategories(categories);
    //     chart.series[0].setData(values);
    //     chart.pointFormat[0].setData(values);
    //     chart.update({
    //     tooltip: {
    //         pointFormat: `{point.y} ${currencyStr}`
    //     }
    // });
    // }
    

