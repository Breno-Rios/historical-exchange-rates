
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
